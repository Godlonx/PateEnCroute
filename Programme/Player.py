import sqlite3
from xmlrpc.client import FastMarshaller

class Player:
    def __init__(self):
        self.stat = {'id_player': None, 'money':0, 'soulpoint':0, 'skillpoint': 0, 'pseudo': None}
        
    def get_stat(self, n):
        return self.stat[n]

    def modif_stat(self, n, val):
        self.stat[n] = val
        self.interact("UPDATE Players SET (?) = (?) WHERE id_player = (?)", (n, val, self.stat["id_player"]))

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