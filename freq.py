#! /usr/bin/env python

import sys
import string
import numpy as np
import matplotlib.pyplot as plt

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
    f.close()

    # Code for plotting the data using matplotlib
    N = 26
    ind = np.arange(N)
    width = 0.35
    fig = plt.figure()
    ax = fig.add_subplot(111)
    rects1 = ax.bar(ind+width, [frequency[i] for i in sorted(frequency.keys())], width, color='b')

    ax.set_ylabel('Frequency')
    ax.set_xlabel('Alphabets')
    ax.set_title('Alphabet frequency')
    ax.set_xticks(ind+width)
    ax.set_xticklabels(sorted(frequency.keys()))
    plt.show()

if __name__ == "__main__":
    main()
