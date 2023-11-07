# My pokemon program
import os
import random

healthPlayer = 100
healthRobot = 200
poisonDamage = 0
biteDamage = 0
hasBitten = False
lastMessage = []

def main(name): 
    global lastMessage
    print("Hello " + name)
    while (healthPlayer > 0 and healthRobot > 0):
        os.system('clear')
        print("The robots health is " + str(healthRobot) )
        print("Watch out, your health is " + str(healthPlayer))
        showAttack()
        print("It's your turn! Choose an option:")
        print("1. Attack                      (Deal 4 - 10 damage to robot)")
        print("2. Regenerate                  (Gain 8 healthpoints)")
        print("3. Poison                      (Add 4 to attack forever)")
        print("4. Serpents final strike       (Deal 2 times more damage than attack. One time use and loses you 2 hearts.)")
        lastMessage = []
        move = input("> ")
        #bit weird anouncing what someone just inputted... keeping it for now.
        print("Your move is " + move)
        if move == "1":
            attack()
        elif move == "2":
            regenerate()
        elif move == "3":
            poison()
        elif move == "4":
            bite()
        else:
            print("I dont know that option")
    if (healthPlayer < 0 and healthRobot > 0):
        print("You have been defeated by the robot")

    if (healthRobot < 0 and healthPlayer > 0):
        print("The robot has been slain!")

def showAttack():
    global lastMessage
    result = "\n".join(lastMessage)
    print("")
    print(result)
    print("")


def attack():
    global lastMessage
    global healthRobot
    lastMessage.append("Your attack was an:")
    random_number = random.randint(4,10)
    if random_number > 8:
        lastMessage.append("Uppercut!")
    else:
        lastMessage.append("Light jab")
    damage = random_number + poisonDamage
    healthRobot = healthRobot - damage

def regenerate():
    global lastMessage
    global healthPlayer
    print("Im healing")
    lastMessage.append("Uppercut!")
    healthPlayer = healthPlayer + 8

def poison():
    global lastMessage
    global poisonDamage
    poisonDamage += 4
    print(str(poisonDamage) + " damage points added to your attack from now on")

def bite():
    global lastMessage
    global biteDamage, healthRobot, hasBitten, healthPlayer
    if not hasBitten:
        random_number = random.randint(4,10)
        biteDamage = (random_number + poisonDamage) *2
        healthRobot = healthRobot - biteDamage
        healthPlayer = healthPlayer - 7
        print("My last ditch effort, its now or never!")
        hasBitten = True
    else:
        print("You have already used Serpents final strike")
     

main("nathan")