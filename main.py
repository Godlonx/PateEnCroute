import pygame


class PateEnCroute:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.menu = 1
        self.Titre = pygame.Rect(270, 50, 520, 150)
        self.bouton_start = pygame.image.load('Start.png')
        self.bouton_start = pygame.transform.scale(self.bouton_start, (260, 260))
        self.bouton_start_hitbox = pygame.Rect(40, 280, 260, 260)
        self.bouton_arbre = pygame.Rect(780, 280, 260, 90)
        self.bouton_quit_hitbox = pygame.Rect(410, 500, 260, 90)
        self.bouton_quit = pygame.image.load('Quit.png')
        self.bouton_quit = pygame.transform.scale(self.bouton_quit, (260, 260))
        self.bouton_menu = pygame.Rect(1010, 20, 50, 50)
        self.fond = pygame.image.load('pate.png').convert_alpha()
        self.fond = pygame.transform.scale(self.fond, (500, 500))
        self.fond2 = pygame.image.load('fond.jpg').convert()
        self.fond2 = pygame.transform.scale(self.fond2, (1080, 720))

    def affiche_menu_principale(self):
        screen.blit(self.fond2, (0, 0))
        screen.blit(self.fond, (290, 110))
        self.Titre = pygame.Rect(270, 50, 520, 150)
        pygame.draw.rect(self.screen, (0, 0, 255), self.Titre)
        screen.blit(self.bouton_start, (40, 200))
        pygame.draw.rect(self.screen, (255, 0, 0), self.bouton_arbre)
        screen.blit(self.bouton_quit, (410, 450))

    def affiche_menu_jeu(self):
        screen.blit(self.fond2, (0, 0))
        self.Titre = pygame.Rect(10, 10, 100, 30)
        pygame.draw.rect(self.screen, (255, 0, 0), self.bouton_menu)
        pygame.draw.rect(self.screen, (255, 0, 255), self.Titre)
    def affiche_menu_arbre(self):
        screen.blit(self.fond2, (0, 0))

    def gestion_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                pass

            if self.menu == 1:
                self.bouton_start = pygame.image.load('Start.png')
                self.bouton_start = pygame.transform.scale(self.bouton_start, (260, 260))
                self.bouton_quit = pygame.image.load('Quit.png')
                self.bouton_quit = pygame.transform.scale(self.bouton_quit, (260, 260))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.bouton_start_hitbox, event.pos):
                            self.bouton_start = pygame.image.load('StartNeon.png').convert_alpha()
                            self.bouton_start = pygame.transform.scale(self.bouton_start, (260, 260))
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.bouton_start_hitbox, event.pos):
                            self.menu = 2
                        if pygame.Rect.collidepoint(self.bouton_quit_hitbox, event.pos):
                            self.running = False
                        if pygame.Rect.collidepoint(self.bouton_arbre, event.pos):
                            self.menu = 3
            elif self.menu == 2:
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if pygame.Rect.collidepoint(self.bouton_menu, event.pos):
                            self.menu = 1
            elif self.menu == 3:
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        pass

    def update(self):
        pass

    def display(self):
        if self.menu == 1:
            self.affiche_menu_principale()
        elif self.menu == 2:
            self.affiche_menu_jeu()
        elif self.menu == 3:
            self.affiche_menu_arbre()
        pygame.display.flip()

    def run(self):
        while self.running:
            self.gestion_events()
            self.update()
            self.display()
            self.clock.tick(144)


pygame.init()
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption('Paté En Croute')
game = PateEnCroute(screen)
game.run()

pygame.quit()
