import pygame
import random
import stale

vec = pygame.math.Vector2

class Kulka(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.obraz = pygame.image.load("images/ball.png")
        self.zresetuj_pozycje()
        self.r = 16
        self.przegrana = False

    def zresetuj_pozycje(self):
        self.wspolrzedne = vec(stale.SZEROKOSC_EKRANU / 2, stale.WYSOKOSC_EKRANU - 140)
        self.rect = self.obraz.get_rect(center=self.wspolrzedne)
        self.wektor = vec(0, -10)
        self.kat_nachylenia = random.randrange(-30, 30)
        self.wektor.rotate_ip(self.kat_nachylenia)
        self.przegrana = False
    
    def aktualizuj(self, platforma, klocki):
        self.wspolrzedne += self.wektor
        self.rect.center = self.wspolrzedne
        self.sprawdz_kolizje(platforma, klocki)

    def sprawdz_kolizje(self, platforma, klocki):
        # Krawędzie ekranu
        if self.rect.x <= 0 or self.rect.right >= stale.SZEROKOSC_EKRANU:
            self.wektor.x *= -1

        if self.rect.top <= 0:
            self.wektor.y *= -1

        if self.rect.bottom >= stale.WYSOKOSC_EKRANU:
            self.przegrana = True

        # Platforma
        if self.rect.colliderect(platforma.rect):
            self.wektor.y *= -1
            self.wektor.x += platforma.porusza_sie*5
            
            if self.wektor.x < -10:
                self.wektor.x = -10
            if self.wektor.x > 10:
                self.wektor.x = 10

        # Klocki
        for klocek in klocki:
            if self.sprawdz_kolizje_z_klockiem(klocek):
                klocek.uderzenie()
                break

    def sprawdz_kolizje_z_klockiem(self, klocek):
        dystans_x = abs(self.rect.centerx - klocek.rect.centerx) - klocek.rect.w / 2
        dystans_y = abs(self.rect.centery - klocek.rect.centery) - klocek.rect.h / 2

        if dystans_x < self.r and dystans_y < self.r:
            if dystans_x < dystans_y:
                self.wektor.y *= -1
            else:
                self.wektor.x *= -1
            return True

        return False
        