from sqlite3 import *
import pygame
from Player import Player
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
        pygame.font.init()
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(None, 40)
        self.drawed_first = True
        self.menu = 'choixmonde'
        
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
        elif num == 'choixmonde':
            self.DrawChoixMonde()

    def DrawTitle(self):
        if self.drawed_first:
            self.lien = '../Font/HUD/titre/sprite_0.png'
            self.drawed_first = False
        self.pate = pygame.image.load(self.lien).convert_alpha()
        self.pate = pygame.transform.scale(self.pate, (600, 450))
        
        self.fond2 = pygame.image.load('../Font/HUD/fond/Fond.png').convert()
        self.fond2 = pygame.transform.scale(self.fond2, (1080, 720))
        
        screen.blit(self.fond2, (0, 0))
        screen.blit(self.pate, (245, 110))

        self.bouton_start = pygame.image.load('../Font/HUD/start/Start.png')
        self.bouton_start = pygame.transform.scale(self.bouton_start, (260, 260))
        self.bouton_start_hitbox = pygame.Rect(53, 317, 235, 128)
        
        self.bouton_quit = pygame.image.load('../Font/HUD/quit/Quit.png')
        self.bouton_quit = pygame.transform.scale(self.bouton_quit, (260, 260))
        self.bouton_quit_hitbox = pygame.Rect(793, 317, 234, 128)

        screen.blit(self.bouton_start, (40, 250))
        screen.blit(self.bouton_quit, (780, 250))

    def DrawAccount(self):

        self.font_text = pygame.font.Font('../Font/pixelised.ttf', 30)
        self.ltlfont_text = pygame.font.Font('../Font/pixelised.ttf', 20)
        pos = [80, 75, 65, 55, 45, 35, 25, 15, 10, 0]

        self.fond = pygame.image.load('../Font/HUD/fond/fond n&b.png').convert()
        self.fond = pygame.transform.scale(self.fond, (1080, 720))
        
        screen.blit(self.fond, (0, 0))
        
        self.title = pygame.image.load('../Font/HUD/party/partitre.png').convert_alpha()
        self.title = pygame.transform.scale(self.title, (700, 70))
        screen.blit(self.title, (190, 20))
        
        self.toptext = pygame.font.Font('../Font/pixelised.ttf', 75)
        self.savetitle = self.toptext.render("Choose your file", True, (255,255,255))
        self.textw1 = self.toptext.render("World One", True, (119,80,29))
        screen.blit(self.savetitle, (200, 15))

        
        self.bouton_retour = pygame.image.load('../Font/HUD/button/sprite_leave_red0.png').convert_alpha()
        self.bouton_retour = pygame.transform.scale(self.bouton_retour, (40, 40))
        self.bouton_retour_hitbox = pygame.Rect(20, 20, 40, 40)
        
        
        screen.blit(self.bouton_retour, (20, 20))
        
        sqliteConnection = connect('../Documents/StatsPlayers.db')
        cursor = sqliteConnection.cursor()
        cursor.execute("SELECT id From players")
        info = cursor.fetchall()
        
        
        
        if info != None and (1,) in info:

            self.save1 = pygame.image.load('../Font/HUD/party/case choix de parties.png').convert_alpha()
            self.save1 = pygame.transform.scale(self.save1, (210, 500))
            screen.blit(self.save1, (120, 140))
            self.pdp1 = pygame.image.load('../Font/HUD/party/pdp.png').convert_alpha()
            self.pdp1 = pygame.transform.scale(self.pdp1, (108, 99))
            screen.blit(self.pdp1, (170, 250))
            
            ## sprite_continue0.png

            
            self.continue1 = pygame.image.load('../Font/HUD/button/sprite_continue0.png').convert_alpha()
            self.continue1 = pygame.transform.scale(self.continue1, (130, 60))
            self.continue1_hitbox = pygame.Rect(160, 570, 130, 60)
            screen.blit(self.continue1, (160, 570))
            
            self.delete1 = pygame.image.load('../Font/HUD/poubelle/sprite_poubelle_rouge0.png').convert_alpha()
            self.delete1 = pygame.transform.scale(self.delete1, (40, 40))
            self.delete1_hitbox = pygame.Rect(280, 150, 40, 40)
            screen.blit(self.delete1, (280, 150))

            self.pseudo = self.db('Select pseudo From players where id = ?', (1,))[0][0]  # Une chr = 13 px
            
            self.text_1 = self.font_text.render(self.pseudo, True, (255,255,255))
            screen.blit(self.text_1, (135+ pos[len(self.pseudo)-1], 387))
            self.prof1= self.ltlfont_text.render('File 1:', True, (255,255,255))
            screen.blit(self.prof1, (195, 360))
            # 

            
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
            self.pdp2 = pygame.image.load('../Font/HUD/party/pdp.png').convert_alpha()
            self.pdp2 = pygame.transform.scale(self.pdp2, (108, 99))
            screen.blit(self.pdp2, (480, 250))
            
            ##
            
            self.continue2 = pygame.image.load('../Font/HUD/button/sprite_continue0.png').convert_alpha()
            self.continue2 = pygame.transform.scale(self.continue2, (130, 60))
            self.continue2_hitbox = pygame.Rect(470, 570, 130, 60)
            screen.blit(self.continue2, (470, 570))
            
            
            self.delete2 = pygame.image.load('../Font/HUD/poubelle/sprite_poubelle_rouge0.png').convert_alpha()
            self.delete2 = pygame.transform.scale(self.delete2, (40, 40))
            self.delete2_hitbox = pygame.Rect(590, 150, 40, 40)
    
            screen.blit(self.delete2, (590, 150))

            self.pseudo = self.db('Select pseudo From players where id = ?', (2,))[0][0]  # Une chr = 13 px
            
            self.text_2 = self.font_text.render(self.pseudo, True, (255,255,255))
            screen.blit(self.text_2, (445+ pos[len(self.pseudo)-1], 387))
            self.prof2 = self.ltlfont_text.render('File 2:', True, (255,255,255))
            screen.blit(self.prof2, (505, 360))
            
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
            self.pdp3 = pygame.image.load('../Font/HUD/party/pdp.png').convert_alpha()
            self.pdp3 = pygame.transform.scale(self.pdp3, (108, 99))
            screen.blit(self.pdp3, (790, 250))
            
            ##
            
            self.continue3 = pygame.image.load('../Font/HUD/button/sprite_continue0.png').convert_alpha()
            self.continue3 = pygame.transform.scale(self.continue3, (130, 60))
            self.continue3_hitbox = pygame.Rect(780, 570, 130, 60)
            screen.blit(self.continue3, (780, 570))
            
            
            self.delete3 = pygame.image.load('../Font/HUD/poubelle/sprite_poubelle_rouge0.png').convert_alpha()
            self.delete3 = pygame.transform.scale(self.delete3, (40, 40))
            self.delete3_hitbox = pygame.Rect(900, 150, 40, 40)
    
            screen.blit(self.delete3, (900, 150))
            
            self.pseudo = self.db('Select pseudo From players where id = ?', (3,))[0][0]  # Une chr = 13 px
            
            self.text_3 = self.font_text.render(self.pseudo, True, (255,255,255))
            screen.blit(self.text_3, (755+ pos[len(self.pseudo)-1], 387))
            self.prof3 = self.ltlfont_text.render('File 3:', True, (255,255,255))
            screen.blit(self.prof3, (815, 360))

            self.create3 = None
        else:
            self.create3 = pygame.image.load('../Font/HUD/plus/sprite_plus0.png')
            self.create3_fond = pygame.Rect(839, 380, 20, 20)
            pygame.draw.rect(self.screen, (0, 0, 0), self.create3_fond)
            screen.blit(self.create3, (841, 382))

    def DrawRegister(self, account):
        self.fondcase = pygame.image.load('../Font/HUD/party/case.png').convert_alpha()
        self.fondcase = pygame.transform.scale(self.fondcase, (300, 300))
        screen.blit(self.fondcase, (390,210))
        
        #self.fond = pygame.Rect(390, 210, 300, 300)
        #pygame.draw.rect(self.screen, (44, 47, 51), self.fond)
        #self.fond = pygame.Rect(390, 210, 300, 300)
        #pygame.draw.rect(self.screen, (0, 0, 0), self.fond, 2)
    
        
        self.bouton_retour = pygame.image.load('../Font/HUD/button/sprite_button_x_red0.png')
        self.bouton_retour = pygame.transform.scale(self.bouton_retour, (40,40))
        self.bouton_retour_hitbox = pygame.Rect(635, 230, 40,40)

        
        screen.blit(self.bouton_retour, (635, 230))

        
        self.input_pseudo = InputBox(440, 350, 200, 50) # X, Y, Longeur, Hauteur
        
        self.entree = pygame.image.load('../Font/HUD/button/accept.png').convert_alpha()
        self.entree = pygame.transform.scale(self.entree, (190, 70))
        self.entree_hitbox = pygame.Rect(440, 425, 190, 70)
        screen.blit(self.entree, (445, 425))

        self.quest = pygame.font.Font('../Font/pixelised.ttf', 30)
        self.quest = self.quest.render('What\'s your name?', True, (255,255,255))
        screen.blit(self.quest, (400, 300))
        
        
        

        if account == 1:
            self.input_pseudo.id = 1
            
        elif account == 2:
            self.input_pseudo.id = 2
        else:
            self.input_pseudo.id = 3

    def DrawParty(self):
        self.fond = pygame.image.load('../Font/HUD/fond/fond.png').convert()
        self.fond = pygame.transform.scale(self.fond, (1080, 720))
        screen.blit(self.fond, (0, 0))
        
        self.ready = pygame.image.load('../Font/HUD/party/ready.png').convert_alpha()
        self.ready = pygame.transform.scale(self.ready, (400, 110))
        screen.blit(self.ready, (340, 100))

        self.bouton_start = pygame.image.load('../Font/HUD/start/start1.png')
        self.bouton_start = pygame.transform.scale(self.bouton_start, (260, 130))
        self.bouton_start_hitbox = pygame.Rect(410, 250, 260, 130)
        
        self.bouton_almanach = pygame.image.load('../Font/HUD/button/almanach.png')
        self.bouton_almanach = pygame.transform.scale(self.bouton_almanach, (260, 130))
        self.bouton_almanach_hitbox = pygame.Rect(410, 400, 260, 130)
        

        '''
        A voir
        self.bouton_stats = pygame.Rect(410, 540, 260, 90)
        pygame.draw.rect(self.screen, (250, 150, 50), self.bouton_stats)
        '''
        self.bouton_retour = pygame.image.load('../Font/HUD/button/sprite_leave_red0.png').convert_alpha()
        self.bouton_retour = pygame.transform.scale(self.bouton_retour, (40, 40))
        self.bouton_retour_hitbox = pygame.Rect(20, 20, 40, 40)
        
        
        screen.blit(self.bouton_retour, (20, 20))
        screen.blit(self.bouton_start, (410, 250))
        screen.blit(self.bouton_almanach, (410, 400))

    def DrawMap_Monde(self):
        #self.fond = pygame.Rect(0, 0, 1080, 720)
        #pygame.draw.rect(self.screen, (44, 47, 51), self.fond)

        #self.Name = pygame.Rect()

        self.image = pygame.image.load('../Font/HUD/monde_0.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (1080, 720))
        screen.blit(self.image, (0,0))
        
        self.font_worldname = pygame.font.Font('../Font/pixelised.ttf', 100)
        self.textw = self.font_worldname.render("World 1", True, (255,255,255))
        self.textw1 = self.font_worldname.render("World 1", True, (119,80,29))
        screen.blit(self.textw1, (285, 45))
        screen.blit(self.textw, (280, 40))
        
        self.bouton_retour = pygame.transform.scale(self.bouton_retour, (40, 40))
        self.bouton_retour_hitbox = pygame.Rect(20, 20, 40, 40)
        
        
        screen.blit(self.bouton_retour, (20, 20))

        self.co_lvl = [(100, 244), (295, 397), (490, 244), (685, 397), (880, 244)]

        self.inf_lvl = self.player.lvl-1

        self.lvl = pygame.Rect(self.co_lvl[self.inf_lvl][0], self.co_lvl[self.inf_lvl][1], 100, 100)
        pygame.draw.rect(self.screen, (0,255,255), self.lvl)

    def DrawPates(self):
        # tab de 6x7
        self.fond = pygame.image.load('../Font/HUD/fond/fond.png').convert_alpha()
        self.fond = pygame.transform.scale(self.fond, (1080, 720))
        screen.blit(self.fond, (0, 0))
        self.fen = pygame.image.load('../Font/HUD/fond/fondnoir.png').convert_alpha()
        self.fen = pygame.transform.scale(self.fen, (640, 680))
        screen.blit(self.fen, (20, 20))


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

        #pygame.draw.rect(self.screen, (0, 0, 0), self.z_choisis)
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
        self.bouton_retour = pygame.transform.scale(self.bouton_retour, (40, 40))
        self.bouton_retour_hitbox = pygame.Rect(20, 20, 50, 50)

        self.PatesMenu = pygame.Rect(120, 20, 400, 50)
        pygame.draw.rect(self.screen,(61, 195, 219), self.PatesMenu)

        self.PlantesMenu = pygame.Rect(560, 20, 400, 50)
        pygame.draw.rect(self.screen,(67, 196, 65), self.PlantesMenu)

        self.Info = pygame.Rect(100, 100, 880, 400)
        pygame.draw.rect(self.screen,(35, 39, 42), self.Info)

        self.Deroulant = pygame.Rect(50, 550, 980, 120)
        pygame.draw.rect(self.screen, (255, 255, 255), self.Deroulant, 2)

        self.gauche = pygame.image.load('../Font/HUD/button/arrow_left.png').convert_alpha()
        self.gauche = pygame.transform.scale(self.gauche, (40, 80))
        self.gauche_hitbox = pygame.Rect(70, 570, 40, 80)


        self.droit = pygame.image.load('../Font/HUD/button/arrow_right.png').convert_alpha()
        self.droit = pygame.transform.scale(self.droit, (40, 80))
        self.droite_hitbox = pygame.Rect(970, 570, 40, 80)

        
        screen.blit(self.droit, (970, 570))
        screen.blit(self.gauche, (70, 570))
        screen.blit(self.bouton_retour, (20, 20))
        self.refresh()

    def DrawAffiche(self):
        pass

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
    
    def DrawChoixMonde(self):
        accredidation = {"1" : [2, 3], "2" : [4, 5], "3" : [5, 6], "4" : [7, 8], "5" : [7, 8], "6" : [7, 8], "7" : [9], "8" : [9]}

        self.font_text = pygame.font.Font('../Font/pixelised.ttf', 30)
        self.ltlfont_text = pygame.font.Font('../Font/pixelised.ttf', 20)
        pos = [80, 75, 65, 55, 45, 35, 25, 15, 10, 0]

        self.fond = pygame.image.load('../Font/HUD/fond/fond n&b.png').convert()
        self.fond = pygame.transform.scale(self.fond, (1080, 720))
        
        self.title = pygame.image.load('../Font/HUD/party/partitre.png').convert_alpha()
        self.title = pygame.transform.scale(self.title, (700, 70))
        
        self.toptext = pygame.font.Font('../Font/pixelised.ttf', 75)
        self.savetitle = self.toptext.render("Choose new world", True, (255,255,255))
        self.textw1 = self.toptext.render("World One", True, (119,80,29))

        self.case1 = pygame.image.load('../Font/HUD/party/case choix de parties.png').convert_alpha()
        self.case1 = pygame.transform.scale(self.case1, (350, 500))
        self.case2 = pygame.image.load('../Font/HUD/party/case choix de parties.png').convert_alpha()
        self.case2 = pygame.transform.scale(self.case2, (350, 500))

        screen.blit(self.fond, (0, 0))
        screen.blit(self.title, (190, 20))
        screen.blit(self.savetitle, (200, 15))
        screen.blit(self.case1, (120, 140))
        screen.blit(self.case2, (610, 140))
        
        self.monde = '1'

        suivant1 = accredidation[self.monde][0]
        suivant2 = accredidation[self.monde][1]

        
        self.gauchechoice = pygame.image.load(f"../Font/HUD/infomonde/{suivant1}.png").convert_alpha()
        self.gauchechoice = pygame.transform.scale(self.gauchechoice, (100, 100))

        
        self.droitechoice = pygame.image.load(f"../Font/HUD/infomonde/{suivant2}.png").convert_alpha()
        self.droitechoice = pygame.transform.scale(self.droiteechoice, (100, 100))
        
        screen.blit(self.gauchechoice, (130, 130))
        


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
                                self.player = Player(1)
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
                                self.player = Player(2)
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
                                self.player = Player(3)
                                self.menu = 'party'
                                self.drawed_first = True
                        self.display()

            elif self.menu == 'connect':
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONUP:
                    self.input_pseudo.handle_event(event)
                    self.input_pseudo.draw(self.screen)
                    self.display()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.menu = 'account'
                        self.drawed_first = True
                        self.display()
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        text = self.input_pseudo.text.upper()
                        print(text, isinstance(text, str))
                        id = self.input_pseudo.id
                        self.db("Insert into players(id, pseudo, lvl, monde, money) VALUES(?, ?, ?, ?, ?)", (id, text, 1, 1, 0))
                        self.player = Player(id)
                        print(self.player.monde, self.player.psuedo)
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
                        if pygame.Rect.collidepoint(self.entree_hitbox, event.pos) and len(self.input_pseudo.text) > 0:
                            text = self.input_pseudo.text
                            print(text, isinstance(text, str))
                            id = self.input_pseudo.id
                            self.db("Insert into players(id, pseudo, lvl, monde, money) VALUES(?, ?, ?, ?, ?)", (id, text, 1, 1, 0))
                            self.player = Player(id)
                            self.menu = 'party'
                            self.drawed_first = True
                        self.display()
            
            elif self.menu == 'party':
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.bouton_retour_hitbox, event.pos):
                            self.menu = 'account'
                            self.drawed_first = True
                        if pygame.Rect.collidepoint(self.bouton_start_hitbox, event.pos):
                            self.menu = 'map_monde'
                            self.drawed_first = True
                        if pygame.Rect.collidepoint(self.bouton_almanach_hitbox, event.pos):
                            self.menu = 'almanach'
                            self.drawed_first = True
                        self.display()
                            
            elif self.menu == 'map_monde':
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.bouton_retour_hitbox, event.pos):
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
                                self.terrain = Terrain(self.pates_choisis, 1)
                                self.terrain.first_draw(screen) 
                                self.drawed_first = True
                            self.display()
            
            elif self.menu == 'almanach':
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.gauche_hitbox, event.pos) and self.curseur > 0:
                            self.curseur -= 1
                        if pygame.Rect.collidepoint(self.droite_hitbox, event.pos) and self.curseur < 21:
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
                            self.color_spe = 220
                            self.color_pas = -10
                            self.refresh('plantes')
                            print(20000000)

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
        p, n, v = 0, 0, 0
        
        while self.running:
            if self.menu == 'title':
                n += 1
                if n%7 == 0:
                    self.lien = self.anim(self.lien)
                    self.display()
            if self.menu == 'terrain':
                p+= 1
                if p%15 == 0:
                    v += 1
                    if v%8 == 0:
                        self.terrain.add_enemy()
                    self.terrain.update_terrain(self.screen)
            self.gestion_events()
            self.clock.tick(60)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption('Paté En Croute')
    game = Game(screen)
    game.run()

pygame.quit()