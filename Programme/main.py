from sqlite3 import *
import pygame
import PlayerMob, start_game
from inputbox import InputBox


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.menu = 4
        self.affiche = 0
        self.t_case = 100

    
    def Draw_menu(self, num):
        if num == 1:
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
            self.bouton_start_hitbox = pygame.Rect(40, 280, 260, 260)
            
            self.bouton_quit = pygame.image.load('../Font/Quit.png')
            self.bouton_quit = pygame.transform.scale(self.bouton_quit, (260, 260))
            self.bouton_quit_hitbox = pygame.Rect(410, 605, 260, 90)
    
            
        
            screen.blit(self.bouton_quit, (410, 525))
            screen.blit(self.bouton_start, (40, 250))

        elif num == 2: # afficher le menu de choix des parties
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
            info = cursor.fetchone()
            
            if info != None:
                if 1 in info:
                    self.continue1 = pygame.Rect(120+20, 570, 170, 50)
                    pygame.draw.rect(self.screen,(0, 255, 0), self.continue1)
                    self.copy1 = pygame.Rect(120+130, 150, 30, 30)
                    pygame.draw.rect(self.screen,(0, 0, 255), self.copy1)
                    self.delete1 = pygame.Rect(120+170, 150, 30, 30)
                    pygame.draw.rect(self.screen,(255, 0, 0), self.delete1)
            else:
                self.create1 = pygame.Rect(140, 140+230, 170, 40)
                pygame.draw.rect(self.screen,(0, 0, 0), self.create1)
    
            if info != None:
                if 2 in info:
                    self.continue2 = pygame.Rect(430+20, 570, 170, 50)
                    pygame.draw.rect(self.screen,(0, 255, 0), self.continue2)
                    self.copy2 = pygame.Rect(430+130, 150, 30, 30)
                    pygame.draw.rect(self.screen,(0, 0, 255), self.copy2)
                    self.delete2 = pygame.Rect(430+170, 150, 30, 30)
                    pygame.draw.rect(self.screen,(255, 0, 0), self.delete2)
            else:
                self.create2 = pygame.Rect(450, 140+230, 170, 40)
                pygame.draw.rect(self.screen,(0, 0, 0), self.create2)
                
            if info != None:
                if 3 in info:
                    self.continue3 = pygame.Rect(740+20, 570, 170, 50)
                    pygame.draw.rect(self.screen,(0, 255, 0), self.continue3)
                    self.copy3 = pygame.Rect(740+130, 150, 30, 30)
                    pygame.draw.rect(self.screen,(0, 0, 255), self.copy3)
                    self.delete3 = pygame.Rect(740+170, 150, 30, 30)
                    pygame.draw.rect(self.screen,(255, 0, 0), self.delete3)
            else:
                self.create3 = pygame.Rect(760, 140+230, 170, 40)
                pygame.draw.rect(self.screen,(0, 0, 0), self.create3)
            
            
            
            # delete 2
            
            # delete 3 
            
            
            
            sqliteConnection.commit()
            cursor.close()
    

        
        elif num == 3:
            self.input_pseudo3.draw(self.screen)
        
        elif num == 4:
            
            
            if self.affiche == 0:
                self.fond = pygame.Rect(0, 0, 1080, 720)
                pygame.draw.rect(self.screen, (44, 47, 51), self.fond)
                self.steaks_inf = pygame.Rect(10, 10, 60, 60)
                pygame.draw.rect(self.screen, (0, 0, 255), self.steaks_inf)
                self.wave_inf = pygame.Rect(900, 620, 100, 50)
                pygame.draw.rect(self.screen, (0, 0, 255), self.wave_inf)
                for i in range(5):
                    for j in range(9):
                        self.case = pygame.Rect(150+j*self.t_case, 150+i*self.t_case, self.t_case, self.t_case)
                        pygame.draw.rect(self.screen, (0+j*4,255-(j+i)*6,0+i*4), self.case)
            self.affiche = 1
            
        
#2,5 * en titre , 80 + 260 = 340 => 170 
        
    def DrawRegister(self):
        self.fond = pygame.Rect(0, 0, 1080, 720)
        pygame.draw.rect(self.screen, (44, 47, 51), self.fond)
        
        self.bouton_retour = pygame.Rect(20, 20, 50, 50)
        pygame.draw.rect(self.screen,(255, 0, 50), self.bouton_retour)
        
        self.input_pseudo3 = InputBox(100, 100, 200, 50)
        
        


    def gestion_events(self): # Permet de savoir se qu'il se passe sur le jeux, notamment les interaction par click de l'utilisateur
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.running = False
            

            if self.menu == 1:
                if event.type == pygame.MOUSEBUTTONUP: # Savoir si on relache un boutton de souris
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.bouton_start_hitbox, event.pos):
                            self.menu = 2
                        if pygame.Rect.collidepoint(self.bouton_quit_hitbox, event.pos):
                            self.running = False

            elif self.menu == 2:
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.bouton_retour, event.pos):
                            self.menu = 1
                        if pygame.Rect.collidepoint(self.create3, event.pos):
                            self.DrawRegister()
                            self.menu = 3
            elif self.menu == 3:
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONUP:
                    self.input_pseudo3.handle_event(event)
                    self.input_pseudo3.draw(self.screen)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pass
                        #Recup le psuedo, lance la fonction pour enrigstrer et initialiser les donné dans la BDD
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.input_pseudo3.rect, event.pos):
                            self.input_pseudo3.active = True
                        if pygame.Rect.collidepoint(self.bouton_retour, event.pos):
                            self.menu = 2
                
            
    def display(self):
            # C'est ce qui permet d'afficher la fenetre
        self.Draw_menu(self.menu)
        
            
            

        pygame.display.flip()


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
