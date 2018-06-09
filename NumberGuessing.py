"""
Learning Python
Number Guess
"""
from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The max_val is: %d" % max_val
  guess = get_user_guess()
  if guess > max_val:
    print "No, guessing higher than the maximum possible value!"
  else:
    print "Rolling..."
    sleep(2)
    print "The first value is: %d" % first_roll
    sleep(1)
    print "The second value is: %d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print total_roll
    print "Result..."
    if guess > total_roll:
      print "You won!"
    else:
      print "You lost, try again."


roll_dice(6)
