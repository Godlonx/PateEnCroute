import sqlite3

class Enemy:
    def __init__(self):
        self.mobs = {"Normal": {"pv": 2, "speed": 1, "width": (10, 10),"loot":2 , "spe": None},
                     "Speed": {"pv": 1, "speed": 2,"width": (10, 10),"loot":3 , "spe": None},
                     "Gros": {"pv": 3, "speed": 0.5, "width": (20, 15),"loot":8 , "spe": "Division"}}

        self.bosses = {"Invocateur": {"pv": 15, "speed": 0.5, "width": (100, 100), "spe": "Invocation"}}

        self.AllEnemy = []

    def add_mob(self, MobName):
        self.AllEnemy.append(MobName)

    def get_mob_stat(self, MobName, stat):
        return self.mobs[MobName][stat]

    