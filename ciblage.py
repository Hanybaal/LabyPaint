from os import listdir
from os.path import isfile

fichiers = [f for f in listdir("./") if isfile(f)]

name = input("Renseignez une chaîne: ")
lf = []

for file in fichiers:
    if (file[0] != "."):
        f = open(file, "r")
        for line in f:
            if name in line:
                lf.append(file)
                f.close()
                break

for n in lf:
    print(n)
