"""
SpriteSheet.py - Class that takes in a spritesheet and returns a portion of that
                 image based on the inputted x, y, width, and height
Jade Harbert
CSC 235
5-19-21
"""
import pygame


class SpriteSheet:

    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert_alpha()

    def get_image(self, x, y, width, height):
        image = pygame.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        return image
