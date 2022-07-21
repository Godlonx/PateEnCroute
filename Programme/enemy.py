import sqlite3

class Plante:
    def __init__(self, id) -> None:
        self.id = id
        self.pos_x = 0
        self.nom = self.get_stat('nom')
        self.pv = self.get_stat('pv')
        self.atk = self.get_stat('atk')
        self.ms = self.get_stat('ms')
        self.power_lvl = self.get_stat('pwr_lvl')
        self.spawn_rate = self.get_stat('spawn_rate')
        self.lien = f'../Font/Plantes/{self.nom}/0.png'

    def get_stat(self, stat):
        sqliteConnection = sqlite3.connect('../Documents/StatsPlayers.db')
        cursor = sqliteConnection.cursor()
        cursor.execute(f'''SELECT {stat} from Plantes where id = {self.id}''')
        stats = cursor.fetchone()
        sqliteConnection.commit()
        cursor.close()
        return stats[0]