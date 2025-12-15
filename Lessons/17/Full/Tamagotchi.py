import pygame
import random
import Kolory

class Tamagotchi:
    def __init__(self):
        self.maks_poziom = 100
        self.poziom_glodu = 50
        self.poziom_szczescia = 50
        self.przegrana = False
        self.efekt_zabawa_czas = 0
        self.efekt_zabawa = []
    
    def nakarm(self):
        self.poziom_glodu += 10
        if self.poziom_glodu > self.maks_poziom:
            self.poziom_glodu = self.maks_poziom

    def pobaw_sie(self):
        self.poziom_szczescia += 10
        if self.poziom_szczescia > self.maks_poziom:
            self.poziom_szczescia = self.maks_poziom

        self.efekt_zabawa_czas = 30
        self.efekt_zabawa = [(random.randint(50, 350), random.randint(50, 350)) for i in range(10)]
        
    def aktualizuj(self):
        if self.przegrana:
            return
        
        self.poziom_glodu -= 0.1
        self.poziom_szczescia -= 0.1
        
        if self.efekt_zabawa_czas > 0:
            self.efekt_zabawa_czas -= 1
        
        # sprawdzenie, czy nastąpił koniec gry
        if self.poziom_szczescia <= 0 or self.poziom_glodu <= 0:
            self.przegrana = True
    
    def rysuj(self, ekran):
        # głowa
        pygame.draw.circle(ekran, Kolory.KOLOR_NIEBIESKI, (200, 200), 50)
        pygame.draw.circle(ekran, Kolory.KOLOR_CZARNY, (200, 200), 50, 3)

        # oczy
        proc_szczescia = self.poziom_szczescia / self.maks_poziom
        pygame.draw.circle(ekran, Kolory.KOLOR_CZARNY, (185, 185), 8 * proc_szczescia)
        pygame.draw.circle(ekran, Kolory.KOLOR_CZARNY, (215, 185), 8 * proc_szczescia)
        
        #usta
        if self.poziom_glodu > self.maks_poziom / 3:
            pygame.draw.rect(ekran, Kolory.KOLOR_CZERWONY, (185, 225, 30, 3))
        else:
            pygame.draw.rect(ekran, Kolory.KOLOR_CZERWONY, (185, 220, 30, 10), 3)
        
        # efekt zabawa
        if self.efekt_zabawa_czas > 0:
            for efekt in self.efekt_zabawa:
                x, y = efekt
                promien = random.randint(5, 15)
                pygame.draw.circle(ekran, Kolory.KOLOR_ZOLTY, (x, y), promien)