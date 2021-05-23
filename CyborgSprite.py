import pygame
import Constants


class CyborgSprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((75, 10))
        self.image.fill(Constants.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT - 200
        self.speed_x, self.speed_y = 0, 0
