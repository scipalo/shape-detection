import matplotlib.pyplot as plt
from numpy.linalg import norm
import numpy
import networkx as nx
import blender_import
import itertools
import timeit

def naive_vr(points, epsilon, draw):

   # get edge list

   pointsIter = [numpy.array(x) for x in points]
   vrComplex = [(x,y) for (x,y) in list(itertools.combinations(pointsIter, 2)) if norm(x - y) < 2*epsilon]
   edgelist = [[tuple(vertex) for vertex in edge] for edge in vrComplex]
   #print("edges: ",edgelist)

   # compose graph and get cliques

   D = nx.from_edgelist(edgelist)
   D.add_nodes_from(points)
   C = nx.algorithms.clique.enumerate_all_cliques(D)
   clicquelist = [clique for clique in C]

   if draw == True:
      nx.draw(D, with_labels=True)
      plt.show()

   return clicquelist

def vr_from_data(filename, epsilon, draw):

    S = blender_import.import_native(filename)
    VR = naive_vr(S,epsilon, draw)

    return VR

def get_naive_vr_set(models, draw = False):

    stop_condition = False
    step = 0.1

    for model in models:
    #model = models[0]

        print(model)
        f = open("complexes/"+model+".txt", "w")

        #while stop_condition is False:
        for epsilon in numpy.arange(0.1, 0.8,0.2):

            start = timeit.default_timer()
            vr = vr_from_data(model, epsilon, draw)
            time = timeit.default_timer() - start

            f.write("Epsilon: "+str(epsilon)+", Time: "+str(time)+"\n")
            f.write("VR: "+ str(vr)+"\n")
            print(epsilon,": ",len(vr))
            #epsilon = epsilon + step
            #stop_condition = True

        f.close()

models = ["plane", "line", "circle", "sphere", "torus"]
get_naive_vr_set(models, True)
