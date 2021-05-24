"""
CyborgSprite.py - Sprite class for a Cyborg character to be used as enemies in Main.py
Jade Harbert
CSC 235
5-19-21
"""
from Constants import *
from SpriteSheet import SpriteSheet

vec = pygame.math.Vector2


class CyborgSprite(pygame.sprite.Sprite):

    def __init__(self, x, y, acceleration):
        super().__init__()

        self.run_sheet = SpriteSheet(CYBORG_RUN_FILENAME)
        self.idle_sheet = SpriteSheet(CYBORG_IDLE_FILENAME)
        self.death_sheet = SpriteSheet(CYBORG_DEATH_FILENAME)

        self.idle = False
        self.running = False
        self.dying = False
        self.done_dying = False

        self.current_frame = 0
        self.last_update = 0

        self.idle_frames = []
        self.run_frames_r = []
        self.run_frames_l = []
        self.death_frames = []

        self.load_images()

        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.count = 0

        self.image = self.idle_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = SCREEN_WIDTH / 2, 526
        self.rect.bottom = 381
        self.acceleration = acceleration

    # Loads all of the sprite sheet images
    def load_images(self):

        self.idle_frames = [self.idle_sheet.get_image(0, 0, 48, 48),
                            self.idle_sheet.get_image(48, 0, 48, 48),
                            self.idle_sheet.get_image(96, 0, 48, 48),
                            self.idle_sheet.get_image(144, 0, 48, 48)]
        for frame in self.idle_frames:
            frame.set_colorkey(BLACK)

        self.run_frames_r = [self.run_sheet.get_image(0, 0, 48, 48),
                             self.run_sheet.get_image(48, 0, 48, 48),
                             self.run_sheet.get_image(96, 0, 48, 48),
                             self.run_sheet.get_image(144, 0, 48, 48),
                             self.run_sheet.get_image(192, 0, 48, 48),
                             self.run_sheet.get_image(240, 0, 48, 48)]
        for frame in self.run_frames_r:
            frame.set_colorkey(BLACK)
            self.run_frames_l.append(pygame.transform.flip(frame, True, False))

        self.death_frames = [self.death_sheet.get_image(0, 0, 48, 48),
                             self.death_sheet.get_image(48, 0, 48, 48),
                             self.death_sheet.get_image(96, 0, 48, 48),
                             self.death_sheet.get_image(144, 0, 48, 48),
                             self.death_sheet.get_image(192, 0, 48, 48),
                             self.death_sheet.get_image(240, 0, 48, 48)]
        for frame in self.death_frames:
            frame.set_colorkey(BLACK)

    # Animates all of the different movements
    def animate(self):
        now = pygame.time.get_ticks()

        if self.vel.x != 0:
            self.running = True
            self.idle = False
        elif self.vel.x == 0:
            self.running = False
            self.idle = True

        if self.idle:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames)
                self.image = self.idle_frames[self.current_frame]
        if self.running:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.run_frames_r)
                if self.vel.x > 0:
                    self.image = self.run_frames_r[self.current_frame]
                else:
                    self.image = self.run_frames_l[self.current_frame]
        if self.dying:
            if now - self.last_update > 150:
                self.count += 1
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.death_frames)
                self.image = self.death_frames[self.current_frame]
            if self.count > 4:
                self.dying = False
                self.done_dying = True
                self.kill()

    # Updates the sprite based on time
    def update(self, character):
        self.animate()
        self.acc = vec(0, 0.5)

        # if the protagonist is within 150 pixels in the x direction and 50 pixels in the y direction, then the
        # sprite will move towards the character
        if abs(character.pos.x - self.pos.x) < 150 and abs(character.pos.y - self.pos.y) < 50 and not self.dying:
            if character.pos.x > self.pos.x:
                self.acc.x = self.acceleration
            else:
                self.acc.x = -self.acceleration
        else:
            self.acc.x = 0

        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        if abs(self.vel.x) < 0.2:
            self.vel.x = 0

        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

        if self.pos.x < 0 - self.rect.width / 2:
            self.pos.x = SCREEN_WIDTH
        elif self.pos.x > SCREEN_WIDTH + self.rect.width / 2:
            self.pos.x = 0

    # Function for dying
    def death(self):
        self.dying = True
        self.running = False
        self.idle = False
        self.vel = vec(0, 0)

    # Returns self.done_dying
    def get_done_dying(self):
        return self.done_dying
