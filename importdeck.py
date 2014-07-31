#!/usr/bin/env python3
import os
import sys
import time

# these much match the cursor locations on your screen
search_box = (1582,1000)
first_match = (1062,381) # first card location
second_match = (1269,332) # gold card (2nd card location)

dirs = [
    "~/Dropbox/decks",
    os.path.dirname(os.path.join(sys.argv[0], "decks"))
]

deck = None
try:
    deck = sys.argv[1]
except:
    print("Run program with: ./importdeck.py [deckname]")
    print("  Example: ./importdeck.py zoo")
    sys.exit(1)
    
f = None
for d in dirs:
    d = os.path.expanduser(d)
    try:
        f = open(os.path.join(d,"%s.txt" % sys.argv[1]))
    except FileNotFoundError:
        pass
    break

if not f:
    print("Deck not found.")
    sys.exit(1)
    
os.system("xdotool search --onlyvisible --classname Hearthstone windowfocus")
time.sleep(0.1)
for card in f.readlines():
    if not card.strip():
        continue # blank line
    card = card[:-1]
    count = 1
    if card.strip().startswith("#"):
        continue # comment
    
    print(card)
    
    if card.startswith("2x "):
        card = card[len("2x "):]
        count = 2
    os.system("xdotool mousemove %s %s" % search_box)
    #time.sleep(0.1)
    os.system("xdotool click 1")
    #time.sleep(1.0)
    os.system("xdotool type \"%s\"" % card);
    #for c in card:
    #    os.system("xdotool keydown %s" % c)
    #    time.sleep(0.1)
    #    os.system("xdotool keyup %s" % c)
    os.system("xdotool key KP_Enter")
    time.sleep(0.2) # definitely need delay here
    os.system("xdotool mousemove %s %s" % second_match) # try for gold
    #time.sleep(0.1)
    for i in range(count):
        os.system("xdotool click 1")
        time.sleep(0.1)
    os.system("xdotool mousemove %s %s" % first_match)
    for i in range(count):
        os.system("xdotool click 1")
        time.sleep(0.1)
    time.sleep(0.2)

