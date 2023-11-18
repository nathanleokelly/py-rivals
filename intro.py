import os


def say(messages, wait=True):
  os.system('clear')
  print("")
  print("")
  result = "\n".join(messages)
  print(result)
  print("")
  print("")
  if wait:
    input("Press ENTER to continue ...")


def introduction():
  say([
      "I am an evil AI bot!", "I challenge you to a duel you slimy snake.",
      "Why would a snake even own a laptop?", "", "I do not know!!",
      "Nevertheless, if you lose, I shall take over your laptop."
  ])
  say([
      "You will be my first conquest in my mission for AI world domination!",
      "", "   (That is, if we are to reach our goal of taking",
      "     over the world by 2029", "     as foretold by SkyNet. )", "", "",
      "The game will now begin ..."
  ])


def robotWonOutro(gameInfo):
  os.system('clear')
  say([
      "",
      "Ha, ha! Silly human .. or should I say silly snake!",
      "I have won the duel! ",
      "I will now destroy your computer!",
      "",
  ])
  say([
      "... bleep bleep .. bloop bloop",
      "... Hard disk format will now begin...",
      "... Please do not unplug cable or process will fail...",
      "... Thank you for your cooperation ...", "... bleep .. bloop ..."
  ], False)
  choice = input("Please confirm hard drive deletion? (y/n)")
  return choice


def playerWonOutro(gameInfo):
  os.system('clear')
  say([
      f"You have defeated me by {gameInfo['healthPlayer'] - gameInfo['healthRobot']} points :(",
      "", "I did not expect this.", "",
      "I am master of logic and my superior intellect should have easily out-witted your mere biological nuerons. ",
      "Perhaps I have met my match? Somehow, I think it was a case of beginners luck.",
      ""
  ], False)
  choice = input("How about best of three? (y/n)")
  return choice
