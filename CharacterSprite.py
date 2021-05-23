import pygame
import Constants
from SpriteSheet import SpriteSheet

run_file = "Images/Biker_run.png"


class CharacterSprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.attack_sheet = SpriteSheet(Constants.CHAR_ATTACK_FILENAME)
        self.run_sheet = SpriteSheet(Constants.CHAR_RUN_FILENAME)
        self.idle_sheet = SpriteSheet(Constants.CHAR_IDLE_FILENAME)
        self.jump_sheet = SpriteSheet(Constants.CHAR_JUMP_FILENAME)
        self.dbljump_sheet = SpriteSheet(Constants.CHAR_DBLJUMP_FILENAME)
        self.death_sheet = SpriteSheet(Constants.CHAR_DEATH_FILENAME)

        self.image = pygame.Surface((48, 48))
        self.image.fill(Constants.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT - 175
        self.speed_x, self.speed_y = 0, 0

        self.idle = True
        self.running = False
        self.attacking = False
        self.jumping = False
        self.dbljumping = False
        self.dying = False

        self.current_frame = 0
        self.last_update = 0

        self.idle_frames = []
        self.run_frames = []
        self.jump_frames = []
        self.dbljump_frames = []
        self.attack_frames = []
        self.death_frames = []

        self.load_images()

    def load_images(self):
        self.idle_frames = [self.idle_sheet.get_image(0, 0, 48, 48),
                            self.idle_sheet.get_image(48, 0, 48, 48),
                            self.idle_sheet.get_image(96, 0, 48, 48),
                            self.idle_sheet.get_image(144, 0, 48, 48)]
        for frame in self.idle_frames:
            frame.set_colorkey(Constants.BLACK)

        self.run_frames = [self.run_sheet.get_image(0, 0, 48, 48),
                           self.run_sheet.get_image(48, 0, 48, 48),
                           self.run_sheet.get_image(96, 0, 48, 48),
                           self.run_sheet.get_image(144, 0, 48, 48),
                           self.run_sheet.get_image(192, 0, 48, 48),
                           self.run_sheet.get_image(240, 0, 48, 48), ]
        for frame in self.run_frames:
            frame.set_colorkey(Constants.BLACK)

        self.jump_frames = [self.jump_sheet.get_image(0, 0, 48, 48),
                            self.jump_sheet.get_image(48, 0, 48, 48),
                            self.jump_sheet.get_image(96, 0, 48, 48),
                            self.jump_sheet.get_image(144, 0, 48, 48),
                            self.jump_sheet.get_image(192, 0, 48, 48),
                            self.jump_sheet.get_image(240, 0, 48, 48), ]
        for frame in self.jump_frames:
            frame.set_colorkey(Constants.BLACK)

        self.dbljump_frames = [self.dbljump_sheet.get_image(0, 0, 48, 48),
                               self.dbljump_sheet.get_image(48, 0, 48, 48),
                               self.dbljump_sheet.get_image(96, 0, 48, 48),
                               self.dbljump_sheet.get_image(144, 0, 48, 48),
                               self.dbljump_sheet.get_image(192, 0, 48, 48),
                               self.dbljump_sheet.get_image(240, 0, 48, 48), ]
        for frame in self.dbljump_frames:
            frame.set_colorkey(Constants.BLACK)

        self.attack_frames = [self.attack_sheet.get_image(0, 0, 48, 48),
                              self.attack_sheet.get_image(48, 0, 48, 48),
                              self.attack_sheet.get_image(96, 0, 48, 48),
                              self.attack_sheet.get_image(144, 0, 48, 48),
                              self.attack_sheet.get_image(192, 0, 48, 48),
                              self.attack_sheet.get_image(240, 0, 48, 48), ]
        for frame in self.attack_frames:
            frame.set_colorkey(Constants.BLACK)

        self.death_frames = [self.death_sheet.get_image(0, 0, 48, 48),
                             self.death_sheet.get_image(48, 0, 48, 48),
                             self.death_sheet.get_image(96, 0, 48, 48),
                             self.death_sheet.get_image(144, 0, 48, 48),
                             self.death_sheet.get_image(192, 0, 48, 48),
                             self.death_sheet.get_image(240, 0, 48, 48), ]
        for frame in self.death_frames:
            frame.set_colorkey(Constants.BLACK)

    def animate(self):
        now = pygame.time.get_ticks()

        if self.idle:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames)
                self.image = self.idle_frames[self.current_frame]

        elif self.running:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.run_frames)
                self.image = self.run_frames[self.current_frame]

        elif self.attacking:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.attack_frames)
                self.image = self.idle_frames[self.current_frame]

        elif self.jumping:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.jump_frames)
                self.image = self.idle_frames[self.current_frame]

        elif self.dbljump_sheet:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.dbljump_frames)
                self.image = self.idle_frames[self.current_frame]

    def update(self, left_key, right_key, up_key, down_key, secs):
        gravity = 100
        vel = 400
        keys = pygame.key.get_pressed()

        self.animate()
        self.speed_x, self.speed_y = 0, 0
        self.speed_y += gravity * secs

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

        print(self.rect.bottom)

    def collision(self, midTop):
        self.rect.bottom = midTop
        print(midTop)

