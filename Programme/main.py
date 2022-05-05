from sqlite3 import *
import pygame
import PlayerMob, start_game
from inputbox import InputBox
from plateau import Terrain

##### 720x1080 screen

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.drawed_first = True
        self.menu = 'choix_pates'
    
    def Draw_menu(self, num):
        if num == 'Title':
            self.DrawTitle()
        elif num == 'account': # afficher le menu de choix des parties
            self.DrawAccount()   
        elif num == 'connect':
            self.input_pseudo.draw(self.screen)
        elif num == 'party':
            self.DrawParty()        
        elif num == 'map_monde':
            # affiche les niveau dispo dans le monde choisis
            self.DrawMap_Monde()
        elif num == 'choix_pates':
            self.DrawPates()
        elif num == 'terrain':
            self.terrain.draw(self.screen)
        elif num == 'pause':
            self.terrain.draw(self.screen)

    def DrawTitle(self):
        self.fond = pygame.image.load('../Font/pate.png').convert_alpha()
        self.fond = pygame.transform.scale(self.fond, (500, 500))

        self.fond2 = pygame.image.load('../Font/fond.jpg').convert()
        self.fond2 = pygame.transform.scale(self.fond2, (1080, 720))
        
        screen.blit(self.fond2, (0, 0))
        screen.blit(self.fond, (290, 110))
    
    
        self.Titre = pygame.Rect(270, 50, 520, 150)
        pygame.draw.rect(self.screen, (0, 0, 255), self.Titre)


        self.bouton_start = pygame.image.load('../Font/Start.png')
        self.bouton_start = pygame.transform.scale(self.bouton_start, (260, 260))
        self.bouton_start_hitbox = pygame.Rect(40, 330, 260, 90)
        
        self.bouton_quit = pygame.image.load('../Font/Quit.png')
        self.bouton_quit = pygame.transform.scale(self.bouton_quit, (260, 260))
        self.bouton_quit_hitbox = pygame.Rect(780, 330, 260, 90)
        


        screen.blit(self.bouton_quit, (780, 250))
        screen.blit(self.bouton_start, (40, 250))
    
    def DrawAccount(self):
        self.fond = pygame.Rect(0, 0, 1080, 720)
        pygame.draw.rect(self.screen, (44, 47, 51), self.fond)

        self.title = pygame.Rect(190, 20 , 1080-380, 70)
        pygame.draw.rect(self.screen, (35, 39, 42) , self.title)

        self.bouton_retour = pygame.Rect(20, 20, 50, 50)
        pygame.draw.rect(self.screen,(255, 0, 50), self.bouton_retour)

        self.save1 = pygame.Rect(120, 140, 210, 500)
        pygame.draw.rect(self.screen, (35, 39, 42) , self.save1)
        self.save2 = pygame.Rect(430, 140, 210, 500)
        pygame.draw.rect(self.screen, (35, 39, 42) , self.save2)
        self.save3 = pygame.Rect(740, 140, 210, 500)
        pygame.draw.rect(self.screen, (35, 39, 42) , self.save3)

        sqliteConnection = connect('../Documents/StatsPlayers.db')
        cursor = sqliteConnection.cursor()
        cursor.execute("SELECT id From players")
        info = cursor.fetchall()
        
        if info != None and (1,) in info:
            self.continue1 = pygame.Rect(120+20, 570, 170, 50)
            pygame.draw.rect(self.screen,(0, 255, 0), self.continue1)
            self.delete1 = pygame.Rect(120+170, 150, 30, 30)
            pygame.draw.rect(self.screen,(255, 0, 0), self.delete1)
            self.create1 = None
        else:
            self.create1 = pygame.Rect(140, 140+230, 170, 40)
            pygame.draw.rect(self.screen,(0, 0, 0), self.create1)

        if info != None and (2,) in info:
            self.continue2 = pygame.Rect(430+20, 570, 170, 50)
            pygame.draw.rect(self.screen,(0, 255, 0), self.continue2)
            self.delete2 = pygame.Rect(430+170, 150, 30, 30)
            pygame.draw.rect(self.screen,(255, 0, 0), self.delete2)
            self.create2 = None
        else:
            self.create2 = pygame.Rect(450, 140+230, 170, 40)
            pygame.draw.rect(self.screen,(0, 0, 0), self.create2)
            
        if info != None and (3,) in info:
            self.continue3 = pygame.Rect(740+20, 570, 170, 50)
            pygame.draw.rect(self.screen,(0, 255, 0), self.continue3)
            self.delete3 = pygame.Rect(740+170, 150, 30, 30)
            pygame.draw.rect(self.screen,(255, 0, 0), self.delete3)
            self.create3 = None
        else:
            self.create3 = pygame.Rect(760, 140+230, 170, 40)
            pygame.draw.rect(self.screen,(0, 0, 0), self.create3)

    def DrawRegister(self, account):
        self.fond = pygame.Rect(390, 210, 300, 300)
        pygame.draw.rect(self.screen, (44, 47, 51), self.fond)
        
        self.fond = pygame.Rect(390, 210, 300, 300)
        pygame.draw.rect(self.screen, (0, 0, 0), self.fond, 2)

        self.bouton_retour = pygame.Rect(620, 230, 50, 50)
        pygame.draw.rect(self.screen,(255, 0, 50), self.bouton_retour)
        
        self.input_pseudo = InputBox(440, 360, 200, 50) # X, Y, Longeur, Hauteur
        
        self.entree = pygame.Rect(440, 425, 200, 50)
        pygame.draw.rect(self.screen,(0, 255, 0), self.entree)
        

        if account == 1:
            self.input_pseudo.id = 1
        elif account == 2:
            self.input_pseudo.id = 2
        else:
            self.input_pseudo.id = 3
        ################## Faire le bouton entrer ##################

    def DrawParty(self):
        self.fond = pygame.Rect(0, 0, 1080, 720)
        pygame.draw.rect(self.screen, (44, 47, 51), self.fond)

        self.Titre = pygame.Rect(270, 50, 520, 150)
        pygame.draw.rect(self.screen, (0, 0, 255), self.Titre)

        self.bouton_start = pygame.image.load('../Font/Start.png')
        self.bouton_start = pygame.transform.scale(self.bouton_start, (260, 260))
        self.bouton_start_hitbox = pygame.Rect(410, 260, 260, 90)
        
        self.bouton_option = pygame.Rect(410, 400, 260, 90)
        pygame.draw.rect(self.screen, (50, 150, 50), self.bouton_option)

        self.bouton_stats = pygame.Rect(410, 540, 260, 90)
        pygame.draw.rect(self.screen, (250, 150, 50), self.bouton_stats)

        self.bouton_retour = pygame.Rect(20, 20, 50, 50)
        pygame.draw.rect(self.screen,(255, 0, 50), self.bouton_retour)
               
        screen.blit(self.bouton_start, (410, 180))

    def DrawMap_Monde(self):
        #self.fond = pygame.Rect(0, 0, 1080, 720)
        #pygame.draw.rect(self.screen, (44, 47, 51), self.fond)

        #self.Name = pygame.Rect()

        self.image = pygame.image.load('../Font/Plateau2.png').convert_alpha()
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
            self.pates_choisis = []
            self.pates = {}
            n = 0
            for i in range(7):
                for j in range(6):
                    # 95 par ? avec 10 d'ecart en x et ? d'ecart en y
                    n += 1
                    self.pates[f'pate{n}'] = [pygame.Rect(30+j*105, 130+i*80, 95, 70),n, (0,255,255)]
                
        for pate in self.pates.keys():
            pygame.draw.rect(self.screen, self.pates[pate][2], self.pates[pate][0])
        if len(self.pates_choisis) == 6:
            self.start = pygame.Rect(720, 600, 250, 80)
            pygame.draw.rect(self.screen, (0, 255, 0), self.start)
            
            

        self.undo =  pygame.Rect(680, 20, 50, 50)
        pygame.draw.rect(self.screen, (255, 0, 0), self.undo)

        self.z_choisis = pygame.Rect(20, 20, 640, 90)

        pygame.draw.rect(self.screen, (0, 0, 0), self.z_choisis)
        self.pates_choix = {}
        
        for i in range(len(self.pates_choisis)):
            self.pates_choix[f'pate{i}'] = pygame.Rect(30 + i*105, 30, 95, 70)
            pygame.draw.rect(self.screen, (0, 255, 255), self.pates_choix[f'pate{i}'])
        
        self.drawed_first = False
        
    def DrawAlmanach(self):
        self.fond = pygame.Rect(0, 0, 1080, 720)
        pygame.draw.rect(self.screen, (44, 47, 51), self.fond)
        
        self.bouton_retour = pygame.Rect(20, 20, 50, 50)
        pygame.draw.rect(self.screen,(255, 0, 50), self.bouton_retour)

        
        self.PatesMenu = pygame.Rect(120, 20, 400, 50)
        pygame.draw.rect(self.screen,(35, 39, 42), self.PatesMenu)
        
        self.PlantesMenu = pygame.Rect(560, 20, 400, 50)
        pygame.draw.rect(self.screen,(35, 39, 42), self.PlantesMenu)
        
        self.Info = pygame.Rect(100, 100, 880, 400)
        pygame.draw.rect(self.screen,(35, 39, 42), self.Info)
        
        self.Deroulant = pygame.Rect(50, 550, 980, 120)
        pygame.draw.rect(self.screen, (255, 255, 255), self.Deroulant, 2)
        
        self.Gauche = pygame.Rect(70, 570, 40, 80)
        pygame.draw.rect(self.screen, (0,255,0), self.Gauche)
        
        self.almanach = {}
        self.curseur = 0
        
        
        for i in range(1, 21):
            # a terminer
            self.almanach[f'id{i}'] = pygame.Rect(150+i*100,565, 80, 90)
            
        self.curseur = 5
            
        for j in range(self.curseur, self.curseur+9):
            pygame.draw.rect(self.screen, (0+10*i, 0+10*i, 0+10*i), self.almanach[f'id{i}'])
        
        self.Droite = pygame.Rect(970, 570, 40, 80)
        pygame.draw.rect(self.screen, (0, 255, 0), self.Droite)

    def connect(self, id):
        info = self.db("SELECT money, lvl, monde FROM players where id = ?", (id,))

    def gestion_events(self): # Permet de savoir se qu'il se passe sur le jeux, notamment les interaction par click de l'utilisateur
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.running = False

            if self.menu == 'Title':
                if event.type == pygame.MOUSEBUTTONUP: # Savoir si on relache un boutton de souris
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.bouton_start_hitbox, event.pos):
                            self.menu = 'account'
                        if pygame.Rect.collidepoint(self.bouton_quit_hitbox, event.pos):
                            self.running = False
                        self.display()

            elif self.menu == 'account':
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.bouton_retour, event.pos):
                            self.menu = 'Title'
                        if self.create1 != None:
                            if pygame.Rect.collidepoint(self.create1, event.pos):
                                self.DrawRegister(1)
                                self.menu =  'connect'
                        else:
                            if pygame.Rect.collidepoint(self.delete1, event.pos):
                                self.db2('Delete From players where id=1')
                            elif pygame.Rect.collidepoint(self.continue1, event.pos):
                                self.connect(1)
                                self.menu = 'party'
                        if self.create2 != None:
                            if pygame.Rect.collidepoint(self.create2, event.pos):
                                self.DrawRegister(2)
                                self.menu =  'connect'
                        else:
                            if pygame.Rect.collidepoint(self.delete2, event.pos):
                                self.db2('Delete From players where id=2')
                            if pygame.Rect.collidepoint(self.continue2, event.pos):
                                self.connect(2)
                                self.menu = 'party'
                        if self.create3 != None:
                            if pygame.Rect.collidepoint(self.create3, event.pos):
                                self.DrawRegister(3)
                                self.menu =  'connect'
                        else:
                            if pygame.Rect.collidepoint(self.delete3, event.pos):
                                self.db2('Delete From players where id=3')
                            if pygame.Rect.collidepoint(self.continue3, event.pos):
                                self.connect(3)
                                self.menu = 'party'
                        self.display()

            elif self.menu == 'connect':
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONUP:
                    self.input_pseudo.handle_event(event)
                    self.input_pseudo.draw(self.screen)
                    self.display()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
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
                        if pygame.Rect.collidepoint(self.bouton_retour, event.pos):
                            self.menu = 'account'
                        if pygame.Rect.collidepoint(self.entree, event.pos) and len(self.input_pseudo.text) > 0:
                            self.menu = 'party'
                        self.display()
            
            elif self.menu == 'party':
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.bouton_retour, event.pos):
                            self.menu = 'account'
                        if pygame.Rect.collidepoint(self.bouton_start_hitbox, event.pos):
                            self.menu = 'map_monde'
                        self.display()
                            
            elif self.menu == 'map_monde':
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.bouton_retour, event.pos):
                            self.menu = 'account'
                        if pygame.Rect.collidepoint(self.lvl, event.pos):
                            self.menu = 'choix_pates'
                        self.display()
            
            elif self.menu == 'choix_pates':
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
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
                            self.display()
            
            elif self.menu == 'terrain':
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.terrain.gevent(event)
                        

    def display(self):
            # C'est ce qui permet d'afficher la fenetre
        self.Draw_menu(self.menu)
        print('A')
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
    
    def run(self):
        self.display()
        while self.running:
            if self.menu == 'terrain':
                pass
            self.gestion_events()
            self.clock.tick(60)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption('Paté En Croute')
    game = Game(screen)
    game.run()

pygame.quit()
