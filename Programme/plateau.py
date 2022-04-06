import pygame



class Terrain:
    def __init__(self):
        self.t_case = 100
        self.nb_case_X = 9
        self.nb_case_Y = 5
        
    def draw(self, screen):
                self.fond = pygame.Rect(0, 0, 1080, 720)
                pygame.draw.rect(screen, (44, 47, 51), self.fond)
                
                self.steaks_inf = pygame.Rect(10, 10, 100, 80)
                pygame.draw.rect(screen, (0, 0, 255), self.steaks_inf)
                
                self.pause_inf = pygame.Rect(990, 10, 60, 60) # Button pause in game (option, quitter, reprendre)
                pygame.draw.rect(screen, (255, 0, 0), self.pause_inf)
                
                self.wave_inf = pygame.Rect(900, 670, 150, 20) # penser à modifier la taille en fonction du nombre de wave
                pygame.draw.rect(screen, (0, 0, 255), self.wave_inf)
                
                for i in range(5):
                    for j in range(9):
                        self.case = pygame.Rect(150+j*self.t_case, 150+i*self.t_case, self.t_case, self.t_case)
                        pygame.draw.rect(screen, (0+j*4,255-(j+i)*6,0+i*4), self.case)
                
                for k in range(6):
                    self.case = pygame.Rect(120+k*105, 10, 105, 70)
                    pygame.draw.rect(screen, (0,0,130+k*20), self.case)
    
    def gevent(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if pygame.Rect.collidepoint(self.pate1, event.pos):
                    if self.pate1.usable:
                        
        