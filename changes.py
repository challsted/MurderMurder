#!/usr/bin/python

import random

"""
This file is for writeing up random chances that might happen in the game,
"""

def villan(attacker):
    attacker = random.random()

    if attacker >=0.0 <=0.59:
        a = murder # Do something here
    elif attacker >=0.6 <=0.89:
        a = robber # Do something here to find out if there is more then 1 robber
    else:
        a = rapist # Do something here to find out if there is more then 1 rapist

    return attacker

def children(number_of_children):
    number_of_children = random.choice(0, 1, 2, 3)
    return number_of_children
