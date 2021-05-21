import pygame
import Constants


class CharacterSprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((75, 10))
        self.image.fill(Constants.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT - 50
        self.speed_x, self.speed_y = 0, 0

    def update(self, left_key, right_key, up_key, down_key, secs):
        self.speed_x, self.speed_y = 0, 0
        vel = 800
        keys = pygame.key.get_pressed()

        if keys[left_key]:
            self.speed_x = -(vel * secs)
        if keys[right_key]:
            self.speed_x = (vel * secs)
        if keys[up_key]:
            self.speed_y = -(vel * secs)
        if keys[down_key]:
            self.speed_y = (vel * secs)

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Responsible for making sure the paddle doesn't go off the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > Constants.SCREEN_WIDTH:
            self.rect.right = Constants.SCREEN_WIDTH
        elif self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > Constants.SCREEN_HEIGHT:
            self.rect.bottom = Constants.SCREEN_HEIGHT
