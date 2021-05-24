import pygame
import Constants


class SpriteSheet:

    def __init__(self, filename):
        self.spritesheet = pygame.image.load(filename).convert_alpha()

    def get_image(self, x, y, width, height):
        image = pygame.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        #image = pygame.transform.scale(image, (width * 2, height * 2))
        return image
