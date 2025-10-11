import pygame
import random
import time
import os

# Ustawienie katalogu roboczego
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Szerokość i wysokość ekranu
SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 608
Punkty = 0

# Ustawienia
pygame.init()
pygame.font.init()
# Obiekt ekranu i zegara
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
# Obiekt czcionki
moja_czcionka = pygame.font.SysFont("Comic Sans MS", 24)

pygame.quit()
