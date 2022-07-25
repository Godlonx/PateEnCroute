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

## les valeurs de puissances des mondes (val_pwr) : exemple possible : niveau 1/5 = 10, niveau 2/5 = 15, niveau 4/5 = 20 et niveau 3/5 et 5/5 = mini jeu et BOSS.


class Wave():
    def __init__(self, monde: int, val_pwr: int, difficulty: int):
        self.monde = monde # le monde dans laquelle le joueur est rendu
        self.val_pwr = val_pwr # indice de puissance qui sert a créer une vague d'ennemis équilibré
        self.difficulty = difficulty # la difficulté de jeu
        self.diff_lvl = 0 # la différence de puissance en la moyenne et la vague créer, elle servira a rééquillibré le niveau grace au challenge
        self.mob_dispo = [] # liste des ennemis disponnible dans se monde

        self.flag = 1 # nombre de drapeau de la vague
        self.chall = [] # liste de challenge selectionné
        self.compo = [] # ennemis selectionné pour la vague
        self.mob_spawn_list = [] # tab a défilé pour savoir quelle mob spawn
        self.create_wave()


    def bestiaire_dispo(self): # récupéré depuis la database tout les mobs du monde: "self.monde"
        idmob = self.db(f'Select id_mob from Bestiaire where id_monde = {self.monde}')
        for i in range(len(idmob)):
            self.mob_dispo.append(self.db(f'Select nom, pwr_lvl, id, spawn_rate from Plantes where id = {idmob[i][0]}'))




    def db(self, request): # sert a récupéré les informations dans la bdd
        sqliteConnection = connect('../Documents/StatsPlayers.db')
        cursor = sqliteConnection.cursor()
        cursor.execute(request)
        info = cursor.fetchall()
        sqliteConnection.commit()
        cursor.close()
        return info



    def selection_mobs(self): # self.mob_dispo : tout les mobs présent dans se monde > sert a savoir quelle mob sont séléctionnable pour se lvl. self.difficulty : indice de modificateur de difficulté, où 0 = quasi pacifique, 1 = facile, 2 = normal ect. self.val_pwr : indice de la puissance disponnible pour créer une séléction de mob > sert a donné une valeur de difficulté pour un niveau comme lvl1 = 10, lvl2 = 15 et lvl4 = 20.
        select = []
        for i in range(len(self.mob_dispo)):
            if self.mob_dispo[i][0][1] == -1:
                select.append(self.mob_dispo[i][0])
            elif self.mob_dispo[i][0][1] > 0 <= self.val_pwr:
                #print((self.mob_dispo[i][0][0], testproba(self.mob_dispo[i][0][1], self.val_pwr, self.difficulty))) # sert pour test
                if randint(0,int((1 + self.mob_dispo[i][0][1]) * 5)) <= int((self.val_pwr / 2) * (1 + ((self.difficulty * 2) / 10))):
                    select.append(self.mob_dispo[i][0])
                    self.diff_lvl += self.mob_dispo[i][0][1]
        # diff_lvl peut servir a voir si la difficulté est trop haute ou trop basse par rapport a la moyenne et alors ajustez la difficulté avec des évenemnts aléatoires, terrains plus compliqué et/ou condition de victoire...
        #print(select)
        return select


    def challenge(self):
        diff = self.val_pwr - self.diff_lvl
        if diff >= 12:
            self.chall.append(4) # id : Chall Hard
        elif diff >= 8:
            self.chall.append(3) # id : Chall normal
        elif diff >= 4:
            self.chall.append(2) # id : Chall ez
        elif diff >= 0:
            self.chall.append(1) # id : No Chall
        else:
            self.chall.append(0) # id : Chall bonus / aide
        self.flag = int(2 + ((diff + self.difficulty * 3 - 5) / 12))



    def file_mobs(self):
        v = ((1 + self.difficulty * 0.2) * (self.flag * 0.8)) * 50
        val_max = randint(int(v * 0.9), int(v * 1.1))
        val = 0
        spawn = [] # spawn potential
        #print(self.compo)
        for i in range(len(self.compo)):
            for j in range(self.compo[i][3]):
                spawn.append(self.compo[i][2])
        #print(spawn)
        self.mob_spawn_list.append(spawn[0]) # être sur que les 3 premiers végétaux soit des trucs basiques, puis après roues libres
        self.mob_spawn_list.append(spawn[0])
        self.mob_spawn_list.append(spawn[0])

        for _ in range(self.flag):
            while val < val_max // self.flag: # lorsque l'on summon la wave : si la val est >= 0 alors summon l'unité de cette id, sinon summon avec un délaie de ~6 frame les ||val|| prochaine unités (et affiché le texte de la wave)
                self.mob_spawn_list.append(spawn[randint(0,len(spawn) - 1)])
                val = val + 1
            val = 0
            vague_nbr = randint(10, 10 + self.difficulty * 3 + int(self.val_pwr * 0.2))
            self.mob_spawn_list.append(vague_nbr * -1)
            for _ in range(vague_nbr):
                self.mob_spawn_list.append(spawn[randint(0,len(spawn) - 1)])



    def create_wave(self): # exécute toute les étapes de créations de la vague en une seule fonction
        self.bestiaire_dispo()
        self.compo = self.selection_mobs()
        self.challenge()
        self.file_mobs()



def testproba(val, pwr, diff): # sert a testé le pourcentage de chance de pop d'un mob dans une compo avec plein de paramètre
    nbr = 0
    for i in range(10000):
        if randint(0,int((1 + val) * 5)) <= int((pwr / 2) * (1 + ((diff * 2) / 10))):
            nbr = nbr + 1
    return nbr / 100


