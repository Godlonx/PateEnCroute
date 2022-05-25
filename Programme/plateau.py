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
        self.steaks = 90000
        self.drawed_first = True
        print(self.info_pates)

    def draw(self, screen):
       

       
        
        self.terrain = pygame.image.load('../Font/Terrain/damier.png')
        

        if self.drawed_first == True:
            self.fond = pygame.Rect(0, 0, 1080, 720)
            pygame.draw.rect(screen, (44, 47, 51), self.fond)
            self.pates = {}
            n = 0
            for i in range(5):
                for j in range(9):
                    n += 1
                    self.tab_case[f'case{n}'] = case(n, pygame.Rect(150+j*self.t_case, 150+i*self.t_case, self.t_case, self.t_case), (150+j*self.t_case, 150+i*self.t_case))
                    
            for i in range(6):
                pate = pygame.image.load(f'../Font/pates/pate{self.info_pates[i]}/0.png')
                pate = pygame.transform.scale(pate, (100, 100))
                self.pates[f'pate{self.info_pates[i]}'] = pate_graine(self.info_pates[i], pygame.Rect(120+i*105, 10, 95, 70), pate)
            
            screen.blit(self.terrain, (150,150))
            self.drawed_first = False


        self.steaks_inf = pygame.Rect(10, 10, 100, 80)
        pygame.draw.rect(screen, (0, 0, 255), self.steaks_inf)

        self.pause = pygame.Rect(990, 10, 60, 60) # Button pause in game (option, quitter, reprendre)
        pygame.draw.rect(screen, (255, 0, 0), self.pause)

        self.wave_inf = pygame.Rect(900, 670, 150, 20) # penser à modifier la taille en fonction du nombre de wave
        pygame.draw.rect(screen, (0, 0, 255), self.wave_inf)
        

        
        #n = 0
        #for i in range(5):
        #    for j in range(9):
        #        n += 1
        #        pygame.draw.rect(screen, (0+j*4,255-(i+j)*6,0+i*4), self.tab_case[f'case{n}'].pos)

        for i in range(6):
            pygame.draw.rect(screen, (0,255,255), self.pates[f'pate{self.info_pates[i]}'].hitbox)


    def Pause(self, screen):
        self.bouton_retour = pygame.Rect(465, 335, 50, 50)
        pygame.draw.rect(screen,(255, 0, 50), self.bouton_retour)

    def gevent(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if self.using_pates == None:
                    for pate in self.pates.keys():
                        if pygame.Rect.collidepoint(self.pates[pate].hitbox, event.pos):
                            if self.pates[pate].usable:
                                if self.pates[pate].cout <= self.steaks:
                                    self.using_pates = self.pates[pate].id
                                    print('Pates Utiliser est: ', self.pates[pate].nom)
                                    self.steaks -= self.pates[pate].cout
                    if pygame.Rect.collidepoint(self.pause, event.pos):
                        pass
                else:
                    for case in self.tab_case.keys():
                        if pygame.Rect.collidepoint(self.tab_case[case].pos, event.pos):
                            if self.tab_case[case].used == None:
                                print(self.tab_case[case].used)
                                self.tab_case[case].used = self.using_pates
                                self.tab_case[case].sprite = self.pates[f'pate{self.using_pates}'].sprite
                                self.pates[f'pate{self.using_pates}'].recup = self.pates[f'pate{self.using_pates}'].cd
                                self.pates[f'pate{self.using_pates}'].usable = False
                                print(self.tab_case[case].id, 'a comme paté', self.using_pates, self.tab_case[case].used)
                    self.using_pates = None
                                
                if pygame.Rect.collidepoint(self.pause, event.pos):
                    return 'pause'
                return None

    def update_pate(self, screen):
        print(self.steaks)
        for pate in self.pates.keys():
            if self.pates[pate].recup > 0:
                self.pates[pate].recup -= 1
            else:
                self.pates[pate].usable = True

        for case in self.tab_case.keys():
            if self.tab_case[case].sprite != None:
                screen.blit(self.tab_case[case].sprite, self.tab_case[case].co)
        pygame.display.flip()
        

class case:
    def __init__(self, id, rect, co) -> None:
        self.id = id
        self.used = None # L'id du paté present dessus.
        self.pos = rect
        self.sprite = None
        self.co = co


class pate_graine:
    def __init__(self, id, rect, sprite) -> None:
        self.id = id
        self.nom = self.get_stat('nom')
        self.hitbox = rect
        self.sprite = sprite
        self.usable = True
        self.cout = self.get_stat('cout')[0]
        self.cd = self.get_stat('cd')[0]
        self.recup = 0

    def get_stat(self, stat):
        sqliteConnection = sqlite3.connect('../Documents/StatsPlayers.db')
        cursor = sqliteConnection.cursor()
        cursor.execute(f'''SELECT {stat} from pates where id = {self.id}''')
        stati = cursor.fetchone()
        sqliteConnection.commit()
        cursor.close()
        return stati