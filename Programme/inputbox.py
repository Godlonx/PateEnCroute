import pygame as pg
pg.font.init()




class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.COLOR_INACTIVE = pg.Color('lightskyblue3')
        self.COLOR_ACTIVE = pg.Color('dodgerblue2')
        self.rect = pg.Rect(x, y, w, h)
        self.font=pg.font.Font('../Font/pixelised.ttf',32)
        self.color = self.COLOR_INACTIVE
        self.text = text
        self.id = 0
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pg.K_RETURN or event.key == pg.K_ESCAPE or event.key == pg.K_TAB:
                    pass
                elif len(self.text) <= 9:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, 'white')




    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        pg.draw.rect(screen, (0,0,0), self.rect)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)