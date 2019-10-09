#!/usr/bin/python3

# Creation d'un programme `./prog_thread` qui ouvre un fichier `f`, et qui va lire un nombre de bloc limité `b` d'un taille donnée `s`.
#
# `./prog_thread f b s`
#
# On va ensuite faire un hash de chacun de ces blocs `xn`, on les concaténe et on fait un hash md5 de tout ça `x1 + x2 + x3 + ... + xn`.

# /autofs/unitytravail/travail/mocafrain/debian-10.0.0-amd64-netinst.iso


import os
import sys
from threading import Thread, Lock
import hashlib

def tmain(f, s, n):
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

# Gestion d'erreur
def main():
    if len(sys.argv) < 4:
        print ("Wrong arguments")
        sys.exit() #EX_USAGE

# File path
    path = sys.argv[1]

# Declaration de toutes les variables de l'énoncé
    f = os.open(path, os.O_RDONLY)
    s = int(sys.argv[3])
    n = int(sys.argv[2])

    count = 1
    threads = []
    for i in range(count):
        print("Creating thread no %d" % (i+1))
        # Petites modif du programme pour passer plusieurs args
        thread = Thread(target=tmain, args=(f,s,n))

        try:
            thread.start()
        except Exception as e:
            print('Unable to create thread')
            break
        threads.append(thread)

    for t in threads:
        try:
            thread.join()
        except Exception as e:
            print('Unable to join thread')
            continue

if __name__ == "__main__":
    main()
