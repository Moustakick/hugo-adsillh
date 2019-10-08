#!/usr/bin/python3
import sys
import os
import atexit
def trigger_exit():
	print("Invoking exit handler!")
def main():
	print("Invoking main()...")
	atexit.register(trigger_exit)
	print("Before exiting()...")
	sys.exit(os.EX_OK);

main()

