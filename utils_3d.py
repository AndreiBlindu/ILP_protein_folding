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