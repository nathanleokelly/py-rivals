import random

def showAttack(gameInfo):
    result = "\n".join(gameInfo['lastMessage'])
    print("")
    print(result)
    print("")

def attack(gameInfo, fighter):
    gameInfo['lastMessage'].append("Your attack was an:")
    random_number = random.randint(4,10)
    if random_number > 8:
        gameInfo['lastMessage'].append("Uppercut!")
    else:
        gameInfo['lastMessage'].append("Light jab")
    if fighter == "player":
        damage = random_number + gameInfo['poisonDamagePlayer']
        gameInfo['healthRobot'] = gameInfo['healthRobot'] - damage
    else:
        damage = random_number + gameInfo['poisonDamageRobot']
        gameInfo['healthPlayer'] = gameInfo['healthPlayer'] - damage

def regenerate(gameInfo, fighter):
    if fighter == "player":
        print("Im healing")
        gameInfo['lastMessage'].append("I've healed some health!")
        gameInfo['healthPlayer'] = gameInfo['healthPlayer'] + 8
    else:
        gameInfo['lastMessage'].append("The robot has recharged 8%")
        gameInfo['healthRobot'] = gameInfo['healthRobot'] + 8

def poison(gameInfo, fighter):
    if fighter == "player":
        gameInfo['poisonDamagePlayer'] += 4
        print(str(gameInfo['poisonDamagePlayer']) + " damage points added to your attack from now on")
    else:
        gameInfo['poisonDamageRobot'] += 6
        print("He improved the code of his attack! " + str(gameInfo['poisonDamageRobot']) + " damage points will be added to each the robots attack from now on.")

def bite(gameInfo, fighter):
    if not gameInfo['hasBitten']:
        random_number = random.randint(4,10)
        gameInfo['biteDamage'] = (random_number + gameInfo['poisonDamage']) * 2
        gameInfo['healthRobot'] = gameInfo['healthRobot'] - gameInfo['biteDamage']
        gameInfo['healthPlayer'] = gameInfo['healthPlayer'] - 7
        print("My last ditch effort, its now or never!")
        gameInfo['hasBitten'] = True
    else:
        print("You have already used Serpents final strike")