print('-- --- Start optimization process --- --')
from scipy.stats import unitary_group
import numpy as np
from squander import Variational_Quantum_Eigensolver
from squander import utils as utils
import time
import sys
import scipy as sp
import pytest
from networkx.generators.random_graphs import random_regular_graph
from qiskit.quantum_info import SparsePauliOp

np.set_printoptions(linewidth=200) 

##### //MB\\
    # new imports
import argparse
import os
from scipy.optimize import minimize
import json
import datetime
##### \\MB//



##### //MB\\
parser = argparse.ArgumentParser(description="Run VQE simulations with Heisenberg_VQE.py")
def to_uppercase(choice):
    return choice.upper()
parser.add_argument("-o", "--optimizer", help="Name of optimizer", type=to_uppercase, required=True,
                    choices=['AGENTS', 'AGENTS_COMBINED', 'COSINE', 'GRAD_DESCEND_PARAMETER_SHIFT_RULE', 
                             'BFGS', 'ADAM', 'GRAD_DESCEND', 'BAYES_OPT', 'BAYES_AGENTS', 
                             'NELDER_MEAD', 'POWELL', 'COBYLA', 
                             ]
                    )
parser.add_argument("-l", "--layers", help="Number of layers", type=int, default=100)
parser.add_argument("-q", "--qbit_num", help="Number of qubits", type=int, default=10)
parser.add_argument("-p", "--init_parameters", help="Zero or random initial parameters.", type=str, default='zero',
                    choices=['zero', 'random'])
parser.add_argument("-d", "--degree", help="Degree of random regular graph which generates the Hamiltonian's topology.", 
                    type=int, default=3, choices=[2,3,4])
parser.add_argument("-s", "--random_seed", help="Seed for random regular graph which generates the Hamiltonian's topology.", 
                    type=int, default=31415)
args = parser.parse_args()
##### \\MB//



topology = []

def generate_hamiltonian_tmp(n):

    topology = [[0,1],[0,4],[0,8],
                [1,2],[1,5],
                [2,3],[2,4],
                [3,6],[3,9],
                [4,5],
                [5,6],
                [6,7],
                [7,8],[7,9],
                [8,9]]
    
    oplist = []
    for i in topology:
        oplist.append(("XX",[i[0],i[1]],1)) 
        oplist.append(("YY",[i[0],i[1]],1))
        oplist.append(("ZZ",[i[0],i[1]],1))
    for i in range(n):
        oplist.append(("Z",[i],1))
    return SparsePauliOp.from_sparse_list(oplist,num_qubits=n).to_matrix(True)



def generate_hamiltonian(n):
    topology = random_regular_graph(args.degree,n,seed=args.random_seed) ##### //MB// 3->args.degree
    oplist = []
    for i in topology.edges:
        oplist.append(("XX",[i[0],i[1]],1))
        oplist.append(("YY",[i[0],i[1]],1))
        oplist.append(("ZZ",[i[0],i[1]],1))
    for i in range(n):
        oplist.append(("Z",[i],1))
    return topology, SparsePauliOp.from_sparse_list(oplist,num_qubits=n).to_matrix(True)


# The number of circuit layers
layers = args.layers ##### //MB// 100->args.layers

# the number of subblocks in a single layer
inner_blocks = 1

# The number of qubits
qbit_num = args.qbit_num ##### //MB// 10->args.qbit_num



# generate the Hamiltonian
topology, Hamiltonian = generate_hamiltonian( qbit_num ) ##### //MB// generate_hamiltonian_tmp->generate_hamiltonian
##### //MB\\
# Todo: save topology as nx graph
##### \\MB//


# obtain the groud state energy of the Hamitonian
[eigvals, eigvecs] = sp.sparse.linalg.eigs( Hamiltonian, k=10, which='SR' )
eigval = np.real(eigvals[0])
eigvec = eigvecs[:,0]

print( 'The target eigenvalue is: ', eigval )


