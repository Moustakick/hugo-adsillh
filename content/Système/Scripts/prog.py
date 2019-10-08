#!/usr/bin/python3

import sys
import os

def main():
	#Fork avec gestion d'erreur
	try:
		pid = os.fork()
		print("PID =",pid)
	except OSError as e:
		print("Unable to fork")

	#Execution dans le fils
	if pid == 0:
		print("Starting child with PID=%d (my parent PID=%d)" % (os.getpid(), os.getppid()))
		try:
			os.execvp(sys.argv[1],sys.argv[1:])
			sys.exit(os.EX_OK)
		except FileNotFoundError as e:
			sys.exit(os.EX_DATAERR)

	#Fin du fork fils
	pid, status = os.waitpid(-1, os.WNOHANG)
	if pid > 0:
		print("Process with PID=%d has terminated with status=%d" % (pid, status))

	#Retour dans le process parent
	print(os.getpid())

main()
