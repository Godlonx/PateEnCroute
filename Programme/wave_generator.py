from random import *
import collections
from sqlite3 import *


creer_file_vide = collections.deque
file_vide = lambda file: len(file) == 0
enfiler = collections.deque.append
premier = lambda file: file[0]
defiler = collections.deque.popleft




# Ne pas suppr, je m'en sert pour mes tests (je le vire dés que il sert plus)
tab_test = [('Tofu',-1),('Citron',1),('Brocogneur',3),('Olive',2),('Noix de coco',5),('Carotte',2),('Super-Tomate',1)]

## les difficultés : 0 = pacifique (on la mettera pas ingame mais si on veut faire des tests sans galérés ça peut servir)
# 1 = facile
# 2 = normal
# 3 = difficile

## les valeurs de puissances des mondes (val_pwr) : exemple possible : niveau 1/5 = 10, niveau 2/5 = 20, niveau 4/5 = 30 et niveau 3/5 et 5/5 = mini jeu et BOSS.


class Wave():
    def __init__(self, monde: int, val_pwr: int, difficulty: int):
        self.monde = monde
        self.val_pwr = val_pwr
        self.difficulty = difficulty
        self.diff_lvl = 0
        self.mob_dispo

        self.flag = 1
        self.mob_spawn_list = creer_file_vide # file a défilé pour savoir quelle mob spawn


    def bestiare_dispo(self):
        pass # récupéré depuis la database tout les mobs du monde: "self.monde"



    def mixeur_wave(self): # self.mob_dispo : tout les mobs présent dans se monde > sert a savoir quelle mob sont séléctionnable pour se lvl. self.difficulty : indice de modificateur de difficulté, où 0 = quasi pacifique, 1 = facile, 2 = normal ect. self.val_pwr : indice de la puissance disponnible pour créer une séléction de mob > sert a donné une valeur de difficulté pour un niveau comme lvl1 = 10, lvl2 = 20 et lvl4 = 30.
        select = []
        for i in range(len(self.mob_dispo)):
            if self.mob_dispo[i][1] == -1:
                select.append(self.mob_dispo[i][0])
            elif self.mob_dispo[i][1] > 0 <= self.val_pwr:
                print((self.mob_dispo[i][0], testproba(self.mob_dispo[i][1], self.val_pwr, self.difficulty))) # sert pour test
                if randint(0,int((1 + self.mob_dispo[i][1]) * 4)) <= int((self.val_pwr / 2) * (1 + ((self.difficulty * 2) / 10))):
                    select.append(self.mob_dispo[i][0])
                    self.diff_lvl += self.mob_dispo[i][1]
        # diff_lvl peut servir a voir si la difficulté est trop haute ou trop basse par rapport a la moyenne et alors ajustez la difficulté avec des évenemnts aléatoires, terrains plus compliqué et/ou condition de victoire...




        return select






def testproba(val, pwr, diff): # sert a testé le pourcentage de chance de pop d'un mob dans une compo avec plein de paramètre
    nbr = 0
    for i in range(10000):
        if randint(0,int((1 + val) * 4)) <= int((pwr / 2) * (1 + ((diff * 2) / 10))):
            nbr = nbr + 1
    return nbr / 100




