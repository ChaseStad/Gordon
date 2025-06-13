from sc2.ids.unit_typeid import UnitTypeId
from sc2.unit import Unit
from sc2.units import Units
from sc2.position import Point2

class BuildingManager:
    def __init__(self):
        self.depotPositions = []
        self.barracksPositions = []
        self.pendingDepotPositions = []
        self.pendingBarracksPositions = []
        self.map = None
        self.spawn = None

    def detectSpawn(self, mapPick, cc):
        if mapPick == "InterloperAIE": #REMEMBER TO DO THIS
            self.map = "InterloperAIE"
            topSpawn = Point2((26.5, 137.5))
            bottomSpawn = Point2((125.5, 30.5))
            if cc.position.distance_to(topSpawn) < 1:
                self.spawn = "T"
                return "T-InterloperAIE"
            elif cc.position.distance_to(bottomSpawn) < 1:
                self.spawn = "B"
                return "B-InterloperAIE"
            else:
                print(f"Unknown spawn position: {cc.position}")
                return None

        if mapPick == "ThunderbirdAIE": #REMEMBER TO DO THIS
            self.map = "ThunderbirdAIE"
            topSpawn = Point2((38.5, 133.5))
            bottomSpawn = Point2((153.5, 22.5))
            if cc.position.distance_to(topSpawn) < 1:
                self.spawn = "T"
                return "T-ThunderbirdAIE"
            elif cc.position.distance_to(bottomSpawn) < 1:
                self.spawn = "B"
                return "B-ThunderbirdAIE"
            else:
                print(f"Unknown spawn position: {cc.position}")
                return None 
        print(mapPick)
        if mapPick == "PylonAIE": #REMEMBER TO DO THIS
            print("IT WORKED")
            self.map = "PylonAIE"
            topSpawn = Point2((72.5, 171.5))
            bottomSpawn = Point2((175.5, 76.5))
            if cc.position.distance_to(topSpawn) < 1:
                print("TOP SPAWN")
                self.spawn = "T"
                return "T-PylonAIE"
            elif cc.position.distance_to(bottomSpawn) < 1:
                self.spawn = "B"
                print("BOTTOM SPAWN")
                return "B-PylonAIE"
            else:
                print(f"Unknown spawn position: {cc.position}")
                return None 
        
        if mapPick == "TorchesAIE": #REMEMBER TO DO THIS
            self.map = "TorchesAIE"
            topSpawn = Point2((124.5, 159.5))
            bottomSpawn = Point2((124.5, 48.5))
            if cc.position.distance_to(topSpawn) < 1:
                self.spawn = "T"
                return "T-TorchesAIE"
            elif cc.position.distance_to(bottomSpawn) < 1:
                self.spawn = "B"
                return "B-TorchesAIE"
            else:
                print(f"Unknown spawn position: {cc.position}")
                return None

        if mapPick == "PersephoneAIE": #REMEMBER TO DO THIS
            self.map = "PersephoneAIE"
            topSpawn = Point2((37.5, 145.5))
            bottomSpawn = Point2((37.5, 34.5))
            if cc.position.distance_to(topSpawn) < 1:
                self.spawn = "T"
                return "T-PersephoneAIE"
            elif cc.position.distance_to(bottomSpawn) < 1:
                self.spawn = "B"
                return "B-PersephoneAIE"
            else:
                print(f"Unknown spawn position: {cc.position}")
                return None 

        if mapPick == "LeyLinesAIE":
            self.map = "LeyLinesAIE"
            topSpawn = Point2((155.5, 133.5))
            bottomSpawn = Point2((40.5, 69.5))
            if cc.position.distance_to(topSpawn) < 1:
                self.spawn = "T"
                return "T-LeyLinesAIE"
            elif cc.position.distance_to(bottomSpawn) < 1:
                self.spawn = "B"
                return "B-LeyLinesAIE"
            else:
                print(f"Unknown spawn position: {cc.position}")
                return None            

        if mapPick == "MagannathaAIE":
            self.map = "MagannathaAIE"
            topSpawn = Point2((38.5, 141.5))
            bottomSpawn = Point2((141.5, 38.5))
            if cc.position.distance_to(topSpawn) < 1:
                self.spawn = "T"
                return "T-MagannathaAIE"
            elif cc.position.distance_to(bottomSpawn) < 1:
                self.spawn = "B"
                return "B-MagannathaAIE"
            else:
                print(f"Unknown spawn position: {cc.position}")
                return None 



        if mapPick == "IncorporealAIE":
            self.map = "IncorporealAIE"
            topSpawn = Point2((32.5, 139.5))
            bottomSpawn = Point2((123.5, 24.5))
            if cc.position.distance_to(topSpawn) < 1:
                self.spawn = "T"
                return "T-IncorporealAIE"
            elif cc.position.distance_to(bottomSpawn) < 1:
                self.spawn = "B"
                return "B-IncorporealAIE"
            else:
                print(f"Unknown spawn position: {cc.position}")
                return None            

        if mapPick == "AutomatonAIE":
            print(cc.position)
            topSpawn = Point2((154.5, 114.5))
            bottomSpawn = Point2((29.5, 65.5))
            self.map = "AutomatonAIE" 
            if cc.position.distance_to(topSpawn) < 1:
                self.spawn = "T"
                return "T-AutomatonAIE"
            elif cc.position.distance_to(bottomSpawn) < 1:
                self.spawn = "B"
                return "B-AutomatonAIE"
            else:
                print(f"Unknown spawn position: {cc.position}")

        if mapPick == "AcropolisAIE":
            topSpawn = Point2((33.5, 138.5))
            bottomSpawn = Point2((142.5,33.5))
            self.map = "AcropolisAIE"
            if cc.position.distance_to(topSpawn) < 1:
                self.spawn = "T"
                return "T-AcropolisAIE"
            elif cc.position.distance_to(bottomSpawn) < 1:
                self.spawn = "B"
                return "B-AcropolisAIE"
            else:
                print(f"Unknown spawn position: {cc.position}")
                return None


        if mapPick == "EphemeronAIE":
            topSpawn = Point2(((29.5, 138.5)))
            bottomSpawn = Point2((130.5, 21.5))
            self.map = "EphemeronAIE"
            print("We know map")
            if cc.position.distance_to(topSpawn) < 1:
                self.spawn = "T"
                print("Top Side")
                return "T-EphemeronAIE"
            elif cc.position.distance_to(bottomSpawn) < 1:
                self.spawn = "B"
                print("Bottom Side")
                return "B-EphemeronAIE"
            else:
                print(f"Unknown spawn position: {cc.position}")
                return None
        
        if mapPick == "AbyssalReefAIE":
            topSpawn = Point2((38.5, 122.5))
            bottomSpawn = Point2((161.5, 21.5))
            self.map = "AbyssalReefAIE"

            if cc.position.distance_to(topSpawn) < 1:
                self.spawn = "T"
                return "T-AbyssalReefAIE"
            elif cc.position.distance_to(bottomSpawn) < 1:
                self.spawn = "B"
                return "B-AbyssalReefAIE"
            else:
                print(f"Unknown spawn position: {cc.position}")
                return None

    def findType(self, building):
        if building == UnitTypeId.BARRACKS or building == UnitTypeId.FACTORY or building == UnitTypeId.STARPORT or building == UnitTypeId.ENGINEERINGBAY or building == UnitTypeId.ARMORY:
            return self.barracksPositions, self.pendingBarracksPositions

        if building == UnitTypeId.SUPPLYDEPOT:
            return self.depotPositions, self.pendingDepotPositions

    
    def populateBuildingPositions(self):
        if self.map == "AbyssalReefAIE":
            if self.spawn == "T":
                self.depotPositions = [
                    Point2((56,121)), Point2((53,118)),  # These are the wall
                    Point2((38.0, 119.0)), Point2((40.0, 119.0)), Point2((54.0, 122.0)), Point2((40.0, 117.0)), Point2((54.0, 126.0)), Point2((34.0, 131.0)), Point2((29.0, 122.0)), Point2((42.0, 122.0)), Point2((37.0, 112.0)), Point2((39.0, 112.0)), Point2((30.0, 128.0)), Point2((42.0, 132.0)), Point2((29.0, 119.0)), Point2((33.0, 112.0)), Point2((42.0, 124.0)), Point2((46.0, 117.0)), Point2((32.0, 117.0)), Point2((42.0, 120.0)), Point2((35.0, 112.0)), Point2((42.0, 117.0)), Point2((38.0, 117.0)), Point2((41.0, 109.0)), Point2((44.0, 117.0)), Point2((44.0, 112.0))
                ]
                
                self.barracksPositions = [Point2((51.5, 120.5)),  Point2((32.5, 79.5)), Point2((36.5, 114.5)), Point2((30.5, 114.5)), Point2((62.5, 83.5)), Point2((44.5, 114.5)), Point2((43.5, 109.5)), Point2((34.5, 86.5)), Point2((65.5, 113.5)), Point2((44.5, 119.5)), Point2((70.5, 73.5)), Point2((50.5, 87.5)), Point2((44.5, 84.5)), Point2((57.5, 110.5)), Point2((64.5, 76.5)), Point2((51.5, 101.5)), Point2((51.5, 124.5)), Point2((49.5, 94.5)), Point2((36.5, 109.5)), Point2((44.5, 124.5)), Point2((51.5, 128.5)),Point2((76.5, 76.5))]
            elif self.spawn == "B":
                self.depotPositions = [Point2((147.0, 26.0)),Point2((144.0, 23.0)),
                Point2((171.0, 18.0)), Point2((171.0, 26.0)), Point2((143.0, 12.0)), 
                Point2((151.0, 21.0)), Point2((169.0, 15.0)), Point2((166.0, 13.0)),
                Point2((171.0, 23.0)) , Point2((171.0, 29.0)), Point2((142.0, 17.0)), 
                Point2((161.0, 36.0)), Point2((140.0, 14.0)), Point2((153.0, 14.0)), 
                Point2((151.0, 31.0)), Point2((143.0, 15.0)), Point2((156.0, 14.0)), 
                Point2((162.0, 12.0)),  Point2((143.0, 20.0)), Point2((158.0, 36.0)), 
                Point2((150.0, 28.0)), Point2((153.0, 17.0)), Point2((146.0, 12.0)), 
                Point2((156.0, 17.0))]
                self.barracksPositions = [Point2((146.5, 23.5)), Point2((154.5, 28.5)), 
                Point2((154.5, 20.5)), Point2((154.5, 32.5)), Point2((160.5, 32.5)), 
                Point2((160.5, 28.5)), Point2((166.5, 27.5)), Point2((154.5, 24.5)), 
                Point2((146.5, 15.5)), Point2((146.5, 19.5)), Point2((166.5, 32.5)),Point2((147.5, 42.5)), Point2((141.5, 55.5)), Point2((120.5, 30.5)), Point2((147.5, 51.5)), Point2((134.5, 28.5)), Point2((164.5, 59.5)), Point2((150.5, 56.5)), Point2((136.5, 60.5)), Point2((130.5, 64.5)), Point2((154.5, 59.5)), Point2((165.5, 66.5))]
        elif self.map == "IncorporealAIE":
            print("Detected Map as IncorporealAIE")
            if self.spawn == "T":
                self.depotPositions = [
                    Point2((24.0, 146.0)), Point2((23.0, 136.0)), Point2((24.0, 139.0)),
                    Point2((22.0, 140.0)), Point2((37.0, 151.0)), Point2((33.0, 150.0)),
                    Point2((22.0, 138.0)), Point2((24.0, 144.0)), Point2((25.0, 148.0)),
                    Point2((35.0, 149.0)), Point2((34.0, 147.0)), Point2((21.0, 136.0)),
                    Point2((45.0, 138.0)), Point2((32.0, 148.0)), Point2((27.0, 148.0)),
                    Point2((37.0, 149.0)), Point2((35.0, 151.0)), Point2((31.0, 150.0)),
                    Point2((48.0, 141.0)), Point2((26.0, 146.0)), Point2((30.0, 148.0)),
                    Point2((24.0, 142.0)), Point2((29.0, 150.0)), Point2((22.0, 144.0))
                ]
                self.barracksPositions = [
                    Point2((43.5, 145.5)), Point2((86.5, 126.5)), Point2((57.5, 132.5)),
                    Point2((79.5, 127.5)), Point2((36.5, 130.5)), Point2((64.5, 127.5)),
                    Point2((72.5, 122.5)), Point2((64.5, 137.5)), Point2((64.5, 132.5)),
                    Point2((22.5, 130.5)), Point2((50.5, 132.5)), Point2((22.5, 125.5)),
                    Point2((65.5, 117.5)), Point2((36.5, 140.5)), Point2((72.5, 117.5)),
                    Point2((36.5, 135.5)), Point2((65.5, 122.5)), Point2((72.5, 127.5)),
                    Point2((43.5, 140.5)), Point2((79.5, 122.5)), Point2((58.5, 122.5)),
                    Point2((29.5, 130.5)), Point2((29.5, 125.5)), Point2((28.5, 135.5))
                ]

            
            elif self.spawn == "B":
                print("Detected Spawn as B")
                self.depotPositions = [
                    Point2((126.0, 16.0)), Point2((122.0, 13.0)), Point2((131.0, 18.0)),
                    Point2((128.0, 15.0)), Point2((134.0, 20.0)), Point2((132.0, 20.0)),
                    Point2((108.0, 23.0)), Point2((135.0, 28.0)), Point2((133.0, 18.0)),
                    Point2((120.0, 13.0)), Point2((131.0, 16.0)), Point2((122.0, 17.0)),
                    Point2((111.0, 26.0)), Point2((124.0, 14.0)), Point2((133.0, 22.0)),
                    Point2((120.0, 15.0)), Point2((134.0, 24.0)), Point2((124.0, 16.0)),
                    Point2((126.0, 14.0)), Point2((133.0, 26.0)), Point2((122.0, 15.0)),
                    Point2((135.0, 26.0)), Point2((135.0, 22.0)), Point2((133.0, 28.0))
                ]

                self.barracksPositions = [
                    Point2((84.5, 19.5)), Point2((84.5, 24.5)), Point2((75.5, 42.5)),
                    Point2((82.5, 42.5)), Point2((89.5, 32.5)), Point2((96.5, 32.5)),
                    Point2((131.5, 38.5)), Point2((124.5, 38.5)), Point2((68.5, 37.5)),
                    Point2((117.5, 23.5)), Point2((103.5, 32.5)), Point2((124.5, 33.5)),
                    Point2((95.5, 14.5)), Point2((68.5, 32.5)), Point2((89.5, 42.5)),
                    Point2((88.5, 15.5)), Point2((89.5, 27.5)), Point2((82.5, 37.5)),
                    Point2((75.5, 32.5)), Point2((117.5, 33.5)), Point2((89.5, 37.5)),
                    Point2((110.5, 23.5)), Point2((75.5, 37.5)), Point2((117.5, 28.5)),
                    Point2((110.5, 18.5)), Point2((131.5, 33.5))
                ]

        elif self.map == "PylonAIE":
            print("Detected Map as PylonAIE")
            if self.spawn == "T":
                self.depotPositions = [
                    Point2((61.0, 172.0)), Point2((68.0, 180.0)), Point2((73.0, 184.0)), Point2((63.0, 168.0)),
                    Point2((74.0, 179.0)), Point2((68.0, 178.0)), Point2((66.0, 178.0)), Point2((77.0, 183.0)),
                    Point2((67.0, 182.0)), Point2((63.0, 172.0)), Point2((62.0, 174.0)), Point2((85.0, 166.0)),
                    Point2((61.0, 168.0)), Point2((69.0, 184.0)), Point2((70.0, 180.0)), Point2((75.0, 181.0)),
                    Point2((64.0, 176.0)), Point2((72.0, 180.0)), Point2((77.0, 181.0)), Point2((75.0, 183.0)),
                    Point2((64.0, 174.0)), Point2((71.0, 184.0)), Point2((88.0, 163.0)), Point2((63.0, 170.0))
                ]
                self.barracksPositions = [
                    Point2((87.5, 137.5)), Point2((76.5, 168.5)), Point2((94.5, 162.5)), Point2((76.5, 158.5)),
                    Point2((101.5, 137.5)), Point2((94.5, 137.5)), Point2((69.5, 163.5)), Point2((101.5, 147.5)),
                    Point2((94.5, 167.5)), Point2((69.5, 158.5)), Point2((115.5, 162.5)), Point2((108.5, 167.5)),
                    Point2((105.5, 162.5)), Point2((101.5, 132.5)), Point2((76.5, 153.5)), Point2((106.5, 157.5)),
                    Point2((115.5, 167.5)), Point2((83.5, 158.5)), Point2((106.5, 152.5)), Point2((101.5, 167.5)),
                    Point2((76.5, 163.5)), Point2((101.5, 142.5)), Point2((83.5, 163.5)), Point2((94.5, 132.5))
                ]


            
            elif self.spawn == "B":
                print("Detected Spawn as B")
                self.depotPositions = [
                    Point2((184.0, 72.0)), Point2((171.0, 65.0)), Point2((173.0, 65.0)), Point2((185.0, 78.0)),
                    Point2((179.0, 67.0)), Point2((178.0, 69.0)), Point2((186.0, 74.0)), Point2((179.0, 65.0)),
                    Point2((181.0, 68.0)), Point2((187.0, 76.0)), Point2((182.0, 70.0)), Point2((184.0, 74.0)),
                    Point2((185.0, 80.0)), Point2((163.0, 82.0)), Point2((181.0, 66.0)), Point2((186.0, 72.0)),
                    Point2((180.0, 70.0)), Point2((183.0, 66.0)), Point2((185.0, 68.0)), Point2((173.0, 67.0)),
                    Point2((185.0, 76.0)), Point2((184.0, 70.0)), Point2((171.0, 67.0)), Point2((176.0, 68.0)),
                    Point2((186.0, 70.0)), Point2((183.0, 68.0)), Point2((187.0, 80.0))
                ]


                self.barracksPositions = [
                    Point2((115.5, 79.5)), Point2((166.5, 74.5)), Point2((129.5, 84.5)), Point2((143.5, 84.5)),
                    Point2((162.5, 89.5)), Point2((129.5, 79.5)), Point2((176.5, 89.5)), Point2((162.5, 84.5)),
                    Point2((144.5, 96.5)), Point2((169.5, 84.5)), Point2((169.5, 79.5)), Point2((113.5, 74.5)),
                    Point2((176.5, 84.5)), Point2((136.5, 84.5)), Point2((150.5, 84.5)), Point2((137.5, 95.5)),
                    Point2((183.5, 84.5)), Point2((150.5, 79.5)), Point2((106.5, 74.5)), Point2((143.5, 79.5)),
                    Point2((106.5, 69.5)), Point2((136.5, 89.5)), Point2((122.5, 79.5)), Point2((169.5, 89.5))
                ]


        elif self.map == "LeyLinesAIE":
            print("Detected Map as LeyLinesAIE")
            if self.spawn == "T":
                self.depotPositions = [
                    Point2((164.0, 137.0)), Point2((166.0, 139.0)), Point2((156.0, 142.0)),
                    Point2((168.0, 135.0)), Point2((158.0, 142.0)), Point2((164.0, 139.0)),
                    Point2((168.0, 133.0)), Point2((160.0, 143.0)), Point2((166.0, 133.0)),
                    Point2((156.0, 144.0)), Point2((166.0, 135.0)), Point2((156.0, 121.0)),
                    Point2((162.0, 143.0)), Point2((168.0, 137.0)), Point2((154.0, 143.0)),
                    Point2((164.0, 133.0)), Point2((154.0, 141.0)), Point2((166.0, 137.0)),
                    Point2((158.0, 144.0)), Point2((158.0, 146.0)), Point2((156.0, 146.0)),
                    Point2((162.0, 141.0)), Point2((159.0, 118.0)), Point2((160.0, 145.0))
                ]

                self.barracksPositions = [
                    Point2((134.5, 100.5)), Point2((134.5, 110.5)), Point2((120.5, 119.5)),
                    Point2((143.5, 135.5)), Point2((148.5, 105.5)), Point2((127.5, 110.5)),
                    Point2((151.5, 130.5)), Point2((120.5, 114.5)), Point2((148.5, 110.5)),
                    Point2((144.5, 125.5)), Point2((141.5, 105.5)), Point2((154.5, 98.5)),
                    Point2((144.5, 130.5)), Point2((134.5, 105.5)), Point2((143.5, 140.5)),
                    Point2((134.5, 95.5)), Point2((158.5, 125.5)), Point2((148.5, 115.5)),
                    Point2((151.5, 125.5)), Point2((134.5, 90.5)), Point2((127.5, 95.5)),
                    Point2((149.5, 100.5)), Point2((158.5, 120.5)), Point2((162.5, 95.5))
                ]


            
            elif self.spawn == "B":
                print("Detected Spawn as B")
                self.depotPositions = [
                    Point2((40.0, 30.0)), Point2((44.0, 31.0)), Point2((42.0, 30.0)),
                    Point2((40.0, 32.0)), Point2((34.0, 35.0)), Point2((32.0, 41.0)),
                    Point2((30.0, 39.0)), Point2((44.0, 33.0)), Point2((38.0, 29.0)),
                    Point2((30.0, 37.0)), Point2((36.0, 31.0)), Point2((32.0, 39.0)),
                    Point2((32.0, 35.0)), Point2((30.0, 41.0)), Point2((46.0, 31.0)),
                    Point2((38.0, 31.0)), Point2((42.0, 32.0)), Point2((34.0, 41.0)),
                    Point2((34.0, 37.0)), Point2((36.0, 33.0)), Point2((34.0, 33.0)),
                    Point2((32.0, 37.0)), Point2((39.0, 56.0)), Point2((42.0, 53.0)),
                    Point2((40.0, 28.0))
                ]


                self.barracksPositions = [
                    Point2((61.5, 82.5)), Point2((54.5, 92.5)), Point2((52.5, 38.5)),
                    Point2((54.5, 66.5)), Point2((44.5, 48.5)), Point2((61.5, 77.5)),
                    Point2((72.5, 77.5)), Point2((54.5, 71.5)), Point2((61.5, 66.5)),
                    Point2((54.5, 97.5)), Point2((68.5, 82.5)), Point2((37.5, 48.5)),
                    Point2((47.5, 66.5)), Point2((47.5, 61.5)), Point2((47.5, 71.5)),
                    Point2((52.5, 33.5)), Point2((51.5, 48.5)), Point2((61.5, 87.5)),
                    Point2((61.5, 61.5)), Point2((61.5, 92.5)), Point2((47.5, 102.5)),
                    Point2((37.5, 53.5)), Point2((61.5, 71.5)), Point2((51.5, 43.5))
                ]

        elif self.map == "TorchesAIE":
            print("Detected Map as TorchesAIE")
            if self.spawn == "T":
                self.depotPositions = [
                    Point2((134.0, 158.0)), Point2((135.0, 162.0)), Point2((136.0, 158.0)),
                    Point2((135.0, 164.0)), Point2((133.0, 164.0)), Point2((136.0, 160.0)),
                    Point2((137.0, 162.0)), Point2((131.0, 166.0)), Point2((133.0, 168.0)),
                    Point2((110.0, 155.0)), Point2((127.0, 172.0)), Point2((131.0, 168.0)),
                    Point2((129.0, 171.0)), Point2((125.0, 172.0)), Point2((135.0, 166.0)),
                    Point2((137.0, 164.0)), Point2((129.0, 169.0)), Point2((127.0, 168.0)),
                    Point2((134.0, 160.0)), Point2((133.0, 162.0)), Point2((131.0, 170.0)),
                    Point2((133.0, 170.0)), Point2((135.0, 168.0)), Point2((125.0, 168.0)),
                    Point2((125.0, 170.0)), Point2((127.0, 170.0)), Point2((113.0, 152.0)),
                    Point2((133.0, 166.0)), Point2((129.0, 167.0))
                ]


                self.barracksPositions = [
                    Point2((75.5, 126.5)), Point2((106.5, 145.5)), Point2((75.5, 137.5)),
                    Point2((82.5, 122.5)), Point2((133.5, 149.5)), Point2((112.5, 159.5)),
                    Point2((126.5, 149.5)), Point2((112.5, 164.5)), Point2((68.5, 137.5)),
                    Point2((82.5, 137.5)), Point2((75.5, 142.5)), Point2((68.5, 132.5)),
                    Point2((112.5, 154.5)), Point2((99.5, 150.5)), Point2((106.5, 140.5)),
                    Point2((99.5, 145.5)), Point2((126.5, 154.5)), Point2((112.5, 169.5)),
                    Point2((119.5, 149.5)), Point2((85.5, 155.5)), Point2((82.5, 127.5)),
                    Point2((119.5, 154.5)), Point2((92.5, 150.5)), Point2((82.5, 132.5))
                ]



            
            elif self.spawn == "B":
                print("Detected Spawn as B")
                self.depotPositions = [
                    Point2((132.0, 43.0)), Point2((137.0, 45.0)), Point2((113.0, 56.0)),
                    Point2((134.0, 41.0)), Point2((136.0, 47.0)), Point2((132.0, 39.0)),
                    Point2((128.0, 41.0)), Point2((122.0, 39.0)), Point2((136.0, 43.0)),
                    Point2((135.0, 49.0)), Point2((133.0, 45.0)), Point2((134.0, 47.0)),
                    Point2((135.0, 45.0)), Point2((120.0, 38.0)), Point2((126.0, 38.0)),
                    Point2((124.0, 36.0)), Point2((136.0, 41.0)), Point2((130.0, 39.0)),
                    Point2((128.0, 37.0)), Point2((136.0, 51.0)), Point2((122.0, 37.0)),
                    Point2((134.0, 39.0)), Point2((130.0, 37.0)), Point2((126.0, 36.0)),
                    Point2((128.0, 39.0)), Point2((130.0, 41.0)), Point2((134.0, 43.0)),
                    Point2((126.0, 40.0)), Point2((124.0, 38.0)), Point2((134.0, 51.0)),
                    Point2((110.0, 53.0)), Point2((124.0, 40.0)), Point2((132.0, 41.0)),
                    Point2((133.0, 49.0))
                ]


                self.barracksPositions = [
                    Point2((82.5, 70.5)), Point2((82.5, 85.5)), Point2((100.5, 58.5)),
                    Point2((75.5, 81.5)), Point2((68.5, 75.5)), Point2((126.5, 57.5)),
                    Point2((86.5, 53.5)), Point2((82.5, 80.5)), Point2((112.5, 38.5)),
                    Point2((112.5, 53.5)), Point2((75.5, 70.5)), Point2((112.5, 43.5)),
                    Point2((75.5, 65.5)), Point2((100.5, 53.5)), Point2((100.5, 63.5)),
                    Point2((82.5, 75.5)), Point2((107.5, 63.5)), Point2((93.5, 58.5)),
                    Point2((89.5, 80.5)), Point2((133.5, 57.5)), Point2((119.5, 53.5)),
                    Point2((112.5, 48.5)), Point2((68.5, 70.5)), Point2((119.5, 58.5))
                ]


        elif self.map == "PersephoneAIE":
            print("Detected Map as PersephoneAIE")
            if self.spawn == "T":
                self.depotPositions = [
                     Point2((26.0, 142.0)), Point2((33.0, 156.0)), Point2((35.0, 153.0)),
                     Point2((26.0, 146.0)), Point2((39.0, 154.0)), Point2((31.0, 152.0)),
                     Point2((26.0, 144.0)), Point2((29.0, 150.0)), Point2((38.0, 156.0)),
                     Point2((29.0, 148.0)), Point2((38.0, 158.0)), Point2((40.0, 156.0)),
                     Point2((53.0, 142.0)), Point2((28.0, 144.0)), Point2((42.0, 155.0)),
                     Point2((33.0, 154.0)), Point2((37.0, 154.0)), Point2((56.0, 139.0)),
                     Point2((28.0, 146.0)), Point2((40.0, 158.0)), Point2((42.0, 157.0)),
                     Point2((35.0, 155.0)), Point2((28.0, 142.0)), Point2((33.0, 152.0)),
                     Point2((36.0, 157.0))
                ]


                self.barracksPositions = [
                    Point2((44.5, 139.5)), Point2((44.5, 144.5)), Point2((44.5, 134.5)),
                    Point2((44.5, 129.5)), Point2((44.5, 149.5)), Point2((67.5, 138.5)),
                    Point2((51.5, 139.5)), Point2((74.5, 142.5)), Point2((74.5, 132.5)),
                    Point2((37.5, 134.5)), Point2((81.5, 127.5)), Point2((51.5, 134.5)),
                    Point2((74.5, 127.5)), Point2((81.5, 132.5)), Point2((67.5, 143.5)),
                    Point2((65.5, 116.5)), Point2((37.5, 139.5)), Point2((67.5, 131.5)),
                    Point2((74.5, 137.5)), Point2((30.5, 139.5)), Point2((67.5, 121.5)),
                    Point2((61.5, 144.5)), Point2((83.5, 122.5)), Point2((67.5, 126.5)),
                ]



            
            elif self.spawn == "B":
                print("Detected Spawn as B")
                self.depotPositions = [
                    Point2((27.0, 34.0)), Point2((42.0, 25.0)), Point2((25.0, 34.0)),
                    Point2((26.0, 38.0)), Point2((24.0, 36.0)), Point2((31.0, 28.0)),
                    Point2((33.0, 26.0)), Point2((28.0, 32.0)), Point2((44.0, 28.0)),
                    Point2((29.0, 28.0)), Point2((28.0, 38.0)), Point2((33.0, 24.0)),
                    Point2((28.0, 36.0)), Point2((26.0, 36.0)), Point2((35.0, 26.0)),
                    Point2((29.0, 30.0)), Point2((27.0, 30.0)), Point2((39.0, 26.0)),
                    Point2((31.0, 26.0)), Point2((53.0, 38.0)), Point2((56.0, 41.0)),
                    Point2((38.0, 24.0)), Point2((37.0, 26.0)), Point2((42.0, 23.0)),
                    Point2((40.0, 24.0)), Point2((38.0, 22.0)), Point2((40.0, 22.0)),
                    Point2((26.0, 32.0)), Point2((35.0, 24.0))
                ]



                self.barracksPositions = [
                    Point2((44.5, 35.5)), Point2((44.5, 50.5)), Point2((44.5, 45.5)),
                    Point2((44.5, 30.5)), Point2((44.5, 40.5)), Point2((75.5, 38.5)),
                    Point2((82.5, 48.5)), Point2((68.5, 36.5)), Point2((68.5, 48.5)),
                    Point2((37.5, 45.5)), Point2((75.5, 53.5)), Point2((82.5, 53.5)),
                    Point2((30.5, 40.5)), Point2((75.5, 43.5)), Point2((51.5, 40.5)),
                    Point2((37.5, 40.5)), Point2((61.5, 36.5)), Point2((75.5, 48.5)),
                    Point2((73.5, 31.5)), Point2((49.5,35.5)),  Point2((68.5, 58.5)),
                    Point2((68.5, 53.5)), Point2((51.5, 45.5)), Point2((68.5, 41.5))
                ]
 

        elif self.map == "MagannathaAIE":
            print("Detected Map as MagannathaAIE")
            if self.spawn == "T":
                self.depotPositions = [
                    Point2((25.0, 146.0)), Point2((29.0, 146.0)), Point2((37.0, 150.0)),
                    Point2((24.0, 144.0)), Point2((23.0, 142.0)), Point2((27.0, 142.0)),
                    Point2((39.0, 150.0)), Point2((35.0, 150.0)), Point2((31.0, 150.0)),
                    Point2((25.0, 142.0)), Point2((33.0, 150.0)), Point2((27.0, 150.0)),
                    Point2((29.0, 148.0)), Point2((29.0, 142.0)), Point2((28.0, 144.0)),
                    Point2((31.0, 148.0)), Point2((36.0, 129.0)), Point2((23.0, 146.0)),
                    Point2((39.0, 126.0)), Point2((26.0, 144.0)), Point2((27.0, 146.0)),
                    Point2((25.0, 148.0)), Point2((30.0, 144.0)), Point2((27.0, 148.0)),
                    Point2((29.0, 150.0))
                ]


                self.barracksPositions = [
                    Point2((34.5, 110.5)), Point2((34.5, 120.5)), Point2((50.5, 100.5)),
                    Point2((43.5, 105.5)), Point2((31.5, 133.5)), Point2((36.5, 85.5)),
                    Point2((48.5, 144.5)), Point2((38.5, 128.5)), Point2((36.5, 105.5)),
                    Point2((36.5, 90.5)), Point2((43.5, 100.5)), Point2((45.5, 138.5)),
                    Point2((28.5, 78.5)), Point2((36.5, 100.5)), Point2((36.5, 95.5)),
                    Point2((38.5, 133.5)), Point2((20.5, 80.5)), Point2((43.5, 95.5)),
                    Point2((45.5, 133.5)), Point2((34.5, 115.5)), Point2((50.5, 95.5)),
                    Point2((31.5, 138.5))
                ]



            
            elif self.spawn == "B":
                print("Detected Spawn as B")
                self.depotPositions = [
                    Point2((152.0, 33.0)), Point2((151.0, 42.0)), Point2((153.0, 42.0)),
                    Point2((151.0, 46.0)), Point2((144.0, 31.0)), Point2((152.0, 37.0)),
                    Point2((150.0, 35.0)), Point2((147.0, 44.0)), Point2((148.0, 25.0)),
                    Point2((152.0, 29.0)), Point2((149.0, 46.0)), Point2((152.0, 35.0)),
                    Point2((150.0, 31.0)), Point2((149.0, 44.0)), Point2((126.0, 39.0)),
                    Point2((150.0, 29.0)), Point2((153.0, 46.0)), Point2((152.0, 39.0)),
                    Point2((152.0, 31.0)), Point2((129.0, 36.0)), Point2((148.0, 31.0)),
                    Point2((146.0, 31.0)), Point2((147.0, 46.0)), Point2((150.0, 33.0)),
                    Point2((150.0, 39.0)), Point2((150.0, 27.0)), Point2((151.0, 44.0)),
                    Point2((148.0, 27.0))
                ]



                self.barracksPositions = [
                    Point2((80.5, 33.5)), Point2((135.5, 33.5)), Point2((94.5, 40.5)),
                    Point2((128.5, 43.5)), Point2((135.5, 38.5)), Point2((76.5, 28.5)),
                    Point2((94.5, 50.5)), Point2((115.5, 35.5)), Point2((108.5, 35.5)),
                    Point2((142.5, 48.5)), Point2((135.5, 28.5)), Point2((87.5, 35.5)),
                    Point2((101.5, 40.5)), Point2((108.5, 30.5)), Point2((94.5, 35.5)),
                    Point2((101.5, 50.5)), Point2((128.5, 38.5)), Point2((135.5, 48.5)),
                    Point2((108.5, 40.5)), Point2((101.5, 45.5)), Point2((135.5, 43.5)),
                    Point2((94.5, 45.5)), Point2((142.5, 28.5)), Point2((135.5, 53.5))
                ]

        

        elif self.map == "InterloperAIE":
            print("Detected Map as InterloperAIE")
            if self.spawn == "T":
                self.depotPositions = [Point2((34.0, 125.0)), Point2((27.0, 147.0)), Point2((31.0, 148.0)), Point2((16.0, 130.0)), Point2((23.0, 145.0)), Point2((18.0, 143.0)), Point2((16.0, 132.0)), Point2((25.0, 147.0)), Point2((15.0, 136.0)), Point2((23.0, 147.0)), Point2((19.0, 147.0)), Point2((37.0, 122.0)), Point2((17.0, 137.0)), Point2((27.0, 149.0)), Point2((15.0, 138.0)), Point2((21.0, 148.0)),Point2((21.0, 145.0)), Point2((29.0, 148.0)), Point2((17.0, 146.0)), Point2((17.0, 139.0)), Point2((16.0, 142.0)), Point2((16.0, 144.0)), Point2((15.0, 140.0)), Point2((19.0, 145.0)), Point2((25.0, 149.0)), Point2((16.0, 134.0)), Point2((18.0, 141.0)), Point2((23.0, 149.0))]
                self.barracksPositions = [Point2((24.5, 102.5)), Point2((18.5, 105.5)), Point2((69.5, 136.5)), Point2((36.5, 139.5)), Point2((53.5, 113.5)), Point2((37.5, 149.5)), Point2((41.5, 113.5)), Point2((36.5, 144.5)), Point2((29.5, 128.5)), Point2((33.5, 114.5)), Point2((36.5, 124.5)), Point2((36.5, 134.5)), Point2((41.5, 105.5)), Point2((44.5, 118.5)), Point2((29.5, 133.5)), Point2((51.5, 122.5)), Point2((22.5, 128.5)), Point2((55.5, 140.5)), Point2((36.5, 129.5)), Point2((70.5, 127.5)), Point2((43.5, 145.5)), Point2((43.5, 135.5)), Point2((33.5, 107.5)), Point2((43.5, 140.5))]
            
            elif self.spawn == "B":
                print("Detected Spawn as B")
                self.depotPositions = [Point2((115.0, 18.0)), Point2((135.0, 26.0)), Point2((126.0, 21.0)), Point2((137.0, 29.0)), Point2((130.0, 23.0)), Point2((115.0, 46.0)), Point2((135.0, 22.0)), Point2((123.0, 21.0)), Point2((125.0, 19.0)), Point2((120.0, 20.0)), Point2((128.0, 21.0)), Point2((136.0, 31.0)), Point2((134.0, 24.0)), Point2((117.0, 21.0)), Point2((132.0, 21.0)), Point2((136.0, 24.0)), Point2((113.0, 21.0)), Point2((129.0, 19.0))]
                self.barracksPositions = [Point2((90.5, 51.5)), Point2((87.5, 45.5)), Point2((115.5, 43.5)), Point2((115.5, 54.5)), Point2((108.5, 28.5)), Point2((82.5, 41.5)), Point2((121.5, 65.5)), Point2((83.5, 31.5)), Point2((115.5, 33.5)), Point2((96.5, 54.5)), Point2((115.5, 38.5)), Point2((129.5, 38.5)), Point2((115.5, 23.5)), Point2((122.5, 38.5)), Point2((128.5, 65.5)), Point2((115.5, 28.5)), Point2((99.5, 46.5)), Point2((108.5, 23.5)), Point2((108.5, 54.5)), Point2((108.5, 33.5)), Point2((105.5, 49.5)), Point2((126.5, 60.5)), Point2((116.5, 60.5)), Point2((109.5, 60.5)), Point2((82.5, 36.5))]
        elif self.map == "ThunderbirdAIE":
            print("Detected Map as ThunderbirdAIE")
            if self.spawn == "T":
                self.depotPositions = [Point2((46.0, 145.0)), Point2((36.0, 144.0)), Point2((38.0, 143.0)), Point2((40.0, 144.0)), Point2((44.0, 144.0)), Point2((28.0, 135.0)), Point2((40.0, 146.0)), Point2((36.0, 142.0)), Point2((32.0, 141.0)), Point2((30.0, 141.0)), Point2((37.0, 118.0)), Point2((28.0, 133.0)), Point2((28.0, 137.0)), Point2((38.0, 145.0)), Point2((34.0, 142.0)), Point2((44.0, 146.0)), Point2((27.0, 131.0)), Point2((30.0, 139.0)), Point2((42.0, 144.0)), Point2((34.0, 144.0)), Point2((42.0, 146.0)), Point2((46.0, 143.0)), Point2((32.0, 143.0))]
                self.barracksPositions = [Point2((74.5, 130.5)), Point2((77.5, 117.5)), Point2((49.5, 140.5)), Point2((69.5, 136.5)), Point2((63.5, 117.5)), Point2((51.5, 107.5)), Point2((44.5, 107.5)), Point2((40.5, 96.5)), Point2((54.5, 112.5)), Point2((35.5, 120.5)), Point2((61.5, 112.5)), Point2((49.5, 135.5)), Point2((35.5, 125.5)), Point2((78.5, 123.5)), Point2((49.5, 125.5)), Point2((42.5, 130.5)), Point2((44.5, 101.5)), Point2((56.5, 117.5)), Point2((62.5, 136.5)), Point2((70.5, 117.5)), Point2((71.5, 123.5)), Point2((42.5, 125.5)), Point2((49.5, 130.5)), Point2((52.5, 102.5))]
            elif self.spawn == "B":
                self.barracksPositions = [Point2((121.5, 39.5)), Point2((112.5, 38.5)), Point2((115.5, 18.5)), Point2((147.5, 30.5)), Point2((147.5, 25.5)), Point2((154.5, 30.5)), Point2((125.5, 43.5)), Point2((112.5, 23.5)), Point2((133.5, 40.5)), Point2((140.5, 25.5)), Point2((142.5, 56.5)), Point2((142.5, 46.5)), Point2((142.5, 51.5)), Point2((147.5, 20.5)), Point2((149.5, 59.5)), Point2((112.5, 33.5)), Point2((127.5, 47.5)), Point2((140.5, 20.5)), Point2((140.5, 15.5)), Point2((140.5, 30.5)), Point2((154.5, 35.5)), Point2((112.5, 28.5)), Point2((161.5, 30.5))]
                self.depotPositions = [Point2((157.0, 14.0)), Point2((155.0, 14.0)), Point2((163.0, 24.0)), Point2((163.0, 26.0)), Point2((165.0, 26.0)), Point2((162.0, 20.0)), Point2((153.0, 12.0)), Point2((153.0, 14.0)), Point2((165.0, 24.0)), Point2((163.0, 18.0)), Point2((162.0, 16.0)), Point2((159.0, 14.0)), Point2((161.0, 14.0)), Point2((155.0, 12.0)), Point2((151.0, 10.0)), Point2((164.0, 20.0)), Point2((159.0, 12.0)), Point2((160.0, 16.0)), Point2((164.0, 22.0)), Point2((158.0, 16.0)), Point2((149.0, 10.0)), Point2((155.0, 38.0)), Point2((157.0, 12.0))]
       
        elif self.map == "AutomatonAIE":
            print("Detected Map as AutomatonAIE")
            if self.spawn == "T":
                self.depotPositions = [Point2((164.0, 114.0)), Point2((150.0, 108.0)), Point2((164.0, 120.0)), Point2((150.0, 114.0)), Point2((150.0, 116.0)), Point2((153.0, 106.0)), Point2((162.0, 108.0)), Point2((164.0, 112.0)), Point2((163.0, 124.0)), Point2((164.0, 122.0)), Point2((150.0, 112.0)), Point2((151.0, 106.0)), Point2((153.0, 130.0)), Point2((164.0, 118.0)), Point2((164.0, 116.0)), Point2((164.0, 108.0)), Point2((150.0, 110.0)), Point2((164.0, 110.0)), Point2((152.0, 108.0)), Point2((159.0, 106.0)), Point2((157.0, 106.0)), Point2((161.0, 106.0)), Point2((163.0, 106.0)), Point2((155.0, 106.0))]

                self.barracksPositions = [Point2((146.5, 141.5)), Point2((141.5, 96.5)), Point2((139.5, 141.5)), Point2((125.5, 131.5)), Point2((159.5, 102.5)), Point2((139.5, 146.5)), Point2((145.5, 107.5)), Point2((118.5, 126.5)), Point2((145.5, 117.5)), Point2((132.5, 136.5)), Point2((125.5, 126.5)), Point2((152.5, 127.5)), Point2((145.5, 102.5)), Point2((145.5, 122.5)), Point2((118.5, 121.5)), Point2((152.5, 97.5)), Point2((152.5, 122.5)), Point2((132.5, 131.5)), Point2((159.5, 127.5)), Point2((145.5, 112.5)), Point2((139.5, 136.5)), Point2((152.5, 102.5)), Point2((125.5, 136.5)), Point2((139.5, 151.5))]

            elif self.spawn == "B":
                self.barracksPositions = [
    Point2((42.5, 30.5)), Point2((38.5, 40.5)), Point2((43.5, 77.5)), Point2((43.5, 57.5)),
    Point2((43.5, 62.5)), Point2((29.5, 57.5)), Point2((52.5, 51.5)), Point2((59.5, 46.5)),
    Point2((36.5, 62.5)), Point2((39.5, 35.5)), Point2((36.5, 57.5)), Point2((45.5, 46.5)),
    Point2((31.5, 40.5)), Point2((36.5, 67.5)), Point2((36.5, 77.5)), Point2((43.5, 67.5)),
    Point2((36.5, 72.5)), Point2((43.5, 72.5)), Point2((59.5, 51.5)), Point2((29.5, 79.5)),
    Point2((45.5, 40.5)), Point2((52.5, 46.5)), Point2((29.5, 74.5)), Point2((29.5, 52.5))
]

                self.depotPositions = [
    Point2((27.0, 82.0)), Point2((20.0, 72.0)), Point2((21.0, 74.0)), Point2((26.0, 78.0)),
    Point2((27.0, 84.0)), Point2((25.0, 82.0)), Point2((20.0, 70.0)), Point2((22.0, 78.0)),
    Point2((22.0, 72.0)), Point2((27.0, 74.0)), Point2((20.0, 62.0)), Point2((34.0, 53.0)),
    Point2((22.0, 76.0)), Point2((24.0, 76.0)), Point2((20.0, 64.0)), Point2((23.0, 80.0)),
    Point2((20.0, 68.0)), Point2((20.0, 66.0)), Point2((31.0, 50.0)), Point2((26.0, 76.0)),
    Point2((23.0, 74.0)), Point2((25.0, 74.0)), Point2((27.0, 80.0)), Point2((25.0, 80.0))
]
        elif self.map == "EphemeronAIE":
            if self.spawn == "T":
                self.barracksPositions = [
    Point2((47.5, 119.5)), Point2((43.5, 139.5)), Point2((68.5, 129.5)), Point2((29.5, 129.5)),
    Point2((68.5, 124.5)), Point2((36.5, 139.5)), Point2((29.5, 134.5)), Point2((61.5, 129.5)),
    Point2((61.5, 124.5)), Point2((54.5, 124.5)), Point2((43.5, 134.5)), Point2((36.5, 134.5)),
    Point2((36.5, 144.5)), Point2((36.5, 129.5)), Point2((22.5, 129.5)), Point2((46.5, 114.5)),
    Point2((43.5, 129.5)), Point2((43.5, 144.5)), Point2((39.5, 114.5)), Point2((54.5, 119.5)),
    Point2((39.5, 107.5)), Point2((68.5, 134.5)), Point2((46.5, 107.5)), Point2((36.5, 124.5))
]

                self.depotPositions = [
    Point2((20.0, 139.0)), Point2((18.0, 137.0)), Point2((26.0, 149.0)), Point2((34.0, 125.0)),
    Point2((20.0, 135.0)), Point2((22.0, 149.0)), Point2((24.0, 147.0)), Point2((18.0, 141.0)),
    Point2((30.0, 147.0)), Point2((18.0, 135.0)), Point2((24.0, 149.0)), Point2((26.0, 147.0)),
    Point2((22.0, 145.0)), Point2((18.0, 143.0)), Point2((20.0, 145.0)), Point2((18.0, 145.0)),
    Point2((20.0, 147.0)), Point2((30.0, 149.0)), Point2((20.0, 137.0)), Point2((28.0, 149.0)),
    Point2((20.0, 141.0)), Point2((20.0, 143.0)), Point2((28.0, 147.0)), Point2((22.0, 147.0)),
    Point2((18.0, 139.0))
]

            elif self.spawn == "B":
                self.barracksPositions = [
    Point2((121.5, 52.5)), Point2((88.5, 23.5)), Point2((121.5, 15.5)), Point2((93.5, 33.5)),
    Point2((100.5, 38.5)), Point2((114.5, 20.5)), Point2((121.5, 20.5)), Point2((121.5, 45.5)),
    Point2((128.5, 30.5)), Point2((88.5, 28.5)), Point2((121.5, 35.5)), Point2((100.5, 33.5)),
    Point2((88.5, 18.5)), Point2((114.5, 45.5)), Point2((114.5, 25.5)), Point2((121.5, 30.5)),
    Point2((121.5, 25.5)), Point2((114.5, 52.5)), Point2((107.5, 45.5)), Point2((135.5, 30.5)),
    Point2((128.5, 25.5)), Point2((114.5, 15.5)), Point2((107.5, 40.5)), Point2((114.5, 30.5))
]

                self.depotPositions = [
    Point2((138.0, 15.0)), Point2((142.0, 19.0)), Point2((141.0, 26.0)), Point2((132.0, 9.0)),
    Point2((137.0, 27.0)), Point2((136.0, 9.0)), Point2((141.0, 24.0)), Point2((123.0, 38.0)),
    Point2((143.0, 24.0)), Point2((132.0, 13.0)), Point2((132.0, 11.0)), Point2((142.0, 21.0)),
    Point2((136.0, 13.0)), Point2((140.0, 20.0)), Point2((140.0, 13.0)), Point2((140.0, 17.0)),
    Point2((134.0, 11.0)), Point2((134.0, 13.0)), Point2((138.0, 13.0)), Point2((142.0, 17.0)),
    Point2((138.0, 11.0)), Point2((139.0, 27.0)), Point2((126.0, 35.0)), Point2((140.0, 15.0))
]
        elif self.map == "AcropolisAIE":
            if self.spawn == "T":
                self.barracksPositions = [
    Point2((33.5, 91.5)), Point2((35.5, 129.5)), Point2((50.5, 66.5)), Point2((42.5, 134.5)),
    Point2((33.5, 96.5)), Point2((40.5, 81.5)), Point2((35.5, 134.5)), Point2((37.5, 114.5)),
    Point2((40.5, 71.5)), Point2((42.5, 144.5)), Point2((33.5, 78.5)), Point2((40.5, 91.5)),
    Point2((40.5, 86.5)), Point2((45.5, 91.5)), Point2((37.5, 109.5)), Point2((40.5, 76.5)),
    Point2((31.5, 106.5)), Point2((42.5, 124.5)), Point2((33.5, 101.5)), Point2((28.5, 129.5)),
    Point2((43.5, 66.5)), Point2((40.5, 96.5)), Point2((42.5, 129.5)), Point2((42.5, 139.5))
]
                self.depotPositions =  [
    Point2((22.0, 141.0)), Point2((34.0, 148.0)), Point2((36.0, 148.0)), Point2((22.0, 137.0)),
    Point2((24.0, 137.0)), Point2((36.0, 150.0)), Point2((25.0, 145.0)), Point2((34.0, 150.0)),
    Point2((26.0, 143.0)), Point2((31.0, 146.0)), Point2((27.0, 146.0)), Point2((22.0, 143.0)),
    Point2((38.0, 148.0)), Point2((40.0, 125.0)), Point2((43.0, 122.0)), Point2((32.0, 148.0)),
    Point2((32.0, 150.0)), Point2((24.0, 135.0)), Point2((24.0, 141.0)), Point2((30.0, 148.0)),
    Point2((22.0, 139.0)), Point2((28.0, 148.0)), Point2((29.0, 146.0)), Point2((24.0, 143.0)),
    Point2((38.0, 150.0)), Point2((30.0, 150.0)), Point2((24.0, 139.0)), Point2((22.0, 135.0))
]
            elif self.spawn == "B":
                self.barracksPositions = [
    Point2((136.5, 68.5)), Point2((131.5, 47.5)), Point2((131.5, 42.5)), Point2((144.5, 76.5)),
    Point2((136.5, 88.5)), Point2((133.5, 103.5)), Point2((145.5, 42.5)), Point2((140.5, 93.5)),
    Point2((138.5, 42.5)), Point2((136.5, 78.5)), Point2((131.5, 27.5)), Point2((131.5, 37.5)),
    Point2((136.5, 83.5)), Point2((133.5, 93.5)), Point2((138.5, 37.5)), Point2((124.5, 37.5)),
    Point2((133.5, 98.5)), Point2((126.5, 103.5)), Point2((136.5, 73.5)), Point2((135.5, 62.5)),
    Point2((129.5, 83.5)), Point2((126.5, 108.5)), Point2((135.5, 57.5)), Point2((131.5, 32.5))
]
                self.depotPositions = [
    Point2((147.0, 22.0)), Point2((152.0, 33.0)), Point2((154.0, 35.0)), Point2((152.0, 35.0)),
    Point2((145.0, 22.0)), Point2((154.0, 29.0)), Point2((154.0, 33.0)), Point2((152.0, 27.0)),
    Point2((139.0, 24.0)), Point2((152.0, 31.0)), Point2((141.0, 22.0)), Point2((136.0, 47.0)),
    Point2((150.0, 28.0)), Point2((141.0, 24.0)), Point2((145.0, 24.0)), Point2((152.0, 29.0)),
    Point2((143.0, 24.0)), Point2((139.0, 22.0)), Point2((147.0, 24.0)), Point2((143.0, 22.0)),
    Point2((152.0, 37.0)), Point2((154.0, 37.0)), Point2((154.0, 31.0)), Point2((133.0, 50.0))
]
    






                
            
        
                




        
         

    