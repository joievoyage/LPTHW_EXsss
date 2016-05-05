#This is stuff I typed into a file.        <-- These 3 lines are something I
#It is really cool stuff.                  <--- Type into a file. ex15.txt
#Lots and lots of fun to have in here.

from sys import argv    ## use argv (arguments) to get a file.
                        ## sys means system specific parameters
                        ## sys is http://docs.python.org/library/sys

script, filename = argv # means that your script must be called with one argument
                        # the value of the argument will be saved into `filename` variable

txt = open(filename)   # opens a file for reading. The name of the file to open is stored inside `filename`.
                       # `txt` is a variable of type file

print "Here's your file %r:" % filename ## then print out a message that I requested to open.
print txt.read()       # `txt` has a method `read` which allows us to get whole content of a previously opened file

print "Type the filename again:"
file_again = raw_input("> ") ## then we key in something as raw_input

txt_again = open(file_again) ## It's a file object but it can't return the contents of the file.

print txt_again.read()

## But this file, I guess can't opened it own, need to open with another .txt or .py
## Thats why from LPTHW 'what you should see'
## show that python ex15.py ex15_sample.txt

# try: python ex15.py ex14.py
# when you see "Type the filename again:" type README.md

# i just added a new line
