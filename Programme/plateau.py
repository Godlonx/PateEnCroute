import pygame
from random import randint
from wave_generator import Wave
from enemy import Plante
import sqlite3



class Terrain:
    def __init__(self, pates, monde):
        self.t_case = 100
        self.nb_case_X = 9
        self.nb_case_Y = 5
        self.tab_case = {}
        self.info_pates = pates
        self.wave = Wave(monde, 15, 2)
        self.mob_wave = self.wave.mob_spawn_list
        self.mob_wave.reverse()
        self.monde = monde
        self.terrain_enemy = [[], [], [], [], []]
        self.using_pates = None
        self.steaks = 90000
        self.drawed_first = True

    def draw(self, screen):
        self.steaks_inf = pygame.Rect(10, 10, 100, 80)
        pygame.draw.rect(screen, (0, 0, 255), self.steaks_inf)

        self.pause = pygame.Rect(990, 10, 60, 60) # Button pause in game (option, quitter, reprendre)
        pygame.draw.rect(screen, (255, 0, 0), self.pause)

        self.wave_inf = pygame.Rect(900, 670, 150, 20) # penser à modifier la taille en fonction du nombre de wave
        pygame.draw.rect(screen, (0, 0, 255), self.wave_inf)

        for i in range(6):
            pygame.draw.rect(screen, (0,255,255), self.pates[f'pate{self.info_pates[i]}'].hitbox)
        
        self.update_terrain(screen)

    def first_draw(self, screen):
        self.n = 1
        self.p = 1
        self.fond = pygame.Rect(0, 0, 1080, 720)
        pygame.draw.rect(screen, (44, 47, 51), self.fond)
        self.pates = {}
        n = 0
        for i in range(5):
            for j in range(9):
                n += 1
                self.tab_case[f'case{n}'] = case(n, pygame.Rect(150+j*self.t_case, 150+i*self.t_case, self.t_case, self.t_case), (150+j*self.t_case, 150+i*self.t_case), i)
        for i in range(6):
            lien = f'../Font/pates/pate{self.info_pates[i]}/0.png'
            #pate = pygame.transform.scale(pate, (100, 100))
            self.pates[f'pate{self.info_pates[i]}'] = pate_graine(self.info_pates[i], pygame.Rect(120+i*105, 10, 95, 70), lien)
        self.terrain = pygame.image.load('../Font/Terrain/damier.png')
        screen.blit(self.terrain, (150,150))
          

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
                    if pygame.Rect.collidepoint(self.pause, event.pos):
                        pass
                else:
                    for case in self.tab_case.keys():
                        if pygame.Rect.collidepoint(self.tab_case[case].pos, event.pos):
                            if self.tab_case[case].used == None:
                                self.tab_case[case].used = self.using_pates
                                self.tab_case[case].lien = self.pates[f'pate{self.using_pates}'].lien
                                self.tab_case[case].event = 'Normal'
                                self.tab_case[case].cd = self.pates[f'pate{self.using_pates}'].shoot_cd
                                self.pates[f'pate{self.using_pates}'].recup = self.pates[f'pate{self.using_pates}'].cd
                                self.pates[f'pate{self.using_pates}'].usable = False
                                self.steaks -= self.pates[f'pate{self.using_pates}'].cout
                                
                    self.using_pates = None
                                
                if pygame.Rect.collidepoint(self.pause, event.pos):
                    self.drawed_first = True
                    return 'pause'
                return None


    def update_terrain(self, screen):
        self.terrain = pygame.image.load('../Font/Terrain/damier.png')
        screen.blit(self.terrain, (150,150))


        # Décrementé le cd des pates
        for pate in self.pates.keys():
            if self.pates[pate].recup > 0:
                self.pates[pate].recup -= 1
            else:
                self.pates[pate].usable = True

        #Afficher les pates sur les cases
        for case in self.tab_case.keys():
            if self.tab_case[case].lien != None:
                self.update_case(self.tab_case[case], screen)

        pygame.display.flip()

    def add_enemy(self):
        # Ajouter les plantes
        if self.mob_wave[len(self.mob_wave)-1] >= 0:
            self.terrain_enemy[randint(0, 4)].append(Plante(self.mob_wave.pop()).id)
        else:
            for _ in range(abs(self.mob_wave.pop())):
                self.terrain_enemy[randint(0, 4)].append(Plante(self.mob_wave.pop()).id)
        print(self.terrain_enemy)

    def update_case(self, case, screen):
        if len(self.terrain_enemy[case.ligne]) > 0 and case.cd == 0:
            if case.event != 'Tir':
                case.event = 'Tir'
                case.lien = f'../Font/pates/tir{case.used}/0.png'
            
        elif len(self.terrain_enemy[case.ligne]) == 0 or case.cd == 30:
            if case.event != 'Normal':
                case.event = 'Normal'
                case.lien = f'../Font/pates/pate{case.used}/0.png'
            
        if case.event == 'Normal':
            if case.cd > 0:
                case.cd -= 1
            case.lien = self.anim_pate(case.lien, 10)
        elif case.event == 'Tir':
            if case.cd < 10:
                case.cd += 1
            case.lien = self.anim_pate(case.lien, 10)
        screen.blit(pygame.image.load(case.lien), (case.co[0], case.co[1]+10))
            

    def anim_pate(self, lien, nb_sprite):
        tab = lien.split('/')
        tab[4] = str((int(tab[4][0])+1)%nb_sprite)+'.png'
        lien = ''
        for i in tab:
            lien += i+'/'
        lien = lien[:len(lien)-1]
        return lien

class case:
    def __init__(self, id, rect, co, ligne) -> None:
        self.id = id
        self.ligne = ligne
        self.cd = None
        self.event = None
        self.used = None # L'id du paté present dessus.
        self.pos = rect
        self.lien = None
        self.co = co


class pate_graine:
    def __init__(self, id, rect, lien) -> None:
        self.id = id
        self.nom = self.get_stat('nom')
        self.hitbox = rect
        self.lien = lien
        self.shoot_cd = 8
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