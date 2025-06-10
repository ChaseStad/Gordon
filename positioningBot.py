import random
from random import randint

import numpy as np

import math

import logging

logging.getLogger("sc2.bot_ai").setLevel(logging.CRITICAL)

from sc2 import maps
from sc2.bot_ai import BotAI
from sc2.data import Race, Difficulty
from sc2.ids.ability_id import AbilityId
from sc2.ids.upgrade_id import UpgradeId
from sc2.ids.unit_typeid import UnitTypeId
from sc2.main import run_game
from sc2.player import Bot, Computer
from sc2.position import Point2, Point3
from sc2.unit import Unit
from sc2.units import Units
from sc2.data import Result
from sc2.constants import *
from unitmanager import UnitManager 
from buildingManager import BuildingManager

class PosBot(BotAI):
    async def on_step(self, iteration: int):
        ccs: Units = self.townhalls.filter(
            lambda cc: cc.type_id in {
            UnitTypeId.COMMANDCENTER,
            UnitTypeId.ORBITALCOMMAND,
            UnitTypeId.PLANETARYFORTRESS,
            }
        )
        self.client.debug_all_resources()



        if ccs:
            cc: Unit = ccs.first
        

        print(cc.position)
        list = []
        for item in self.structures(UnitTypeId.BARRACKS):
            list.append(f"Point2({item.position})")
        print(len(list))
        print(f"Barracks Positions: {list}")
        list = []
        for item in self.structures(UnitTypeId.SUPPLYDEPOT):
            list.append(f"Point2({item.position})")
        print(len(list))
        print(f"Depot Positions: {list}")


        

        


