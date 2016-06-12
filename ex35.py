from sys import exit  ## another import library exercise.

def gold_room():      ## When I taunt bear, and open door, it will run this part of code.
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.") ## but the code it was showed "Man, learn to type a number. Good job!
                                             ## the "good job" did not shows here.
                                             ## That is because `dead` function adds "Good job" to anything passed to it as argument.

    if how_much < 50:   ## If type less than 50 it will show this line
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:              ## It I type too much, then will die.
        dead("You greedy bastard!")


def bear_room(): ## I can not understand why bear_moved have default False or True. When will False or True?
                 ## initially `bear_moved` is set to `False` intentionally
                 ## `bear_moved` will change to `True` if you type "taunt bear" once
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:   ## This part is tricky for me, I was struggle at the 2 "taunt bear"
                  ## both are elif, but it's seems like run the first taunt bear and then run the second one.
                  ## but normally in this status, it's need to use another elif under the first "taunt bear"?
                  ## The tricky part is that each `elif` has a double test: condition1 and condition2
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:  ## <-- the code below will run only when you type 'taunt beer' for the 1st time
            print "The bear has moved from the door. You can go through it now"

            bear_moved = True
        elif choice == "taunt bear" and bear_moved:    ## <-- the code below will run only when you type 'taunt beer' for the 2d time
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insance."
    print "Do you flee for your life or eat your head."

    choice = raw_input("> ")

    if "flee" in choice: ## oh no! If I type flee, everything loop again. 
        start()
    elif "head" in choice:
        dead("Well that we tasty!")
    else:
        cthulhu_room()


def dead(why): ## I can not understand how makes it have a (why), and make it print? It's like line 10, then run this line?
               ## The purpose of this function is to print a message stored in `why` and exit from the program
               ## It is called `dead` because the user looses the game.
               ## You could rename `dead` to `terminate` and change `why` to `reason` if it makes more sense to you.
    print why, "Good job!"
    exit(0)


def start(): ## this is the story where start from, but I can not understand, why the start is put at the last?
             ## and how ti make it run it at the beginning of the story? is it because of the last line of start()?
             ## You can put functions in any order. The only thing that matter is in what order the functions are called.
             ## The last line of this exercice is `start()` which means that is the only function which is called when the program runs.
             ## When `start` is executed it will call other functions depending on what the user types.
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take."

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
