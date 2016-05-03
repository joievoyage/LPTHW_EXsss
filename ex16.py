from sys import argv ##I guess is a module called sys a.k.a. system functionality.
                     ## That's a module import names(!?)
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN." ## These first few lines is a function
                                         # In Python 2.x, `print` is a statement, not a function
                                         # but in Python 3 `print` became function that is why you will have to use ()
                                         # print("We're going to erase %r." % filename)

raw_input("?")  # note that we are not saving the output of `raw_input` into any variable

print "Opening the file..."
target = open(filename, 'w') ## Then these 3 lines is another function.
                             ## 'w' is a 2d argument for `open`. it's a string character. 'w' means open the file in 'write' mode
                             ## We also can use 'r' for read, and 'a' for append.
print "Truncaitng the file. Goodbye!"
target.truncate()  ## Empty the file. <<Caution!!>> if need the file, have to use it carefully!

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1) ## write(something) means write the value of `something` into a file variable `target`.
target.write("\n")  # write "new line" character
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()  ## close the file. Just like File --> Save--> close


# try the following in the terminal:
# cp ex16.py ex16_copy.py
# python ex16_copy.py ex16_copy.py
