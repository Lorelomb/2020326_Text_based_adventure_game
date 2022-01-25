import sys
import time
player = {"damage": (3,15), "health": 50 , "name": None}
Goblin = {"damage": (5, 18), "health": 25, "name": "Goblin", "restart": 3}
# Caster_Goblin = {"damage": (5, 20), "health": (15), "name": "Goblin Shaman"}
# Archer_Goblin = {"damage": (5, 13), "health": (20), "name": "Goblin Hunter"}
# Hulk_Goblin = {"damage": (5, 25), "health": (35), "name": "Giant Goblin"}
King_Goblin = {"damage": (6, 35), "health": 41, "name": "Goblin Leader", "restart": 3}
Fire_Staff = (3, 20)
Healing_Staff = (3, 10)
Shadow_Daggers = (3, 16)
Battle_Axe = (3, 18)
DwarvenBow = (3, 13)
inventory = []
healed = 1
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
            player["damage"] = Fire_Staff
            print()
            print('"I think I am a mage"'"- You "'')
            time.sleep(a)
            print("~ You have acquired a Fire Staff ~")
        elif mage == "no" or "N" or mage == "n" or mage == "NO":
            class_choice()
        elif mage != "yes" or mage == "Y" or mage == "y" or mage == "YES" \
                or mage == "no" or "N" or mage == "n" or mage == "NO":
            class_choice()

    elif class_option == "cleric" or class_option == "Cleric":
        cleric = input("Are you sure? :")
        if cleric == "yes" or cleric == "Y" or cleric == "y" or cleric == "YES":
            player["damage"] = Healing_Staff
            print()
            print('"I think I am a cleric"'"- You "'')
            time.sleep(a)
            print("~ You have acquired a Healing Staff ~")
        elif cleric == "no" or cleric == "N" or cleric == "n" or cleric == "NO":
            class_choice()
        elif cleric != "yes" or cleric == "Y" or cleric == "y" or cleric == "YES" \
                or "no" or cleric == "N" or cleric == "n" or cleric == "NO":
            class_choice()

    elif class_option == "rogue" or class_option == "Rogue":
        rogue = input("Are you sure? :")
        if rogue == "yes" or rogue == "Y" or rogue == "y" or rogue == "YES":
            player["damage"] = Shadow_Daggers
            print()
            print('"I think I am a rogue"'"- You "'')
            time.sleep(a)
            print("~ You have acquired a Shadow Daggers~")
        elif rogue == "no" or rogue == "N" or rogue == "n" or rogue == "NO":
            class_choice()
        elif rogue != "yes" or rogue == "Y" or rogue == "y" or rogue == "YES" or rogue == \
                "no" or rogue == "N" or rogue == "n" or rogue == "NO":
            class_choice()

    elif class_option == "warrior" or class_option == "Warrior":
        warrior = input("Are you sure? :")
        if warrior == "yes" or warrior == "Y" or warrior == "y" or warrior == "YES":
            player["damage"] = Battle_Axe
            print()
            print('"I think I am a warrior"'"- You "'')
            time.sleep(a)
            print("~ You have acquired a Battle Axe ~")
        elif warrior == "no" or warrior == "N" or warrior == "n" or warrior == "NO":
            class_choice()
        elif warrior != "yes" or warrior == "Y" or warrior == "y" or warrior == "YES" \
                or "no" or warrior == "N" or warrior == "n" or warrior == "NO":
            class_choice()

    elif class_option == "archer" or class_option == "Archer":
        print()
        archer = input("Are you sure? :")
        if archer == "yes" or archer == "Y" or archer == "y" or archer == "YES":
            player["damage"] = DwarvenBow
            print()
            print('"I think I am a archer"'"- You "'')
            time.sleep(a)
            print("~ You have acquired a DwarvenBow ~")
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
    player["name"] = name
    print(player["name"])
    n_confirm()


