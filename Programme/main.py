from sqlite3 import *
import pygame
import PlayerMob, start_game
from inputbox import InputBox
from plateau import Terrain

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.menu = 'Title'
    
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
            self.DrawMap_Monde()
            # affiche les niveau dispo dans le monde choisis
            pass
        elif num == 'terrain':
            self.terrain = Terrain()
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
        self.bouton_quit_hitbox = pygame.Rect(410, 605, 260, 90)
        


        screen.blit(self.bouton_quit, (410, 525))
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
            self.copy1 = pygame.Rect(120+130, 150, 30, 30)
            pygame.draw.rect(self.screen,(0, 0, 255), self.copy1)
            self.delete1 = pygame.Rect(120+170, 150, 30, 30)
            pygame.draw.rect(self.screen,(255, 0, 0), self.delete1)
            self.create1 = None
        else:
            self.create1 = pygame.Rect(140, 140+230, 170, 40)
            pygame.draw.rect(self.screen,(0, 0, 0), self.create1)

        if info != None and (2,) in info:
            self.continue2 = pygame.Rect(430+20, 570, 170, 50)
            pygame.draw.rect(self.screen,(0, 255, 0), self.continue2)
            self.copy2 = pygame.Rect(430+130, 150, 30, 30)
            pygame.draw.rect(self.screen,(0, 0, 255), self.copy2)
            self.delete2 = pygame.Rect(430+170, 150, 30, 30)
            pygame.draw.rect(self.screen,(255, 0, 0), self.delete2)
            self.create2 = None
        else:
            self.create2 = pygame.Rect(450, 140+230, 170, 40)
            pygame.draw.rect(self.screen,(0, 0, 0), self.create2)
            
        if info != None and (3,) in info:
            self.continue3 = pygame.Rect(740+20, 570, 170, 50)
            pygame.draw.rect(self.screen,(0, 255, 0), self.continue3)
            self.copy3 = pygame.Rect(740+130, 150, 30, 30)
            pygame.draw.rect(self.screen,(0, 0, 255), self.copy3)
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
        
        self.input_pseudo = InputBox(440, 400, 200, 50) # X, Y, Longeur, Hauteur

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

        self.bouton_start = pygame.image.load('../Font/Start.png')
        self.bouton_start = pygame.transform.scale(self.bouton_start, (260, 260))
        self.bouton_start_hitbox = pygame.Rect(410, 260, 260, 260)
        
        self.bouton_option = pygame.Rect(410, 400, 260, 90)
        pygame.draw.rect(self.screen, (50, 150, 50), self.bouton_option)

        self.bouton_stats = pygame.Rect(410, 540, 260, 90)
        pygame.draw.rect(self.screen, (250, 150, 50), self.bouton_stats)
        
        
        screen.blit(self.bouton_start, (410, 180))

    def DrawMap_Monde(self):
        #self.fond = pygame.Rect(0, 0, 1080, 720)
        #pygame.draw.rect(self.screen, (44, 47, 51), self.fond)

        #self.Name = pygame.Rect()

        self.image = pygame.image.load('../Font/Plateau1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (1080, 720))
        screen.blit(self.image, (0,0))

    def connect(self, id):
        

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
                        if self.create2 != None:
                            if pygame.Rect.collidepoint(self.create2, event.pos):
                                self.DrawRegister(2)
                                self.menu =  'connect'
                        else:
                            if pygame.Rect.collidepoint(self.delete2, event.pos):
                                self.db2('Delete From players where id=2')
                        if self.create3 != None:
                            if pygame.Rect.collidepoint(self.create3, event.pos):
                                self.DrawRegister(3)
                                self.menu =  'connect'
                        else:
                            if pygame.Rect.collidepoint(self.delete3, event.pos):
                                self.db2('Delete From players where id=3')

            elif self.menu == 'connect':
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONUP:
                    self.input_pseudo.handle_event(event)
                    self.input_pseudo.draw(self.screen)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        text = self.input_pseudo.text
                        print(text, isinstance(text, str))
                        id = self.input_pseudo.id
                        self.db("Insert into players(id, pseudo) VALUES(?, ?)", (id, text))
                        self.menu = 'party'
                        
                        #Recup le psuedo, lance la fonction pour enrigstrer et initialiser les donné dans la BDD
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.input_pseudo.rect, event.pos):
                            self.input_pseudo.active = True
                        if pygame.Rect.collidepoint(self.bouton_retour, event.pos):
                            self.menu = 'account'
            
            elif self.menu == 'party':
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.bouton_start_hitbox, event.pos):
                            self.menu = 'map_monde'

    def display(self):
            # C'est ce qui permet d'afficher la fenetre
        self.Draw_menu(self.menu)
        pygame.display.flip()

    def db(self, request, data, type=None):
        sqliteConnection = connect('../Documents/StatsPlayers.db')
        cursor = sqliteConnection.cursor()
        info = None
        cursor.execute(request, data)
        if type == "recup":
            info = cursor.fetchall()
            return info
        sqliteConnection.commit()
        cursor.close()
    
    def db2(self, request):
        sqliteConnection = connect('../Documents/StatsPlayers.db')
        cursor = sqliteConnection.cursor()
        cursor.execute(request)
        sqliteConnection.commit()
        cursor.close()
    
    def run(self):
        while self.running:
            self.display()
            self.gestion_events()
            self.clock.tick(60)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption('Paté En Croute')
    game = Game(screen)
    game.run()

pygame.quit()
