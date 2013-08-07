#! /usr/bin/env python

import sys
import string
import numpy as np
import matplotlib.pyplot as plt
import argparse

frequency = {}

# Parsing command line arguments
# Default is alphabets(lower and upper case)

parser = argparse.ArgumentParser(description="Know the frequency of Letters/Numbers/Symbols")
parser.add_argument("filepath", help="path where the file is located along with filename")
parser.add_argument("-u", action="store_true", help="Uppercase alphabets")
parser.add_argument("-l", action="store_true", help="Lowercase alphabets")
parser.add_argument("-n", action="store_true", help="Numbers")
parser.add_argument("-p", action="store_true", help="Punctuation(Symbols)")
parser.add_argument("-a", action="store_true", help="Alphabets(upper and lower) Numbers and Punctuations")
args = parser.parse_args()
if args.a:
    choice = string.digits + string.letters + string.punctuation
    xlabel = 'Alphabets Numbers Punctuation'
elif args.u:
    choice = string.uppercase
    xlabel = 'Alphabets(upper)'
elif args.l:
    choice = string.lowercase
    xlabel = 'Alphabets(lower)'
elif args.n:
    choice = string.digits
    xlabel = 'Numbers'
elif args.p:
    choice = string.punctuation
    xlabel = 'Punctuation'
else:  # Default choice
    choice = string.letters
    xlabel = 'Alphabets(lower and upper)'
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
        if i in frequency:
            frequency[i] = frequency[i] + 1
    f.close()

    # Code for plotting the data using matplotlib
    N = len(choice)
    ind = np.arange(N)
    width = 0.35
    fig = plt.figure()
    ax = fig.add_subplot(111)
    rects1 = ax.bar(ind+width, [frequency[i] for i in sorted(frequency.keys())], width, color='b')

    ax.set_ylabel('Frequency')
    ax.set_xlabel(xlabel)
    ax.set_title('Alphabet frequency')
    ax.set_xticks(ind+width)
    ax.set_xticklabels(sorted(frequency.keys()))
    plt.show()

if __name__ == "__main__":
    main()
