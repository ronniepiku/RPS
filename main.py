#This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import play_quincy, play_abbey, play_kris, play_mrugesh
from unittest import main

play(play_quincy, quincy, 5000)
play(play_abbey, abbey, 5000, verbose=False)
play(play_kris, kris, 5000, verbose=False)
play(play_mrugesh, mrugesh, 5000, verbose=False)

# Uncomment line below to play interactively against a bot:
# play(human, mrugesh, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(human, random_player, 1000)



# Uncomment line below to run unit tests automatically
#main(module='test_module', exit=False)