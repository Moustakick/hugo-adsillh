#!/usr/bin/python3

import os
from threading import Thread

def tmain(arg):
    print("[T] %s" % (arg))

def main():
    thread = Thread(target=tmain, args=('Hello World!',))

    try:
        thread.start()
    except Exception as e:
        print('Unable to create thread')
        sys.exit(os.EX_OSERR)

    try:
        thread.join()
    except Exception as e:
        print('Unable to join thread')
        sys.exit(os.EX_OSERR)

    print("Thread finished")
