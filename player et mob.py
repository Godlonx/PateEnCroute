# Le Joueur
import pygame.sprite


class Player:
    def __init__(self, pseudo):
        self.stat = {'Pseudo': pseudo, 'Skill_point': 0, 'Skills': [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                                                                    [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
                                                                    [0, 0, 0, 0], [0, 0, 0, 0], [None, 1, None, 1]]}

    def get_stat(self, n):
        return self.stat[n]

    def modif_stat(self, n, val):
        self.stat[n] = val


# Les mobs


class Enemy:
    def __init__(self, mob):
        self.mobs = {"Normal": {"pv": 2, "speed": 1, "width": (10, 10)},
                     "Speed": {"pv": 1, "speed": 2,"width": (10, 10)},
                     "Gros": {"pv": 3, "speed": 0.5, "width": (20, 15)}}


        self.boss = {"Invocateur": {"pv": 15, "speed": 0.5, "Spé": "Invocation", "width": (100, 100)}}
        self.waves = [(1, 1), (1, 5), (1, 11), (1, 15), (2, 10, 3), (2, 12, 7), ]
        self.all_enemy = pygame.sprite.Group()

        self.enemy = self.mobs[mob]

    def create_enemy(self, name):
        enemy = self.mobs[name]

    def launch_wave(self, wave):
        pass
