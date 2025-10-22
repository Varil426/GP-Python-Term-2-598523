import pygame
from Kierunek import Kierunek

class Waz(pygame.sprite.Sprite):
    def __init__(self):
        self.kierunek = Kierunek.GORA
        self.nowy_kierunek = self.kierunek
        self.oryginalny_obraz = pygame.image.load("images/head.png")
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, -90 * self.kierunek.value)
        self.rect = self.obraz.get_rect(center=(12*32+16, 9*32+16))

    def zmien_kierunek(self, kierunek: Kierunek):
        zmiena_mozliwa = True
        
        if kierunek == Kierunek.GORA and self.kierunek == Kierunek.DOL:
            zmiena_mozliwa = False
        
        if kierunek == Kierunek.PRAWO and self.kierunek == Kierunek.LEWO:
            zmiena_mozliwa = False

        if kierunek == Kierunek.DOL and self.kierunek == Kierunek.GORA:
            zmiena_mozliwa = False

        if kierunek == Kierunek.LEWO and self.kierunek == Kierunek.PRAWO:
            zmiena_mozliwa = False

        if zmiena_mozliwa:
            self.nowy_kierunek = kierunek

    def aktualizuj(self):
        self.kierunek = self.nowy_kierunek
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, (self.kierunek.value * -90))

        przesuniecie = (0, 0)

        match self.kierunek:
            case Kierunek.GORA:
                przesuniecie = (0, -32)
            case Kierunek.PRAWO:
                przesuniecie = (32, 0)
            case Kierunek.DOL:
                przesuniecie = (0, 32)
            case Kierunek.LEWO:
                przesuniecie = (-32, 0)

        self.rect.move_ip(przesuniecie[0], przesuniecie[1])