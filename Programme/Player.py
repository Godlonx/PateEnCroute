import sqlite3
from xmlrpc.client import FastMarshaller

class Player:
    def __init__(self, id):
        self.id = id
        self.psuedo = self.recup(f'Select pseudo from players where id = {self.id}')
        self.monde = self.recup(f'Select monde from players where id = {self.id}')
        self.lvl = self.recup(f'Select lvl from players where id = {self.id}')

    def modif_stat(self, n, val):
        self.interact("UPDATE Players SET (?) = (?) WHERE id_player = (?)", (n, val, self.stat["id_player"]))
    
    def connect(self):
        vals = "SELECT P.pseudo, I.money, I.skillpoint, I.niveau From info_p as I Join players as P on P.id = I.id Where P.id = (?)"
        for i in range(1, 5):
            self.stat[list(self.stat.keys())[i]] = vals[i][0]

    def recup(self, request, val=None):
        sqliteConnection = sqlite3.connect('../Documents/StatsPlayers.db')
        cursor = sqliteConnection.cursor()
        if val == None:
            cursor.execute(request)
        else:
            cursor.execute(request, val)
        value = cursor.fetchall()[0][0]
        sqliteConnection.commit()
        cursor.close
        return value

    def interact(self, request, val=None):
        sqliteConnection = sqlite3.connect('../Documents/StatsPlayers.db')
        cursor = sqliteConnection.cursor()
        if val == None:
            cursor.execute(request)
        else:
            cursor.execute(request, val)
        sqliteConnection.commit()
        cursor.close