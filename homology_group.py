import collections

def prave_betti(tabela_betties):
    tabela = [*zip(*tabela_betties)]
    dic_0 = isci_beti(tabela[0])
    dic_1 = isci_beti(tabela[1])
    dic_2 = isci_beti(tabela[2])
    print(dic_0, '\n', dic_1, '\n', dic_2)


def isci_beti(sez):
    dic = {}
    beti = 0
    st = 1
    X = collections.deque(sez)
    while X:
        i = X.popleft()
        if i == betti:
            st += 1
        else:
            if i in dic.keys:
                dic[beti] = max(st, dic[i])
            else:
                dic[beti] = st
            betti = i
            st = 1
    return dic

# GET BETTI NUMBER ARRAYS
m = 'circle_betti'
with open("shape-detection/betti/"+m+"txt", 'w') as g:
   for betti in betti_table:
       g.write('{} {} {}'.format(betti(0), betti(1), betti(2)))
g.close()

# DETECT SHAPES
# detect shape