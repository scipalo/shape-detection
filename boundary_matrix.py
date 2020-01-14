import numpy as np
from mogutda import SimplicialComplex
import ast
import timeit


def betti(complex):
    betti = []
    # find max dimension
    max_dim = max([len(c) for c in complex])
    sim_com = SimplicialComplex(simplices=complex)
    for i in range(3):
        betti.append(sim_com.betti_number(i))
    return (betti)

def betti_numbers(VRs, epsilon):
    VR_data = []
    VR_epslons = []
    with open(VRs, 'r') as f:
        for line in f:

            if (line.split()[0]) == 'Epsilon:':
                pass

            else:
                seznam = ''
                for j in line.split()[1:]:
                    seznam += j
                VR_data.append(ast.literal_eval(seznam))
    f.close()

    betties = []
    dolzina_b = []
    for i in VR_data:
        start = timeit.default_timer()
        b = betti(i)
        time = timeit.default_timer() - start
        print('betti cas:', time)
        betties.append(b)
        dolzina_b.append(len(b))

    n = max(dolzina_b)
    for idi, i in enumerate(betties):
        betties[idi] = i + [0 for j in range(n - dolzina_b[idi])]
    return betties

def betti_direkt(VR):
    betties = []
    #dolzina_b = []
    start = timeit.default_timer()
    b = betti(VR)
    time = timeit.default_timer() - start
    print('betti cas:', time)
    return b

def test_betti():

    C = [(1, 2, 3), (3, 4), (4, 2)]
    torus_sc = [(1, 2, 4), (4, 2, 5), (2, 3, 5), (3, 5, 6), (5, 6, 1), (1, 6, 2), (6, 7, 2), (7, 3, 2),
                (1, 3, 4), (3, 4, 6), (4, 6, 7), (4, 5, 7), (5, 7, 1), (7, 3, 1)]
    torus_c = SimplicialComplex(simplices=torus_sc)

    t1 = timeit.default_timer()
    print(betti_numbers('complexes/1.0/circle.txt', 0))
    t2 = timeit.default_timer()
    print('cas circle:', t2 - t1)
    print(betti_numbers('complexes/1.0/line.txt', 0))
    t3 = timeit.default_timer()
    print('cas line', t3 - t2)
    print(betti_numbers('complexes/1.0/sphere.txt', 0))
    t4 = timeit.default_timer()
    print('cas sphere', t4 - t3)
    print(betti_numbers('complexes/1.0/torus.txt', 0))
    t5 = timeit.default_timer()
    print('cas torus:', t5 - t4)
    print(betti_numbers('complexes/1.0/plane.txt', 0))
    t6 = timeit.default_timer()
    print('cas plane:',t6 - t5)