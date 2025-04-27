##### //MB\\

LAYERS=100
QUBITS=12
DEGREES=(2 3 4)
SEEDS=(42 137 4242 999999)
OPTIMIZERS=("adam" "cosine" "powell")


for OPT in "${OPTIMIZERS[@]}"; do
    for SEED in "${SEEDS[@]}"; do
        hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=$OPT --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS --degree=3 --random_seed=$SEED
    done
done



# Generate datasets with different degrees

#for OPT in "${OPTIMIZERS[@]}"; do
#    for DEGREE in "${DEGREES[@]}"; do
#        hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=$OPT --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS --degree=$DEGREE
#    done
#done

##### \\MB//



