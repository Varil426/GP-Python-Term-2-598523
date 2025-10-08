import pygame

class Obraz(pygame.sprite.Sprite):
    def __init__(self, sciezka):
        super().__init__()
        self.obraz = pygame.image.load(sciezka)

class Element():
    def __init__(self, typ):
        self.wybrany = 0
        self.list_obrazow = []

        for i in range(1, 4):
            sciezka = f"images/{typ}{i}.png"
            wczytany_obrazek = Obraz(sciezka)
            self.list_obrazow.append(wczytany_obrazek)

    def wybierzNastepny(self):
        self.wybrany += 1
        if self.wybrany > len(self.list_obrazow) - 1:
            self.wybrany = 0

    def wybranyObraz(self):
        return self.list_obrazow[self.wybrany].obraz
    
class NakrycieGlowy(Element):
    def __init__(self):
        super().__init__("head")

class UbranieElement(Element):
    def __init__(self):
        super().__init__("body")

class OczyElement(Element):
    def __init__(self):
        super().__init__("eye")

class BronElement(Element):
    def __init__(self):
        super().__init__("weapon")