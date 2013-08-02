This program takes a file and plots a graph with the alphabets in x-axis and their frequency in y-axis.
The code is written in python 2. 


Requirements:                                                                                            
numpy.                                                                                      
Matplotlib -- To plot the bar graph.                                                                   
Python2.7                                                              


Installing Dependencies:  
The following packages are required    
1. Numpy.                                                              
2. Matplotlib.                                                                            
                                                                                            
In ubuntu:                                                                                             
Numpy: $ sudo apt-get install python-numpy python-scipy            
Matplotlib: $ sudo apt-get install python-matplotlib                         

In osx:                                                                  
Install the packages either from macports or homebrew. You can also install these packages manually from source.                        

USAGE: python freq.py [args] [filename with exact path]             
HELP: python freq.py -h                    


By default the program looks for alphabets(Both lower and upper case). It also supports numbers and symbols.         

Arguments:                     
-u  Only upper case letters.                     
-l  Only lower case letters.         
-n  Numbers.               
-p  Punctuation(Symbols).             
-a  Alphabets(upper and lower) Numbers and Punctuation.            

If no argument is specified, the default alphabets(lower and upper case) is taken.                                
You cannot specify multiple arguments.                       
