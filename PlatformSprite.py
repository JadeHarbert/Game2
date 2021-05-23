import pygame
import Constants


class PlatformSprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # self.image = pygame.image.load(Constants.PLATFORM_FILENAME).convert_alpha()
        self.image = pygame.Surface((1000, 88))
        self.image.fill(Constants.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = Constants.SCREEN_HEIGHT - 88



