#This is stuff I typed into a file.        <-- These 3 lines are something I
#It is really cool stuff.                  <--- Type into a file. ex15.txt
#Lots and lots of fun to have in here.

from sys import argv  ## use argv (arguments) to get a file.
                          ## sys means system specific parameters
script, filename = argv # I guess is from system to get a argv file.

txt = open(filename)   ## then use this command to open the txt or file which I want.

print "Here's your file %r:" % filename ## then print out a message that I requested to open.
print txt.read() ## then we called out a function on the txt and we named read.

print "Type the filename again:"
file_again = raw_input("> ") ## then we key in something as raw_input

txt_again = open(file_again) ## It's a file object but it can't return the contents of the file.

print txt_again.read()

## But this file, I guess can't opened it own, need to open with another .txt or .py
## Thats why from LPTHW 'what you should see'
## show that python ex15.py ex15_sample.txt
