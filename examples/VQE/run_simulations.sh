##### //MB\\

LAYERS=100
QUBITS=10

# Opt: ADAM
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=adam --init_parameters=zero --layers=$LAYERS --qbit_num=$QUBITS
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=adam --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS

# Opt: BFGS
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=bfgs --init_parameters=zero --layers=$LAYERS --qbit_num=$QUBITS
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=bfgs --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS

# Opt: COSINE
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=cosine --init_parameters=zero --layers=$LAYERS --qbit_num=$QUBITS
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=cosine --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS

# Opt: GRAD_DESCEND
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=grad_descend --init_parameters=zero --layers=$LAYERS --qbit_num=$QUBITS
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=grad_descend --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS

# Opt: GRAD_DESCEND_PARAMETER_SHIFT_RULE
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=grad_descend_parameter_shift_rule --init_parameters=zero --layers=$LAYERS --qbit_num=$QUBITS
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=grad_descend_parameter_shift_rule --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS

# Opt: POWELL
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=powell --init_parameters=zero --layers=$LAYERS --qbit_num=$QUBITS
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=powell --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS

# Opt: COBYLA
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=cobyla --init_parameters=zero --layers=$LAYERS --qbit_num=$QUBITS
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=cobyla --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS

# Opt: NELDER_MEAD
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=nelder_mead --init_parameters=zero --layers=$LAYERS --qbit_num=$QUBITS
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=nelder_mead --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS



#=================#
LAYERS=100
QUBITS=14

# Opt: ADAM
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=adam --init_parameters=zero --layers=$LAYERS --qbit_num=$QUBITS
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=adam --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS

# Opt: BFGS
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=bfgs --init_parameters=zero --layers=$LAYERS --qbit_num=$QUBITS
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=bfgs --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS

# Opt: COSINE
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=cosine --init_parameters=zero --layers=$LAYERS --qbit_num=$QUBITS
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=cosine --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS

# Opt: GRAD_DESCEND
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=grad_descend --init_parameters=zero --layers=$LAYERS --qbit_num=$QUBITS
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=grad_descend --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS

# Opt: GRAD_DESCEND_PARAMETER_SHIFT_RULE
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=grad_descend_parameter_shift_rule --init_parameters=zero --layers=$LAYERS --qbit_num=$QUBITS
hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=grad_descend_parameter_shift_rule --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS

# Opt: POWELL
#hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=powell --init_parameters=zero --layers=$LAYERS --qbit_num=$QUBITS
#hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=powell --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS

# Opt: COBYLA
#hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=cobyla --init_parameters=zero --layers=$LAYERS --qbit_num=$QUBITS
#hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=cobyla --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS

# Opt: NELDER_MEAD
#hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=nelder_mead --init_parameters=zero --layers=$LAYERS --qbit_num=$QUBITS
#hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=nelder_mead --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS


##### \\MB//

