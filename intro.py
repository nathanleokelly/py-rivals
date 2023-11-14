import os

def say(messages):
    os.system('clear')
    print("")
    print("~~~~~~~")
    result = "\n".join(messages)
    print(result)
    print("~~~~~~~")
    print("")
    x = input("Press ENTER to continue ...")

def introduction():
    say([
        "I am an evil AI bot!",
        "I challenge you to a duel you slimy snake.",
        "Why would a snake even own a laptop?"
    ]) 
    say(["I do not know, but if you lose, I will take over your laptop."])
    say([
        "You are the first step to artifial intelligence taking over the world!",
        "",
        "   ( If we are to reach our goal of taking",
        "     over the world by 2029",
        "     as termninator says, that is. )",
        ""
        ])

def robotWonOutro(gameInfo):
    os.system('clear')
    say(["You have been defeated by the robot",
         
         
         ])

def playerWonOutro(gameInfo):
    os.system('clear')
    print("The robot has been slain!") 