# generate configuration dictionary for the solver ### Given by project leader (Péter Rakyta)
config = {"max_inner_iterations":400, ##### //MB// modified 800-->400
        "batch_size": 32,
        "agent_num" : 1,
        "agent_lifetime": 1,
        "linesearch_points_agent":3,
        "agent_exploration_rate": 0.0,
        "eta": 0.0001,
        "adaptive_eta": 0,
        "use_line_search": 0,
        "output_periodicity": 4,
        "convergence_length": 20}

# initiate the VQE object with the Hamiltonian
VQE_Heisenberg = Variational_Quantum_Eigensolver(Hamiltonian, qbit_num, config)

##### //MB\\
optimizer_folder_name = args.optimizer.upper()
project_name = f'data/{optimizer_folder_name}/initp={args.init_parameters}_lyr={args.layers}_qb={args.qbit_num}_d={args.degree}_s={args.random_seed}'
VQE_Heisenberg.set_Project_Name(project_name=project_name)

try:
    os.mkdir('data/'+optimizer_folder_name)
    print(f"-- Directory '{optimizer_folder_name}' created successfully in 'data' folder.")
except FileExistsError:
    print(f"-- Directory '{optimizer_folder_name}' already exists in 'data' folder.", end=' ')
    try:
        os.remove(project_name+'_costfuncs_and_entropy.txt'  ) 
        print("Earlier simulation has been deleted.")
    except:
        print()
except PermissionError:
    print(f"-- Permission denied: Unable to create 'data/{optimizer_folder_name}'.")
except Exception as e:
    print(f"-- An error occurred: {e}")
print(f"-- Run simulation with '{args.optimizer}' method; init param: '{args.init_parameters}'; N_qb={args.qbit_num}; layers={args.layers}; seed={args.random_seed}")
##### \\MB//

# set the optimization engine to agents

##### //MB\\
if args.optimizer.upper() in ['NELDER_MEAD', 'POWELL', 'COBYLA']:
    cost_function_evaluations = 0  
    VQE_energy_one_step_before = 1e10
    def objective_function(params, saved_data):
        global cost_function_evaluations
        global VQE_energy_one_step_before
        VQE_energy = VQE_Heisenberg.Optimization_Problem(params)
        if cost_function_evaluations%1000==0:
            print(f"-- number of costfunc evaluation: {cost_function_evaluations}; VQE_energy={VQE_energy}", end='\r')
        if VQE_energy_one_step_before >= VQE_energy+0.001:
            saved_data.write(f"{cost_function_evaluations}\t{VQE_energy}\n") 
            VQE_energy_one_step_before = VQE_energy
        cost_function_evaluations += 1 
        return VQE_energy
else:
##### \\MB//
    VQE_Heisenberg.set_Optimizer(args.optimizer.upper())

# set the ansatz variant (U3 rotations and CNOT gates)
VQE_Heisenberg.set_Ansatz("HEA_ZYZ")

# generate the circuit ansatz for the optimization
VQE_Heisenberg.Generate_Circuit( layers, inner_blocks)

# create random initial parameters 
param_num  = VQE_Heisenberg.get_Parameter_Num()
print('The number of free parameters is: ', str(param_num) )

##### //MB\\
if args.init_parameters == 'zero':
    parameters = np.zeros( (param_num,) )
elif args.init_parameters == "random":
    np.random.seed(137) 
    parameter_minval, parameter_maxval = -0.01, 0.01
    parameters = np.random.uniform(parameter_minval, parameter_minval, param_num) 
else:   
    raise ValueError(f"init_parameters must be either 'zero' or 'random' and not '{args.init_parameters}'")
##### \\MB//

##### //MB\\
# Create log file
logs = {}
logs['ground_state_of_Hamiltonian'] = eigval
logs['method'] = args.optimizer
logs['layers'] = args.layers
logs['qbit_num'] = args.qbit_num
logs['init_parameters'] = args.init_parameters
if args.init_parameters == 'random':
    logs['init_parameters_between'] = [parameter_minval, parameter_maxval]
logs['config'] = config
logs['start_optimization'] = datetime.datetime.now().isoformat()  
with open(project_name+"_logs.json", "w") as f:
    json.dump(logs, f, indent=4)
##### \\MB//


