import pygame, PlayerMob, main

class StartGame:
    def __init__(self):
        self.wave = main.Game.account.get_stat("wave")
    def StartWave(self):
        if self.wave == 1:
            pass
        elif self.wave != 1 and self.wave%10 != 0:
            pass
        else:
            pass
        # Laisser un compteur si c'est la premier vague
        # Lancer la vague
