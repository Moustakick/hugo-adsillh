#!/usr/bin/python3
import sys
def main():
	for i,arg in enumerate(sys.argv):
		print("argv[%d]=%s" % (i, arg))

main()
