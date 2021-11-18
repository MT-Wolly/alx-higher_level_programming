#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    result = 0
    for arg in range(length):
        if arg == 0:
	    continue
        result += int(sys.argv[i])
    print("{}".format(result))
