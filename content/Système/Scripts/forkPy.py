#!/usr/bin/python3
import os
import sys
def main():
	print("Starting process with PID=%d" % (os.getpid()))
	try:
		pid = os.fork()
	except OSError as e:
		print("Unable to fork")

	if pid == 0:
		print("Starting child with PID=%d (my parent PID=%d)" % (os.getpid(), os.getppid()))
	else:
		print("Still in process with PID=%d" % (os.getpid()))
	print("Finishing process with PID=%d" % (os.getpid()))

	sys.exit(os.EX_OK);

main()
