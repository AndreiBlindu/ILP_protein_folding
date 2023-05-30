import numpy as np

def get_even_indices(n):
    Ie = []
    for i in range(n):
        if i % 2 == 0:
            Ie.append(i)
    return Ie

def get_odd_indices(n):
    Io = []
    for i in range(n):
        if i % 2 == 1:
            Io.append(i)
    return Io

def get_HP_indices(seq, polarity, parity):
    indices = []
    for idx in range(len(seq)):
        if idx % 2 == parity and seq[idx] == str(polarity):
            indices.append(idx)
    return indices

def get_feasible_set(m, n, l_size):
    E = []
    l2 = l_size*l_size
    for v in range(m):
        for w in range(m):
            #if w == v-1 or w == v+1 or w == v-n or w == v+n:
            if (w == v-1 and (w+1)%l_size != 0) or (w == v+1 and w%l_size != 0) or (w == v-l_size and w // l2 == v // l2) or (w == v+l_size and w // l2 == v // l2) or w == v+l2 or w == v-l2:
                E.append((v,w))
    return E

def neighboring_set_3d(v, l_size):
    lattice_size = l_size*l_size*l_size
    l2 = l_size*l_size
    n_set = []

    for k in range(lattice_size):
        if (k == v-1 and (k+1)%l_size != 0) or (k == v+1 and k%l_size != 0) or (k == v-l_size and k // l2 == v // l2) or (k == v+l_size and k // l2 == v // l2) or k == v+l2 or k == v-l2 :
            n_set.append(k)
    
    return n_set

def convert_1d_to_3d(v, l_size):
    l2 = l_size*l_size
    return (v % l_size, v % l2 // l_size, v // l2)

def lattice_positions_from_optimal(X, l_size):
    x_positions = []
    y_positions = []
    z_positions = []
    positions = []
    pos = []
    for i in range(len(X)):
        for v in range(len(X[i])):
            if X[i][v] == 1:
                x, y, z = convert_1d_to_3d(v, l_size)
                x_positions.append(x)
                y_positions.append(y)
                z_positions.append(z)
                positions.append((x,y,z))
                pos.append(v)
    return np.asarray(x_positions), np.asarray(y_positions), np.asarray(z_positions), np.asarray(positions), np.asarray(pos)