'''
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

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/.

'''

import numpy as np
import time
import random






from qiskit import QuantumCircuit
import numpy as np



from squander import utils
from squander import Circuit
from squander import Qiskit_IO



try:
    from mpi4py import MPI
    MPI_imported = True
except ModuleNotFoundError:
    MPI_imported = False


##
# @brief Function to generate a test Qiskit circuit
# @return Returns with a QISKIT circuit
def pauli_exponent( alpha=0.6217*np.pi ):
	# creating Qiskit quantum circuit
	qc_orig = QuantumCircuit(5)
	
	qc_orig.h(1)
	qc_orig.cx(1,2)

	qc_orig.rx(np.pi/2,0)
	qc_orig.rx(np.pi/2,1)
	qc_orig.cx(2,4)
	qc_orig.cx(0,1)

	qc_orig.rx(np.pi/2,0)
	qc_orig.h(2)
	qc_orig.cx(0,2)


	qc_orig.rx(np.pi/2,0)
	qc_orig.h(3)
	qc_orig.rz(alpha,4)
	qc_orig.cx(0,3)

	qc_orig.h(0)
	qc_orig.rz(-alpha,1)
	qc_orig.cx(2,4)

	qc_orig.cx(2,1)
	qc_orig.rz(-alpha,4)
	qc_orig.cx(3,1)

	qc_orig.rz(alpha,1)
	qc_orig.cx(0,1)
	qc_orig.cx(3,1)
	qc_orig.cx(4,1)

	qc_orig.rz(-alpha,1)
	qc_orig.cx(2,1)

	qc_orig.rz(alpha,1)
	qc_orig.cx(3,1)
	qc_orig.cx(4,1)

	qc_orig.rz(alpha,1)
	qc_orig.cx(2,4)
	qc_orig.cx(0,1)

	qc_orig.h(0)
	qc_orig.cx(3,1)
	qc_orig.cx(0,3)

	qc_orig.rx(-np.pi/2,0)
	qc_orig.h(3)
	qc_orig.cx(0,2)

	qc_orig.rx(-np.pi/2,0)
	qc_orig.h(2)
	qc_orig.cx(0,1)

	qc_orig.rx(-np.pi/2,0)
	qc_orig.rx(-np.pi/2,1)
	qc_orig.cx(2,4)
	qc_orig.cx(1,2)
	qc_orig.h(1)
	
	return qc_orig





class Test_Qiskit_IO:
    """This is a test class of the python iterface to the decompsition classes of the QGD package"""


    def test_circuit_import(self):

	# load circuit via Qiskit from QASM
        qc_trial = pauli_exponent()#
        
        # get the unitary of the quantum circuit
        Umtx = utils.get_unitary_from_qiskit_circuit( qc_trial )
        
        Circuit_Squander, parameters = Qiskit_IO.convert_Qiskit_to_Squander( qc_trial )
        
       
        input = (Umtx.conj().T).copy()
        Circuit_Squander.apply_to( parameters, input )

        input = input * np.conj(input[0,0]) - np.eye( input.shape[0], dtype=np.complex128 )

        
        from numpy import linalg as LA
        norm = LA.norm( input )
        
        assert( norm < 1e-6 )


        gates = Circuit_Squander.get_Gates()
        for gate in gates:
            print( gate )

        input = (Umtx.conj().T).copy()
        gates[1].apply_to( input )



