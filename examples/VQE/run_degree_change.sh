##### //MB\\

LAYERS=100
QUBITS=12
DEGREES=(2 3 4)
SEEDS=(42 137 31415 999999)
OPTIMIZERS=("adam" "cosine" "powell")


# Generate datasets with different random seed
for OPT in "${OPTIMIZERS[@]}"; do
    for SEED in "${SEEDS[@]}"; do
        hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=$OPT --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS --random_seed=$SEED --max_func_eval=2e6 --max_outer_iter=35
    done
done


# Generate datasets with different degrees
for OPT in "${OPTIMIZERS[@]}"; do
    for DEGREE in "${DEGREES[@]}"; do
        hwloc-bind --membind node:0 --cpubind node:0 -- python3 Heisenberg_VQE.py --optimizer=$OPT --init_parameters=random --layers=$LAYERS --qbit_num=$QUBITS --degree=$DEGREE --max_func_eval=2e6 --max_outer_iter=35
    done
done

##### \\MB//



