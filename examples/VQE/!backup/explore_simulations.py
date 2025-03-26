import numpy as np
import matplotlib.pyplot as plt
import json
import argparse
FS=20 # fontsize for plots
COLORS = ["b", "g", "r", "c", "m", "y", "navy", 'orange']

def loadjson(filename):
    with open(filename, "r") as f:
        loaded_data = json.load(f)
    return loaded_data

parser = argparse.ArgumentParser(description="explore_simulations.py")
parser.add_argument("-f", "--format", help="File format of saved figures", 
                    type=str, default='jpg',
                    choices=['jpg', 'pdf'])
args = parser.parse_args()

### Used optimizers:
# 'ADAM', 'BFGS', 'COSINE', 'GRAD_DESCEND', 'GRAD_DESCEND_PARAMETER_SHIFT_RULE', <-- gradient-based optimizers
# 'POWELL', 'COBYLA', 'NELDER_MEAD' <-- gradient-free optimizers
optimizers = ['ADAM', 'BFGS', 'COSINE', 'GRAD_DESCEND', 'GRAD_DESCEND_PARAMETER_SHIFT_RULE', 'POWELL', 'COBYLA', 'NELDER_MEAD']

# initial parameters; number of layers; number of qubits
fig_params = [
    ['zero', 100, 10], 
    ['random', 100, 10],
    ['zero', 100, 14],
    ['random', 100, 14]
]

# plotting method
for ip, lyr, qb in fig_params:
    data = []
    existing_optimizers = []
    max_num_of_cost_func_eval_per_method = []
    for opt in optimizers:
        try:             
            data.append(np.loadtxt(f"{opt}/initp={ip}_lyr={lyr}_qb={qb}_costfuncs_and_entropy.txt"))
            existing_optimizers.append(opt)
            max_num_of_cost_func_eval_per_method.append(data[-1][-1][0])
        except:
            pass
    logs = loadjson(f"{existing_optimizers[0]}/initp={ip}_lyr={lyr}_qb={qb}_logs.json")
    
    plt.figure(figsize=(16,9))
    plt.hlines(logs['ground_state_of_Hamiltonian'], -5e5, max(max_num_of_cost_func_eval_per_method)*1.05,  color='black', linestyles='dashdot', label=r'$E_{ground}$')
    for i, opt in enumerate(data):
        try:
            plt.plot(opt[:,0], opt[:,1], color=COLORS[i], label=existing_optimizers[i])
        except:
            pass
    plt.title("Optimization process with different methods\n"+\
              f"{ip} initial parameter, "+r"$N_{qubits}=$"+f"{lyr}, "+\
              r"$N_{layers}=$"+f"{qb}", fontsize=FS+3)
    plt.xlabel("Number of cost function evaluation", fontsize=FS)
    plt.ylabel("Minimized energy", fontsize=FS)
    plt.xticks(fontsize=FS-3)  
    plt.yticks(fontsize=FS-3)
    plt.xlim(-5e5, max(max_num_of_cost_func_eval_per_method))
    plt.legend(loc='upper right', fontsize=FS-4)
    plt.grid()
    plt.savefig(f"figures/{args.format}/initp={ip}_lyr={lyr}_qb={qb}."+args.format, bbox_inches="tight")
    plt.xlim(-5e4, max(max_num_of_cost_func_eval_per_method)*0.1)
    plt.savefig(f"figures/{args.format}/initp={ip}_lyr={lyr}_qb={qb}_zoomed."+args.format, bbox_inches="tight")
    print(f"Figure 'figures/{args.format}/initp={ip}_lyr={lyr}_qb={qb}.{args.format}' saved.")


