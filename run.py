from vietoris_rips_complex import get_vietoris_rips_complex
import boundary_matrix
from numpy import arange
import timeit


def set_vrscx_data(models, draw=False):
    stop_condition = False
    step = 0.1

    for model in models:

        print(model)
        # f = open("shape-detection/complexes/1.0+model"+".txt", "w")

        for epsilon in arange(0.01, 0.02, 0.01):

            start = timeit.default_timer()
            vr = get_vietoris_rips_complex(model, epsilon, draw)
            betti = boundary_matrix.betti_direkt(vr)
            print(betti)
            time = timeit.default_timer() - start

            # f.write("Epsilon: "+str(epsilon)+", Time: "+str(time)+"\n")
            # f.write("VR: "+ str(vr)+"\n")

        # f.close()


draw = False
models = ["plane", "line", "circle", "sphere", "torus"]
m = "torus"

# SAVE VIETORI RIPS COMPLEXSES IN FILES
set_vrscx_data([m], draw)

# GET BETTI NUMBER ARRAYS
# betti_table = boundary_matrix.betti_numbers("shape-detection/complexes/1.0/"+m+'.txt', 0)
# with open("shape-detection/betties"+m+"txt", 'w') as g:
#    for betti in betti_table:
#        g.write('{} {} {}'.format(betti(0), betti(1), betti(2)))
# g.close()

# DETECT SHAPES
# detect shape


