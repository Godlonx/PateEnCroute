import sqlite3
from xmlrpc.client import FastMarshaller

class Player:
    def __init__(self):
        self.stat = {'id':None, 'pseudo': None, 'money':0, 'skillpoint':0, 'niveau':None}
        
    def get_stat(self, n):
        return self.stat[n]

    def modif_stat(self, n, val):
        self.stat[n] = val
        self.interact("UPDATE Players SET (?) = (?) WHERE id_player = (?)", (n, val, self.stat["id_player"]))
    
    def connect(self):
        vals = "SELECT P.pseudo, I.money, I.skillpoint, I.niveau From info_p as I Join players as P on P.id = I.id Where P.id = (?)"
        for i in range(1, 5):
            self.stat[list(self.stat.keys())[i]] = vals[i][0]

    def recup(self, request, val=None):
        sqliteConnection = sqlite3.connect('StatsPLayers.db')
        cursor = sqliteConnection.cursor()
        cursor.execute(request, val)
        value = cursor.fetchall()
        sqliteConnection.commit()
        cursor.close
        return value

    def interact(self, request, val=None):
        sqliteConnection = sqlite3.connect('StatsPLayers.db')
        cursor = sqliteConnection.cursor()
        cursor.execute(request, val)
        sqliteConnection.commit()
        cursor.close