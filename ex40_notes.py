#myDog = Dog("Fluffy","Poodle","White") ## It is an object of type Dog. Dog is the class.
                                       ## myDog is a local variable. It can be named anything,
                                       ## it is just a label attached to some object.
                                       ## Dog create an instance of class Dog, will call the __init__ method implicitly.
                                       ## "Fluffy", "Poodle", "White" the parameters to pass to the __init__ method.

class Dog:
    def __init__(self, name, breed, colour):
        #set attributes
        self.name = name
        self.breed = breed
        self.colour = colour
        ## This creates a Dog object by calling the __init__ function in the Dog class.
        ## In this method you should set the data attributes,
        ## or instance variables (the traits "global" to every dog),
        ##Each class has one __init__ function, but may have many instance variables.
        ## Now the behaviour is specified by methods within the class specification.

    def bark(self):
        print("{} barks!".format(self.name))
        ##The behaviour is specified by methods within the class specification.

dog1 = Dog("Fluffy", "Poodle", "White")  ## Here can get some multipies dogs.
dog2 = Dog("Lassie", "Collie", "Brown, dark streaks with white chest")
dalmatians = []
for i in range(0,101):
    dalmatians.append(Dog(i,"Dalmatian","White with black spots"))


## When you call a method of an object self is passed in implicitly
## and is the object you're calling the method on.
## For example, myDog.bark() does the same thing as Dog.bark(myDog).
##When using Dog("Fluffy", "Poodle", "White") to create a new dog,
##things are a bit trickier. __init__ can't be called straight away with self
##because self doesn't exist yet. Python actually uses a different class method,
##  __new__, to create a new object, then passes this newly created object as the self parameter to __init__,
## which initialises the object. You can override the __new__ method if you want but that's hardly ever necessary.

