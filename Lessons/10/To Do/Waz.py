import pygame
import copy
from Kierunek import Kierunek
from Segment import Segment

class Waz(pygame.sprite.Sprite):
    def __init__(self):
        self.kierunek = Kierunek.GORA
        self.nowy_kierunek = self.kierunek
        self.oryginalny_obraz = pygame.image.load("images/head.png")
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, -90 * self.kierunek.value)
        self.rect = self.obraz.get_rect(center=(12*32+16, 9*32+16))
        self.ostatnia_pozycja = self.rect
        self.dodaj_segment = False
        self.segmenty = []

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

        self.ostatnia_pozycja = copy.deepcopy(self.rect)

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

        for i in range(len(self.segmenty)):
            if i == 0:
                self.segmenty[i].przesun(self.ostatnia_pozycja)
            else:
                self.segmenty[i].przesun(self.segmenty[i-1].ostatnia_pozycja)

        if self.dodaj_segment:
            nowy_segment = Segment()
            nowa_pozycja = None

            if len(self.segmenty) > 0:
                nowa_pozycja = copy.deepcopy(self.segmenty[-1].pozycja)
            else:
                nowa_pozycja = copy.deepcopy(self.ostatnia_pozycja)

            nowy_segment.pozycja = nowa_pozycja
            self.segmenty.append(nowy_segment)
            self.dodaj_segment = False

    def rysuj_segmenty(self, ekran):
        for segment in self.segmenty:
            ekran.blit(segment.obraz, segment.pozycja)
    
    def jedz_jablko(self):
        self.dodaj_segment = True

    def sprawdz_kolizje(self):
        for segment in self.segmenty:
            if self.rect.topleft == segment.pozycja.topleft:
                return True
        
        if self.rect.top < 0 or self.rect.top >= 608 or self.rect.left < 0 or self.rect.left >= 800:
            return True

        return False