import sqlite3
import pygame

class Pate:
    def __init__(self, id) -> None:
        self.id = id
        self.nom = self.get_stat('nom')
        self.pv = self.get_stat('pv')
        self.atk = self.get_stat('atk')
        self.lien = f'../Font/pates/pate{id}/0.png'
        self.nb_sprite = self.get_stat('nb_sprites')
        

    def get_stat(self, stat):
        sqliteConnection = sqlite3.connect('../Documents/StatsPlayers.db')
        cursor = sqliteConnection.cursor()
        cursor.execute(f'''SELECT {stat} from Pates where id = {self.id}''')
        stats = cursor.fetchone()
        sqliteConnection.commit()
        cursor.close()
        return stats[0]

class Bullet:
    def __init__(self, id, dmg, pos, ligne):
        self.id = id
        self.ligne = ligne
        self.lien = f'../Font/HUD/bullet/pate{id}/0.png'
        self.pos_x = pos[0]+80
        self.pos_y = pos[1]+55
        self.hitbox = pygame.Rect(self.pos_x, self.pos_y, 24, 16)
        self.dmg = dmg
