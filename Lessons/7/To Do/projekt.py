# dodanie modułu pygame
import pygame

# dodanie modułu OS
import os

# Zmiana obecnej ścieżki pracy
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Utworzenie stałych
SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600

obraz_tla = pygame.image.load("images/background.png")
obraz_baza_postaci = pygame.image.load("images/base.png")

pygame.init()

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

gra_dziala = True
while gra_dziala:
    for zdarzenie in pygame.event.get():
        match zdarzenie.type:
            case pygame.KEYDOWN:
                # Obsługa klawiszy 
                match zdarzenie.key:
                   case pygame.K_ESCAPE:
                       gra_dziala = False
            case pygame.QUIT:
                gra_dziala = False

    ekran.blit(obraz_tla, (0,0))
    ekran.blit(obraz_baza_postaci, (270, 130))

    pygame.display.flip()
    zegar.tick(30)

pygame.quit()