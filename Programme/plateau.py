import pygame
import sqlite3



class Terrain:
    def __init__(self, pates):
        self.t_case = 100
        self.nb_case_X = 9
        self.nb_case_Y = 5
        self.tab_case = {}
        self.info_pates = pates
        self.using_pates = None
        print(self.info_pates, 11111)

    def draw(self, screen):
        self.fond = pygame.Rect(0, 0, 1080, 720)
        pygame.draw.rect(screen, (44, 47, 51), self.fond)

        self.steaks_inf = pygame.Rect(10, 10, 100, 80)
        pygame.draw.rect(screen, (0, 0, 255), self.steaks_inf)

        self.pause = pygame.Rect(990, 10, 60, 60) # Button pause in game (option, quitter, reprendre)
        pygame.draw.rect(screen, (255, 0, 0), self.pause)

        self.wave_inf = pygame.Rect(900, 670, 150, 20) # penser à modifier la taille en fonction du nombre de wave
        pygame.draw.rect(screen, (0, 0, 255), self.wave_inf)

        for i in range(5):
            for j in range(9):
                self.tab_case[f'case{i}{j}'] = pygame.Rect(150+j*self.t_case, 150+i*self.t_case, self.t_case, self.t_case)
                pygame.draw.rect(screen, (0+j*4,255-(j+i)*6,0+i*4), self.tab_case[f'case{i}{j}'])

        print(self.tab_case)

        self.pates = {}

        for i in range(6):
            self.pates[f'pate{self.info_pates[i]}'] = pate(self.info_pates[i], pygame.Rect(120+i*105, 10, 95, 70))
            pygame.draw.rect(screen, (0,255,255), self.pates[f'pate{self.info_pates[i]}'].pos)




    def Pause(self, screen):
        self.bouton_retour = pygame.Rect(465, 335, 50, 50)
        pygame.draw.rect(screen,(255, 0, 50), self.bouton_retour)

    def gevent(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if self.using_pates == None:
                    for pates in self.pates.keys():
                        if pygame.Rect.collidepoint(self.pates[pates].pos, event.pos):
                            if self.pates[pates].usable:
                                self.using_pates = self.pates[pates].id
                                print('Pates Utiliser est: ', self.pates[pates].id)

                    if pygame.Rect.collidepoint(self.pause, event.pos):
                        pass
                else:
                    self.using_pates = None

            

class pate:
    def __init__(self, id, rect) -> None:
        self.id = id
        self.pos = rect
        self.usable = True
        self.cout = self.get_stat('cout')
        print(self.id, self.cout)

    def get_stat(self, stat):
        sqliteConnection = sqlite3.connect('../Documents/StatsPlayers.db')
        cursor = sqliteConnection.cursor()
        cursor.execute(f'SELECT (?) from pates where id = {self.id}', (stat,))
        stati = cursor.fetchall()
        sqliteConnection.commit()
        cursor.close()
        return stati