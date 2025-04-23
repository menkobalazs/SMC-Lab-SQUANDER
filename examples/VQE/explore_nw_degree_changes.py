import numpy as np
import matplotlib.pyplot as plt
import json
import os
import argparse

FS=12 # fontsize for plots
COLORS = ["b", "g", "r", "navy"]
COLORS2 = ["c", "m", "y"]


import networkx as nx
import matplotlib.pyplot as plt
from networkx.generators.random_graphs import random_regular_graph
from qiskit.quantum_info import SparsePauliOp


def generate_hamiltonian(qubits, degree=3, random_seed=31415):
    return random_regular_graph(degree, qubits, seed=random_seed) 


def loadjson(filename):
    with open(filename, "r") as f:
        loaded_data = json.load(f)
    return loaded_data

parser = argparse.ArgumentParser(description="Explore simulations of VQE algorithm.")
parser.add_argument("-f", "--format", help="File format of saved figures", 
                    type=str, default='jpg',
                    choices=['jpg', 'pdf'])
args = parser.parse_args()

### Used optimizers:
# 'ADAM', 'BFGS', 'COSINE', 'GRAD_DESCEND', 'GRAD_DESCEND_PARAMETER_SHIFT_RULE', <-- gradient-based optimizers
# 'POWELL', 'COBYLA', 'NELDER_MEAD' <-- gradient-free optimizers
optimizers = ['ADAM', 'COSINE', 'POWELL']
optimizers_labels = ['ADAM', 'Cosine', 'Powell']
hlines_linestyles = ['solid', 'dashdot', 'dashed']
plot_linestyles = ['-', '-.', '- -']

# initial parameters; number of layers; number of qubits
ip, lyr, qb = 'random', 100, 12

# Generated dataset constants
random_seeds = [42, 137, 4242, 999999] 
degrees= [2,3,4]


# figures for different degrees
for i, degree in enumerate(degrees): 
    plt.figure(figsize=(6, 4))  
    # save topologies
    topology = generate_hamiltonian(qb, degree=degree)
    plt.figure(figsize=(8, 6))
    nx.draw(topology, with_labels=True, node_color=COLORS2[i], edge_color='black',
            node_size=800, font_size=30, font_weight='bold')
    plt.title(f"d={degrees[i]}", fontsize=30)
    plt.savefig(f"figures/{args.format}/degree/graph_initp={ip}_lyr={lyr}_qb={qb}_d={degree}." + args.format, bbox_inches="tight")
    plt.close()
    
    plt.figure(figsize=(6, 4))  
    for k, opt in enumerate(optimizers):
        E_g = loadjson(f"data/{opt}/initp={ip}_lyr={lyr}_qb={qb}_d={degree}_logs.json")['ground_state_of_Hamiltonian']
        data = np.loadtxt(f"data/{opt}/initp={ip}_lyr={lyr}_qb={qb}_d={degree}_costfuncs_and_entropy.txt")
        
        if k==0:
            plt.hlines(E_g, 0, 1e9, color=COLORS[-1], linestyles=hlines_linestyles[0],
                       label=rf'$E_{{ground}}$')
        plt.plot(data[:, 0], data[:, 1], plot_linestyles[0], color=COLORS[k],
                 label=f'{optimizers_labels[k]}')
        
    plt.title(f"d={degree}\n" +
              rf"$N_{{qubits}}={qb}$, " + rf"$N_{{layers}}={lyr}$",
              fontsize=FS+3)
    plt.xlabel("Number of cost function evaluations", fontsize=FS)
    plt.ylabel("Minimized energy", fontsize=FS)
    plt.xticks(fontsize=FS-3)
    plt.yticks(fontsize=FS-3)
    plt.xlim(-5e3, 5e5)
    plt.legend(loc='upper right', fontsize=FS-4)
    plt.grid()
    plt.savefig(f"figures/{args.format}/degree/initp={ip}_lyr={lyr}_qb={qb}_d={degree}." + args.format, bbox_inches="tight")

    print(f"Figures saved. Format: {args.format}; initial parameter: {ip}; layers={lyr}; qubits={qb}")

print("---")

# figures for different seed values

if False: # For the third presentation not all simulations finished.
    fixed_degree=3

    for k, opt in enumerate(optimizers):
        plt.figure(figsize=(6, 4))

        for j, seed in enumerate(random_seeds):
            seed_label = f's={seed}'
            filename_base = f"data/{opt}/initp={ip}_lyr={lyr}_qb={qb}_d={fixed_degree}_s={seed}"
            E_g = loadjson(f"{filename_base}_logs.json")['ground_state_of_Hamiltonian']
            data = np.loadtxt(f"{filename_base}_costfuncs_and_entropy.txt")
            
            plt.hlines(E_g, 0, 1e9, color=COLORS[j], linestyles='dashed',
                    label=rf'$E_{{ground}}$(seed={seed})')
            plt.plot(data[:, 0], data[:, 1], '-', color=COLORS[j],
                    label=f'seed={seed}')

        plt.title(f"{optimizers_labels[k]} optimizer, fixed degree={fixed_degree}\n" +
                rf"$N_{{qubits}}={qb}$, $N_{{layers}}={lyr}$", fontsize=FS+3)
        plt.xlabel("Number of cost function evaluations", fontsize=FS)
        plt.ylabel("Minimized energy", fontsize=FS)
        plt.xticks(fontsize=FS-3)
        plt.yticks(fontsize=FS-3)
        plt.legend(loc='upper right', fontsize=FS-4)
        plt.grid()
        plt.xlim(xlims[k])

        save_path = f"figures/{args.format}/seed/{opt}"
        os.makedirs(save_path, exist_ok=True)
        plt.savefig(f"{save_path}/initp={ip}_lyr={lyr}_qb={qb}_d={fixed_degree}.{args.format}", bbox_inches="tight")
        print(f"Figures for different seeds saved in {save_path}")








