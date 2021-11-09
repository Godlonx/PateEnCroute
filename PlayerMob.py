import sqlite3

# Le Joueur

class Player:
    def __init__(self):
        self.stat = {'id_player': None, "wave": 1, 'money':0, 'soulpoint':0, 'skillpoint': 0, 'pseudo': None, 'id_skilltree':None }
        
    def get_stat(self, n):
        return self.stat[n]

    def modif_stat(self, n, val):
        self.stat[n] = val
        sqliteConnection = sqlite3.connect('StatsPLayers.db')
        cursor = sqliteConnection.cursor()
        cursor.execute("UPDATE Players SET "+n+" = "+str(val)+" WHERE id_player = ?", (self.stat["id_player"]))
        sqliteConnection.commit()
        cursor.close

    def add_skilltree(self, id_skilltree):
        request = """INSERT INTO Skills (id_skill"""

    def get_account(self, pseudo): # permet au joueur de recupere les donne de jeu
        sqliteConnection = sqlite3.connect('StatsPLayers.db')
        cursor = sqliteConnection.cursor()
        request = '''SELECT id_player FROM Players WHERE pseudo = ?'''
        cursor.execute(request, (pseudo,))
        account = cursor.fetchone()
        print("1", account)
        if not account:
            maxi = 1
            request = """SELECT id_player FROM Players"""
            cursor.execute(request)
            for i in cursor.fetchall():
                if i[0] >= maxi:
                    maxi += 1
            print("2", maxi)
            data = (maxi, 1, 0, 0, 0, pseudo, maxi)           
            request = """INSERT INTO Players (id_player, wave, money, soulpoint, skillpoint, pseudo, id_skilltree) VALUES (?, ?, ?, ?, ?, ?, ?)"""
            cursor.execute(request, data)
            print("3")
            self.add_skilltree(maxi)
            sqliteConnection.commit()
            
        
        request = """SELECT wave, skillpoint, money, soulpoint, id_player FROM Players WHERE id_player = ?"""
        cursor.execute(request, account)
        stats = cursor.fetchall()
        self.stat["pseudo"] = pseudo
        self.stat["wave"] = stats[0][0]
        self.stat["skillpoint"] = stats[0][1]
        self.stat["money"] = stats[0][2]
        self.stat["soulpoint"] = stats[0][3]
        self.stat["id_player"] = stats[0][4]
        self.stat["id_skilltree"] = stats[0][4]
        cursor.close
        print(self.stat)


class Enemy:
    def __init__(self):
        self.mobs = {"Normal": {"pv": 2, "speed": 1, "width": (10, 10),"loot":2 , "spe": None},
                     "Speed": {"pv": 1, "speed": 2,"width": (10, 10),"loot":3 , "spe": None},
                     "Gros": {"pv": 3, "speed": 0.5, "width": (20, 15),"loot":8 , "spe": "Division"}}

        self.bosses = {"Invocateur": {"pv": 15, "speed": 0.5, "width": (100, 100), "spe": "Invocation"}}

        self.AllEnemy = []

    def add_mob(self, MobName):
        self.AllEnemy.append(MobName)

    def get_mob_stat(self, MobName, stat):
        return self.mobs[MobName][stat]

    