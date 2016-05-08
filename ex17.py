from sys import argv       ## Import library is a way to get something some programmers have written already.
                           ## Then we no need to write it again.

from os.path import exists ## Now import another command named exists.
                           ## If the return is True, the file exists based on its name a string
                           ## as an argument.
                           ## os.path is common pathname manipulations, Python can't do path expansion automatically
                           ## That's why we have to import something from os.path
script, from_file, to_file = argv ## Now is unpacked the argv, now have 3 variables inside the argv
                                  ## I am not sure about it, but I guess is it need to use script to call 2 arguments?
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file)  ## is it open a in_file from (from_file)??, and read it?
indata = in_file.read()    ## That's really not understand and can not figure it what is it.

print "The input file is %d bytes long" % len(indata)
                           ## It's length of the string tha then return that as number (I googled it(
                           ## But I don't know how to play with it.

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open (to_file, 'w')## It's something similiar like my red line 14?
                              ## But I not sure how to use it.
out_file.write(indata)        ## I guess it's something like line 15, I also don't know what is it.

print "Alright, all done."

out_file.close()              ## close the out_file?
in_file.close()               ## close the )in_file?

## I am very can not understand this exercise.
## But I have some question, it's common thing about import more than 1 library in 1 time?
## Why need to use library?
## If use library is it very easy and make the coding less lines and looks more easier to read?

