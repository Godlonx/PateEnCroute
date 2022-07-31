import sqlite3
import pygame

class Plante:
    def __init__(self, id, ligne) -> None:
        self.id = id
        self.nom = self.get_stat('nom')
        self.pv = self.get_stat('pv')
        self.atk = self.get_stat('atk')
        self.lien = f'../Font/Pate/{self.nom}/0.png'
        self.nb_sprite = self.get_stat('nb_sprites')
        

    def get_stat(self, stat):
        sqliteConnection = sqlite3.connect('../Documents/StatsPlayers.db')
        cursor = sqliteConnection.cursor()
        cursor.execute(f'''SELECT {stat} from Plantes where id = {self.id}''')
        stats = cursor.fetchone()
        sqliteConnection.commit()
        cursor.close()
        return stats[0]
