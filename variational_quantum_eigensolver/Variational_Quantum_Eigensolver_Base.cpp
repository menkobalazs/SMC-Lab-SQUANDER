/*
Created on Fri Jun 26 14:13:26 2020
Copyright 2020 Peter Rakyta, Ph.D.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

@author: Peter Rakyta, Ph.D.
*/
/*! \file Variational_Quantum_Eigensolver_Base.cpp
    \brief Class to solve VQE problems
*/
#include "Variational_Quantum_Eigensolver_Base.h"


/**
@brief A base class to solve VQE problems
This class can be used to approximate the ground state of the input Hamiltonian (sparse format) via a quantum circuit
*/
Variational_Quantum_Eigensolver_Base::Variational_Quantum_Eigensolver_Base() {

    // logical value describing whether the decomposition was finalized or not
    decomposition_finalized = false;


    // error of the unitarity of the final decomposition
    decomposition_error = DBL_MAX;


    // The current minimum of the optimization problem
    current_minimum = DBL_MAX;
    
    global_target_minimum = -DBL_MAX;

    // logical value describing whether the optimization problem was solved or not
    optimization_problem_solved = false;


    // The maximal allowed error of the optimization problem
    optimization_tolerance = -DBL_MAX;

    // The convergence threshold in the optimization process
    convergence_threshold = -DBL_MAX;
    
    alg = AGENTS;
    
    iteration_threshold_of_randomization = 2500000;

    random_shift_count_max = 100;
    
    adaptive_eta = false;
    
    cost_fnc = VQE;
    
    ansatz = HEA;
}




/**
@brief Constructor of the class.
@param Hamiltonian_in The Hamiltonian describing the physical system
@param qbit_num_in The number of qubits spanning the unitary Umtx
@param config_in A map that can be used to set hyperparameters during the process
@return An instance of the class
*/
Variational_Quantum_Eigensolver_Base::Variational_Quantum_Eigensolver_Base( Matrix_sparse Hamiltonian_in, int qbit_num_in, std::map<std::string, Config_Element>& config_in) : N_Qubit_Decomposition_Base(Matrix(Power_of_2(qbit_num_in),1), qbit_num_in, false, config_in, RANDOM, accelerator_num) {

	Hamiltonian = Hamiltonian_in;
    // config maps
    config   = config_in;
    // logical value describing whether the decomposition was finalized or not
    decomposition_finalized = false;


    // error of the unitarity of the final decomposition
    decomposition_error = DBL_MAX;


    // The current minimum of the optimization problem
    current_minimum = DBL_MAX;


    // logical value describing whether the optimization problem was solved or not
    optimization_problem_solved = false;

    // override optimization parameters governing the convergence used in gate decomposition applications
    global_target_minimum  = -DBL_MAX;
    optimization_tolerance = -DBL_MAX;
    convergence_threshold  = -DBL_MAX;
    
    
    iteration_threshold_of_randomization = 2500000;

    random_shift_count_max = 100;
    
    adaptive_eta = false;
    
    qbit_num = qbit_num_in;
	
    Zero_state = Matrix( Power_of_2(qbit_num) , 1);
	
    std::random_device rd;  
    
    gen = std::mt19937(rd());
    
    alg = BAYES_OPT;
    
    cost_fnc = VQE;
    
    ansatz = HEA;
    
}




/**
@brief Destructor of the class
*/
Variational_Quantum_Eigensolver_Base::~Variational_Quantum_Eigensolver_Base(){

}




/**
@brief Call to start solving the VQE problem to get the approximation for the ground state  
*/ 
void Variational_Quantum_Eigensolver_Base::Get_ground_state(){

    initialize_zero_state();


    if (gates.size() == 0 ) {
        std::string error("Variational_Quantum_Eigensolver_Base::Get_ground_state: for VQE process the circuit needs to be initialized");
        throw error;
    }

    int num_of_parameters =  optimized_parameters_mtx.size();
    if ( num_of_parameters == 0 ) {
        std::string error("Variational_Quantum_Eigensolver_Base::Get_ground_state: No intial parameters were given");
        throw error;
    }


    if ( num_of_parameters != get_parameter_num() ) {
        std::string error("Variational_Quantum_Eigensolver_Base::Get_ground_state: The number of initial parameters does not match with the number of parameters in the circuit");
        throw error;
    }    


    // start the VQE process
    Matrix_real solution_guess = optimized_parameters_mtx.copy();
    solve_layer_optimization_problem(num_of_parameters, solution_guess);


    // prepare to export the quantum circuit (QISKIT, Cirq formats are supported)
    prepare_gates_to_export();


    return;
}





