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

import pickle



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
    topology = random_regular_graph(3,n,seed=31415).edges
    oplist = []
    for i in topology:
        oplist.append(("XX",[i[0],i[1]],1))
        oplist.append(("YY",[i[0],i[1]],1))
        oplist.append(("ZZ",[i[0],i[1]],1))
    for i in range(n):
        oplist.append(("Z",[i],1))
    return SparsePauliOp.from_sparse_list(oplist,num_qubits=n).to_matrix(True)





# The number of circuit layers
layers = 20

# the number of subblocks in a single layer
inner_blocks = 1

# The number of qubits
qbit_num = 10



# generate the Hamiltonian
Hamiltonian = generate_hamiltonian_tmp( qbit_num )


# obtain the groud state energy of the Hamitonian
[eigvals, eigvecs] = sp.sparse.linalg.eigs( Hamiltonian, k=10, which='SR' )
eigval = np.real(eigvals[0])
eigvec = eigvecs[:,0]

print( 'The target eigenvalue is: ', eigval )


# generate configuration dictionary for the solver
config = {"max_inner_iterations":800, 
	"batch_size": 128,
	"convergence_length": 20}

# initiate the VQE object with the Hamiltonian
VQE_Heisenberg = Variational_Quantum_Eigensolver(Hamiltonian, qbit_num, config)

# set the optimization engine to agents
VQE_Heisenberg.set_Optimizer("grad_descend_parameter_shift_rule")

print("--- End program.")

