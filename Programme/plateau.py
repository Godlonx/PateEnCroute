import pygame



class Terrain:
    def __init__(self):
        self.t_case = 100
        self.nb_case_X = 9
        self.nb_case_Y = 5
        self.tab_case = {}
        self.pates = [[],[],[],[],[],[]]

    def draw(self, screen):
        self.fond = pygame.Rect(0, 0, 1080, 720)
        pygame.draw.rect(screen, (44, 47, 51), self.fond)

        self.steaks_inf = pygame.Rect(10, 10, 100, 80)
        pygame.draw.rect(screen, (0, 0, 255), self.steaks_inf)

        self.pause = pygame.Rect(990, 10, 60, 60) # Button pause in game (option, quitter, reprendre)
        pygame.draw.rect(screen, (255, 0, 0), self.pause)

        self.wave_inf = pygame.Rect(900, 670, 150, 20) # penser à modifier la taille en fonction du nombre de wave
        pygame.draw.rect(screen, (0, 0, 255), self.wave_inf)

        for i in range(5):
            for j in range(9):
                self.tab_case[f'case{i}{j}'] = pygame.Rect(150+j*self.t_case, 150+i*self.t_case, self.t_case, self.t_case)
                pygame.draw.rect(screen, (0+j*4,255-(j+i)*6,0+i*4), self.tab_case[f'case{i}{j}'])

        print(self.tab_case)

        self.pate0 = pygame.Rect(120, 10, 105, 70)
        pygame.draw.rect(screen, (0,0,130), self.pate0)

        self.pate1 = pygame.Rect(120+1*105, 10, 105, 70)
        pygame.draw.rect(screen, (0,0,130+1*20), self.pate1)

        self.pate2 = pygame.Rect(120+2*105, 10, 105, 70)
        pygame.draw.rect(screen, (0,0,130+2*20), self.pate2)

        self.pate3 = pygame.Rect(120+3*105, 10, 105, 70)
        pygame.draw.rect(screen, (0,0,130+3*20), self.pate3)

        self.pate4 = pygame.Rect(120+4*105, 10, 105, 70)
        pygame.draw.rect(screen, (0,0,130+4*20), self.pate4)

        self.pate5 = pygame.Rect(120+5*105, 10, 105, 70)
        pygame.draw.rect(screen, (0,0,130+5*20), self.pate5)



    def Pause(self, screen):
        self.bouton_retour = pygame.Rect(465, 335, 50, 50)
        pygame.draw.rect(screen,(255, 0, 50), self.bouton_retour)

    def gevent(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if pygame.Rect.collidepoint(self.pate1, event.pos):
                    if self.pate1:
                        pass
                if pygame.Rect.collidepoint(self.pause, event.pos):
                    pass

