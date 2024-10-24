# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 14:42:56 2020
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
"""
## \file example_heavy_hex.py
## \brief Example to decompose on heavy hexagonal lattice



# cerate unitary q-bit matrix
from scipy.stats import unitary_group
from squander import utils
import numpy as np



def create_custom_gate_structure_heavy_hex_3(qbit_num):
    r"""
    This method is called to create custom gate structure for the decomposition on IBM QX2

    """

    from squander import Circuit

    # creating an instance of the wrapper class Circuit
    Circuit_ret = Circuit( qbit_num )

    disentangle_qubit = qbit_num - 1 

        

    for qbit in range(0, disentangle_qubit ):

        # creating an instance of the wrapper class Circuit
        Layer = Circuit( qbit_num )


        if qbit == 0:

            # add U3 fate to the block
            Theta = True
            Phi = False
            Lambda = True      
            Layer.add_U3( 0, Theta, Phi, Lambda )                 
            Layer.add_U3( disentangle_qubit, Theta, Phi, Lambda ) 

            # add CNOT gate to the block
            Layer.add_CNOT( 0, disentangle_qubit)

        elif qbit == 1:

            # add U3 fate to the block
            Theta = True
            Phi = False
            Lambda = True      
            Layer.add_U3( 0, Theta, Phi, Lambda )                 
            Layer.add_U3( 1, Theta, Phi, Lambda ) 

            # add CNOT gate to the block
            Layer.add_CNOT( 0, 1)



        elif qbit == 2:

            # add U3 fate to the block
            Theta = True
            Phi = False
            Lambda = True      
            Layer.add_U3( 2, Theta, Phi, Lambda )                 
            Layer.add_U3( disentangle_qubit, Theta, Phi, Lambda ) 

            # add CNOT gate to the block
            Layer.add_CNOT( disentangle_qubit, 2 )

         

        Circuit_ret.add_Circuit( Layer )

    return Circuit_ret





def create_custom_gate_structure_heavy_hex_4(qbit_num):
    r"""
    This method is called to create custom gate structure for the decomposition on IBM QX2

    """

    from squander import Circuit

    # creating an instance of the wrapper class Circuit
    Circuit_ret = Circuit( qbit_num )

    disentangle_qubit = qbit_num - 1 

        

    for qbit in range(0, disentangle_qubit ):

        # creating an instance of the wrapper class Circuit
        Layer = Circuit( qbit_num )


        if qbit == 0:

            # add U3 fate to the block
            Theta = True
            Phi = False
            Lambda = True      
            Layer.add_U3( 0, Theta, Phi, Lambda )                 
            Layer.add_U3( disentangle_qubit, Theta, Phi, Lambda ) 

            # add CNOT gate to the block
            Layer.add_CNOT( 0, disentangle_qubit)

        elif qbit == 1:

            # add U3 fate to the block
            Theta = True
            Phi = False
            Lambda = True      
            Layer.add_U3( 0, Theta, Phi, Lambda )                 
            Layer.add_U3( 1, Theta, Phi, Lambda ) 

            # add CNOT gate to the block
            Layer.add_CNOT( 0, 1)



        elif qbit == 2:

            # add U3 fate to the block
            Theta = True
            Phi = False
            Lambda = True      
            Layer.add_U3( 2, Theta, Phi, Lambda )                 
            Layer.add_U3( 0, Theta, Phi, Lambda ) 

            # add CNOT gate to the block
            Layer.add_CNOT( 0, 2)

         

        Circuit_ret.add_Circuit( Layer )

    return Circuit_ret
    


from squander import N_Qubit_Decomposition

# the number of qubits spanning the unitary
qbit_num = 4

# determine the soze of the unitary to be decomposed
matrix_size = int(2**qbit_num)
   
# creating a random unitary to be decomposed
Umtx = unitary_group.rvs(matrix_size)
    
# creating an instance of the C++ class
decomp = N_Qubit_Decomposition( Umtx.conj().T )


# create custom gate structure
gate_structure = { 4: create_custom_gate_structure_heavy_hex_4(4), 3: create_custom_gate_structure_heavy_hex_3(3)}        


# adding custom gate structure to the decomposition
decomp.set_Gate_Structure( gate_structure )


# set the maximal number of layers in the decomposition
decomp.set_Max_Layer_Num( {4: 60, 3:16} )

# set the number of block to be optimized in one shot
decomp.set_Optimization_Blocks( 20 )

# starting the decomposition
decomp.Start_Decomposition()   


# list the decomposing operations
decomp.List_Gates()

# get the decomposing operations
quantum_circuit = decomp.get_Qiskit_Circuit()


import numpy.linalg as LA
    
# the unitary matrix from the result object
decomposed_matrix = utils.get_unitary_from_qiskit_circuit( quantum_circuit )
product_matrix = np.dot(Umtx,decomposed_matrix.conj().T)
phase = np.angle(product_matrix[0,0])
product_matrix = product_matrix*np.exp(-1j*phase)
    
product_matrix = np.eye(matrix_size)*2 - product_matrix - product_matrix.conj().T
# the error of the decomposition
decomposition_error =  (np.real(np.trace(product_matrix)))/2
       
print('The error of the decomposition is ' + str(decomposition_error))
