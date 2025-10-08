# dodanie modułu pygame
import pygame

# dodanie modułu OS
import os

# import Element
import Element

# Zmiana obecnej ścieżki pracy
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Utworzenie stałych
SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600

obraz_tla = pygame.image.load("images/background.png")
obraz_baza_postaci = pygame.image.load("images/base.png")

nakrycie_glowy = Element.NakrycieGlowy()
ubranie_element = Element.UbranieElement()
oczy_element = Element.OczyElement()
bron_element = Element.BronElement()

pygame.init()

ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

pygame.font.init()
moja_czcionka = pygame.font.SysFont('Comic Sans MS', 30)

def wypisz_tekst(ekran, tekst, pozycja):
    napis = moja_czcionka.render(tekst, False, (255, 255, 255))
    ekran.blit(napis, pozycja)

gra_dziala = True
zapisywanie = False
while gra_dziala:
    for zdarzenie in pygame.event.get():
        match zdarzenie.type:
            case pygame.KEYDOWN:
                # Obsługa klawiszy 
                match zdarzenie.key:
                    case pygame.K_ESCAPE:
                        gra_dziala = False
                    case pygame.K_q:
                        nakrycie_glowy.wybierzNastepny()
                    case pygame.K_w:
                        oczy_element.wybierzNastepny()
                    case pygame.K_e:
                        ubranie_element.wybierzNastepny()
                    case pygame.K_r:
                        bron_element.wybierzNastepny()
                    case pygame.K_s:
                        zapisywanie = True
            case pygame.QUIT:
                gra_dziala = False

    ekran.blit(obraz_tla, (0,0))
    ekran.blit(obraz_baza_postaci, (270, 130))
    ekran.blit(ubranie_element.wybranyObraz(), (270, 130))
    ekran.blit(oczy_element.wybranyObraz(), (270, 130))
    ekran.blit(nakrycie_glowy.wybranyObraz(), (270, 130))
    ekran.blit(bron_element.wybranyObraz(), (270, 130))

    if zapisywanie:
        pygame.image.save(ekran, 'postac.png')
        zapisywanie = False

    wypisz_tekst(ekran, f"[Q] Głowa: {nakrycie_glowy.wybrany}", (100, 100))
    wypisz_tekst(ekran, f"[W] Oczy: {oczy_element.wybrany}", (100, 140))
    wypisz_tekst(ekran, f"[E] Ubranie: {ubranie_element.wybrany}", (100, 180))
    wypisz_tekst(ekran, f"[R] Broń: {bron_element.wybrany}", (100, 220))
    wypisz_tekst(ekran, "[S] Zapisz", (100, 260))

    pygame.display.flip()
    zegar.tick(30)

pygame.quit()