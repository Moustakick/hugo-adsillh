#!/usr/bin/python3

# Creation d'un programme `./prog_thread` qui ouvre un fichier `f`, et qui va lire un nombre de bloc limité `b` d'un taille donnée `s`.
#
# `./prog_thread f b s`
#
# On va ensuite faire un hash de chacun de ces blocs `xn`, on les concaténe et on fait un hash md5 de tout ça `x1 + x2 + x3 + ... + xn`.

# /autofs/unitytravail/travail/mocafrain/debian-10.0.0-amd64-netinst.iso


import os
import sys
from threading import Thread
import hashlib

def md5sum(data):
    return hashlib.md5(data).hexdigest()

# Gestion d'erreur
def main():
    if len(sys.argv) < 4:
        print ("Wrong arguments")
        sys.exit() #EX_USAGE

# Ajouter de la gestion d'erreur avec pour les arguments


# File path
    path = sys.argv[1]

# Declaration de toutes les variables de l'énoncé
    f = os.open(path, os.O_RDONLY)
    s = int(sys.argv[3])
    n = int(sys.argv[2])


    totalhash = ""
    count = 0
    while count < n:
        os.lseek(f, count*s, os.SEEK_CUR)
        readBytes = os.read(f, s)
        totalhash += md5sum(readBytes)
        count +=1

    # Sortie du resultat
    print(totalhash)
    totalhashencode = totalhash.encode('utf-8')
    print("Resultat final :")
    print(md5sum(totalhashencode))

if __name__ == "__main__":
    main()
