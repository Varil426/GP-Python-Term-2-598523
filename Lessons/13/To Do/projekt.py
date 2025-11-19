import os
import pygame
import stale
from platforma import Platforma
from kulka import Kulka
from klocek import Klocek

# Ustawienie katalogu roboczego
os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
pygame.font.init()

czcionka = pygame.font.SysFont("Comic Sans MS", 24)
ekran = pygame.display.set_mode([stale.SZEROKOSC_EKRANU, stale.WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load("images/background.png")

poziom1 = [
	[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
	[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
	[0, 0, 0, 3, 3, 3, 3, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

poziom2 = [
	[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
	[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

poziom3 = [
	[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
	[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

klocki = pygame.sprite.Group()

def dodaj_klocki():
    wczytany_poziom = None
    if Poziom == 0:
        wczytany_poziom = poziom1
    if Poziom == 1:
        wczytany_poziom = poziom2
    if Poziom == 2:
        wczytany_poziom = poziom3

    for i in range(10):
        for j in range(7):
            if wczytany_poziom[j][i] != 0:
                klocek = Klocek(32+i*96, 32+j*48, wczytany_poziom[j][i])
                klocki.add(klocek)

platforma = Platforma()
kulka = Kulka()
Zycia = 3
Poziom = 0

dodaj_klocki()

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

    if len(klocki.sprites()) == 0:
        Poziom += 1
        if Poziom >= 3:
            break
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()
        dodaj_klocki()

    klocki.update()
    kulka.aktualizuj(platforma, klocki)

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
    for klocek in klocki:
        ekran.blit(klocek.obraz, klocek.rect)

    # Wyświetlanie tekstu
    tekst = czcionka.render(f"Życia: {Zycia}", False, (255, 0, 255))
    ekran.blit(tekst, (16, 16))

    pygame.display.flip()
    zegar.tick(30)

pygame.quit()