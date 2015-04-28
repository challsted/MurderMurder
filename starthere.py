#!/usr/bin/python

from main import *

# Need a place to start, lets try starting here!
def start_bedroom():
    print "Welcome to MurderMurder by MaSammich aka HackingInformation on GitHub" #Gretiem"#, and FullOverRide"
    clear()
    print "Your sleeping in your bed...."
    print "Dreaming of gumdrops, sugar pops, and a lion named Dandy..."
    print "Oh, what sweet dreams your precious mind ponders"
    clear()

def bedroom_p2(awake, fear):
    print "You slightly hear a car door outside of your window, the slam of the door penetrates your sweet dream"
    print "Do you want to investigate or keep sleeping, who knows what you will dream of next?"
    usr_yn("Keep Sleeping?")

    if True:
        print "You drift back to sleep, who cares if someone shut their door too hard"
    else:
        print "You lean over and peak out the window next to your bed,\n you see a old truck in the distance, only slightly illuminated by the moonlight"
        print "Its not on your property, no one seems to be near the truck, you pay it no mind"
        awake += 1

    clear()

    if awake == 1:
        print "As your begining to fall back asleep, you begin to hear footsteps in the distance"
        clear()
        usr_yn("Investigate?")

        if True:
            print "You roll over and peak out your window again, you dont see anyone but you faintly hear the sound of footsteps still and not far from you"
            awake += 1
            usr_yn("Investigate Further?")

            if True:
                print "You stand up and take a look out the window, blood begins to rush though your body a little harder as you do"
                print "You faintly see a shadow slide past the first floor of your house and around a corner"
                print "You rub your eyes but the shadow is gone, your heart speeds up a little and you can feel your self become fully awake"
                awake += 1
                fear += 1
            else:
                print "You lay back in bed, annoyed that you got up to something to simple"

        else:
            print "Its probably just some stray dog walking though the yard, who cares right?"

    return (awake, fear)

def bedroom_p3(awake, fear):
    # Checks the alertness of the player from the previous function
    awake, fear = bedroom_p2(awake, fear)

    if awake == 3:
        print "You hear glass shattering from some room down stairs and a thud on the ground"
        print "You turn around from your window to face the sound, but only see darkness"
        print "\"What was that?\" you wonder to your self slightly outloud, shushing your self for not only thinking it"
        print "Your wife jerks awake and is looking around the room frantically for your consolation, you wisper \"shhhhh\" you say to her"
        fear += 1
    elif awake == 2:
        print "You hear glass shatter from somewhere, your mind franticly decides its coming from somewhere downstairs"
        print "Your wife awakens with a startle and grabs your arm as she sits up"
        print "\"What the fuck was that\" she says terrified"
        print "\"I dont know... it sounded like glass being broken"
        fear += 3
    elif awake == 1:
        print "You are ripped out of your sleep by the unmistakeable sound of glass shadering"
        fear += 4
    else:
        print ""
        fear +=5





start_bedroom()
bedroom_p2()
bedroom_p3()

