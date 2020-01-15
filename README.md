# shape-detection
Topology shape detection project for university class

Models for detection: line, plane, circle, sphere, torus

Usage: 

In object/obj directory save obj file for your model. 
Than set distance parameter for calculating Vietoris-Rips complex and your filne name in python file run.py in function run_test_set().
As a result you will get Betti numbers for each picked distance. 

def run_test_set():
  
    draw = False
    m = "model_file_name"

    for epsilon in arange(0.01, 1.0, 0.01):
        set_vrscx_data([m], epsilon, draw)



To find out which Betti number is corect one, save output as txt file in directory betti/ as betti_model_filename.txt.
Than take python file homology_group.py and set parameters betti_model_filename and model_file_name.

betti = doloci_hom_group('betti_model_filename')
shape_detection.shape_detection('model_filename', betti)
 
As a reult you get printed one of models: line, plane, circla, sphere and torus if input point set is one of the shapes
or is from same homology group. Program has few problems you are wellcome to improve it.



