#!/usr/bin/python3
import os, sys

print ("The child will write text to a pipe and ")
print ("the parent will read the text written by child...")

PAGER = "less"

# file descriptors r, w for reading and writing
r, w = os.pipe()

try:
    processid = os.fork()
except OSError as e:
    print("unable to fork")

if processid > 0:
    os.close(r)
    for i in range(1,1000):
        os.write(w,bytes(i))

    w.close()
else:
    os.close(w)
    r = os.fdopen(r)
