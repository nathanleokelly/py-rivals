# My pokemon program
import os

healthPlayer = 100
healthRobot = 200

def main(name): 
    print("hellllo " + name)
    while (healthPlayer > 0 and healthRobot > 0):
#        os.system('clear')
        print("The robots health is " + str(healthRobot) )
        print("It's your turn! Choose an option:")
        print("1. Attack")
        print("2. Heal")
        move = input("> ")
        print("Your move is " + move)
        if move == "1":
            attack()
        elif move == "2":
            heal()
        else:
            print("I dont know that option")

def attack():
    global healthRobot
    print("im attacking")
    healthRobot = healthRobot - 12

def heal():
    print("Im healing")
    healthRobot = healthRobot + 8


main("nathan")


