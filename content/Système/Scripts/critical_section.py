#!/usr/bin/python3

import os
from threading import Thread, Lock

LOOP_COUNT = 10000000
THREADS_COUNT = 2

glob = 0
lock = Lock()

def tmain():
    global glob
    for i in range(LOOP_COUNT):
        lock.acquire()
        loc = glob
        loc += 1
        glob = loc
        lock.release()

def main():
    threads = []
    for i in range(THREADS_COUNT):
        print("creating thread no %d" % (i+1))
        thread = Thread(target=tmain)
        try:
            thread.start()
        except Exception as e:
            print('Unable to creare thread')
            break
        threads.append(thread)

    for t in threads:
        try:
            thread.join()
        except Exception as e:
            print('Unable to join thread')
            continue

    print("%d =? %d" % (glob, THREADS_COUNT * LOOP_COUNT))

if __name__ == "__main__":
    main()