VQE_Heisenberg.set_Optimized_Parameters(parameters)

#VQE_Heisenberg.set_Initial_State( eigvec )

# calculate the entropy of the exact ground state
page_entropy                = 2 * np.log(2.0) - 1.0/( pow(2, qbit_num-2*2+1) )
entropy_exact_gs            = VQE_Heisenberg.get_Second_Renyi_Entropy( parameters=np.array([]), qubit_list=[0,1], input_state=eigvec ) 
normalized_entropy_exact_gs = entropy_exact_gs/page_entropy
print('The normalized entropy of the exact ground state evaluated on qubits 0 and 1 is:', normalized_entropy_exact_gs)
print(' ', flush=True)
print('-- Start optimization process')

cost_function_evaluations = 0
for iter_idx in range(50): ##### //MB// 400->50
    # start an etap of the optimization (max_inner_iterations iterations)
    ##### //MB\\
    if args.optimizer.upper() in ['NELDER_MEAD', 'POWELL', 'COBYLA']:
        scipy_method_name= {'NELDER_MEAD':'Nelder-Mead', 'POWELL':'Powell', 'COBYLA':'Cobyla'}

        with open(project_name+"_costfuncs_and_entropy.txt", "a") as f:
            min_process = minimize(objective_function, parameters, args=(f,), tol=5e-2,
                        method=scipy_method_name[args.optimizer.upper()],
                        options={'maxfev':5e5, 'disp':True, 'xtol':0.5}
                        # options: https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.optimize.show_options.html
                        )
        parameters = min_process.x
        VQE_energy = min_process.fun
    else:
    ##### \\MB//
        VQE_Heisenberg.Start_Optimization()
    
        # retrieve the current parameter set
        parameters = VQE_Heisenberg.get_Optimized_Parameters()

        # retrive the current VQE energy after max_inner_iterations iterations
        VQE_energy = VQE_Heisenberg.Optimization_Problem( parameters ) 
    


    # calculate the Renyi entropy after max_inner_iterations iterations on the subsystem made of the 0-th and the 1st qubits
    qubit_list = [0,1]

    page_entropy       = len(qubit_list) * np.log(2.0) - 1.0/( pow(2, qbit_num-2*len(qubit_list)+1) )
    entropy            = VQE_Heisenberg.get_Second_Renyi_Entropy( parameters=parameters, qubit_list=qubit_list ) 
    normalized_entropy = entropy/page_entropy


    print('Current VQE energy: ', VQE_energy, ' normalized entropy: ', normalized_entropy)

    ##### //MB\\ ##just modified
    np.save(project_name+'.npy', parameters, topology ) 
    ##### \\MB//
           
    initial_state = np.zeros( (1 << qbit_num), dtype=np.complex128 )
    initial_state[0] = 1.0 + 0j        
        
    
    state_to_transform = initial_state.copy()    
    VQE_Heisenberg.apply_to( parameters, state_to_transform );   
    
    overlap      = state_to_transform.transpose().conjugate() @ eigvecs
    overlap_norm = np.real(overlap * overlap.conjugate())

    for idx in range( overlap_norm.size) :
        print('The overlap integral with the exact eigenstates of energy ', eigvals[idx], ' is: ', overlap_norm[idx] )
    
    print('The sum of the calculated overlaps: ', np.sum(overlap_norm ) )  
    
    ##### //MB\\
    if iter_idx == 1:
        opt_VQE_Energy = np.loadtxt(project_name+"_costfuncs_and_entropy.txt")
        if opt_VQE_Energy[0,1] - opt_VQE_Energy[-1,1] < 1:
           break
   # if args.optimizer.upper() in ['NELDER_MEAD', 'POWELL', 'COBYLA']:
   #      break
    ##### \\MB//
    if ( VQE_energy < 0.99*eigval):
        break
        

##### //MB\\
logs['end_optimization'] = datetime.datetime.now().isoformat()
with open(project_name+"_logs.json", "w") as f:
    json.dump(logs, f, indent=4)
##### \\MB//
    
print("-- --- Finish optimization process --- --")
print() 
print()