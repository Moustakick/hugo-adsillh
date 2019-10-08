#!/usr/bin/python3
import os, sys, time
def main():
	print("Starting parent process with PID=%d" % (os.getpid()))
	for i in range(1,4):
		try:
			pid = os.fork()
		except OSError as e:
			print("Unable to fork")
		if pid == 0:
			print("Starting child process with PID=%d (my parent PID=%d)" % (os.getpid(), os.getppid()))
			time.sleep(i*10)
			print("Finishing child process with PID=%d after %d sec" % (os.getpid(), i*10))
			sys.exit(os.EX_OK)

	cont = True
	while cont:
		try:
			pid, status = os.waitpid(-1, os.WNOHANG)
		except OSError as e:
			cont = False
		if pid > 0:
			print("Process with PID=%d has terminated with status=%d" % (pid, status))

	print("Finishing parent process with PID=%d" % (os.getpid()))
	sys.exit(os.EX_OK)

main()
