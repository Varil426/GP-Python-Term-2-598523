import os
import pygame
import stale
from platforma import Platforma
from kulka import Kulka

# Ustawienie katalogu roboczego
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
pygame.font.init()

czcionka = pygame.font.SysFont("Comic Sans MS", 24)
ekran = pygame.display.set_mode([stale.SZEROKOSC_EKRANU, stale.WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load("images/background.png")

platforma = Platforma()
kulka = Kulka()
Zycia = 3

gra_dziala = True

while gra_dziala:
    # Obsługa zdarzeń
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        platforma.ruszaj_platforma(-1)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        platforma.ruszaj_platforma(1)

    kulka.aktualizuj(platforma)

    if kulka.przegrana:
        Zycia -= 1
        if Zycia <= 0:
            gra_dziala = False
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()

    platforma.aktualizuj()

    # Rysowanie
    ekran.blit(obraz_tla, (0, 0))
    ekran.blit(platforma.obraz, platforma.rect)
    ekran.blit(kulka.obraz, kulka.rect)

    # Wyświetlanie tekstu
    tekst = czcionka.render(f"Życia: {Zycia}", False, (255, 0, 255))
    ekran.blit(tekst, (16, 16))

    pygame.display.flip()
    zegar.tick(30)

pygame.quit()