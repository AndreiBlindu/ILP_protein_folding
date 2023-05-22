import numpy as np
import matplotlib.pyplot as plt

#%pip install networkx
import networkx as nx

def get_binary_string(sequence):
    binary = ""
    for amino_acid in sequence:
        if amino_acid == "H":
            binary += "1"
        elif amino_acid == "P":
            binary += "0"
        else:
            raise Exception("Invalid sequence, only 'H' and 'P' are allowed")
    return binary

def neighboring_set(p, n):
    grid_size = n*n
    n_set = []

    for k in range(grid_size-1):
        if k == p-1 or k == p+1 or k == p-n or k == p+n:
            n_set.append(k)
    
    return n_set

def get_hydrophobic_set(seq):
    hydrophobic_set = []
    for idx in range(len(seq)):
        if seq[idx] == "1":
            hydrophobic_set.append(idx)
    return hydrophobic_set

def calculate_offset(seq):
    count = 0
    for i in range(len(seq) - 1):
        if seq[i] == "1" and seq[i+1] == "1":
            count += 1
    return count

def plot_folding(protein_binary_sequence, protein_sequence, positions, d):
    data = np.asarray(positions)
    n = len(protein_binary_sequence)

    H_set = get_hydrophobic_set(protein_binary_sequence)
    P_set = list(set(np.arange(0,n)) - set(H_set))

    plt.title("Protein sequence: "+protein_sequence)
    plt.plot(data[:,0], data[:,1], 'black') # line segments
    plt.scatter(data[P_set,0], data[P_set,1], c='b', label="P")
    plt.scatter(data[H_set,0], data[H_set,1], c='r', label="H")
    plt.axis([-0.2, d+0.2, -0.2, d+0.2])
    plt.rc('grid', linestyle="--", color='grey')
    plt.grid(True)
    plt.legend()

    plt.show()

def is_adjacent(i, j, u, v):
    return ( u == i and abs(v-j) == 1 ) or ( v == j and abs(u-i) == 1 )

def build_graph(binary_seq):
    G = nx.Graph()

    n = len(binary_seq)
    grid_size = 2*n - 1

    # add nodes
    for i in range(grid_size):
        for j in range(i, grid_size):
                G.add_node( (i, j) )

    # add edges
    for i, j in G.nodes():
         for u, v in G.nodes():
              if is_adjacent(i, j, u, v):
                   G.add_edge( (i, j), (u, v) )
    
    return G