def n_confirm():
    name_confirm = input("Are you sure that is your name?:")
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
    part1_2choice = input("~What would you like to do ? [inventory /talk / walk forward] ~:")
    if part1_2choice == "inventory":
        inventory_access()
    elif part1_2choice == "talk" and player["health"] == 100:
        print("------------------------------------------------------------------")
        part2_1()
    elif part1_2choice == "talk":
        part1_2_talk()
    elif part1_2choice == "walk forward":
        part1_2_walk_forward()
    elif part1_2choice != "inventory" or "talk" or "walk forward":
        part1_2_choice()


def part1_2_talk():
    print()
    print()
    print('"I know everything must be confusing right now ''' + str(player["name"]) +
          ''" but we need to help the others fight the goblins, "
          "talk to me again once you are healed up and ready to fight"' ''" - Thorfin, the dwarf ''')
    print()
    time.sleep(b)
    part1_2_choice()


def part2_1():
    print()
    p1 = '"Great you are back in shape, we need to hurry up the others need our help lad!"'' - Thorfin, the dwarf '''
    for character in p1:
        sys.stdout.write(character)
        sys.stdout.flush()
        sys.stdout.flush()
        time.sleep(c)
    print()
    print()
    time.sleep(b)
    print("- An audible bang can be heard in the distance, "
          "with the corner of your eye you see a shadow flying against the wall of the cave-")
    print("- There is blood on the floor, as you approach the shadow succumbed in the wall you hear Thorfin shouting-")
    print()
    time.sleep(a)
    p2 = '" To your weapon lad!, prepare yourself they have taken out one of us ,' \
         ' but with you back in a one piece lad we will be able to stop the horde of goblins"''- Thorfin, the dwarf '''
    for character in p2:
        sys.stdout.write(character)
        sys.stdout.flush()
        sys.stdout.flush()
        time.sleep(c)
    print()
    if Goblin["restart"] == 3:
        combat_1()


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
    global healed
    print()
    print("Inventory =", inventory)
    time.sleep(b)
    inventory_ac = input("~Which item would you like to use~:")
    if inventory_ac == "powerful potion" and "powerful potion" in inventory:
        player["health"] += 50
        print("You used a [powerful potion], you have healed 50 life points, Health = ", str(player["health"]), "~")
        healed = 2
        if healed == 2:
            print()
            part1_2_choice()
            healed = 1


def combat_1():
    Goblin["restart"] = 2
    commands(player, Goblin)


def combat_2():
    King_Goblin["restart"] = 2
    commands(player, King_Goblin)


def c_rest1():
    print()
    p1 = '"Great job lad!, we have no time to spare have this potion now and prepare for the next battle"'' - Thorfin, the dwarf '''
    for character in p1:
        sys.stdout.write(character)
        sys.stdout.flush()
        sys.stdout.flush()
        time.sleep(c)
    print()
    player["health"] = 100
    time.sleep(b)
    print("~ Thorfin gave you a [higher potion], health restored to", str(player["health"]))
    print()
    print("- As the other goblins are defeated by the rest of the party a mass of shadows approaches - ")
    time.sleep(b)
    print("- GOBLIN KING HAS JOINED THE FIGHT - ")
    print()
    p2 = '"This is it! , the big boy is finally joining the party ,' \
         ' get ready this I will be a though one, once we are done drinks are on me !"'' - Thorfin, the dwarf '''
    for character in p2:
        sys.stdout.write(character)
        sys.stdout.flush()
        sys.stdout.flush()
        time.sleep(c)
    print()
    combat_2()


