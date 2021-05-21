import pygame
import Constants


class CharacterSprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((75, 10))
        self.rect = self.image.get_rect()
        self.rect.center = Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT - 50
        self.speed_x = 0

    def update(self, left_key, right_key, secs):
        self.speed_x = 0
        vel = 800
        keys = pygame.key.get_pressed()

        if keys[left_key]:
            self.speed_x = -(vel * secs)
        elif keys[right_key]:
            self.speed_x = (vel * secs)

        self.rect.x += self.speed_x

        # Responsible for making sure the paddle doesn't go off the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > Constants.SCREEN_WIDTH:
            self.rect.right = Constants.SCREEN_WIDTH
