import sys
import time

player = {"weapon": None, "health": 50, "name": None}
weapons = {"Fire Staff": (3, 10), "Healing Staff": (4, 10), "Battle Axe": (3, 11), "Shadow Daggers": (5, 1),
           "DwarvenBow": (3, 17)}
# enemies = {"Goblin": ,"Caster Goblin":m "Archer Goblin"}
inventory = []
# game_on = True
a = 2
b = 0.2
c = 0.0150
d = 0.150


def intro():
    print("\nHealth = ", player["health"])
    time.sleep(b)
    print("- As you open your eyes from what is seemed to be an eternity you hear a voice -")
    print()
    p1 = '"Lad, you took a serious hit to the head,' \
         'on your feet we still need to clear the rest of the dungeon". " '"- Mysterious Figure"''
    for character in p1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    print()
    time.sleep(a)
    print("- You look around in confusion you see shadowed figures in the background fighting each other -")
    print()
    time.sleep(a)
    p2 = '" You need to get up, we are not done with this dungeon yet,' \
         'the guild will be out of their minds if they find out' \
         ' we haven\'t cleared this place from the goblins." '"- Mysterious Figure"''
    for character in p2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    time.sleep(a)
    p3 = '" The hit was hard so we need to check if everything is fine inside your head,' \
         'do you still remember who you are ? let\'s begin with your class" '"- Mysterious Figure"''
    for character in p3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    print()
    print("- Mage")
    time.sleep(b)
    print("- Cleric")
    time.sleep(b)
    print("- Rogue")
    time.sleep(b)
    print("- Warrior")
    time.sleep(b)
    print("- Archer")
    time.sleep(b)
    print()
    class_choice()


def class_choice():
    class_option = input("So,which one is your class?:")

    if class_option == "mage" or class_option == "Mage":
        mage = input("Are you sure? :")
        if mage == "yes" or mage == "Y" or mage == "y" or mage == "YES":
            player["weapon"] = "Fire Staff"
            print()
            print('"I think I am a mage"'"- You "'')
            time.sleep(a)
            print("~ You have acquired a", player["weapon"], "~")
        elif mage == "no" or "N" or mage == "n" or mage == "NO":
            class_choice()
        elif mage != "yes" or mage == "Y" or mage == "y" or mage == "YES"\
                or mage == "no" or "N" or mage == "n" or mage == "NO":
            class_choice()

    elif class_option == "cleric" or class_option == "Cleric":
        cleric = input("Are you sure? :")
        if cleric == "yes" or cleric == "Y" or cleric == "y" or cleric == "YES":
            player["weapon"] = "Healing Staff"
            print()
            print('"I think I am a cleric"'"- You "'')
            time.sleep(a)
            print("~ You have acquired a", player["weapon"], "~")
        elif cleric == "no" or cleric == "N" or cleric == "n" or cleric == "NO":
            class_choice()
        elif cleric != "yes" or cleric == "Y" or cleric == "y" or cleric == "YES" \
                or "no" or cleric == "N" or cleric == "n" or cleric == "NO":
            class_choice()

    elif class_option == "rogue" or class_option == "Rogue":
        rogue = input("Are you sure? :")
        if rogue == "yes" or rogue == "Y" or rogue == "y" or rogue == "YES":
            player["weapon"] = "Shadow Daggers"
            print()
            print('"I think I am a rogue"'"- You "'')
            time.sleep(a)
            print("~ You have acquired a", player["weapon"], "~")
        elif rogue == "no" or rogue == "N" or rogue == "n" or rogue == "NO":
            class_choice()
        elif rogue != "yes" or rogue == "Y" or rogue == "y" or rogue == "YES" or rogue == \
                "no" or rogue == "N" or rogue == "n" or rogue == "NO":
            class_choice()

    elif class_option == "warrior" or class_option == "Warrior":
        warrior = input("Are you sure? :")
        if warrior == "yes" or warrior == "Y" or warrior == "y" or warrior == "YES":
            player["weapon"] = "Battle Axe"
            print()
            print('"I think I am a warrior"'"- You "'')
            time.sleep(a)
            print("~ You have acquired a", player["weapon"], "~")
        elif warrior == "no" or warrior == "N" or warrior == "n" or warrior == "NO":
            class_choice()
        elif warrior != "yes" or warrior == "Y" or warrior == "y" or warrior == "YES"\
                or "no" or warrior == "N" or warrior == "n" or warrior == "NO":
            class_choice()

    elif class_option == "archer" or class_option == "Archer":
        print()
        archer = input("Are you sure? :")
        if archer == "yes" or archer == "Y" or archer == "y" or archer == "YES":
            player["weapon"] = "DwarvenBow"
            print()
            print('"I think I am a archer"'"- You "'')
            time.sleep(a)
            print("~ You have acquired a", player["weapon"], "~")
        elif archer == "no" or archer == "N" or archer == "n" or archer == "NO":
            class_choice()
        elif archer != "no" or archer == "N" or archer == "n" or archer == "NO" or \
                archer == "yes" or archer == "Y" or archer == "y" or archer == "YES":
            class_choice()

    elif class_option != "mage " or class_option == "Mage" or class_option == "cleric" or class_option == "Cleric" \
            or class_option == "rogue" or class_option == "Rogue" or class_option == "warrior" \
            or class_option == "Warrior" or class_option == "archer" or class_option == "Archer":
        class_choice()

    print()
    time.sleep(a)
    part1_1()


