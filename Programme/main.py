import sqlite3
import pygame
import PlayerMob, start_game
from inputbox import InputBox


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.menu = 1

        self.Titre = pygame.Rect(270, 50, 520, 150) 

        


    def DrawMainMenu(self):
        screen.blit(self.fond2, (0, 0))
        screen.blit(self.fond, (290, 110))

        self.Titre = pygame.Rect(270, 50, 520, 150)
        pygame.draw.rect(self.screen, (0, 0, 255), self.Titre)

        self.bouton_start = pygame.image.load('../Font/Start.png')
        self.bouton_start = pygame.transform.scale(self.bouton_start, (260, 260))
        self.bouton_start_hitbox = pygame.Rect(40, 280, 260, 260)
        screen.blit(self.bouton_start, (40, 250))

        self.bouton_skills = pygame.image.load('../Font/Skills.png')
        self.bouton_skills = pygame.transform.scale(self.bouton_skills, (260, 260))
        self.bouton_skills_hitbox = pygame.Rect(780, 280, 260, 90)
        screen.blit(self.bouton_skills, (780, 250))

        self.bouton_quit = pygame.image.load('../Font/Quit.png')
        self.bouton_quit = pygame.transform.scale(self.bouton_quit, (260, 260))
        self.bouton_quit_hitbox = pygame.Rect(410, 605, 260, 90)
        screen.blit(self.bouton_quit, (410, 525))
        
        self.bouton_menu = pygame.Rect(1010, 20, 50, 50)

        self.fond = pygame.image.load('../Font/pate.png').convert_alpha()
        self.fond = pygame.transform.scale(self.fond, (500, 500))

        self.fond2 = pygame.image.load('../Font/fond.jpg').convert()
        self.fond2 = pygame.transform.scale(self.fond2, (1080, 720))


    def DrawGame(self, wave):
        pass

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
                        if pygame.Rect.collidepoint(self.bouton_skills_hitbox, event.pos):
                            self.menu = 3

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
            
            
    def display(self): # C'est ce qui permet d'afficher la fenetre
        if self.menu == 1: # c'est si on doit afficher le menu 
            self.DrawMainMenu()

        elif self.menu == 2: # Si c'est le 
            self.DrawGame()

            

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
