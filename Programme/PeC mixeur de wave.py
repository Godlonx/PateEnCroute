from random import *

tab_r = [('Tofu',-1),('Citron',1),('Brocogneur',3),('Olive',2),('Noix de coco',5),('Carotte',2),('Super-Tomate',1)]

def mixeur_wave(mob_dispo: list, difficulty: int, val_pwr: int): # mob_dispo : tout les mobs présent dans se monde > sert a savoir quelle mob sont séléctionnable pour se lvl. difficulty : indice de modificateur de difficulté, où 0 = quasi pacifique, 1 = facile, 2 = normal ect. val_pwr : indice de la puissance disponnible pour créer une séléction de mob > sert a donné une valeur de difficulté pour un niveau comme lvl1 = 10, lvl2 = 20 et lvl4 = 30.
    select = []
    diff_lvl = 0
    for i in range(len(mob_dispo)):
        if mob_dispo[i][1] == -1:
            select.append(mob_dispo[i][0])
        elif mob_dispo[i][1] > 0 <= val_pwr:
            print((mob_dispo[i][0], testproba(mob_dispo[i][1], val_pwr, difficulty)))
            if randint(0,int((1 + mob_dispo[i][1]) * 4)) <= int((val_pwr / 2) * (1 + ((difficulty * 2) / 10))):
                select.append(mob_dispo[i][0])
                diff_lvl += mob_dispo[i][1]
    # diff_lvl peut servir a voir si la difficulté est trop haute ou trop basse par rapport a la moyenne et alors ajustez la difficulté avec des évenemnts aléatoires, terrains plus compliqué et/ou condition de victoire...
    return select






def testproba(val, pwr, diff):
    nbr = 0
    for i in range(10000):
        if randint(0,int((1 + val) * 4)) <= int((pwr / 2) * (1 + ((diff * 2) / 10))):
            nbr = nbr + 1
    return nbr / 100




