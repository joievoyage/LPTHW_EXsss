from sys import argv ##I guess is a module called sys a.k.a. system functionality.
                     ## That's a module import names(!?)
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN." ## These first few lines is a function

raw_input("?")

print "Opening the file..."
target = open(filename, 'w') ## Then these 3 lines is another function.
                             ## File name 'w' is a string character, 'w' means open the file in 'write' mode,
                             ## We also can use 'r' for read, and 'a' for append.
print "Truncaitng the file. Goodbye!"
target.truncate()  ## Empty the file. <<Caution!!>> if need the file, have to use it carefully!

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1) ## write(something) means write (something) inside a file.
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()  ## close the file. Just like File --> Save--> close

