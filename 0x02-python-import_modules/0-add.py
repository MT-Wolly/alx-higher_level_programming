#!/usr/bin/python3
"""This program imports a function to be used in this executable script"""
if __name == "__main__":
	from add_0 import add
	a = 1
	b = 2
	print("{} + {} = {}".format(a,b, add(a,b)))
