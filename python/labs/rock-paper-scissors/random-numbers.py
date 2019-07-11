import random

print("Welcome to my Random Playground")

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

sum = die1 + die2
roll = "Roll Again"
move = "You move"

if die1 != die2:
   print("%s %s" % (move, sum))
   # print("Next Players Turn")

elif die1 == die2:
   print("%s" % (roll)
