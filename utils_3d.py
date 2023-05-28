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

def get_feasible_set(m, n):
    E = []
    for v in range(m):
        for w in range(m):
            if w == v-1 or w == v+1 or w == v-n or w == v+n:
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