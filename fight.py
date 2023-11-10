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