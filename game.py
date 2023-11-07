# My pokemon program
import os
import random

healthPlayer = 100
healthRobot = 200
poisonDamage = 0


def main(name): 
    print("hellllo " + name)
    while (healthPlayer > 0 and healthRobot > 0):
#        os.system('clear')
        print("The robots health is " + str(healthRobot) )
        print("Watch out, your health is " + str(healthPlayer))
        print("It's your turn! Choose an option:")
        print("1. Attack")
        print("2. Regenerate")
        print("3. Poison")
        print("4. Bite")
        move = input("> ")
        #bit weird anouncing what someone just inputted... keeping it for now.
        print("Your move is " + move)
        if move == "1":
            attack()
        elif move == "2":
            regenerate()
        elif move == "3":
            poison()
        else:
            print("I dont know that option")
    if (healthPlayer < 0 and healthRobot > 0):
        print("You have been defeated by the robot")

    if (healthRobot < 0 and healthPlayer > 0):
        print("The robot has been slain!")

def attack():
    global healthRobot
    print("Uppercut!")
    random_number = random.randint(4,10)
    damage = random_number + poisonDamage
    healthRobot = healthRobot - damage

def regenerate():
    global healthPlayer
    print("Im healing")
    healthPlayer = healthPlayer + 8

def poison():
    global poisonDamage
    poisonDamage += 4
    print(str(poisonDamage) + " damage points added to youer attack from now on")

 #   global healthPlayer
  #  print("Im healing")


#def bite():
 #   global healthPlayer
  #  print("Im healing")
   # healthPlayer = healthPlayer + 8
     

main("nathan")