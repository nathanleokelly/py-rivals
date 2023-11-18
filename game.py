# My pokemon program
import os
import random

import intro
import fight

gameInfo = {
    'healthPlayer': 100,
    'healthRobot': 200,
    'poisonDamagePlayer': 0,
    'poisonDamageRobot': 0,
    'biteDamage': 0,
    'hasBitten': False,
    'lastMessage': []
}
# Repl.it


def main():
  global gameInfo
  intro.introduction()
  #Applies when the two players are alive
  while (gameInfo['healthPlayer'] > 0 and gameInfo['healthRobot'] > 0):
    os.system('clear')
    print("The robots health is " + str(gameInfo['healthRobot']))
    print("Watch out, your health is " + str(gameInfo['healthPlayer']))
    fight.showAttack(gameInfo)

    # Players turn
    print("It's your turn! Choose an option:")
    print("1. Attack                      (Deal 4 - 10 damage to robot)")
    print("2. Regenerate                  (Gain 8 healthpoints)")
    print("3. Poison                      (Add 5 to attack forever)")
    if not gameInfo['hasBitten']:
      print(
          "4. Serpents final strike       (Deal 2 times more damage than attack. One time use and loses you 2 hearts.)"
      )
    gameInfo['lastMessage'] = []
    move = input("> ")
    fightMove(move, "player")

    gameInfo['lastMessage'].append(" -- ")
    # Robot's turn
    chance = random.randint(1, 10)
    if chance < 6:
      move = 1
    elif chance < 9:
      move = 3
    else:
      move = 2
    fightMove(str(move), "robot")

  # game over: show who won
  if (gameInfo['healthPlayer'] < 0 and gameInfo['healthRobot'] > 0):
    intro.robotWonOutro(gameInfo)

  if (gameInfo['healthRobot'] < 0 and gameInfo['healthPlayer'] > 0):
    intro.playerWonOutro(gameInfo)


def fightMove(move, fighter):
  if move == "1":
    fight.attack(gameInfo, fighter)
  elif move == "2":
    fight.regenerate(gameInfo, fighter)
  elif move == "3":
    fight.poison(gameInfo, fighter)
  elif move == "4":
    fight.bite(gameInfo)
  else:
    print("I dont know that option")


main()
