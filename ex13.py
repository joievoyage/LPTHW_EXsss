from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# On line 1 we have a import. This is the thing,
# we add features to the scipt from Python feature set,
# That's why we need to key in the feature when we run
# this program, and this can keep the program small.

# Is there a difference between Python feature set and Python standard library?

# The argv is "argument variable.'.
# THIS variable holds the arguments, that can pass the 
# Python script when we run it.

# The line 3 is to "unpacks" the argv, not holding it.
# Assigned to four variables `script`, `first`,
# `second` and `third`.
# Yes, this is 'unpacked' the argument.
# That's why the argv is put at behind not argv = blah blah bl
# This is called "called libraries" module.

# Sys - System specific parameters and functions


# try the following:

data = [1, "two", 3.0]
one, two, three = data
print "one is %r; two is %r; three is %r" % (one, two, three)

# compare with the "unpacking" line for `argv`
# what is the type of `argv` and `data`?
