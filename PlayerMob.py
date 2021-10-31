# Le Joueur

class Player:
    def __init__(self, pseudo):
        self.stat = {'Pseudo': pseudo, 'Skill_point': 0, 'Skills': [[None, 1, None, 1],[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                                                                    [0, 0, 0, 0], [0, 0, 0, 0],[0, 0, 0, 0], [0, 0, 0, 0]]}
        
    def get_stat(self, n):
        return self.stat[n]

    def modif_stat(self, n, val):
        self.stat[n] = val



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
