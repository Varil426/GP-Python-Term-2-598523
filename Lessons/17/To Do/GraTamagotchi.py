import pygame
from Tamagotchi import Tamagotchi
from Kolory import *

def okresl_kolor(poziom):
    if poziom > 70:
        return KOLOR_ZIELONY

    if 30 <= poziom <= 70:
        return KOLOR_ZOLTY
    
    return KOLOR_CZERWONY


# Inicjalizacja i ustawienia
pygame.init()
pygame.display.init()
pygame.font.init()
SZEROKOSC, WYSOKOSC = 400, 450
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("Tamagotchi")
zegar = pygame.time.Clock()

CZCIONKA = pygame.font.SysFont("Comic Sans", 20)

tamagotchi = Tamagotchi()

# Główna pętla gry
koniec_gry = False
while not koniec_gry:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                koniec_gry = True
        elif zdarzenie.type == pygame.MOUSEBUTTONDOWN:
            if tamagotchi.przegrana:
                if przycisk_restart.collidepoint(zdarzenie.pos):
                    tamagotchi = Tamagotchi()
            else:
                if przycisk_nakarm.collidepoint(zdarzenie.pos):
                    tamagotchi.nakarm()
                elif przycisk_pobaw.collidepoint(zdarzenie.pos):
                    tamagotchi.pobaw_sie()
        elif zdarzenie.type == pygame.QUIT:
            koniec_gry = True

    tamagotchi.aktualizuj()

    ekran.fill(KOLOR_TLA)
    tamagotchi.rysuj(ekran)

    # Interfejs
    ## Szczęscie - pasek i napis
    kolor_szczescie = okresl_kolor(tamagotchi.poziom_szczescia)
    pygame.draw.rect(ekran, kolor_szczescie, pygame.Rect(50, 50, tamagotchi.poziom_szczescia * 2, 20))
    tekst_szczesie = CZCIONKA.render("Szczęście", True, KOLOR_CZARNY)
    ekran.blit(tekst_szczesie, (50, 20))

    ## Głód - pasek i napis
    kolor_glod = okresl_kolor(tamagotchi.poziom_glodu)
    pygame.draw.rect(ekran, kolor_glod, pygame.Rect(50, 100, tamagotchi.poziom_glodu * 2, 20))
    tekst_glod = CZCIONKA.render("Głód", True, KOLOR_CZARNY)
    ekran.blit(tekst_glod, (50, 70))

    ## Przyciski - Nakarm i Pobaw się
    przycisk_nakarm = pygame.Rect(225, 300, 150, 50)
    przycisk_pobaw = pygame.Rect(25, 300, 150, 50)
    pygame.draw.rect(ekran, KOLOR_BIALY, przycisk_nakarm, 3)
    pygame.draw.rect(ekran, KOLOR_BIALY, przycisk_pobaw, 3)

    tekst_nakarm = CZCIONKA.render("Nakarm", True, KOLOR_CZARNY)
    tekst_pobaw = CZCIONKA.render("Pobaw się", True, KOLOR_CZARNY)
    
    tekst_szer_nakarm, tekst_wys_nakarm = tekst_nakarm.get_size()
    tekst_szer_pobaw, tekst_wys_pobaw = tekst_pobaw.get_size()

    ekran.blit(tekst_nakarm, (
        przycisk_nakarm.x + (przycisk_nakarm.width - tekst_szer_nakarm) // 2,
        przycisk_nakarm.y + (przycisk_nakarm.height - tekst_wys_nakarm) // 2,
    ))

    ekran.blit(tekst_pobaw, (
        przycisk_pobaw.x + (przycisk_pobaw.width - tekst_szer_pobaw) // 2,
        przycisk_pobaw.y + (przycisk_pobaw.height - tekst_wys_pobaw) // 2,
    ))

    ## Interfejs - Koniec Gry
    if tamagotchi.przegrana:
        przycisk_restart = pygame.Rect(50, 380, 300, 50)
        pygame.draw.rect(ekran, KOLOR_BIALY, przycisk_restart, 3)

        tekst_restart = CZCIONKA.render("Spróbuj jeszcze raz", True, KOLOR_CZARNY)
        tekst_szer_restart, tekst_wys_restart = tekst_restart.get_size()
        ekran.blit(
            tekst_restart,
            (
                przycisk_restart.x + (przycisk_restart.width - tekst_szer_restart) // 2,
                przycisk_restart.y + (przycisk_restart.height - tekst_wys_restart) // 2,
            ))
        
        tekst_koniec_gry = CZCIONKA.render("Koniec gry", True, KOLOR_CZARNY)
        ekran.blit(
            tekst_koniec_gry,
              (
                  (SZEROKOSC - tekst_koniec_gry.get_width()) // 2,
                  250
              ))


    pygame.display.flip()
    zegar.tick(30)

pygame.quit()
