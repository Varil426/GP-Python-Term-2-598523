import pygame
import stale

class Platforma(pygame.sprite.Sprite):
    def __init__(self):
        super(Platforma, self).__init__()
        self.obraz = pygame.image.load("images/pad.png")
        self.zresetuj_pozycje()
    
    def zresetuj_pozycje(self):
        self.rect = pygame.Rect(stale.SZEROKOSC_EKRANU / 2 - 70, stale.WYSOKOSC_EKRANU - 100, 140, 30)

    def ruszaj_platforma(self, wartosc):
        predkosc = 10
        self.rect.move_ip(wartosc * predkosc, 0)
        
        if self.rect.left <= 0:
            self.rect.x = 0

        if self.rect.right >= stale.SZEROKOSC_EKRANU:
            self.rect.x = stale.SZEROKOSC_EKRANU - 140