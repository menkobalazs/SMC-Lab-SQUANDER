##### //MB\\

LAYERS=60
QUBITS=12

# Opt: GRAD_DESCEND
hwloc-bind --membind node:0 --cpubind node:0 -- python Heisenberg_VQE.py --optimizer=grad_descend --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS

##### \\MB//

