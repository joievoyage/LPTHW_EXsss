# Upper is ex11, lower part is ex 12
# Both print out are same, but ex11 needs 8 lines,
# ex 12 just need it for 4 lines.


print "How old are you?", # Becasue can't use print and value in same line
age = raw_input()         # That's why need two lines to do so.
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r, old, %r tall and %r heavy." % (age, height, weight)

#---------------------- this is ex11.py
# let's compare!!

age = raw_input("How old are you? ")  # when typed raw_input() the (), which are
height = raw_input("How tall are you? ") #similiar with " %s %s" % (x, y)
weight = raw_input("How much do you weight? ") # that's why the () can put the prompt.

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# as teacher said print and raw_input can't put @ the same line.
# if want to use print and raw_input need to use 2 line!!
# otherwise need to make it like the ex12.py age = raw_input("How old are you? ")

# -------
# The difference btw ex11 and ex12 is the use of prompt string as an
# argument for `raw_input` function

prompt_string = "How old are you? "

print prompt_string
age = raw_input()

# vs

age = raw_input(prompt_string)
