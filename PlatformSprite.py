"""
PlatformSprite.py - Sprite class for platforms to be used in Game2
Jade Harbert
CSC 235
5-19-21
"""
import pygame
import Constants


class PlatformSprite(pygame.sprite.Sprite):

    # Takes in the x, y, width, and height values of a platform and updates accordingly
    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(Constants.WHITE)
        self.image.set_colorkey(Constants.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



