from stat import *
import os
import sys


for file in sys.argv[1:]:

    print(file)
    st = os.stat(file).st_mode

    if S_ISDIR(st):
        print("It's a dir")
    elif S_ISREG(st):
        print("It's a file")
    elif S_ISCHR(st):
        print("It's a character special")
    elif S_ISBLK(st):
        print("block special")
    elif S_ISFIFO(st):
        print("fifo")
    elif S_ISLNK(st):
        print("symbolic link")
    elif socket(st):
        print("It's a character special")
    else:
        print("unknown")
