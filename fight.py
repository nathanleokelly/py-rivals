import random

def showAttack(gameInfo):
    result = "\n".join(gameInfo['lastMessage'])
    print("")
    print(result)
    print("")

def attack(gameInfo, fighter):
    gameInfo['lastMessage'].append(f"Fighter {fighter}, attacked with an:") #Uses fighter variable to decide which fighter attacked. If the attack is big, it will send "Uppercut".
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
    gameInfo['lastMessage'].append(f"Fighter {fighter}, took a medpack to regenerate health")
    if fighter == "player":
        gameInfo['lastMessage'].append("Im healing")
        gameInfo['lastMessage'].append("I've healed some health!")
        gameInfo['healthPlayer'] = gameInfo['healthPlayer'] + 8
    else:
        gameInfo['lastMessage'].append("The robot has recharged 8%")
        gameInfo['healthRobot'] = gameInfo['healthRobot'] + 5

def poison(gameInfo, fighter):
    #finish the game.py
    if fighter == "player":
        gameInfo['poisonDamagePlayer'] += 5
        gameInfo["lastMessage"].append(str(gameInfo['poisonDamagePlayer']) + " damage points added to your attack from now on")
    else:
        gameInfo['poisonDamageRobot'] += 4
        gameInfo['lastMessage'].append("Robot improved the code of his attack system! ")
        gameInfo['lastMessage'].append(str(gameInfo['poisonDamageRobot']) + " damage points will be added to each the robots attack from now on.")

def bite(gameInfo):
    if not gameInfo['hasBitten']:
        random_number = random.randint(4,10)
        gameInfo['biteDamage'] = (random_number + gameInfo['poisonDamagePlayer']) * 2
        gameInfo['healthRobot'] = gameInfo['healthRobot'] - gameInfo['biteDamage']
        gameInfo['healthPlayer'] = gameInfo['healthPlayer'] - 7
        gameInfo['lastMessage'].append("My last ditch effort, its now or never!")
        gameInfo['hasBitten'] = True
    else:
        gameInfo['lastMessage'].append("You have already used Serpents final strike. Turn wasted!")