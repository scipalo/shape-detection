from vietoris_rips_complex import get_vietoris_rips_complex
import boundary_matrix
from numpy import arange
import timeit


def set_vrscx_data(models, draw = False):

    stop_condition = False
    step = 0.1

    for model in models:

        print(model)
        f = open("complexes/1.0/"+model+".txt", "w")

        for epsilon in arange(0.01,0.02,0.02):

            epsilon = 0.1

            start = timeit.default_timer()
            vr = get_vietoris_rips_complex(model, epsilon, draw)
            time = timeit.default_timer() - start

            f.write("Epsilon: "+str(epsilon)+", Time: "+str(time)+"\n")
            f.write("VR: "+ str(vr)+"\n")
            print(epsilon,": ",len(vr))

        f.close()


draw = True
models = ["plane", "line", "circle", "sphere", "torus"]
m = "torus"

# SAVE VIETORI RIPS COMPLEXSES IN FILES
set_vrscx_data([m], draw)

# GET BETTI NUMBER ARRAYS
betti_table = boundary_matrix.betti_numbers('complexes/1.0/'+m+'.txt', 0)
for betti in betti_table:
    print(betti)

# DETECT SHAPES
# detect shape



