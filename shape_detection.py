
def shape_detection(name, betti, fileName):

    # plane
    # line
    # ball
    # monkey
    if betti == [1,0,0]:

        # avg razdalja med točkami
        # max razdalja med točkami

        # KROGLA
        # radij = polovica max razdalje
        # gostota = avg kompleksa
        # središče = središčna točka kompleksa kompleksa

        # PRESEK
        # odstrani vse točke, ki so blizu kompleksu
        # d = avg razdala * 1,5?

        # poženi še enkrat voroni, betti

        intersection_betti = [0,0,0]

        if intersection_betti == [1,2,0]:
            print("line")

        if intersection_betti == [2,0,0]:
            print("plane")

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





names = ["plane", "line", "circle", "sphere", "torus"]
bettis = [[1,0,0],[1,0,0],[1,1,0],[1,0,1],[1,2,1]]
for betti,name in zip(bettis,names):
    shape_detection(name, betti)
