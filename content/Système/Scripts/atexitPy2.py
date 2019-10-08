#!/usr/bin/python3
import sys
import os
import atexit
@atexit.register
def trigger_exit():
	print("Invoking exit handler!")
def main():
	print("Invoking main()...")
	print("Before exiting()...")
	sys.exit(os.EX_OK);
main()
