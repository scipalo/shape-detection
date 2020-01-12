import matplotlib.pyplot as plt
from numpy.linalg import norm
import numpy
import networkx as nx
import blender_import
import itertools


def vietoris_rips_native(points, epsilon, draw):

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

def get_vietoris_rips_complex(filename, epsilon, draw):

    S = blender_import.import_native(filename)
    VR = vietoris_rips_native(S,epsilon, draw)

    return VR
