
def import_native(name):

    f = open("objects/obj/"+name+".obj", "r")
    S = []

    for line in f:
        #print(line)
        if line[0:2] == "v ":
            S.append(tuple(float(value) for value in line.split()[1:]))

    return S

def import_ripser(name):

    f = open("objects/obj/"+name+".obj", "r")
    S = []

    for line in f:
        #print(line)
        if line[0:2] == "v ":
            S.append([float(value) for value in line.split()[1:]])

    return S