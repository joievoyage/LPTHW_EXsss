from sys import exit  ## another import library exercise.

def gold_room():      ## When I taunt bear, and open door, it will run this part of code.
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.") ## but the code it was showed "Man, learn to type a number. Good job!
                                             ## the "good job" did not shows here.

    if how_much < 50:   ## If type less than 50 it will show this line
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:              ## It I type too much, then will die.
        dead("You greedy bastard!")


def bear_room(): ## I can not understand why bear_moved have default False or True. When will False or True?
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:   ## This part is tricky for me, I was struggle at the 2 "taunt bear"
                  ## both are elif, but it's seems like run the first taunt bear and then run the second one.
                  ## but normally in this status, it's need to use another elif under the first "taunt bear"?
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now"

            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
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
    print why, "Good job!"
    exit(0)

def start(): ## this is the story where start from, but I can not understand, why the start is put at the last?
             ## and how ti make it run it at the beginning of the story? is it because of the last line of start()?
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
