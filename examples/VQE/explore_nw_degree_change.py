import numpy as np
import matplotlib.pyplot as plt
import json
import argparse
FS=20 # fontsize for plots
COLORS = ["b", "g", "r", "c", "m", "y", "navy", 'orange', '']

def loadjson(filename):
    with open(filename, "r") as f:
        loaded_data = json.load(f)
    return loaded_data

parser = argparse.ArgumentParser(description="Explore simulations of VQE algorithm.")
parser.add_argument("-f", "--format", help="File format of saved figures", 
                    type=str, default='jpg',
                    choices=['jpg', 'pdf'])
args = parser.parse_args()

### Possible optimizers:
# 'ADAM', 'BFGS', 'COSINE', 'GRAD_DESCEND', 'GRAD_DESCEND_PARAMETER_SHIFT_RULE', <-- gradient-based optimizers
# 'POWELL', 'COBYLA', 'NELDER_MEAD' <-- gradient-free optimizers
optimizers = ['ADAM', 'COSINE', 'POWELL']
optimizers_labels = ['ADAM', 'Cosine', 'Powell']
hlines_linestyles = ['dashed', 'dashdot', 'solid']
plot_linestyles = ['--', '-.', '-']

# initial parameters; number of layers; number of qubits
ip, lyr, qb = 'random', 100, 12

data = []
E_ground = []
for opt in optimizers:
    for degree in [2,3,4]:
        E_ground.append(loadjson(f"data/{opt}/initp={ip}_lyr={lyr}_qb={qb}_d={degree}_logs.json")['ground_state_of_Hamiltonian'])



plt.figure(figsize=(16,9))

for i in range(3):
    degree = i+2
    plt.hlines(E_ground[i], 0, 1e9,  color='black', linestyles=hlines_linestyles[i], label=r'$E_{ground}$'+f'(d={degree})')
    for k, opt in enumerate(optimizers):
        data = np.loadtxt(f"data/{opt}/initp={ip}_lyr={lyr}_qb={qb}_d={degree}_costfuncs_and_entropy.txt")
        plt.plot(data[:,0], data[:,1], plot_linestyles[i], color=COLORS[k], label=optimizers_labels[k])#+f' d={degree}')
        
plt.title(r"Optimization process with different network degree in $\hat{H}$ generation"+"\n"+\
              f"{ip} initial parameter, "+r"$N_{qubits}=$"+f"{qb}, "+\
              r"$N_{layers}=$"+f"{lyr}", fontsize=FS+3)
plt.xlabel("Number of cost function evaluation", fontsize=FS)
plt.ylabel("Minimized energy", fontsize=FS)
plt.xticks(fontsize=FS-3)  
plt.yticks(fontsize=FS-3)
plt.xlim(-5e4, 5e6)
plt.legend(loc='upper right', fontsize=FS-4)
plt.grid()
plt.savefig(f"figures/{args.format}/degree/initp={ip}_lyr={lyr}_qb={qb}_d=2-3-4."+args.format, bbox_inches="tight")

plt.xlim(1, 1e9)
plt.xscale('log')
plt.savefig(f"figures/{args.format}/degree/initp={ip}_lyr={lyr}_qb={qb}_d=2-3-4_log_scaled."+args.format, bbox_inches="tight")
print(f"Figures saved. Format: {args.format}; initial parameter: {ip}; layers={lyr}; qubits={qb}")
