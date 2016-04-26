def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


age = add(13, 5)
height = subtract(180, 15)
weight = multiply(30, 2)
iq = divide(300, 2)

print "This is my age",age
print " I am ",height, "cm tall."
print "I am only",weight, "kg. Don't say I am fat and heavy!"
print "Haha, my iq is",iq, ". Well, I admit I am so clever."

print "Let's do some maths with these functions"

#A puzzle for the extra credit, type it in anyway.
print "Here we go!"

# Can we do something to change the line 30?
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"