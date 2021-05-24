import pygame
import Constants


class PlatformSprite(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(Constants.WHITE)
        self.image.set_colorkey(Constants.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



