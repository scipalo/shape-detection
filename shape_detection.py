import vietoris_rips_complex
import blender_import
import boundary_matrix

from numpy.linalg import norm
from numpy import arange
import numpy

def shape_detection(filename, betti):

    # plane
    # line
    # ball
    # monkey
    if betti == [1,0,0]:


        point_set = blender_import.import_native(filename)
        point_trans = [*zip(*point_set)]
        avg_point,dist = [],[]

        for coordinate in point_trans:
            dist.append(max(coordinate) - min(coordinate))
            avg_point.append(sum(coordinate)/len(coordinate))

        print("diff: ",dist)

       # min max razdalja

        premer = max(dist)
        for d in dist:
            if d < premer and d != 0:
                premer = d


        print('premer: ',premer)

        # izberi povprečno točko

        print('avg point: ',avg_point)

        # izdelaj in skaliraj sfero

        sphere_set = blender_import.import_native("enota2")
        scaled_sphere = []

        for point in sphere_set:
            scaled = [point[i]*(0.25*premer) + avg_point[i] for i in range(len(point))]
            scaled_sphere.append(scaled)

        # določi presek

        pointIter = [numpy.array(x) for x in point_set]
        sphereIter = [numpy.array(x) for x in scaled_sphere]

        intersect = []
        for s in sphereIter:
            add = True
            for p in pointIter:
                if norm(s - p) < premer * 0.125:
                    add = False
            if add == True:
                s = [round(x,5) for x in tuple(s)]
                intersect.append(tuple(s))

        # pošlji ostanek preseka v run

        print("Intersect")
        #for i in intersect:
        #    print(i)

        min_dist = min(norm(x-y) for x in sphereIter for y in sphereIter if not numpy.array_equal(x,y))

        # epsilon < premer * 0.125
        # epsilon > min razdalje + malo
        detected = ""

        for epsilon in arange( min_dist + 0.1*min_dist, premer * 0.125,0.01):
            print(epsilon)
            vr = vietoris_rips_complex.vietoris_rips_native(intersect,epsilon, False)
            print("len: ",len(vr))
            betti = boundary_matrix.betti_direkt(vr)
            print("betti", betti)

            if betti == [0,0,0]:
                detected = "ball"

            elif betti == [1,2,0]:
                detected = "line"

            elif betti == [2,0,0]:
                detected = "plane"

            else:
                "WWFTRTTFTFTFTFTFTTFTFTF"

        print(detected)

    # circle
    elif betti == [1, 1, 0]:
        print("circle")

    # sphere
    elif betti == [1, 0, 1]:
        print("sphere")

    # torus
    # šalca
    elif betti == [1,2,1]:
        print("torus")

names = ["plane3", "line3", "circle", "sphere", "torus"]
bettis = [[1,0,0],[1,0,0],[1,1,0],[1,0,1],[1,2,1]]
#for betti,name in zip(bettis,names):
#shape_detection(names[0], bettis[0])
