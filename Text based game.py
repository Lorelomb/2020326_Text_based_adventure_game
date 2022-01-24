# Author: Lorenzo Lombardo - 2020326

import sys
import time
player = {"weapon":None, "health": 50 ,"name":None}
inventory = []
character_name = []
# game_on = True
a = 2
b = 0.2
c = 0.08
d = 0.0150

def intro():

    print("\nHealth = ", player["health"])
    time.sleep(b)
    print()
    p1 = '"Hey!, you took a serious hit to the head,get up we still need to clear the rest of the dungeon. " '"- Mysterious Figure"''
    for character in p1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(d)
    print()
    print()
    time.sleep(a)
    print("- As you look around in confusion you see shadowed figures in the background fighting each other -")
    print()
    time.sleep(a)
    p2  = '" You need to get up, we are not done with this dungeon yet,the guild will be out of their minds if they find out we haven\'t cleared this place from the goblins." '"- Mysterious Figure"''
    for character in p2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(d)
    print()
    time.sleep(a)
    p3 = '" The hit was hard so we need to check if everything is fine inside your head, do you still remember who you are ? let\'s begin with your class" '"- Mysterious Figure"''
    for character in p3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(d)
    print()
    print()
    print("mage")
    time.sleep(b)
    print("cleric")
    time.sleep(b)
    print("rogue")
    time.sleep(b)
    print("warrior")
    time.sleep(b)
    print("archer")
    time.sleep(b)
    print()
    class_choice()

def class_choice():

    class_option = input("So,which one is your class?:")

    if class_option == "mage":
        mage = input("Are you sure? :")
        if mage == "yes":
            print()
            print('"I think I am a mage"'"- You "'')
        elif mage == "no":
            class_choice()

    elif class_option == "cleric":
        cleric = input("Are you sure? :")
        if cleric == "yes":
            print()
            print('"I think I am a cleric"'"- You "'')
        elif cleric == "no":
            class_choice()

    elif class_option == "rogue":
        rogue = input("Are you sure? :")
        if rogue == "yes":
            print()
            print('"I think I am a rogue"'"- You "'')
        elif rogue == "no":
            class_choice()

    elif class_option == "warrior":
        warrior = input("Are you sure? :")
        if warrior == "yes":
            print()
            print('"I think I am a warrior"'"- You "'')
        elif warrior == "no":
            class_choice()

    elif class_option == "archer":
        print()
        archer = input("Are you sure? :")
        if archer == "yes":
            print()
            print('"I think I am an archer"'"- You "'')
        elif archer == "no":
            class_choice()

    print()
    part1_1()

def part1_1():
    p1 = '" Ok, glad you still remember but what about your name ?" '"- Mysterious Figure"''
    for character in p1:
        sys.stdout.write(character)
        sys.stdout.flush()
        sys.stdout.flush()
        time.sleep(d)
    print()
    time.sleep(a)
    n_choice()

def n_choice():

    print()
    name = input("What's your name?:")
    character_name.append(name)
    n_confirm()

def n_confirm():

    name_confirm = input("Are you sure this is your name?:")
    if name_confirm == "yes":
        part1_2()
    elif name_confirm == "no":
        character_name.clear()
        n_choice()

def part1_2():

    print()
    p1 = '" Perfect, seems like everything inside that box of yours is fine,anyway take this [powerful potion]' \
         ' it will heal you from that hit and by the ' \
         'way I am Thorfin in case you don\'t remember my name anymore hahahaha." '"- Thorfin, the dwarf"''
    for character in p1:
        sys.stdout.write(character)
        sys.stdout.flush()
        sys.stdout.flush()
        time.sleep(d)
    inventory.append("powerful potion")
    print()
    print()
    print("~ [powerful potion] has been added to your inventory ~")
    time.sleep(b)
    print()
    p2 = '" Cool you might want to use that potion though,' \
         ' the others are fighting a group of goblins and they need our help,' \
         ' you can\'t  join the fight in that state." '"- Thorfin, the dwarf"''
    for character in p2:
            sys.stdout.write(character)
            sys.stdout.flush()
            sys.stdout.flush()
            time.sleep(d)
    print()
    print()
    part1_2_choice = input("~What would you like to do ? {inventory, talk or walk forward} ~:")
    if part1_2_choice == "inventory":
        inventory_access()

def inventory_access():
    print()
    print("Inventory =",inventory)
    time.sleep(b)
    inventory_ac = input("~Which item would you like to use~:")
    for string in inventory:
        if inventory_ac == "powerful potion" and "powerful potion" in inventory:
            powerful_potion()
        else:
            inventory_access()

def powerful_potion():

    if "powerful potion" in inventory:
        player["health"] += 50
        print(player["health"])

def reduce_health():

  healthcheck = int(player["health"])
  enemyattack = int("enemy_damage")
  player["health"] = healthcheck - enemyattack
  print (player["health"])
  if player["health"] <= 0:
    game_over()

# def title_screen():
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
startGame = input("Would you like to start the adventure [yes/no]:")
if startGame == "no" or startGame == "N" or startGame == "n" or startGame == "NO":
    print()
    print("Maybe next time then!")
    print()
    print("############")
    print("#   bye!   #")
    print("############")
    exit()
elif startGame == "yes" or startGame == "Y" or startGame == "y" or startGame == "YES":
    intro()

def game_over():
    print()
    print("Maybe next time then!")
    print()
    print("#############")
    print("# you lost! #")
    print("#############")
    exit()

# while game_on:
#     title_screen()