/**
@brief Call to evaluate the expectation value of the energy.
@param State The state for which the expectation value is evaluated
@return The calculated expectation value
*/
double Variational_Quantum_Eigensolver_Base::Expectation_value_of_energy(Matrix& State) {

    Matrix tmp = mult(Hamiltonian, State);
    double Energy= 0.0;

    for (int idx=0; idx<State.rows; idx++){
	Energy += State[idx].real*tmp[idx].real + State[idx].imag*tmp[idx].imag;
    }
 
    tmp.release_data();
    number_of_iters++;

    return Energy;
}




/**
@brief The optimization problem of the final optimization
@param parameters Array containing the parameters to be optimized.
@param void_instance A void pointer pointing to the instance of the current class.
@return Returns with the cost function. (zero if the qubits are desintangled.)
*/
double Variational_Quantum_Eigensolver_Base::optimization_problem_non_static(Matrix_real parameters, void* void_instance){

    double Energy=0.;

    Variational_Quantum_Eigensolver_Base* instance = reinterpret_cast<Variational_Quantum_Eigensolver_Base*>(void_instance);

    Matrix State = instance->Zero_state.copy();

    instance->apply_to(parameters, State);
    Energy = instance->Expectation_value_of_energy(State);

    return Energy;
}


/**
@brief The optimization problem of the final optimization
@param parameters An array of the free parameters to be optimized. (The number of teh free paramaters should be equal to the number of parameters in one sub-layer)
@return Returns with the cost function. (zero if the qubits are desintangled.)
*/
double Variational_Quantum_Eigensolver_Base::optimization_problem(Matrix_real& parameters)  {

    double Energy;
    initialize_zero_state();
	
    Matrix State = Zero_state.copy();
	
    apply_to(parameters, State);
	
    //State.print_matrix();
	
    Energy = Expectation_value_of_energy(State);
    number_of_iters++;
	
    return Energy;
}



/**
@brief Call to calculate both the cost function and the its gradient components.
@param parameters Array containing the free parameters to be optimized.
@param void_instance A void pointer pointing to the instance of the current class.
@param f0 The value of the cost function at x0.
@param grad Array containing the calculated gradient components.
*/
void Variational_Quantum_Eigensolver_Base::optimization_problem_combined_non_static( Matrix_real parameters, void* void_instance, double* f0, Matrix_real& grad ) {

    Variational_Quantum_Eigensolver_Base* instance = reinterpret_cast<Variational_Quantum_Eigensolver_Base*>(void_instance);

    // the number of free parameters
    int parameter_num_loc = parameters.size();

    Matrix_real cost_function_terms;

    // vector containing gradients of the transformed matrix
    std::vector<Matrix> State_deriv;

    tbb::parallel_invoke(
        [&]{
            *f0 = instance->optimization_problem_non_static(parameters, reinterpret_cast<void*>(instance));
        },
        [&]{
	    instance->initialize_zero_state();
            Matrix State_loc = instance->Zero_state.copy();
            State_deriv = instance->apply_derivate_to( parameters, State_loc );
            State_loc.release_data();
    });

    tbb::parallel_for( tbb::blocked_range<int>(0,parameter_num_loc,2), [&](tbb::blocked_range<int> r) {
        for (int idx=r.begin(); idx<r.end(); ++idx) { 
            grad[idx] = instance->Expectation_value_of_energy(State_deriv[idx]);
        }
    });


    return;
}






/**
@brief Call to calculate both the cost function and the its gradient components.
@param parameters Array containing the free parameters to be optimized.
@param f0 The value of the cost function at x0.
@param grad Array containing the calculated gradient components.
*/
void Variational_Quantum_Eigensolver_Base::optimization_problem_combined( Matrix_real parameters, double* f0, Matrix_real grad )  {

    optimization_problem_combined_non_static( parameters, this, f0, grad );
    return;
}




