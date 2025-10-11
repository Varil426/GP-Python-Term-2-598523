import pygame
import random

class Jablko(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.obraz = pygame.image.load("images/apple.png")
        losowa_pozycja = pygame.Rect(random.randint(0,24)*32, random.randint(1,18)*32, 32, 32)
        self.rect = losowa_pozycja