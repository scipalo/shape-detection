from vietoris_rips_complex import get_vietoris_rips_complex
import boundary_matrix
from numpy import arange
import timeit


def set_vrscx_data(models, epsilon, draw=False):
    stop_condition = False
    step = 0.1

    for model in models:

        print(model)
        # f = open("shape-detection/complexes/1.0+model"+".txt", "w")
        start = timeit.default_timer()
        vr = get_vietoris_rips_complex(model, epsilon, draw)
        betti = boundary_matrix.betti_direkt(vr)
        print(betti, len(vr))

        # f.write("Epsilon: "+str(epsilon)+", Time: "+str(time)+"\n")
        # f.write("VR: "+ str(vr)+"\n")
        # f.close()


def run_test_set():
    draw = False
    models = ["plane3", "line", "circle", "sphere", "torus"]
    m = "plane3"

    # SAVE VIETORI RIPS COMPLEXSES IN FILES
    for epsilon in arange(0.01, 1.0, 0.01):
        set_vrscx_data([m], epsilon, draw)

run_test_set()


