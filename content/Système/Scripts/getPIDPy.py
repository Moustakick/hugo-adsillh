#!/usr/bin/python3
import sys
def main():
	i = 0
	for arg in sys.argv:
		print("argv[%d]=%s" % (i, arg))
		i += 1

main()