def part1_1():
    p1 = '" Splendid lad!, glad you still remember but what about your name ?" '"- Mysterious Figure"''
    for character in p1:
        sys.stdout.write(character)
        sys.stdout.flush()
        sys.stdout.flush()
        time.sleep(c)
    print()
    time.sleep(c)
    n_choice()


def n_choice():
    print()
    name = input("What's your name?:")
    if input:
        player["name"] = name
        n_confirm()


def n_confirm():
    name_confirm = input("Are you sure  " + player["name"] + "  is your name?:")
    if name_confirm == "yes" or name_confirm == "Y" or name_confirm == "y" or name_confirm == "YES":
        print("------------------------------------------------------------------")
        part1_2()
    elif name_confirm == "no" or name_confirm == "N" or name_confirm == "n" or name_confirm == "NO":
        player["name"] = None
        n_choice()


def part1_2():
    print()
    p1 = '" Fantastic lad!, seems like everything inside that box of yours is fine,take this [powerful potion]' \
         ' it will heal you from that hit and by the ' \
         'way I am Thorfin in case you don\'t remember my name anymore HAHAHAHA." '"- Thorfin, the dwarf"''
    for character in p1:
        sys.stdout.write(character)
        sys.stdout.flush()
        sys.stdout.flush()
        time.sleep(c)
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
        time.sleep(c)
    print()
    print()
    part1_2_choice()


def part1_2_choice():
    part1_2choice = input("~What would you like to do ? {inventory, talk or walk forward} ~:")
    if part1_2choice == "inventory":
        inventory_access()
    elif part1_2choice == "talk":
        part1_2_talk()
    elif part1_2choice == "walk forward":
        part1_2_walk_forward()
    elif part1_2choice != "inventory" or "talk" or "walk forward":
        part1_2_choice()
    elif part1_2choice == "talk" and player["health"] == 100:
        part2_1()


def part1_2_talk():
    print()
    print()
    print('"I know everything must be confusing right now ''' + player["name"] +
          ''" but we need to help the others fight the goblins, "
          "talk to me again once you are healed up and ready to fight"' ''" - Thorfin, the dwarf ''')
    print()
    time.sleep(b)
    part1_2_choice()


def part2_1():
    print()
    print()
    p1 = '"Great you are back in shape, we need to hurry up the others need our help lad!"''" - Thorfin, the dwarf '''
    for character in p1:
        sys.stdout.write(character)
        sys.stdout.flush()
        sys.stdout.flush()
        time.sleep(c)
    print()
    time.sleep(b)
    print("- An audible bang can be heard in the distance, "
          "with the corner of your eye you see a shadow flying against the wall of the cave-")
    print("- There is blood on the floor, as you approach the shadow succumbed in the wall you hear Thorfin shouting-")
    print()
    time.sleep(a)
    p2 = '"'


def part1_2_walk_forward():
    print()
    print()
    print("- You take a few steps forward but the cave is badly illuminated,"
          " you can't really see anything in front of you, "
          "the only source of light comes from Thorfin and the other members of "
          "the party holding their torches as they fight the group of goblins -")
    time.sleep(b)
    print('"I think I should head back and help Thorfin "'"- You "'')
    time.sleep(b)
    print()
    part1_2_choice()


def inventory_access():
    print()
    print("Inventory =", inventory)
    time.sleep(b)
    inventory_ac = input("~Which item would you like to use~:")
    for string in inventory:
        if inventory_ac == "powerful potion" and "powerful potion" in inventory:
            player["health"] += 50
            print("You used a [powerful potion], you have healed 50 life points, Health = ", player["health"], "~")

        else:
            inventory_access()


