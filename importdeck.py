#!/usr/bin/env python3
import os
import sys
import time

# these much match the cursor locations on your screen
search_box = (1582,1000)
first_match = (1062,381) # first card location
second_match = (1269,332) # gold card (2nd card location)

try:
    deck = sys.argv[1]
except:
    print("Run program with: ./importdeck.py [deckname]")
    print("  Example: ./importdeck.py zoo")
    sys.exit()
    
os.system("xdotool search --onlyvisible --classname Hearthstone windowfocus")
f = open("decks/%s.txt" % sys.argv[1])
for card in f.readlines():
    card = card[:-1]
    count = 1
    if card.startswith("2x "):
        card = card[len("2x "):]
        count = 2
    os.system("xdotool mousemove %s %s" % search_box)
    os.system("xdotool click 1")
    time.sleep(0.1)
    os.system("xdotool type \"%s\"" % card);
    #for c in card:
    #    os.system("xdotool keydown %s" % c)
    #    time.sleep(0.1)
    #    os.system("xdotool keyup %s" % c)
    os.system("xdotool key KP_Enter")
    time.sleep(0.1) 
    os.system("xdotool mousemove %s %s" % second_match) # try for gold
    time.sleep(0.1)
    for i in range(count):
        os.system("xdotool click 1")
        time.sleep(0.1)
    os.system("xdotool mousemove %s %s" % first_match)
    for i in range(count):
        os.system("xdotool click 1")
        time.sleep(0.1)
    time.sleep(0.1)

