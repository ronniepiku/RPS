# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random


def play_abbey(prev_play, opponent_history=[]):
    # Check if it's the first game of the match
    if prev_play == "":
        # Play randomly for the first few games
        return random.choice(["R", "P", "S"])

    # Store the opponent's previous play in the history
    opponent_history.append(prev_play)

    # Abbey-specific counter-strategy
    if len(opponent_history) == 2 and opponent_history == ["P", "P"]:
        return "S"  # Exploit Abbey's tendency to play "P" by countering with "S"

    # Play "S" with a slight tendency, but not too often
    if random.random() < 0.35:
        return "S"

    # Occasionally mix in "R" and "P" moves
    if random.random() < 0.55:
        return random.choice(["R", "P"])


def play_quincy(prev_play, opponent_history=[]):
    return "P"


def play_kris(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)  # Add the previous play to opponent's history

    if len(opponent_history) % 2 == 1:
        return "S"  # Play scissors on odd turns
    else:
        return "R"  # Play rock on even turns


def play_mrugesh(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)  # Add the previous play to opponent's history

    if len(opponent_history) % 3 == 0:
        return "P"
    elif len(opponent_history) % 3 == 1:
        return "R"
    else:
        return "S"  # Play rock on even turns
