import pygame
from Kolory import *

class Tamagotchi:
    def __init__(self):
        self.maks_poziom = 100
        self.poziom_glodu = 50 
        self.poziom_szczescia = 50
        self.przegrana = False

    def nakarm(self):
        self.poziom_glodu += 10
        if self.poziom_glodu > self.maks_poziom:
            self.poziom_glodu = self.maks_poziom

    def pobaw_sie(self):
        self.poziom_szczescia += 10
        if self.poziom_szczescia > self.maks_poziom:
            self.poziom_szczescia = self.maks_poziom

    def aktualizuj(self):
        if self.przegrana:
            return

        self.poziom_glodu -= 0.1
        self.poziom_szczescia -= 0.1

        if self.poziom_szczescia <= 0 or self.poziom_glodu <= 0:
        # if any(x <= 0 for x in [self.poziom_szczescia, self.poziom_glodu]):
            self.przegrana = True

    def rysuj(self, ekran):
        # Głowa
        pygame.draw.circle(ekran, KOLOR_NIEBIESKI, (200, 200), 50)
        pygame.draw.circle(ekran, KOLOR_CZARNY, (200, 200), 50, 3)

        # Oczy
        proc_szczesica = self.poziom_szczescia / self.maks_poziom
        pygame.draw.circle(ekran, KOLOR_CZARNY, (185, 185), 8 * proc_szczesica)
        pygame.draw.circle(ekran, KOLOR_CZARNY, (215, 185), 8 * proc_szczesica)

        # Usta
        if self.poziom_glodu > self.maks_poziom / 3:
            pygame.draw.rect(ekran, KOLOR_CZERWONY, (185, 225, 30, 3))
        else:
            pygame.draw.rect(ekran, KOLOR_CZERWONY, (185, 225, 30, 10), 3)
