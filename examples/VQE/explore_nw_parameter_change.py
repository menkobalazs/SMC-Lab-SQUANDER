import numpy as np
import matplotlib.pyplot as plt
import json
import os
import argparse

FS=12 # fontsize for plots
COLORS = ["b", "g", "r", "navy"]
COLORS2 = ["c", "m", "y", 'purple']


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

optimizers = ['ADAM', 'COSINE', 'POWELL']
optimizers_labels = ['ADAM', 'Cosine', 'Powell']
hlines_linestyles = ['solid', 'dashdot', 'dashed']
plot_linestyles = ['-', '-.', '--']

# initial parameters; number of layers; number of qubits
ip, lyr, qb = 'random', 100, 12

# Generated dataset constants
random_seeds = [42, 137, 31415, 999999] 
degrees = [2,3,4]
fixed_degree = 3

# figures for different random seeds
print("-- figures for different random seeds")
for i, seed in enumerate(random_seeds):
    topology = generate_hamiltonian(qb, degree=fixed_degree, random_seed=seed)
    plt.figure(figsize=(8, 6))
    nx.draw(topology, with_labels=True, node_color=COLORS2[i], edge_color='black',
            node_size=2500, font_size=35, font_weight='bold')
    plt.title(f"d=3, seed={seed}", fontsize=30)
    plt.savefig(f"figures/{args.format}/seed/graph_initp={ip}_lyr={lyr}_qb={qb}_d={fixed_degree}_s={seed}." + args.format, bbox_inches="tight")
    plt.close()
    
    plt.figure(figsize=(6, 4))
    for k, opt in enumerate(optimizers):
        seed_label = f's={seed}'
        filename_base = f"data/{opt}/initp={ip}_lyr={lyr}_qb={qb}_d={fixed_degree}_s={seed}"
        E_g = loadjson(f"{filename_base}_logs.json")['ground_state_of_Hamiltonian']
        data = np.loadtxt(f"{filename_base}_costfuncs_and_entropy.txt")
        
        plt.plot(data[:, 0], data[:, 1], '-', color=COLORS[k],
                label=f'{optimizers_labels[k]}')
        
    plt.hlines(E_g, 0, 1e9, color='black', linestyles='dashed',
                label=rf'$E_{{ground}}$')

    plt.title(f"Seed={seed}\n" +
              rf"$N_{{qubits}}={qb}$, " + rf"$N_{{layers}}={lyr}$",
              fontsize=FS+3)
    plt.xlabel("Number of cost function evaluations", fontsize=FS)
    plt.ylabel("Minimized energy", fontsize=FS)
    plt.xticks(fontsize=FS-3)
    plt.yticks(fontsize=FS-3)
    plt.legend(loc='upper right', fontsize=FS-4)
    plt.grid()
    plt.xlim(-5e3, 1e6)
    
    save_path = f"figures/{args.format}/seed"
    os.makedirs(save_path, exist_ok=True)
    plt.savefig(f"{save_path}/initp={ip}_lyr={lyr}_qb={qb}_d={fixed_degree}_s={seed}.{args.format}", bbox_inches="tight")
    print(f"Figures for different seeds saved in {save_path}")

print("---")




# figures for different degrees
for i, degree in enumerate(degrees): 
    topology = generate_hamiltonian(qb, degree=degree)
    plt.figure(figsize=(8, 6))
    nx.draw(topology, with_labels=True, node_color=COLORS2[i], edge_color='black',
            node_size=2500, font_size=30, font_weight='bold')
    plt.title(f"d={degrees[i]}", fontsize=35)
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

# figures for different degrees
print("--  figures for different degrees")
for i, degree in enumerate(degrees): 
    topology = generate_hamiltonian(qb, degree=degree)
    plt.figure(figsize=(8, 6))
    nx.draw(topology, with_labels=True, node_color=COLORS2[i], edge_color='black',
            node_size=2500, font_size=30, font_weight='bold')
    plt.title(f"d={degrees[i]}", fontsize=35)
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
