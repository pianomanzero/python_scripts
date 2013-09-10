#!/usr/bin/env python

from sys import exit

def gold_room():
  print "You find yourself in a room full of gold. How much do you take?"
  next = raw_input("> ")
  
  if "0" in next or "1" in next:
    how_much = int(next)
  else:
    dead("Learn to type a number!")

  if how_much < 50:
    print "Nice, you're not greedy, you win!"
    exit(0)
  else:
    dead("You greedy bastard!")


def bear_room():
  print "You see a big fat bear in this room"
  print "The bear has a bunch of honey."
  print "The fat bear is in front of another door"
  print "How are you going to move the bear?"
  bear_moved = False

  while True:
    next = raw_input("> ")

    if next == "take honey":
      dead("The bear looks at you and slaps your face off.")
    elif next == "taunt bear" and not bear_moved:
      print "The bear has moved from th edoor. You can go through it now."
      bear_moved = True
    elif next == "taunt bear" and bear_moved:
      dead("The bear gets pissed off and chews your face off.")
    elif next == "open door" and bear_moved:
      gold_room()
    elif next == "clue":
      print "You could try taking the bear's honey, or taunting the bear..."
    else:
      print "I've got no idea what that means... try typing 'clue'"

def cthulhu_room():
  print "Here you see the great evil Cthulhu."
  print "He, it, whatever stares at you and you go insane."
  print "Do you flee for your life or eat your own face?"

  next = raw_input("> ")

  if "flee" in next:
    start()
  elif "face" in next:
    dead("Well, that was tasty!")
  else:
    cthulhu_room()

def dead(why):
  print why,"Good job!"
  exit(0)

def start():
  print "You are in a dark, damp-smelling room."
  print "There is a door to your right and another to your left."
  print "Which one do you take?"

  next = raw_input("> ")

  if next == "left":
    bear_room()
  elif next == "right":
    cthulhu_room()
  else:
    dead("You stumble around the room until you starve.")

start()
