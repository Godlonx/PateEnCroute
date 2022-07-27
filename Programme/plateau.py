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
        '''  A mettre apres les test lorsque l'on auras tous les sprites :
        
        self.mob_wave = self.wave.mob_spawn_list
        self.mob_wave.reverse()

        '''
        self.mob_wave = [0,5,0,0,0,0]
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

        for i in self.info_pates:
            pygame.draw.rect(screen, (0,255,255), self.pates[f'pate{i}'].hitbox)
        
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
        for i in range(len(self.info_pates)):
            lien = f'../Font/pates/pate{self.info_pates[i]}/0.png'
            #pate = pygame.transform.scale(pate, (100, 100))
            self.pates[f'pate{self.info_pates[i]}'] = socket(self.info_pates[i], pygame.Rect(120+i*105, 10, 95, 70), lien)
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
                                self.tab_case[case].event = 'Normal'
                                self.tab_case[case].anim_normal = f'../Font/pates/pate{self.using_pates}/0.png'
                                self.tab_case[case].anim_tir = f'../Font/pates/tir{self.using_pates}/0.png'
                                self.tab_case[case].lien = f'../Font/pates/pate{self.using_pates}/0.png'
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

        for ligne in self.terrain_enemy:
            for plante in ligne:
                image = pygame.image.load(plante[0].lien)
                image = pygame.transform.scale(image, (100, 100))
                plante.append(image)
                screen.blit(plante[1], (plante[0].pos_x, plante[0].pos_y))
                self.anim_plante(plante[0])
                plante[0].pos_x -= plante[0].ms


        pygame.display.flip()

    def add_enemy(self):
        print(self.terrain_enemy)
        if len(self.mob_wave) > 0:
            # Ajouter les plantes
            if self.mob_wave[len(self.mob_wave)-1] >= 0:
                ligne = randint(0, 4)
                self.terrain_enemy[ligne].append([Plante(self.mob_wave.pop(), ligne)])
            else:
                for _ in range(abs(self.mob_wave.pop())):
                    ligne = randint(0, 4)
                    self.terrain_enemy[ligne].append([Plante(self.mob_wave.pop(), ligne)])

        

    def update_case(self, case, screen):
        if case.event == 'Normal':
            if len(self.terrain_enemy[case.ligne]) > 0:
                if case.anim_cd == 0:
                    case.event = 'Tir'
                    case.anim_cd = 0
                elif case.anim_cd > -12:
                    case.anim_cd -= 1

        elif case.event == 'Tir':
            if len(self.terrain_enemy[case.ligne]) > 0:
                if case.anim_cd == 9:
                    case.event = 'Normal'
                elif case.anim_cd < 9:
                    case.anim_cd += 1
            elif len(self.terrain_enemy[case.ligne]) == 0:
                case.event = 'Normal'
            
        if case.event == 'Normal':
            case.lien = case.anim_normal
            case.anim_normal = self.anim_pate(case.anim_normal, 10)
            case.anim_tir = f'../Font/pates/tir{case.used}/0.png'
        elif case.event == 'Tir':
            case.lien = case.anim_tir
            case.anim_tir = self.anim_pate(case.anim_tir, 10)
            case.anim_normal = f'../Font/pates/pate{case.used}/0.png'

        screen.blit(pygame.image.load(case.lien), (case.co[0], case.co[1]+10))
            

    def anim_pate(self, lien, nb_sprite):
        tab = lien.split('/')
        tab[4] = str((int(tab[4][0])+1)%nb_sprite)+'.png'
        lien = ''
        for i in tab:
            lien += i+'/'
        lien = lien[:len(lien)-1]
        return lien
    
    def anim_plante(self, plante):
        lien = plante.lien
        tab = lien.split('/')
        tab[4] = str((int(tab[4][0])+1)%plante.nb_sprite)+'.png'
        lien = ''
        for i in tab:
            lien += i+'/'
        lien = lien[:len(lien)-1]
        return lien

class case:
    def __init__(self, id, rect, co, ligne) -> None:
        self.id = id
        self.ligne = ligne
        self.cd = 10
        self.anim_normal = None
        self.anim_tir = None
        self.anim_cd = 20
        self.event = None
        self.used = None # L'id du paté present dessus.
        self.pos = rect
        self.lien = None
        self.co = co


class socket:
    def __init__(self, id, rect, lien) -> None:
        self.id = id
        self.nom = self.get_stat('nom')
        self.hitbox = rect
        self.lien = lien
        self.shoot_cd = 10
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