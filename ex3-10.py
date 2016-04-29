# ex 3 and 4

cats = 2        # A single equal sign ( = ),
tuna = 3        # is used to set a variable to a
salmon = 4      # new value.
lobster = 1.0   # cats, tuna and salmon are integers (int), lobster is float (real) number
prawn = 10
cats_ate_fish = tuna + salmon  # variable name can not contain spaces, use underscore instead
seafood_platter = salmon + lobster + tuna + prawn # we can create values from math expression based on existing variables
                                                  # and assign it to a new variable (same as 4 + 1.0 + 3 + 10)
                                                  # seafood_platter will be float because lobster is float


print "I am telling a story."  # we can display text on the screen
                               # text (string) values are enclosed in single (') or double (") quotes

print "We have", cats, "cats."  # we can print multiple values
                                # cats is replaced with it's current value (4).
                                # It has nothing to do with text value "cats"
print "They are food lover."
print "They love to eat lots of seafood, not only fish."
print " They ate", cats_ate_fish, "fishes. And they were big fresh fish."
print " But they are", cats, "cats, so they ate", cats_ate_fish * 2, "fishes."  # it's ok to do simple math inside print stmt
print " But we are not cats, we can eat a big platter."

print " - " * 35   # doing math with strings does funny (but useful) things

# this is ex 5

baby = 'Janelle'       # this is string
gender = 'female'
her_age = '1'          # that's a also string and not an int, her_age * 5 will produce '11111'
her_height = '72 cm'   # number and letters inside a string are just text characters
her_weight = '9 kg'
her_teeth = 8          # that's not a string, because didn't ' ', that's a <int>
                       # it would be better to rename this variable as nb_of_teeth
 
print "Hi everyone, let me introduce my daughter %s." % baby  # %s means String format, we add a % after the print,
print "And she is a %s." % gender                             # because we need to call out the value.
print "She is %s year old." % her_age                    # Otherwise, it will shows "TypeError: 'Str' object is not callable.
print "She has %d teeth." % her_teeth # because 8 isn't a string, that's need to use %d (Decimal integers)
print "She is %s tall and her weight is %s." % (her_height, her_weight) #the print not only 1 value, thats, need a ( )
print "She loves to smile and be friend with everyone."


print " * " * 35

# this is ex 6

a = "There is %d baby, " % 1
b = "and she is a %s." % gender
is_not = "isn't" # We can not make a space bar, which isn't inside quote, need to put a _ between words.
                 # ??? you seem to be confusion variable names and associated values

print a + b
print "She %s a boy." % is_not

boy = False # We default a boolean, "True or False", so now boy = False is a boolean
Seriously = "Is she a boy? %r" # %r is a Repr format a.k.a. (debugging format), but it's under string.

print Seriously % boy

print " + " * 35

# ex7

print "Let me tell you my daughter's name again."
print "." * 20

J1 = "J"
J2 = "A"
J3 = "N"
J4 = "E"
J5 = "L"
J6 = "L"
J7 = "E"

print "This is her name."
print J1 + J2 + J3 + J4 + J5 + J6 + J7

print "~" * 25

# ex8          # Question what's the different between %s and %r, I tried to use either %r or %s in same line, output are same.

music = " %s %s %s %s"
print music % ("do", "re", "mi", "fa")
print music % (1, 2, 3, 4)
print music % (False, True, False, False)
print music % (                                   # same using like """ """ triple quote,
    "Mary have a little lamb",                    # but after % need to put ( )
    "Little lamb", "Little lamb",
    "Mary loves her little lamb."
 )

print " + " * 28

#ex9

melody = "Do Re Mi Fa So La Ti Do"
lyrics = "Blah\nLa\nLa\nLala\nFalala\nLulalu\nLalalala\nBlah"      # \n means a new line,
                                                               # If you want to set something that's too long, use \n to
print "Lets hear some music: ", melody                       #to make a different line.
print "Here we go!", lyrics

print """
Let's sing this.
Why we need the triple-quotes.
We can write everything we can.
After that we can print it out nicely.
Blah lalalalala, Let's do this.
Ok, I know my song is bad.
But this demo is enough already.
"""                           #If triple quote something behind a print, if it's too long.

print " . " * 25

# ex10
triple_sec = "\ttriple_sec\\"           # \t is a tab, same like use a 4 spaces,
rum_and_coke = "rum \\ and \\ coke\t"    # \\ is If I want to put a \ on a line, I have to put it for double.
tequila = "\\tequila\\"
vodka = "\\VOdk@\t"
gin = "\\GiN\t"

Long_Island_Iced_Tea = """
Let me make one for you:
\t* Triple Sec
\t* Rum
\t* Tequila
\t* Vodka
\t* Gin
\t* Diet Coke
\t* Two Ice Cube
"""
print Long_Island_Iced_Tea
print "This is l0ng |s|@nd |ced Te@"
print triple_sec + rum_and_coke + tequila + vodka + gin

# ex 10 sample
print "I am 6'2\" tall."
print 'I am 6\'2" tall.'

# ex 11
print "Who are you?"  #try to not use input, if need to use input, put it lke name = Joie,
name = raw_input()    # the different between raw_input() and input(), is raw_input didn't set anything
                       #when saved the code, it's can install anything while you are running the program.
print "Nice to meet you, %r." % name
