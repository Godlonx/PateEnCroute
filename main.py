import sqlite3
import pygame
import PlayerMob, start_game
from inputbox import InputBox


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.active = False

        self.text = ""
        

        self.menu = 1

        self.Titre = pygame.Rect(270, 50, 520, 150) 

        self.bouton_signin_hitbox = pygame.Rect(410, 500, 260, 90)

        self.account = 0

        self.input_active = False

        self.bouton_start = pygame.image.load('Start.png')
        self.bouton_start = pygame.transform.scale(self.bouton_start, (260, 260))
        self.bouton_start_hitbox = pygame.Rect(40, 280, 260, 260)

        self.bouton_quit = pygame.image.load('Quit.png')
        self.bouton_quit = pygame.transform.scale(self.bouton_quit, (260, 260))
        self.bouton_quit_hitbox = pygame.Rect(410, 605, 260, 90)

        self.bouton_skills_hitbox = pygame.Rect(780, 280, 260, 90)
 
        self.bouton_menu = pygame.Rect(1010, 20, 50, 50)

        self.fond = pygame.image.load('pate.png').convert_alpha()
        self.fond = pygame.transform.scale(self.fond, (500, 500))

        self.fond2 = pygame.image.load('fond.jpg').convert()
        self.fond2 = pygame.transform.scale(self.fond2, (1080, 720))


    def set_account(self, pseudo):
        self.player = PlayerMob.Player()
        self.player.get_account(pseudo)


    def DrawMainMenu(self):
        screen.blit(self.fond2, (0, 0))
        screen.blit(self.fond, (290, 110))

        self.Titre = pygame.Rect(270, 50, 520, 150)
        pygame.draw.rect(self.screen, (0, 0, 255), self.Titre)

        self.bouton_start = pygame.image.load('Start.png')
        self.bouton_start = pygame.transform.scale(self.bouton_start, (260, 260))
        screen.blit(self.bouton_start, (40, 250))

        self.bouton_skills = pygame.image.load('Skills.png')
        self.bouton_skills = pygame.transform.scale(self.bouton_skills, (260, 260))
        screen.blit(self.bouton_skills, (780, 250))

        self.bouton_quit = pygame.image.load('Quit.png')
        self.bouton_quit = pygame.transform.scale(self.bouton_quit, (260, 260))
        screen.blit(self.bouton_quit, (410, 525))

        self.bouton_signin = pygame.image.load('Sign_in.png')
        self.bouton_signin = pygame.transform.scale(self.bouton_signin, (260, 260))
        screen.blit(self.bouton_signin, (410, 425))



    def DrawGame(self, wave):
        party = start_game.StartGame()
        party.StartWave(wave)
        screen.blit(self.fond2, (0, 0))
        pygame.draw.rect(self.screen, (255, 0, 0), self.bouton_menu)

        # Afficher le monde
        # Afficher le "gold"
        # Afficher "les essences"
        # Afficher la vage


    def DrawSkillMenu(self):
        screen.blit(self.fond2, (0, 0))
        pygame.draw.rect(self.screen, (255, 0, 0), self.bouton_menu)

    def DrawSignInMenu(self):
        
        self.font = pygame.font.Font(None, 45)
        self.txt_surface = self.font.render(self.text, True, (0,0,0))
        self.input = pygame.Rect(145, 530, 765, 50)
        signscreen = pygame.Rect((1080/4)/2, 30, 785, 650)
        self.font2 = pygame.font.Font(None, 65)
        self.textplayer = 'Compte existant : '
        sqliteConnection = sqlite3.connect('StatsPlayers.db')
        cursor = sqliteConnection.cursor()
        request = """SELECT pseudo FROM Players"""
        cursor.execute(request)
        players = cursor.fetchall()
        for player in players:
            self.textplayer += player[0] + ', '
        self.txt_player = self.font.render(self.textplayer, True, (255, 255, 255))
        self.zoneplayer = pygame.Rect(145, 220, 765, 300)

        pygame.draw.rect(self.screen, (15, 5, 30), signscreen)

        pygame.draw.rect(self.screen, (255, 255, 255), self.input)
        screen.blit(self.txt_surface, (self.input.x+5, self.input.y+10))
        
        pygame.draw.rect(self.screen, (0, 0, 0), self.zoneplayer)
        screen.blit(self.txt_player, (self.zoneplayer.x+5, self.zoneplayer.y+10))
        
    def DrawSignOnMenu(self):
        signscreen = pygame.Rect((1080/4)/2, 30, 785, 650)
        pygame.draw.rect(self.screen, (50, 0, 80), signscreen)
        self.input = pygame.Rect(145, 530, 765, 50)
        pygame.draw.rect(self.screen, (50, 50, 50), self.input)
        self.input_hitbox = pygame.Rect(145, 530, 765, 50)

        self.font = pygame.font.Font(None, 45)
        self.txt_surface = self.font.render(self.text, True, (0,0,0))
        
        # Blit the rect.
        pygame.draw.rect(self.screen, (255, 255, 255), self.input)

    def gestion_events(self): # Permet de savoir se qu'il se passe sur le jeux, notamment les interaction par click de l'utilisateur
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                pass

            if self.menu == 1:
                if event.type == pygame.MOUSEBUTTONUP: # Savoir si on relache un boutton de souris
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.bouton_start_hitbox, event.pos) and self.account!=0:
                            self.menu = 2
                        if pygame.Rect.collidepoint(self.bouton_quit_hitbox, event.pos):
                            self.running = False
                        if pygame.Rect.collidepoint(self.bouton_skills_hitbox, event.pos):
                            self.menu = 3
                        if pygame.Rect.collidepoint(self.bouton_signin_hitbox, event.pos):
                            self.menu = 4
            elif self.menu == 2:
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.bouton_menu, event.pos):
                            self.menu = 1
            elif self.menu == 3:
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.bouton_menu, event.pos):
                            self.menu = 1
            elif self.menu == 4:
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.input, event.pos):
                            self.active = True
                        else:
                            self.active = False
                if self.active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.pseudo = self.text
                            print(self.pseudo)
                            self.text = ''
                            self.active = False
                        elif event.key == pygame.K_BACKSPACE:
                            self.text = self.text[:-1]
                        else:
                            self.text += event.unicode
            

    def display(self): # C'est ce qui permet d'afficher la fenetre
        if self.menu == 1: # c'est si on doit afficher le menu 
            self.DrawMainMenu()

        elif self.menu == 2: # Si c'est le 
            if self.account != 0:
                self.DrawGame(self.player.get_stat("wave"))

        elif self.menu == 3:
            self.DrawSkillMenu()
        
        elif self.menu == 4:
            self.DrawSignInMenu()
            
            

        pygame.display.flip()


    def run(self):
        while self.running:
            self.gestion_events()
            self.display()
            self.clock.tick(60)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption('Paté En Croute')
    game = Game(screen)
    game.run()

pygame.quit()
