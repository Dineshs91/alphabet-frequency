This program takes a file and plots a graph with the alphabets in x-axis and their frequency in y-axis.
The code is written in python 2. 

Requirements:
numpy
Matplotlib -- To plot the bar graph.
Python2.7

Installing Dependencies:
In ubuntu:
Numpy: $ sudo apt-get install python-numpy python-scipy

Matplotlib: $ sudo apt-get install python-matplotlib

Python: $ sudo apt-get install python

USAGE: python freq.py -n -p [filename with exact path]
HELP: python freq.py -h

By default the program looks for alphabets(Both lower and upper case). It also supports numbers and symbols.

-u  Only upper case letters.
-l  Only lower case letters.
-n  Numbers.
-p  Punctuation(Symbols).
-a  Alphabets(upper and lower) Numbers and Punctuation.

