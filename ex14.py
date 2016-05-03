from sys import argv

script, user_name = argv
prompt = '> ' # that's mean we can put any value at the prompt

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print  "Where do you live %s?" % user_name
lives = raw_input(prompt)

print  "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me,
You live in %r, Not sure where that is.
And you have a %r computer, Nice.
""" % (likes, lives, computer)

# If we make a prompt variable to set something what we want
# Then we should use raw_input(prompt) to do it.

# What happens when you run this script as
# python ex14.py

# and
# python ex14.py John Smith

# how can you pass the full name as the argument to the script?
