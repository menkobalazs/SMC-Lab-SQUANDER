# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 14:42:56 2020
Copyright (C) 2020 Peter Rakyta, Ph.D.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/.

@author: Peter Rakyta, Ph.D.
"""

# @brief Automatic test procedures to test the functionalities of the code


import ctypes



#load test library for operations
_qgd_library = ctypes.cdll.LoadLibrary('.libs/libqgd.so')  





# *******************************
# test of general two qubit decomposition

# defining the input argument
_qgd_library.iface_new_N_Qubit_Decomposition.argtypes = (ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_int,)
_qgd_library.iface_new_N_Qubit_Decomposition.restype = ctypes.c_void_p
_qgd_library.iface_start_decomposition.argtypes = (ctypes.c_void_p,)
_qgd_library.iface_delete_N_Qubit_Decomposition.argtypes = (ctypes.c_void_p,)



# cerate unitary q-bit matrix
from scipy.stats import unitary_group
import numpy as np

    
# the number of qubits
qbit_num = 5
    
matrix_size = int(2**qbit_num)

Umtx = unitary_group.rvs(matrix_size)

# arranging all the elements of the matrix into one row (row major order)
Umtx_real = np.real(Umtx).reshape(matrix_size*matrix_size)
Umtx_imag = np.imag(Umtx).reshape(matrix_size*matrix_size)

# definig ctypes array storing the real and imaginary parts of the unitary
array_type = ctypes.c_double * (matrix_size*matrix_size)

# calling the test function
c_instance = _qgd_library.iface_new_N_Qubit_Decomposition( array_type(*Umtx_real), array_type(*Umtx_imag), ctypes.c_int(qbit_num) )

_qgd_library.iface_start_decomposition( c_instance )

_qgd_library.iface_delete_N_Qubit_Decomposition( c_instance )

fff

# *******************************
# test of general four qubit decomposition


# defining the input argument
_decomposition_test_library.four_qubit_decomposition.argtypes = (ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_int,)



# cerate unitary q-bit matrix
from scipy.stats import unitary_group
import numpy as np

    
# the number of qubits
qbit_num = 4
    
matrix_size = int(2**qbit_num)

Umtx = unitary_group.rvs(matrix_size)

# arranging all the elements of the matrix into one row (row major order)
Umtx_real = np.real(Umtx).reshape(matrix_size*matrix_size)
Umtx_imag = np.imag(Umtx).reshape(matrix_size*matrix_size)

# calling the test function
array_type = ctypes.c_double * (matrix_size*matrix_size)
_decomposition_test_library.four_qubit_decomposition( array_type(*Umtx_real), array_type(*Umtx_imag), ctypes.c_int(qbit_num) )




fff




from test import operations
from test import decomposition

#%% Tests of operations
operations.test_general_operation()
operations.test_U3_operation()
operations.test_CNOT_operation()
operations.test_operations()

#%% Test of two-qubit decomposition
decomposition.two_qubit_decomposition()

#%% Test of general three-qubit decomposition
decomposition.three_qubit_decomposition()

#%% Test of the decomposition of the IBM challenge
decomposition.IBM_challenge_decomposition()

#%% Test of general four-qubit decomposition
decomposition.four_qubit_decomposition()

#%% Test of the decomposition of "few CNOT unitary"
decomposition.few_CNOT_unitary_decomposition()

#%% Test of general five-qubit decomposition
decomposition.five_qubit_decomposition()
