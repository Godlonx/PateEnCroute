

class Mob():
    # création d'un ennemis qui va etre stocké et dont ces infos servirons a le généré
    def __init__(self, mob_type): 
    # mob_type est une id pour connaitre les stats et particularité d'un mob, ex: name, pv, ms, effet, fréquence(taux de spawn), délai (avant le premiers spawn possible, genre pas de gargantuar en 1er ennemis sur un coup du hasard)...
        self.mob_type = mob_type
        self.pv = ...
        self.ms = ...
        self.effet = []


class Wave():
    # création d'une pile 
    def __init__(self, difficulty, Flag, mob_type_list):
        # difficulty: pour le nombre d'ennemis et la vitesse de spawn, flag: le nombre de vague et donc la durée de la partie et mob_type_list: tab de toute les id des mobs qui seront présent dans cette partie
        
        self.mob_spawn_list = []
        # génération de la liste (pile?) d'une longueur de "base_spawn * difficulty + flag_nbr * difficulty" ...