/**
@brief Calculate the derivative of the cost function with respect to the free parameters.
@param parameters Array containing the free parameters to be optimized.
@param void_instance A void pointer pointing to the instance of the current class.
@param grad Array containing the calculated gradient components.
*/
void Variational_Quantum_Eigensolver_Base::optimization_problem_grad_vqe( Matrix_real parameters, void* void_instance, Matrix_real& grad ) {

    double f0;
    Variational_Quantum_Eigensolver_Base* instance = reinterpret_cast<Variational_Quantum_Eigensolver_Base*>(void_instance);
    instance->optimization_problem_combined_non_static(parameters, void_instance, &f0, grad);
    return;

}




/**
@brief The optimization problem of the final optimization
@param parameters An array of the free parameters to be optimized. (The number of teh free paramaters should be equal to the number of parameters in one sub-layer)
@return Returns with the cost function. (zero if the qubits are desintangled.)
*/
double Variational_Quantum_Eigensolver_Base::optimization_problem( double* parameters ) {

    // get the transformed matrix with the gates in the list
    Matrix_real parameters_mtx(parameters, 1, parameter_num );
    
    return optimization_problem( parameters_mtx );


}




/**
@brief Initialize the state used in the quantun circuit. All qubits are initialized to state 0
*/
void Variational_Quantum_Eigensolver_Base::initialize_zero_state( ) {

    Zero_state[0].real = 1.0;
    Zero_state[0].imag = 0.0;
    memset(Zero_state.get_data()+2, 0.0, (Zero_state.size()*2-2)*sizeof(double) );      

    return;
}





/**
@brief Call to set the ansatz type. Currently imp
@param ansatz_in The ansatz type . Possible values: "HEA" (hardware efficient ansatz with U3 and CNOT gates).
*/ 
void Variational_Quantum_Eigensolver_Base::set_ansatz(ansatz_type ansatz_in){

    ansatz = ansatz_in;
    
    return;
}





/**
@brief Call to generate the circuit ansatz
@param layers The number of layers. The depth of the generated circuit is 2*layers+1 (U3-CNOT-U3-CNOT...CNOT-U3)
*/
void Variational_Quantum_Eigensolver_Base::generate_circuit( int layers ) {


    switch (ansatz){
    
        case HEA:
        {

            release_gates();

            if ( qbit_num < 2 ) {
                std::string error("Variational_Quantum_Eigensolver_Base::generate_initial_circuit: number of qubits should be at least 2");
                throw error;
            }

            for (int layer_idx=0; layer_idx<layers ;layer_idx++){

                add_u3(1, true, true, true);                          
                add_u3(0, true, true, true);
                add_cnot(1,0);

                if (layer_idx==layers-1){
                    add_u3(0, true, true, true);                      
                }
                for (int control_qbit=1; control_qbit<qbit_num-1; control_qbit=control_qbit+2){
                    if (control_qbit+2<qbit_num){

                        add_u3(control_qbit+1, true, true, true);
                        add_u3(control_qbit+2, true, true, true);             

                        add_cnot(control_qbit+2,control_qbit+1);

                    }

                    add_u3(control_qbit+1, true, true, true);  
                    add_u3(control_qbit, true, true, true);  

                    add_cnot(control_qbit+1,control_qbit);

                    if (layer_idx==layers-1){
                        add_u3(control_qbit, true, true, true);
                        add_u3(control_qbit+1, true, true, true);                        
                    }
                }
            }

            if (qbit_num%2==0){
                add_u3(qbit_num-1, true, true, true);
            }


            return;
        }
        case HEA_ZYZ:
        {

            release_gates();

            if ( qbit_num < 2 ) {
                std::string error("Variational_Quantum_Eigensolver_Base::generate_initial_circuit: number of qubits should be at least 2");
                throw error;
            }

            for (int layer_idx=0; layer_idx<layers ;layer_idx++){


                add_rz(1);
                add_ry(1);
                add_rz(1);                                

                add_rz(0);
                add_ry(0);
                add_rz(0);                    
                
                add_cnot(1,0);

                if (layer_idx==layers-1){
                    add_rz(0);
                    add_ry(0);
                    add_rz(0);                        
                }
                for (int control_qbit=1; control_qbit<qbit_num-1; control_qbit=control_qbit+2){
                    if (control_qbit+2<qbit_num){

                        add_rz(control_qbit+1);
                        add_ry(control_qbit+1);
                        add_rz(control_qbit+1);                            

                        add_rz(control_qbit+2);
                        add_ry(control_qbit+2);
                        add_rz(control_qbit+2);                               

                        add_cnot(control_qbit+2,control_qbit+1);

                    }

                    add_rz(control_qbit+1);
                    add_ry(control_qbit+1);
                    add_rz(control_qbit+1);                    

                    add_rz(control_qbit);
                    add_ry(control_qbit);
                    add_rz(control_qbit);                    

                    add_cnot(control_qbit+1,control_qbit);

                    if (layer_idx==layers-1){
                        add_rz(control_qbit);
                        add_ry(control_qbit);
                        add_rz(control_qbit);                          

                        add_rz(control_qbit+1);
                        add_ry(control_qbit+1);
                        add_rz(control_qbit+1);                          
                    }
                }
            }

            if (qbit_num%2==0){
                add_rz(qbit_num-1);
                add_ry(qbit_num-1);
                add_rz(qbit_num-1);                  
            }


            return;
        }        
        default:
            std::string error("Variational_Quantum_Eigensolver_Base::generate_initial_circuit: ansatz not implemented");
            throw error;
    }

}


