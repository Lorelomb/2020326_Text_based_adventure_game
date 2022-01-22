# Author: Lorenzo Lombardo - 2020326

import sys
import time
player_health = 30
inventory = []
a = 2
b = 0.2
c = 0.08
d = 0.0150

def intro():
    time.sleep(a)
    print("\n Health", player_health)
    time.sleep(a)
    print("Hey!, you took a serious hit to the head,"
          "\n get up we still need to clear the rest of the dungeon - Mysterious Voice")


print()
print()
title_screen = "###################################\n#                                 #" \
             "\n#       DUNGEON CRAWLERS          #" \
             "\n#                                 #\n###################################"
for character in title_screen:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(d)
print()
print()
time.sleep(b)
startGame = input("Would you like to start the adventure [yes/no]: ")
if startGame == "no" or startGame == "N":
    print("Maybe next time then!")
elif startGame == "yes" or startGame == "Y":
    intro()

