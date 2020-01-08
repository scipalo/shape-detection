from ripser import ripser
from persim import plot_diagrams
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
import blender_import

datafile = "sphere"
data = np.array(blender_import.get_vertex_set(datafile))

dgms = ripser(data, thresh=2)['dgms']
plot_diagrams(dgms, show=True)