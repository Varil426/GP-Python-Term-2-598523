import pygame
import random
import time
import os
from Kierunek import Kierunek
from Waz import Waz
from Jablko import Jablko

# Ustawienie katalogu roboczego
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Szerokość i wysokość ekranu
SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 608
Punkty = 0

tlo = pygame.Surface((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))
for i in range(25):
    for j in range(19):
        obraz = pygame.image.load("images/background.png")
        
        maska = (random.randrange(0, 20), random.randrange(0, 20), random.randrange(0, 20))
        obraz.fill(maska, special_flags=pygame.BLEND_ADD)

        tlo.blit(obraz, (i*32, j*32))

# Ustawienia
pygame.init()
pygame.font.init()
# Obiekt ekranu i zegara
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

# Wąż
waz = Waz()
PORUSZ_WEZEM = pygame.USEREVENT + 1
pygame.time.set_timer(PORUSZ_WEZEM, 200)

# Jabłka
jablko = Jablko()

jablka = pygame.sprite.Group()
jablka.add(jablko)

# Obiekt czcionki
moja_czcionka = pygame.font.SysFont("Comic Sans MS", 24)

gra_dziala = True

# Czyszczenie zdarzeń
pygame.event.clear()

while gra_dziala:
    for zdarzenie in pygame.event.get():
        match zdarzenie.type:
            case x if x == pygame.QUIT:
                gra_dziala = False
            case x if x == pygame.KEYDOWN:
                match zdarzenie.key:
                    case x if x == pygame.K_ESCAPE:
                        gra_dziala = False
                    case x if x == pygame.K_w:
                        waz.zmien_kierunek(Kierunek.GORA)
                    case x if x == pygame.K_d:
                        waz.zmien_kierunek(Kierunek.PRAWO)
                    case x if x == pygame.K_s:
                        waz.zmien_kierunek(Kierunek.DOL)
                    case x if x == pygame.K_a:
                        waz.zmien_kierunek(Kierunek.LEWO)
            case x if x == PORUSZ_WEZEM:
                waz.aktualizuj()

    # Sprawdzenie kolizji z jabłkiem
    kolizja_z_jablkiem = pygame.sprite.spritecollideany(waz, jablka)
    if kolizja_z_jablkiem != None:
        kolizja_z_jablkiem.kill()
        waz.jedz_jablko()
        jablka.add(Jablko())

    # Rysowanie tła
    ekran.blit(tlo, (0, 0))

    # Rysowanie głowy wężą
    ekran.blit(waz.obraz, waz.rect)

    # Rysowanie segmentów
    waz.rysuj_segmenty(ekran)

    # Rysowanie jabłek
    for jablko in jablka:
        ekran.blit(jablko.obraz, jablko.rect)

    if waz.sprawdz_kolizje():
        gra_dziala = False

    pygame.display.flip()
    zegar.tick(30)

time.sleep(3)

pygame.quit()
