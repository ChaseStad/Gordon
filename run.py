import sys

from ladder import run_ladder_game

from gordonBot import ChaseBot

import random 

from sc2 import maps
from sc2.data import Difficulty, Race
from sc2.main import run_game, run_multiple_games
from sc2.player import Bot, Computer, Human

from sc2.bot_ai import BotAI
from sc2.data import Difficulty, Race
from sc2.ids.ability_id import AbilityId
from sc2.ids.unit_typeid import UnitTypeId
from sc2.position import Point2, Point3
from sc2.unit import Unit
from sc2.units import Units

from sc2.ids.buff_id import BuffId
from sc2.ids.upgrade_id import UpgradeId

import numpy as np



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
        run_game(maps.get("TorchesAIE"), [ChaseBot, Computer(Race.Terran,Difficulty.VeryHard)], realtime=False, save_replay_as=f"lastReplay.SC2Replay")

            