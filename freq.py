#! /usr/bin/env python

import sys
import string
import numpy as np
import matplotlib.pyplot as plt
import argparse

frequency = {}

# Parsing command line arguments
# Default is alphabets

parser = argparse.ArgumentParser(description="Know the frequency of letter/numbers/symbols")
parser.add_argument("filepath", help="path where the file is located along with filename")
parser.add_argument("-n", action="store_true", help="Numbers")
parser.add_argument("-p", action="store_true", help="Punctuation")
args = parser.parse_args()
if args.n:
    choice = string.digits
elif args.s:
    choice = string.punctuation
else:
    choice = string.lowercase
file = args.filepath

def main():
    try:
        f = open(file, 'r')
    except IOError:
        print "file does'nt exist"
        return

    for j in choice:
        frequency[j] = 0
    for i in f.read():
        if i.lower() in frequency.keys():
            frequency[i.lower()] = frequency[i.lower()] + 1
    f.close()

    # Code for plotting the data using matplotlib
    N = len(choice)
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