def reduce_health():
    healthcheck = int(player["health"])
    enemyattack = int("enemy_damage")
    player["health"] = healthcheck - enemyattack
    print(player["health"])
    if player["health"] <= 0:
        game_over()


def game_start():
    startGame = input("Would you like to resume the adventure [yes/no]:")
    if startGame == "no" or startGame == "N" or startGame == "n" or startGame == "NO":
        print()
        print("Maybe next time then!")
        print()
        print("############")
        print("#   bye!   #")
        print("############")
        exit()
    elif startGame == "yes" or startGame == "Y" or startGame == "y" or startGame == "YES":
        print("------------------------------------------------------------------")
        intro()
    elif startGame != "yes" or startGame == "Y" or startGame == "y" or startGame == "YES"\
            or startGame == "no" or startGame == "N" or startGame == "n" or startGame == "NO":
        game_start()


def game_over():
    print()
    print("Maybe next time then!")
    print()
    print("#############")
    print("# you lost! #")
    print("#############")
    exit()


# def title_screen():
print()
print()
print("""##########################################################################################################################################################################################
#                                                                                                                                                                                        #
# ████████▄  ███    █▄  ███▄▄▄▄      ▄██████▄     ▄████████  ▄██████▄  ███▄▄▄▄         ▄████████    ▄████████    ▄████████  ▄█     █▄   ▄█          ▄████████    ▄████████    ▄████████  #
# ███   ▀███ ███    ███ ███▀▀▀██▄   ███    ███   ███    ███ ███    ███ ███▀▀▀██▄      ███    ███   ███    ███   ███    ███ ███     ███ ███         ███    ███   ███    ███   ███    ███  #
# ███    ███ ███    ███ ███   ███   ███    █▀    ███    █▀  ███    ███ ███   ███      ███    █▀    ███    ███   ███    ███ ███     ███ ███         ███    █▀    ███    ███   ███    █▀   #
# ███    ███ ███    ███ ███   ███  ▄███         ▄███▄▄▄     ███    ███ ███   ███      ███         ▄███▄▄▄▄██▀   ███    ███ ███     ███ ███        ▄███▄▄▄      ▄███▄▄▄▄██▀   ███         #
# ███    ███ ███    ███ ███   ███ ▀▀███ ████▄  ▀▀███▀▀▀     ███    ███ ███   ███      ███        ▀▀███▀▀▀▀▀   ▀███████████ ███     ███ ███       ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ▀███████████  #
# ███    ███ ███    ███ ███   ███   ███    ███   ███    █▄  ███    ███ ███   ███      ███    █▄  ▀███████████   ███    ███ ███     ███ ███         ███    █▄  ▀███████████          ███  #
# ███   ▄███ ███    ███ ███   ███   ███    ███   ███    ███ ███    ███ ███   ███      ███    ███   ███    ███   ███    ███ ███ ▄█▄ ███ ███▌    ▄   ███    ███   ███    ███    ▄█    ███  #
# ████████▀  ████████▀   ▀█   █▀    ████████▀    ██████████  ▀██████▀   ▀█   █▀       ████████▀    ███    ███   ███    █▀   ▀███▀███▀  █████▄▄██   ██████████   ███    ███  ▄████████▀   #
#                                                                                                 ███    ███                                                   ███    ███                #
##########################################################################################################################################################################################


                                                                      Author: Lorenzo Lombardo - 2020326""")
print()
print()
time.sleep(b)
intro1 = "-- Welcome to the world of Vastan adventurer! \n" \
         " Prepare yourself to live the life of an adventurer in the magical world of Vastan. \n " \
         "You and your party have recently embarked on a quest " \
         "as requested by the Vastan Guild of Adventurers. \n " \
         "Your job is to enter an abandon mine now turned a dungeon by the goblin pests " \
         "and eradicate all goblin there, the guild has promised a generous amount " \
         "of gold once the task is completed.--"
for character in intro1:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(c)
print()
print()
intro2 = "-- As a new member, your leader decided this was a perfect opportunity to test your skills.\n" \
         "As you and your party make your way deeper in the dungeon slaying goblins left and right,however, " \
         "the adventure takes a sudden turn as you get knocked out " \
         "by a separate group of goblins arriving from the entrance of the dungeon. \n" \
         "You and your party have been ambushed!--"
for character in intro2:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(c)
print()
print()
print("- Everything is dark -")
print()
game_start()

# while game_on:
#     title_screen()
