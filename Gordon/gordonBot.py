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

class ChaseBot(BotAI):

    def __init__(self):
        self.UM = UnitManager()
        self.BM = BuildingManager()
        self.firstDepot = False
        self.wave = 1
        self.current_target_army = 5
        self.EndingMessage = False 

    async def on_start(self):
        ccs: Units = self.townhalls.filter(
            lambda cc: cc.type_id in {
            UnitTypeId.COMMANDCENTER,
            UnitTypeId.ORBITALCOMMAND,
            UnitTypeId.PLANETARYFORTRESS,
            }
        )



        if ccs:
            cc: Unit = ccs.first
        mapName = self.game_info.map_name
        mappy = mapName.replace(" ","")
        self.BM.detectSpawn(mappy,cc)
        self.BM.populateBuildingPositions()
    
    async def on_step(self, iteration: int):

        ccs: Units = self.townhalls.filter(
            lambda cc: cc.type_id in {
            UnitTypeId.COMMANDCENTER,
            UnitTypeId.ORBITALCOMMAND,
            UnitTypeId.PLANETARYFORTRESS,
            }
        )


        if ccs:
            cc: Unit = ccs.first
        else:
            if self.EndingMessage == False:
                await self.chat_send("GG")
                print("Called GG")
                self.EndingMessage = True
            cc = None

        




        
        await self._client._send_debug()
        await self.textOnBuildings()     
        

        await self.whipLazyWorkers(cc)
        await self.keepAttacking()
        if self.time < 120:
            await self.defendWorkerRush()
        
        for cc in self.townhalls(UnitTypeId.COMMANDCENTER).ready.idle: 
            if self.can_afford(UnitTypeId.ORBITALCOMMAND):
                self.do(cc(AbilityId.UPGRADETOORBITAL_ORBITALCOMMAND))        
        productionFacs: Units = self.structures.filter(
            lambda cc: cc.type_id in {
            UnitTypeId.BARRACKS,
            UnitTypeId.FACTORY,
            UnitTypeId.STARPORT,
            }
        )        
        if productionFacs.amount >= ccs.amount * 3 or self.supply_used == 200:
            await self.expand()
        else:
            await self.doUpgrades()
            await self.buildArmory(cc)
            await self.trainSCVs(ccs)
            await self.buildSupplyDepots(cc)
            await self.buildStarport(ccs)
            await self.buildFactory(ccs)
            await self.buildBarracks(ccs)        
            await self.buildEngineeringBay()
            await self.buildGas(cc,ccs)

        for scv in self.units(UnitTypeId.SCV):
            if scv.orders:
                for order in scv.orders:
                    if order.ability.id == AbilityId.TERRANBUILD_BARRACKS or order.ability.id == AbilityId.TERRANBUILD_FACTORY or order.ability.id == AbilityId.TERRANBUILD_STARPORT or order.ability.id == AbilityId.TERRANBUILD_ENGINEERINGBAY or order.ability.id == AbilityId.TERRANBUILD_ARMORY:
                        if order.target not in self.BM.pendingBarracksPositions:
                            self.BM.pendingBarracksPositions.append(order.target)
                    if order.ability.id == AbilityId.TERRANBUILD_SUPPLYDEPOT:
                        if order.target not in self.BM.pendingDepotPositions:
                            self.BM.pendingDepotPositions.append(order.target)

        
        await self.addAddons()       
        await self.trainArmy()        

        await self.defend_base()
        if self.supply_used < 100 or self.supply_used == 200:
            await self.harrass()
        await self.attacks()
        #await self.draw2(cc)
        await self.controlMedivacs()
        if self.units:
            self.UM.remove_dead_units(self.units)

        await self.giveUnitsTags()
        await self.siegeTanks()
        await self.attackClosest()
        

        await self.lowerDepots()
        try: #This breaks in long games and its annoying as hell
            await self.distribute_workers()
        except:
            await self.chat_send("Distribute Workers didn't work for some reason")

        
        await self.mule()
   

    async def textOnBuildings(self):
        for item in self.structures:
            self._client.debug_text_world(
            text=f"{item.position}",

            pos=Point3((item.position[0],item.position[1],self.get_terrain_z_height(item))),        # Can be a Point2 or Point3
            size=12,                   # Optional: font size
            color=(255, 255, 0))
         
        

    async def trainSCVs(self,ccs):
        total_workers = self.units(UnitTypeId.SCV).amount
        if self.can_afford(UnitTypeId.SCV) and (self.units(UnitTypeId.SCV).amount < (ccs.amount * 16) + (self.structures(UnitTypeId.REFINERY).amount * 3)):
            for cc in self.townhalls.ready.idle:
                if self.can_afford(UnitTypeId.SCV) and total_workers < 80:
                    self.do(cc.train(UnitTypeId.SCV))
                    break

    async def chaseBuild(self,building):
        if not self.townhalls:
            return 
        if self.units(UnitTypeId.SCV):
            worker = self.select_build_worker(self.townhalls.first.position) #We might want top change this later to find the most efficent worker
            position = None
            if worker:
                buildingPositions, pendingPositions = self.BM.findType(building)
                for pos in buildingPositions:
                    if pos not in pendingPositions:
                        position = Point2(pos)
                        break
                if position != None:
                    worker.build(building, position)

    async def buildBarracks(self,ccs):
        if self.firstDepot and self.can_afford(UnitTypeId.BARRACKS):
            await self.chaseBuild(UnitTypeId.BARRACKS) 

    async def buildEngineeringBay(self):
        if self.supply_used > 50 and (self.structures(UnitTypeId.ENGINEERINGBAY).amount + self.already_pending(UnitTypeId.ENGINEERINGBAY)) < 2 and self.can_afford(UnitTypeId.ENGINEERINGBAY) and self.already_pending(UnitTypeId.BARRACKS) < 2 and len(self.BM.barracksPositions) > 0 :
            await self.chaseBuild(UnitTypeId.ENGINEERINGBAY)
                                           
    async def buildFactory(self,ccs):
        if not self.already_pending(UnitTypeId.FACTORY) and self.can_afford(UnitTypeId.FACTORY) and self.structures(UnitTypeId.BARRACKS).ready.amount >= 2 and len(self.BM.barracksPositions) > 0 and not self.structures(UnitTypeId.FACTORY).idle and self.structures(UnitTypeId.FACTORY).amount < ccs.amount:
            await self.chaseBuild(UnitTypeId.FACTORY)
                    
    async def buildStarport(self,ccs):
        if not self.already_pending(UnitTypeId.STARPORT) and self.structures(UnitTypeId.FACTORY).ready.amount >= 2 and len(self.BM.barracksPositions) > 0 and self.townhalls and self.structures(UnitTypeId.STARPORT).amount < ccs.amount :
            await self.chaseBuild(UnitTypeId.STARPORT)
                    
    async def buildArmory(self,cc):
        if self.already_pending_upgrade(UpgradeId.TERRANINFANTRYWEAPONSLEVEL1) and self.already_pending_upgrade(UpgradeId.TERRANINFANTRYARMORSLEVEL1) and self.structures(UnitTypeId.ARMORY).amount == 0 and cc:
            await self.chaseBuild(UnitTypeId.ARMORY)
                    
    async def buildSupplyDepots(self,cc):
        if not self.firstDepot and not self.already_pending(UnitTypeId.SUPPLYDEPOT) and cc:
            await self.chaseBuild(UnitTypeId.SUPPLYDEPOT)
            self.firstDepot = True
                        

        if self.firstDepot and self.supply_used >= self.supply_cap and not self.already_pending(UnitTypeId.SUPPLYDEPOT):
            await self.chaseBuild(UnitTypeId.SUPPLYDEPOT)
                    
        elif self.firstDepot and self.supply_used > self.supply_cap - 10 and self.supply_used > 25 and self.supply_cap != 200:
            await self.chaseBuild(UnitTypeId.SUPPLYDEPOT)           
                        
                

    async def draw2(self,cc):
        if cc.position == (38.5,122.5):
            box_size = .5
            p_min = Point3((55.5 - box_size,120.5 - box_size,10))
            p_max = Point3((55.5 + box_size * 2 , 120.5 + box_size * 2,15))
            self.client.debug_box_out(p_min,p_max,(255,0,0))
        else:
            
            exit()    

    async def defendWorkerRush(self):
        enemies = self.all_enemy_units
        structures = self.structures
        defense_radius = 30
        nearby_enemies = enemies.filter(lambda enemy: any(enemy.distance_to(building) < defense_radius for building in structures))
        scvs = self.units(UnitTypeId.SCV)
        if nearby_enemies.exists:
            if len(nearby_enemies) > 2:
                
                for unit in scvs:
                    closest_enemy = nearby_enemies.closest_to(unit)
                    self.do(unit.attack(closest_enemy))




    async def buildGas(self,cc,ccs):
        if self.supply_used >= 16 and self.structures(UnitTypeId.REFINERY).amount < 1 or self.structures(UnitTypeId.REFINERY).amount < ccs.amount / 2 and self.structures(UnitTypeId.REFINERY).amount >= 1:
            if self.can_afford(UnitTypeId.REFINERY) and cc is not None:
                vgs = self.vespene_geyser.closer_than(15.0,cc)
                for vg in vgs:
                    if self.structures(UnitTypeId.REFINERY).closer_than(1.0, vg).exists:
                        break

                    worker = self.select_build_worker(vg.position)
                    if worker is None:
                        break
                    self.do(worker.build(UnitTypeId.REFINERY, vg))

    async def trainArmy(self):
        for rax in self.structures(UnitTypeId.BARRACKS).ready.idle:
            addon = self.structures.find_by_tag(rax.add_on_tag)
            
            if addon and addon.name == "BarracksTechLab":
                self.do(rax.train(UnitTypeId.MARAUDER))
            if addon and addon.name == "BarracksReactor":
                self.do(rax.train(UnitTypeId.MARINE))
                self.do(rax.train(UnitTypeId.MARINE))
            if not addon:
                self.do(rax.train(UnitTypeId.MARINE))
        for fac in self.structures(UnitTypeId.FACTORY).ready.idle:
            addon = self.structures.find_by_tag(fac.add_on_tag)
            if addon and addon.name == "FactoryTechLab":
                self.do(fac.train(UnitTypeId.SIEGETANK))
            else:
                self.do(fac.train(UnitTypeId.CYCLONE))
        for star in self.structures(UnitTypeId.STARPORT).ready.idle:
            addon = self.structures.find_by_tag(star.add_on_tag)
            if addon and addon.name == "StarportTechLab":
                self.do(star.train(UnitTypeId.BATTLECRUISER))
            else:
                self.do(star.train(UnitTypeId.MEDIVAC))

    async def addAddons(self):
        for rax in self.structures(UnitTypeId.BARRACKS):
            if self.supply_used >= 24 and rax.is_ready and rax.is_idle:
                if self.structures(UnitTypeId.BARRACKSTECHLAB).amount * 2 > self.structures(UnitTypeId.BARRACKSREACTOR).amount:
                    self.do(rax.build(UnitTypeId.BARRACKSREACTOR))
                else:
                    self.do(rax.build(UnitTypeId.BARRACKSTECHLAB))

        for fac in self.structures(UnitTypeId.FACTORY):
            self.do(fac.build(UnitTypeId.FACTORYTECHLAB))        

        for fac in self.structures(UnitTypeId.STARPORT):
            self.do(fac.build(UnitTypeId.STARPORTTECHLAB))

    async def whipLazyWorkers(self,cc):
        for scv in self.workers.idle:
            if cc:
                closest_mineral = self.mineral_field.closest_to(cc) #This breaks based on the absence of a mineral field I think but I am not sure its possibly the absence of a cc but I already check that Match ID: 3946314
                if closest_mineral:
                    scv.gather(closest_mineral)
    
    async def expand(self):
        if self.can_afford(UnitTypeId.COMMANDCENTER) and not self.already_pending(UnitTypeId.COMMANDCENTER):
            await self.expand_now()
            

    async def lowerDepots(self):
        for depot in self.structures(UnitTypeId.SUPPLYDEPOT).ready:
            if self.supply_used > 20:
                self.do(depot(AbilityId.MORPH_SUPPLYDEPOT_LOWER))
    
    async def mule(self):
        for orbital in self.townhalls(UnitTypeId.ORBITALCOMMAND).filter(lambda x: x.energy >= 50):
            abilities = await self.get_available_abilities(orbital)
            mfs = Units = self.mineral_field.closer_than(10, orbital)
            if mfs:
                mf: Unit = max(mfs, key=lambda x: x.mineral_contents)
                self.do(orbital(AbilityId.CALLDOWNMULE_CALLDOWNMULE, mf))

    async def siegeTanks(self):
        tanks = self.units(UnitTypeId.SIEGETANK)
        enemyUnits = self.all_enemy_units
        enemyBuildings = self.all_enemy_units.structure
        siegedTanks = self.units(UnitTypeId.SIEGETANKSIEGED) 
        for tank in tanks:
            buildingsInRange = enemyBuildings.in_attack_range_of(tank)
            if buildingsInRange:
                tank(AbilityId.SIEGEMODE_SIEGEMODE)
        for tank in siegedTanks:
            buildingsInRange = enemyBuildings.in_attack_range_of(tank)
            if not buildingsInRange:
                tank(AbilityId.UNSIEGE_UNSIEGE)


    async def dealWithCreep(self):
        pass

    async def workerScout(self):
        pass

    async def draw(self,cc):
        for angle in range(0,360,15):
            offset = Point2((math.cos(math.radians(angle)), math.sin(math.radians(angle)))) * 12
            rax_pos = cc.position + offset
            box_size = 1
            height = self.get_terrain_height(rax_pos)
            p_min = Point3((rax_pos.x - box_size, rax_pos.y - box_size,10))
            p_max = Point3((rax_pos.x + box_size, rax_pos.y + box_size,15))
            self.client.debug_box_out(p_min,p_max)
    
    async def build_barracks(self):
        if self.can_afford(UnitTypeId.BARRACKS):
            for cc in self.townhalls:  
                for angle in range(0, 360, 15):
                    offset = Point2((math.cos(math.radians(angle)), math.sin(math.radians(angle)))) * 12
                    rax_pos = cc.position + offset
                    if await self.can_place(UnitTypeId.BARRACKS, rax_pos):
                        await self.build(UnitTypeId.BARRACKS, rax_pos)
                        return

    
    async def manageGas(self):
        for refinery in self.units(UnitTypeId.REFINERY).ready:
            if refinery.assigned_harvesters < refinery.ideal_harvesters:
                worker = self.select_build_worker(refinery.position)
                if worker:
                    worker.gather(refinery) #Might be useless
    
    async def defend_base(self):
        defender_units = self.UM.get_units_by_role(self.units,"defender")
        army_units = self.UM.get_units_by_role(self.units,"army")
        enemies = self.all_enemy_units
        structures = self.structures
        defense_radius = 30
        nearby_enemies = enemies.filter(
            lambda enemy: any(enemy.distance_to(building) < defense_radius for building in structures)
        )
        if nearby_enemies.exists:
            for unit in defender_units:
                if unit.is_idle:
                    closest_enemy = nearby_enemies.closest_to(unit)
                    if closest_enemy:
                        self.do(unit.attack(closest_enemy))
            for unit in army_units:
                if unit.is_idle:
                    closest_enemy = nearby_enemies.closest_to(unit)
                    if closest_enemy:
                        self.do(unit.attack(closest_enemy))

    async def harrass(self):
        scout_units = self.UM.get_units_by_role(self.units, "scout")
        random_patch = random.choice(self.mineral_field)
        target: Point2 = (random_patch).position
        for unit in scout_units:
            if unit.is_idle:
                self.do(unit.attack(target))





    async def keepAttacking(self):
        army_units  = self.UM.get_units_by_role(self.units, "attacking")
        target: Point2 = self.enemy_structures.random_or(self.enemy_start_locations[0]).position
        for unit in army_units:
            if unit.is_idle:
                self.do(unit.attack(target))

    async def attacks(self):
        global wave
        army_units = self.UM.get_units_by_role(self.units, "army")
        current_army_count = self.UM.count_role("army")
        target: Point2 = self.enemy_structures.random_or(self.enemy_start_locations[0]).position
        if self.wave == 1:
            if current_army_count >= 5:
                for unit in army_units:
                    self.do(unit.attack(target))
                    self.UM.assign_role(unit, "attacking")
                self.wave += 1
                self.current_target_army = 30
        if self.wave == 2 and current_army_count >= 30:
            for unit in army_units:
                self.do(unit.attack(target))
                self.UM.assign_role(unit, "attacking")
            
            self.wave += 1
            self.current_target_army = 60
        if self.wave > 2 and current_army_count >= self.current_target_army or self.supply_used == 200:
            for unit in army_units:
                self.do(unit.attack(target))
                self.UM.assign_role(unit, "attacking")
            self.wave += 1
            if self.current_target_army < 100:
                self.current_target_army += 10    

    async def attackClosest(self):
        marines = self.units(UnitTypeId.MARINE) 
        for marine in marines:
            enemies = self.all_enemy_units
            if enemies:
                enemiesInRange = enemies.in_attack_range_of(marine)
                if enemiesInRange:
                    closest_enemy = enemiesInRange.closest_to(marine)
                    if BuffId.STIMPACK in marine.buffs:
                        self.do(marine.attack(closest_enemy))
                    else:
                        if AbilityId.EFFECT_STIM_MARINE in await self.get_available_abilities(marine):
                            self.do(marine(AbilityId.EFFECT_STIM_MARINE))
        marauders = self.units(UnitTypeId.MARAUDER)
        for marauder in marauders:
            enemies = self.all_enemy_units
            if enemies:
                enemiesInRange = enemies.in_attack_range_of(marauder)
                if enemiesInRange:
                    closest_enemy = enemiesInRange.closest_to(marauder)
                    if BuffId.STIMPACK in marauder.buffs:
                        self.do(marauder.attack(closest_enemy))
                    else:
                        if AbilityId.EFFECT_STIM_MARAUDER in await self.get_available_abilities(marauder):
                            self.do(marauder(AbilityId.EFFECT_STIM_MARAUDER))
        cyclones = self.units(UnitTypeId.CYCLONE)
        for cyclone in cyclones:
            enemies = self.all_enemy_units
            if enemies:
                enemiesInRange = enemies.in_attack_range_of(cyclone)
                if enemiesInRange:
                    closest_enemy = enemiesInRange.closest_to(cyclone)
        tanks = self.units(UnitTypeId.SIEGETANK)
        for tank in tanks:
            enemies = self.all_enemy_units
            if enemies:
                enemiesInRange = enemies.in_attack_range_of(tank)
                if enemiesInRange:
                    closest_enemy = enemiesInRange.closest_to(tank)                    

    async def controlMedivacs(self):
        medivacs = self.units(UnitTypeId.MEDIVAC)
        marines = self.units(UnitTypeId.MARINE)
        marauder = self.units(UnitTypeId.MARAUDER)
        units = self.units(UnitTypeId.MARINE) | self.units(UnitTypeId.MARAUDER)
        hurt_units = units.filter(lambda u: u.health < u.health_max)
        if hurt_units:
            for medivac in medivacs:
                target = hurt_units.closest_to(medivac)
                self.do(medivac.move(target))
        else:
            for medivac in medivacs:
                if units:
                    target = units.closest_to(medivac)

    async def giveUnitsTags(self):
        for marine in self.units(UnitTypeId.MARINE):
            if self.UM.get_role(marine) == "nothing":
                current_army_count = self.UM.count_role("army")
                current_scout_count = self.UM.count_role("scout")
                current_defender_count = self.UM.count_role("defender")
                if current_defender_count < 5:
                    self.UM.assign_role(marine,"defender")
                elif current_scout_count < 3:
                    self.UM.assign_role(marine,"scout")
                else:
                    self.UM.assign_role(marine, "army")
        for marauder in self.units(UnitTypeId.MARAUDER):
            if self.UM.get_role(marauder) == "nothing":
                current_army_count = self.UM.count_role("army")
                current_scout_count = self.UM.count_role("scout")
                current_defender_count = self.UM.count_role("defender")
                if current_defender_count < 5:
                    self.UM.assign_role(marauder,"defender")
                elif current_scout_count < 3:
                    self.UM.assign_role(marauder,"scout")
                else:
                    self.UM.assign_role(marauder, "army")
        for cyclone in self.units(UnitTypeId.CYCLONE):
            if self.UM.get_role(cyclone) == "nothing":
                self.UM.assign_role(cyclone, "army")
        for tank in self.units(UnitTypeId.SIEGETANK):
            if self.UM.get_role(tank) == "nothing":
                self.UM.assign_role(tank, "army")
        for bc in self.units(UnitTypeId.BATTLECRUISER):
            if self.UM.get_role(bc) == "nothing":
                self.UM.assign_role(bc, "army")


    async def doUpgrades(self):
        for bay in self.structures(UnitTypeId.ENGINEERINGBAY).idle:
            if self.can_afford(UpgradeId.TERRANINFANTRYWEAPONSLEVEL1) and self.already_pending_upgrade(UpgradeId.TERRANINFANTRYWEAPONSLEVEL1) == 0:
               self.do(bay.research(UpgradeId.TERRANINFANTRYWEAPONSLEVEL1))
            if self.can_afford(UpgradeId.TERRANINFANTRYWEAPONSLEVEL2)and self.already_pending_upgrade(UpgradeId.TERRANINFANTRYWEAPONSLEVEL2) == 0:
                self.do(bay.research(UpgradeId.TERRANINFANTRYWEAPONSLEVEL2)) 
            if self.can_afford(UpgradeId.TERRANINFANTRYWEAPONSLEVEL3) and self.already_pending_upgrade(UpgradeId.TERRANINFANTRYWEAPONSLEVEL3) == 0:
                self.do(bay.research(UpgradeId.TERRANINFANTRYWEAPONSLEVEL3))
            if self.can_afford(UpgradeId.TERRANINFANTRYARMORSLEVEL1) and self.already_pending_upgrade(UpgradeId.TERRANINFANTRYARMORSLEVEL1) == 0:
                self.do(bay.research(UpgradeId.TERRANINFANTRYARMORSLEVEL1))
            if self.can_afford(UpgradeId.TERRANINFANTRYARMORSLEVEL2) and self.already_pending_upgrade(UpgradeId.TERRANINFANTRYARMORSLEVEL2) == 0:
                self.do(bay.research(UpgradeId.TERRANINFANTRYARMORSLEVEL2))
            if self.can_afford(UpgradeId.TERRANINFANTRYARMORSLEVEL3)and self.already_pending_upgrade(UpgradeId.TERRANINFANTRYARMORSLEVEL3) == 0:
                self.do(bay.research(UpgradeId.TERRANINFANTRYARMORSLEVEL3))   

        if self.can_afford(UpgradeId.STIMPACK) or self.can_afford(UpgradeId.SHIELDWALL):
            for techlab in self.structures(UnitTypeId.BARRACKSTECHLAB).ready:
                if techlab.is_idle:
                    if self.can_afford(UpgradeId.STIMPACK):
                        self.do(techlab.research(UpgradeId.STIMPACK))
                    if self.can_afford(UpgradeId.SHIELDWALL):
                        self.do(techlab.research(UpgradeId.SHIELDWALL))