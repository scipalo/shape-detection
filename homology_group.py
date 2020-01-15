import shape_detection
import collections
import ast

def prave_betti(tabela_betties):
    tabela = [*zip(*tabela_betties)]
    dic_0 = isci_beti(tabela[0])
    dic_1 = isci_beti(tabela[1])
    dic_2 = isci_beti(tabela[2])
    return ([dic_0,  dic_1,  dic_2])


def isci_beti(sez):
    dic = {}
    betti = sez[0]
    st = 1
    X = collections.deque(sez[1:])
    while X:
        i = X.popleft()
        if i == betti:
            st += 1
        else:
            #print(betti, dic, st)
            if betti in dic.keys():
                dic[betti] = max(st, dic[betti])
            else:
                dic[betti] = st
            betti = i
            st = 1
    if i in dic.keys():
        dic[betti] = max(st, dic[i])
    else:
        dic[betti] = st
    res = []
    for j in dic.keys():
        if round(dic[j]/len(sez), 2)>=0.3:
            res.append(j)
    return (max(res))

def doloci_hom_group(filename):
    table = []
    with open('betti/'+filename+'.txt', 'r') as f:
        for line in f:
            table.append(ast.literal_eval(line))
    f.close()
    print(prave_betti(table))
    return(prave_betti(table))

#learning
#circle_betti [1, 1, 0]
#line_betti [1, 0, 0]
#plane_betti [1, 0, 0]
#sphere_betti [1, 0, 1]
#torus_betti [1, 2, 1]

#testing
betti = doloci_hom_group('test_plane_betti')
shape_detection.shape_detection('plane3', betti)