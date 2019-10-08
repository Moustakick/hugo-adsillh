#!/usr/bin/python3

import os
import sys
from threading import Thread

def tmain(arg1, arg2, arg3):
    print("[T%d] Hello World! %d, %d" % (arg1, arg2+arg1, arg3*arg2))

def main():
    if len(sys.argv) != 2:
        print ("Wrong arguments")
        sys.exit(os.EX_USAGE)

    count = int(sys.argv[1])

    threads = []
    for i in range(count):
        print("Creating thread no %d" % (i+1))
        # Petites modif du programme pour passer plusieurs args
        thread = Thread(target=tmain, args=(i+1,i+2,i+3,))

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