/**
@brief Call to set custom layers to the gate structure that are intended to be used in the VQE process.
@param filename The path to the binary file
*/
void 
Variational_Quantum_Eigensolver_Base::set_adaptive_gate_structure( std::string filename ) {

    release_gates();
    Matrix_real optimized_parameters_mtx_tmp;
    Gates_block* gate_structure_tmp = import_gate_list_from_binary(optimized_parameters_mtx_tmp, filename);

    if ( gates.size() > 0 ) {
        gate_structure_tmp->combine( static_cast<Gates_block*>(this) );

        release_gates();
        combine( gate_structure_tmp );


        Matrix_real optimized_parameters_mtx_tmp2( 1, optimized_parameters_mtx_tmp.size() + optimized_parameters_mtx.size() );
        memcpy( optimized_parameters_mtx_tmp2.get_data(), optimized_parameters_mtx_tmp.get_data(), optimized_parameters_mtx_tmp.size()*sizeof(double) );
        memcpy( optimized_parameters_mtx_tmp2.get_data()+optimized_parameters_mtx_tmp.size(), optimized_parameters_mtx.get_data(), optimized_parameters_mtx.size()*sizeof(double) );
        optimized_parameters_mtx = optimized_parameters_mtx_tmp2;
    }
    else {
        combine( gate_structure_tmp );
        optimized_parameters_mtx = optimized_parameters_mtx_tmp;
        gates_num gates_num = get_gate_nums();

        if ( gates_num.u3>0 )  std::cout << gates_num.u3 << " U3 gates," << std::endl;
        if ( gates_num.rx>0 )  std::cout << gates_num.rx << " RX gates," << std::endl;
        if ( gates_num.ry>0 )  std::cout << gates_num.ry << " RY gates," << std::endl;
        if ( gates_num.rz>0 )  std::cout << gates_num.rz << " RZ gates," << std::endl;
        if ( gates_num.cnot>0 )  std::cout << gates_num.cnot << " CNOT gates," << std::endl;
        if ( gates_num.cz>0 )  std::cout << gates_num.cz << " CZ gates," << std::endl;
        if ( gates_num.ch>0 )  std::cout << gates_num.ch << " CH gates," << std::endl;
        if ( gates_num.x>0 )  std::cout << gates_num.x << " X gates," << std::endl;
        if ( gates_num.sx>0 )  std::cout << gates_num.sx << " SX gates," << std::endl; 
        if ( gates_num.syc>0 )  std::cout << gates_num.syc << " Sycamore gates," << std::endl;   
        if ( gates_num.un>0 )  std::cout << gates_num.un << " UN gates," << std::endl;
        if ( gates_num.cry>0 )  std::cout << gates_num.cry << " CRY gates," << std::endl;  
        if ( gates_num.adap>0 )  std::cout << gates_num.adap << " Adaptive gates," << std::endl;    	
    }

}




