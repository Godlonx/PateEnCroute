from sqlite3 import *
import pygame
from inputbox import InputBox
from plateau import Terrain

##### 720x1080 screen


'''

        self.XXXX = pygame.image.load('../Font/pate.png').convert_alpha()
        self.XXXX = pygame.transform.scale(self.XXXX, (500, 500))
        self.XXXX_hitbox = pygame.Rect(40, 330, 260, 90)

        
        screen.blit(self.XXXX, (0, 0))

'''

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(None, 40)
        self.drawed_first = True
        self.menu = 'title'
        
    def Draw_menu(self, num):
        if num == 'title':
            self.DrawTitle()
        elif num == 'account': # afficher le menu de choix des parties
            self.DrawAccount()   
        elif num == 'connect':
            self.input_pseudo.draw(self.screen)
        elif num == 'party':
            self.DrawParty()    
        elif num == 'almanach':
            self.DrawAlmanach()
        elif num == 'map_monde':
            # affiche les niveau dispo dans le monde choisis
            self.DrawMap_Monde()
        elif num == 'choix_pates':
            self.DrawPates()
        elif num == 'terrain':
            self.terrain.draw(self.screen)
        elif num == 'pause':
            self.DrawPause()

    def DrawTitle(self):
        if self.drawed_first:
            self.lien = '../Font/HUD/titre/sprite_0.png'
            self.drawed_first = False
        self.pate = pygame.image.load(self.lien).convert_alpha()
        self.pate = pygame.transform.scale(self.pate, (600, 450))
        
        self.fond2 = pygame.image.load('../Font/HUD/fond/Fond.png').convert()
        self.fond2 = pygame.transform.scale(self.fond2, (1080, 720))
        
        screen.blit(self.fond2, (0, 0))

        screen.blit(self.pate, (290, 110))
    

        #self.Titre = pygame.Rect(270, 50, 520, 150)
        #pygame.draw.rect(self.screen, (0, 0, 255), self.Titre)


        self.bouton_start = pygame.image.load('../Font/HUD/start/Start.png')
        self.bouton_start = pygame.transform.scale(self.bouton_start, (260, 260))
        self.bouton_start_hitbox = pygame.Rect(40, 330, 260, 90)
        
        self.bouton_quit = pygame.image.load('../Font/HUD/quit/Quit.png')
        self.bouton_quit = pygame.transform.scale(self.bouton_quit, (260, 260))
        self.bouton_quit_hitbox = pygame.Rect(780, 330, 260, 90)
        


        screen.blit(self.bouton_quit, (780, 250))
        screen.blit(self.bouton_start, (40, 250))
    
    def DrawAccount(self):
        self.fond = pygame.image.load('../Font/HUD/fond/Fond.png').convert()
        self.fond = pygame.transform.scale(self.fond, (1080, 720))
        
        screen.blit(self.fond, (0, 0))
        
        
        self.title = pygame.Rect(190, 20 , 1080-380, 70)
        pygame.draw.rect(self.screen, (35, 39, 42) , self.title)
        
        
        self.bouton_retour = pygame.image.load('../Font/HUD/button/sprite_leave_red0.png').convert_alpha()
        self.bouton_retour = pygame.transform.scale(self.bouton_retour, (50, 50))
        self.bouton_retour_hitbox = pygame.Rect(20, 20, 50, 50)
        
        
        screen.blit(self.bouton_retour, (20, 20))
        
        sqliteConnection = connect('../Documents/StatsPlayers.db')
        cursor = sqliteConnection.cursor()
        cursor.execute("SELECT id From players")
        info = cursor.fetchall()
        
        
        
        if info != None and (1,) in info:

            self.save1 = pygame.image.load('../Font/HUD/party/case choix de parties.png').convert_alpha()
            self.save1 = pygame.transform.scale(self.save1, (210, 500))
            screen.blit(self.save1, (120, 140))
            
            ## sprite_continue0.png
            
            self.continue1 = pygame.image.load('../Font/HUD/button/sprite_continue0.png').convert_alpha()
            self.continue1 = pygame.transform.scale(self.continue1, (170, 50))
            self.continue1_hitbox = pygame.Rect(140, 570, 170, 50)
            screen.blit(self.continue1, (140, 570))
            
            
            self.delete1 = pygame.image.load('../Font/HUD/poubelle/sprite_poubelle_rouge0.png').convert_alpha()
            self.delete1 = pygame.transform.scale(self.delete1, (40, 40))
            self.delete1_hitbox = pygame.Rect(280, 150, 40, 40)
    
            screen.blit(self.delete1, (280, 150))
            
            self.create1 = None
        else:
            self.create1 = pygame.image.load('../Font/HUD/plus/sprite_plus0.png')
            self.create1_fond = pygame.Rect(215, 380, 20, 20)
            pygame.draw.rect(self.screen, (0, 0, 0), self.create1_fond)
            screen.blit(self.create1, (217, 382))
            
        if info != None and (2,) in info:
            self.save2 = pygame.image.load('../Font/HUD/party/case choix de parties.png').convert_alpha()
            self.save2 = pygame.transform.scale(self.save2, (210, 500))
            screen.blit(self.save2, (430, 140))
            
            ##
            
            self.continue2 = pygame.image.load('../Font/HUD/button/sprite_continue0.png').convert_alpha()
            self.continue2 = pygame.transform.scale(self.continue2, (170, 50))
            self.continue2_hitbox = pygame.Rect(450, 570, 170, 50)
            screen.blit(self.continue1, (450, 570))
            
            
            self.delete2 = pygame.image.load('../Font/HUD/poubelle/sprite_poubelle_rouge0.png').convert_alpha()
            self.delete2 = pygame.transform.scale(self.delete2, (40, 40))
            self.delete2_hitbox = pygame.Rect(590, 150, 40, 40)
    
            screen.blit(self.delete2, (590, 150))
            
            self.create2 = None
        else:
            self.create2 = pygame.image.load('../Font/HUD/plus/sprite_plus0.png')
            self.create2_fond = pygame.Rect(522, 380, 20, 20)
            pygame.draw.rect(self.screen, (0, 0, 0), self.create2_fond)
            screen.blit(self.create2, (524, 382))
            
        if info != None and (3,) in info:
            self.save3 = pygame.image.load('../Font/HUD/party/case choix de parties.png').convert_alpha()
            self.save3 = pygame.transform.scale(self.save3, (210, 500))
            screen.blit(self.save3, (740,140))
            
            ##
            
            self.continue3 = pygame.image.load('../Font/HUD/button/sprite_continue0.png').convert_alpha()
            self.continue3 = pygame.transform.scale(self.continue3, (170, 50))
            self.continue3_hitbox = pygame.Rect(760, 570, 170, 50)
            screen.blit(self.continue1, (760, 570))
            
            
            self.delete3 = pygame.image.load('../Font/HUD/poubelle/sprite_poubelle_rouge0.png').convert_alpha()
            self.delete3 = pygame.transform.scale(self.delete3, (40, 40))
            self.delete3_hitbox = pygame.Rect(900, 150, 40, 40)
    
            screen.blit(self.delete3, (900, 150))
            
            
            self.create3 = None
        else:
            self.create3 = pygame.image.load('../Font/HUD/plus/sprite_plus0.png')
            self.create3_fond = pygame.Rect(839, 380, 20, 20)
            pygame.draw.rect(self.screen, (0, 0, 0), self.create3_fond)
            screen.blit(self.create3, (841, 382))

    def DrawRegister(self, account):
        self.fond = pygame.Rect(390, 210, 300, 300)
        pygame.draw.rect(self.screen, (44, 47, 51), self.fond)
        
        self.fond = pygame.Rect(390, 210, 300, 300)
        pygame.draw.rect(self.screen, (0, 0, 0), self.fond, 2)
    
        
        self.bouton_retour = pygame.image.load('../Font/HUD/button/sprite_button_x_red0.png')
        self.bouton_retour = pygame.transform.scale(self.bouton_retour, (50, 50))
        self.bouton_retour_hitbox = pygame.Rect(620, 230, 50, 50)

        
        screen.blit(self.bouton_retour, (620, 230))

        
        self.input_pseudo = InputBox(440, 360, 200, 50) # X, Y, Longeur, Hauteur
        
        self.entree = pygame.image.load('../Font/HUD/button/sprite_continue0.png').convert_alpha()
        self.entree = pygame.transform.scale(self.entree, (200, 50))
        self.entree_hitbox = pygame.Rect(440, 425, 200, 50)
        screen.blit(self.entree, (440, 425))
        
        self.entree = pygame.Rect(440, 425, 200, 50)
        pygame.draw.rect(self.screen,(0, 255, 0), self.entree)
        

        if account == 1:
            self.input_pseudo.id = 1
        elif account == 2:
            self.input_pseudo.id = 2
        else:
            self.input_pseudo.id = 3

    def DrawParty(self):
        self.fond = pygame.Rect(0, 0, 1080, 720)
        pygame.draw.rect(self.screen, (44, 47, 51), self.fond)

        self.Titre = pygame.Rect(270, 50, 520, 150)
        pygame.draw.rect(self.screen, (0, 0, 255), self.Titre)

        self.bouton_start = pygame.image.load('../Font/HUD/start/Start.png')
        self.bouton_start = pygame.transform.scale(self.bouton_start, (260, 260))
        self.bouton_start_hitbox = pygame.Rect(423, 247, 234, 128)
        
        self.bouton_almanach = pygame.Rect(410, 400, 260, 90)
        pygame.draw.rect(self.screen, (50, 150, 50), self.bouton_almanach)

        self.bouton_stats = pygame.Rect(410, 540, 260, 90)
        pygame.draw.rect(self.screen, (250, 150, 50), self.bouton_stats)

        self.bouton_retour = pygame.Rect(20, 20, 50, 50)
        pygame.draw.rect(self.screen,(255, 0, 50), self.bouton_retour)
               
        screen.blit(self.bouton_start, (410, 180))

    def DrawMap_Monde(self):
        #self.fond = pygame.Rect(0, 0, 1080, 720)
        #pygame.draw.rect(self.screen, (44, 47, 51), self.fond)

        #self.Name = pygame.Rect()

        self.image = pygame.image.load('../Font/HUD/monde_0.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (1080, 720))
        screen.blit(self.image, (0,0))
        
        self.bouton_retour = pygame.Rect(20, 20, 50, 50)
        pygame.draw.rect(self.screen,(255, 0, 50), self.bouton_retour)

        self.co_lvl = [(100, 244), (295, 397), (490, 244), (685, 397), (880, 244)]

        self.inf_lvl = 4

        self.lvl = pygame.Rect(self.co_lvl[self.inf_lvl][0], self.co_lvl[self.inf_lvl][1], 100, 100)
        pygame.draw.rect(self.screen, (0,255,255), self.lvl)

    def DrawPates(self):
        # tab de 6x7
        self.fond = pygame.Rect(0, 0, 1080, 720)
        pygame.draw.rect(self.screen, (44, 47, 51), self.fond)
        self.choix = pygame.Rect(20, 20, 640 , 680)
        pygame.draw.rect(self.screen, (0, 0, 0), self.choix)
        

        if self.drawed_first:
            self.pates_choisis = [1,2,3,4,5,6]
            self.pates = {}
            n = 0
            for i in range(7):
                for j in range(6):
                    # 95 par ? avec 10 d'ecart en x et ? d'ecart en y
                    n += 1
                    self.pates[f'pate{n}'] = [pygame.Rect(30+j*105, 130+i*80, 95, 70),n, (0,255,255)]
            self.drawed_first = False
            
                
        for pate in self.pates.keys():
            pygame.draw.rect(self.screen, self.pates[pate][2], self.pates[pate][0])

        if len(self.pates_choisis) == 6:
            self.start = pygame.Rect(720, 600, 250, 80)
            pygame.draw.rect(self.screen, (0, 255, 0), self.start)
            
            

        self.undo =  pygame.Rect(680, 20, 75, 75)
        pygame.draw.rect(self.screen, (255, 0, 0), self.undo)

        self.retour = pygame.Rect(850, 20, 75, 75)
        pygame.draw.rect(self.screen, (255, 0, 255), self.retour)

        self.z_choisis = pygame.Rect(20, 20, 640, 90)

        pygame.draw.rect(self.screen, (0, 0, 0), self.z_choisis)
        self.pates_choix = {}
        
        self.numtest = self.font.render('1', True, (0, 0, 0))

        for i in range(len(self.pates_choisis)):
            self.pates_choix[f'pate{i}'] = pygame.Rect(30 + i*105, 30, 95, 70)
            pygame.draw.rect(self.screen, (0, 255, 255), self.pates_choix[f'pate{i}'])
        
    def DrawAlmanach(self):
        if self.drawed_first:
            self.curseur = 0
            self.color_spe = 0
            self.color_pas = 5
            self.Part_plantes()
            self.Part_pates()
            self.drawed_first = False

        self.fond = pygame.Rect(0, 0, 1080, 720)
        pygame.draw.rect(self.screen, (44, 47, 51), self.fond)

        self.bouton_retour = pygame.image.load('../Font/HUD/button/sprite_leave_red0.png').convert_alpha()
        self.bouton_retour = pygame.transform.scale(self.bouton_retour, (50, 50))
        self.bouton_retour_hitbox = pygame.Rect(20, 20, 50, 50)

        self.PatesMenu = pygame.Rect(120, 20, 400, 50)
        pygame.draw.rect(self.screen,(61, 195, 219), self.PatesMenu)

        self.PlantesMenu = pygame.Rect(560, 20, 400, 50)
        pygame.draw.rect(self.screen,(67, 196, 65), self.PlantesMenu)

        self.Info = pygame.Rect(100, 100, 880, 400)
        pygame.draw.rect(self.screen,(35, 39, 42), self.Info)

        self.Deroulant = pygame.Rect(50, 550, 980, 120)
        pygame.draw.rect(self.screen, (255, 255, 255), self.Deroulant, 2)

        self.gauche = pygame.Rect(70, 570, 40, 80)
        pygame.draw.rect(self.screen, (0,255,0), self.gauche)

        self.droite = pygame.Rect(970, 570, 40, 80)
        pygame.draw.rect(self.screen, (0, 255, 0), self.droite)


        screen.blit(self.bouton_retour, (20, 20))
        self.refresh()

    def Part_plantes(self):
        print('OK chgt plante')
        self.almanach_plantes = {}
        for i in range(1, 21):
            self.almanach_plantes[f'id{i}'] = pygame.Rect(150,565, 80, 90)

    def Part_pates(self):
        print('OK chgt pate')
        self.almanach_pates = {}
        for i in range(1, 21):
            self.almanach_pates[f'id{i}'] = pygame.Rect(150,565, 80, 90)

    def refresh(self, types = None):

        if types == 'plantes':
            print('plantes', self.color_spe , self.color_pas)
            for j in range(self.curseur, self.curseur+8):

                self.almanach_plantes[f'id{j}'] = pygame.Rect(150+(j-self.curseur)*100, 565, 80 ,90)

                pygame.draw.rect(self.screen, (self.color_spe + self.color_pas*j, self.color_spe + self.color_pas*j, self.color_spe + self.color_pas*j), self.almanach_plantes[f'id{j}'])


            print('refresh des plantes')

        else:
            print('pate', self.color_spe , self.color_pas)
            for j in range(self.curseur, self.curseur+8):

                self.almanach_pates[f'id{j}'] = pygame.Rect(150+(j-self.curseur)*100, 565, 80 ,90)

                pygame.draw.rect(self.screen, (self.color_spe + self.color_pas*j, self.color_spe + self.color_pas*j, self.color_spe + self.color_pas*j), self.almanach_pates[f'id{j}'])

            print('refresh des pates')
        print(self.curseur, "Valeur du curseur")

    def DrawPause(self):
        self.fond = pygame.Rect(290, 210, 500, 300)
        pygame.draw.rect(self.screen, (0, 0, 0), self.fond)
        
        self.fond_contour = pygame.Rect(290, 210, 500, 300)
        pygame.draw.rect(self.screen, (0, 255, 255), self.fond_contour, 2)

        self.abandon = pygame.Rect(390, 360, 100, 100)
        pygame.draw.rect(self.screen, (255, 0, 0), self.abandon)

        self.continuer = pygame.Rect(590, 360, 100, 100)
        pygame.draw.rect(self.screen, (0,255, 0), self.continuer)

    def connect(self, id):
        info = self.db("SELECT money, lvl, monde FROM players where id = ?", (id,))

    def gestion_events(self): # Permet de savoir se qu'il se passe sur le jeux, notamment les interaction par click de l'utilisateur
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.running = False

            if self.menu == 'title':
                if event.type == pygame.MOUSEBUTTONUP: # Savoir si on relache un boutton de souris
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.bouton_start_hitbox, event.pos):
                            self.menu = 'account'
                            self.drawed_first = True
                        if pygame.Rect.collidepoint(self.bouton_quit_hitbox, event.pos):
                            self.running = False
                        self.display()

            elif self.menu == 'account':
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.bouton_retour_hitbox, event.pos):
                            self.menu = 'title'
                            self.drawed_first = True
                        if self.create1 != None:
                            if pygame.Rect.collidepoint(self.create1_fond, event.pos):
                                self.DrawRegister(1)
                                self.menu =  'connect'
                                self.drawed_first = True
                        else:
                            if pygame.Rect.collidepoint(self.delete1_hitbox, event.pos):
                                self.db2('Delete From players where id=1')
                            elif pygame.Rect.collidepoint(self.continue1_hitbox, event.pos):
                                self.connect(1)
                                self.menu = 'party'
                                self.drawed_first = True
                        if self.create2 != None:
                            if pygame.Rect.collidepoint(self.create2_fond, event.pos):
                                self.DrawRegister(2)
                                self.menu =  'connect'
                                self.drawed_first = True
                        else:
                            if pygame.Rect.collidepoint(self.delete2_hitbox, event.pos):
                                self.db2('Delete From players where id=2')
                            if pygame.Rect.collidepoint(self.continue2_hitbox, event.pos):
                                self.connect(2)
                                self.menu = 'party'
                                self.drawed_first = True
                        if self.create3 != None:
                            if pygame.Rect.collidepoint(self.create3_fond, event.pos):
                                self.DrawRegister(3)
                                self.menu =  'connect'
                                self.drawed_first = True
                        else:
                            if pygame.Rect.collidepoint(self.delete3_hitbox, event.pos):
                                self.db2('Delete From players where id=3')
                            if pygame.Rect.collidepoint(self.continue3_hitbox, event.pos):
                                self.connect(3)
                                self.menu = 'party'
                                self.drawed_first = True
                        self.display()

            elif self.menu == 'connect':
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONUP:
                    self.input_pseudo.handle_event(event)
                    self.input_pseudo.draw(self.screen)
                    self.display()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        text = self.input_pseudo.text
                        print(text, isinstance(text, str))
                        id = self.input_pseudo.id
                        self.db("Insert into players(id, pseudo, lvl, monde, money) VALUES(?, ?, ?, ?, ?)", (id, text, 1, 1, 0))
                        self.menu = 'party'
                        self.display()
                    
                        #Recup le psuedo, lance la fonction pour enrigstrer et initialiser les donné dans la BDD
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.input_pseudo.rect, event.pos):
                            self.input_pseudo.active = True
                        if pygame.Rect.collidepoint(self.bouton_retour_hitbox, event.pos):
                            self.menu = 'account'
                            self.drawed_first = True
                        if pygame.Rect.collidepoint(self.entree, event.pos) and len(self.input_pseudo.text) > 0:
                            text = self.input_pseudo.text
                            print(text, isinstance(text, str))
                            id = self.input_pseudo.id
                            self.db("Insert into players(id, pseudo, lvl, monde, money) VALUES(?, ?, ?, ?, ?)", (id, text, 1, 1, 0))
                            self.menu = 'party'
                            self.drawed_first = True
                        self.display()
            
            elif self.menu == 'party':
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.bouton_retour, event.pos):
                            self.menu = 'account'
                            self.drawed_first = True
                        if pygame.Rect.collidepoint(self.bouton_start_hitbox, event.pos):
                            self.menu = 'map_monde'
                            self.drawed_first = True
                        if pygame.Rect.collidepoint(self.bouton_almanach, event.pos):
                            self.menu = 'almanach'
                            self.drawed_first = True
                        self.display()
                            
            elif self.menu == 'map_monde':
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.bouton_retour, event.pos):
                            self.menu = 'account'
                            self.drawed_first = True
                        if pygame.Rect.collidepoint(self.lvl, event.pos):
                            self.menu = 'choix_pates'
                            self.drawed_first = True
                        
                        self.display()
            
            elif self.menu == 'choix_pates':
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.retour, event.pos):
                            self.menu = 'party'
                            self.drawed_first = True
                            self.display()
                        if len(self.pates_choisis) >= 1:
                            if pygame.Rect.collidepoint(self.undo, event.pos):
                                pates = self.pates_choisis.pop()
                                self.pates[f'pate{pates}'][2] = (0, 255, 255)
                                self.display()
                        if len(self.pates_choisis) < 6:
                            for pates in self.pates.keys():
                                if pygame.Rect.collidepoint(self.pates[pates][0], event.pos):
                                    if self.pates[pates][1] not in self.pates_choisis:
                                        self.pates[pates][2] = (153, 170, 181)
                                        self.pates_choisis.append(self.pates[pates][1])
                                        self.display()
                                        break
                        else:
                            if pygame.Rect.collidepoint(self.start, event.pos):
                                self.menu = 'terrain'
                                self.terrain = Terrain(self.pates_choisis)
                                self.drawed_first = True
                            self.display()
            
            elif self.menu == 'almanach':
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.gauche, event.pos) and self.curseur > 0:
                            self.curseur -= 1
                        if pygame.Rect.collidepoint(self.droite, event.pos) and self.curseur < 21:
                            self.curseur += 1
                        if pygame.Rect.collidepoint(self.bouton_retour_hitbox, event.pos):
                            self.menu = 'party'
                            self.drawed_first = True
                        if pygame.Rect.collidepoint(self.PatesMenu, event.pos):
                            print(10000000)
                            self.color_spe = 0
                            self.color_pas = 5
                            self.refresh('pates')
                        if pygame.Rect.collidepoint(self.PlantesMenu, event.pos):
                            print(20000000)
                            self.color_spe = 220
                            self.color_pas = -10
                            self.refresh('plantes')

                        self.display()
            
            elif self.menu == 'terrain':
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        t = self.terrain.gevent(event)
                        if t == 'pause':
                            self.menu = 'pause'
                            self.drawed_first = True
                        self.display()
            
            elif self.menu == 'pause':
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.continuer, event.pos):
                            self.menu = 'terrain'
                            self.drawed_first = True
                            self.display()
                        elif pygame.Rect.collidepoint(self.abandon, event.pos):
                            self.menu = 'party'
                            self.drawed_first = True
                            self.display()

    def display(self):
            # C'est ce qui permet d'afficher la fenetre
        self.Draw_menu(self.menu)
        pygame.display.flip()

    def db(self, request, data):
        sqliteConnection = connect('../Documents/StatsPlayers.db')
        cursor = sqliteConnection.cursor()
        cursor.execute(request, data)
        info = None
        if request[0] == "S":
            info = cursor.fetchall()
        sqliteConnection.commit()
        cursor.close()
        return info

    def db2(self, request):
        sqliteConnection = connect('../Documents/StatsPlayers.db')
        cursor = sqliteConnection.cursor()
        cursor.execute(request)
        sqliteConnection.commit()
        cursor.close()
    
    def anim(self, lien):
        tab = lien.split('/')
        temp = tab[4].split('_')
        temp2 = temp[1].split('.')
        tab[4] = temp[0]+ '_'+str((int(temp2[0])+1)%50)+'.png'
        lien = ''
        for i in tab:
            lien += i+'/'
        lien = lien[:len(lien)-1]
        return lien
    
    def run(self):
        self.display()
        p, n = 0, 0
        
        while self.running:
            if self.menu == 'title':
                n += 1
                if n%7 == 0:
                    self.lien = self.anim(self.lien)
                    self.display()
            if self.menu == 'terrain':
                p+= 1
                if p%10 == 0:
                    self.terrain.update_pate(self.screen)
            self.gestion_events()
            self.clock.tick(60)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption('Paté En Croute')
    game = Game(screen)
    game.run()

pygame.quit()
