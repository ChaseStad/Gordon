import sys



from gordonBot import ChaseBot

import random 
import sys

from __init__ import run_ladder_game
from sc2 import maps
from sc2.data import Difficulty, Race
from sc2.main import run_game, run_multiple_games
from sc2.player import Bot, Computer, Human

from sc2.bot_ai import BotAI







ChaseBot = Bot(Race.Terran,ChaseBot())


# Start game
if __name__ == "__main__":
    if "--LadderServer" in sys.argv:
        # Ladder game started by LadderManager
        print("Starting ladder game...")
        result, opponentid = run_ladder_game(ChaseBot)
        print(result, " against opponent ", opponentid)
    else:
        print("Starting local game...")
        run_game(maps.get("PersephoneAIE"), [ChaseBot, Computer(Race.Terran,Difficulty.VeryHard)], realtime=True, save_replay_as=f"lastReplay.SC2Replay")










  