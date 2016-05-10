from sys import argv       ## Import library is a way to get something some programmers have written already.
                           ## Then we no need to write it again.

from os.path import exists ## Now import another command named exists.
                           ## If the return is True, the file exists based on its name a string
                           ## as an argument.
                           ## os.path is common pathname manipulations, Python can't do path expansion automatically
                           ## That's why we have to import something from os.path
script, from_file, to_file = argv ## Now is unpacked the argv, now have 3 variables inside the argv
                                  ## I am not sure about it, but I guess is it need to use script to call 2 arguments?
                                  ## Yes, argv must contain 3 items (script name, arg1, and arg2)
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
# indata = open(from_file).read()  # and we don't need in_file

in_file = open(from_file)  ## is it open a in_file from (from_file)??, and read it?
                           ## No, we open from_file, which holds the value of the 1st script argument.
                           ## in_file is a special file object variable. try to run help(open) inside python shell
indata = in_file.read()    ## That's really not understand and can not figure it what is it.
                           ## We are reading file content from the file object and saving the results into indata

print "The input file is %d bytes long" % len(indata)
                           ## It's length of the string tha then return that as number (I googled it(
                           ## But I don't know how to play with it.
                           ## name = "Joie"; print len(name)
                           
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open (to_file, 'w')## It's something similiar like my red line 14?
                              ## But I not sure how to use it.
out_file.write(indata)        ## I guess it's something like line 15, I also don't know what is it.
                              ## Yes, except that we open a file for writing, and then write content into it.

print "Alright, all done."

out_file.close()              ## close the out_file?
in_file.close()               ## close the )in_file?
                              ## we call close() method on two file objects
                              ## python will do this automatically when the script finishes,
                              ## but it's a good practice to do is explicitly yourself

## I am very can not understand this exercise.
## But I have some question, it's common thing about import more than 1 library in 1 time?
# Yes, it is very common to import from more than 1 library
## Why need to use library?
## If use library is it very easy and make the coding less lines and looks more easier to read?
# Yes, we can reuse code in different projects.
