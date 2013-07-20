#! /usr/bin/env python

import sys
import string
import matplotlib

frequency = {}

def main():
    if len(sys.argv) != 2:
        print 'usage: freq.py filepath'
        return
    try:
        f = open(sys.argv[1], 'r')
    except IOError:
        print "file does'nt exist"
        return

    for j in string.lowercase:
        frequency[j] = 0
    for i in f.read():
        if i.lower() in frequency.keys():
            frequency[i.lower()] = frequency[i.lower()] + 1
    print frequency,
    f.close()

if __name__ == "__main__":
    main()