def end_game():
    print()
    print(" - And with a combined effort "
          "all the party and you the King Goblin is finally put down -")
    time.sleep(b)
    print("-BOOM-")
    print("The goblin massive body drops dead on the dungeon floor,"
          "but because of its sheer size the cave starts to rumble, pieces of the ceiling are falling and the cave "
          "starts to crumble")
    print()
    p1 = '"WE DID IT HAHAHAHAAHA , we must run away from the crumbling cavern, head for the exit ! "'' - Thorfin, the dwarf '''
    for character in p1:
        sys.stdout.write(character)
        sys.stdout.flush()
        sys.stdout.flush()
        time.sleep(c)
    print()
    print()
    p2 = " -- Having survived the encounter with the Goblin Leader the heroes headed to t" \
         "he Vastan Guild of Adventurers to collect their very deserved reward. \n" \
         "Because of your crucial role during the fight against the Goblin Leader " \
         "the party leader recognised your skills as an adventure allowing your permanent stay.-"
    for character in p2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    print("Bye for now!")
    print()
    print("""
                                                $$$$$$$$\                 $$\ 
                                                $$  _____|                $$ |
                                                $$ |      $$$$$$$\   $$$$$$$ |
                                                $$$$$\    $$  __$$\ $$  __$$ |
                                                $$  __|   $$ |  $$ |$$ /  $$ |
                                                $$ |      $$ |  $$ |$$ |  $$ |
                                                $$$$$$$$\ $$ |  $$ |\$$$$$$$ |
                                                \________|\__|  \__| \_______|
                                                                      
    """)
    exit()


def reduce_health(attacker, defender):
    from random import randint
    dmg = randint(attacker["damage"][0], attacker["damage"][1])
    defender["health"] = defender["health"] - dmg
    if player["health"] <= 0:
        print('{} has been slain!'.format(defender["name"]))
        game_over()
    elif Goblin["health"] <= 0 and Goblin["restart"] == 2:
        print('{} has been slain!'.format(defender["name"]))
        print("------------------------------------------------------------------")
        Goblin["restart"] = 1
        c_rest1()
    elif King_Goblin["health"] <= 0 and King_Goblin["restart"] == 2:
        print('{} has been slain!'.format(defender["name"]))
        print("------------------------------------------------------------------")
        King_Goblin["restart"] = 1
        end_game()
    else:
        print('{} takes {} damage!'.format(defender["name"], dmg))


def commands(hero, enemy):
    while True:
        print("------------------------------------------------------------------")
        cmd = input("Do you want to attack [yes/no] ?:").lower()
        if "yes" in cmd:
            if "yes" in cmd:
                print()
                print("{} attacks the monster!".format(hero["name"]))
                reduce_health(hero, enemy)
                print("monster health is at {}!".format(enemy["health"]))
                print()
                print("{} attacks back!".format(enemy["name"]))
                reduce_health(enemy, hero)
                print("your health is at {}!".format(hero["health"]))
        elif "no" in cmd:
            print()
            print("{} takes the chance to attack!".format(enemy["name"]))
            reduce_health(enemy, hero)
        else:
            pass


def game_start():
    startGame = input("Would you like to resume the adventure [yes/no]:")
    if startGame == "no" or startGame == "N" or startGame == "n" or startGame == "NO":
        print()
        print("Maybe next time then!")
        print()
        print("""
                                            ___   _     ____
                                            | |_) \ \_/ | |_  
                                            |_|_)  |_|  |_|__ 
        """)
        exit()
    elif startGame == "yes" or startGame == "Y" or startGame == "y" or startGame == "YES":
        print("------------------------------------------------------------------")
        intro()
    elif startGame != "yes" or startGame == "Y" or startGame == "y" or startGame == "YES" \
            or startGame == "no" or startGame == "N" or startGame == "n" or startGame == "NO":
        game_start()


def game_over():
    print("------------------------------------------------------------------")
    print()
    print("Your party was defeated")
    print()
    print("""
                                _   _ ____ _  _    _    ____ ____ ___ !
                                 \_/  |  | |  |    |    |  | [__   |  !
                                  |   |__| |__|    |___ |__| ___]  |  !                       
    """)
    print()
    question = input("Would you like to retry? you will start at the first encounter, [yes/no]:")
    if question == "yes":
        Goblin["restart"] = 3
        King_Goblin["restart"] = 3
        player["health"] = 100
        Goblin["health"] = 25
        King_Goblin["health"] = 41
        combat_1()
    if question == "no":
        print()
        print("Maybe next time then!")
        print("""
                                                    ___   _     ____
                                                    | |_) \ \_/ | |_  
                                                    |_|_)  |_|  |_|__ 
        """)
        exit()
        exit()



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
