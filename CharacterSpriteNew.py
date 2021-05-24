from pygame.constants import *

from Constants import *
from SpriteSheet import SpriteSheet

vec = pygame.math.Vector2


class CharacterSprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.attack_sheet = SpriteSheet(CHAR_ATTACK_FILENAME)
        self.run_sheet = SpriteSheet(CHAR_RUN_FILENAME)
        self.idle_sheet = SpriteSheet(CHAR_IDLE_FILENAME)
        self.death_sheet = SpriteSheet(CHAR_DEATH_FILENAME)

        self.idle = True
        self.attacking = False
        self.dying = False
        self.running = False
        self.colliding = False
        self.right_face = True
        self.shooting = False

        self.current_frame = 0
        self.last_update = 0
        self.start_time = 0

        self.idle_frames = []
        self.idle_frames_l = []
        self.run_frames_r = []
        self.run_frames_l = []
        self.attack_frames = []
        self.attack_frames_l = []
        self.death_frames = []

        self.load_images()

        self.image = self.idle_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = SCREEN_WIDTH / 2, 526
        self.speed_x, self.speed_y = 0, 0

        self.pos = vec(SCREEN_WIDTH / 2, 500)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.count = 0
        self.lives = PLAYER_LIVES

    def load_images(self):
        self.idle_frames = [self.idle_sheet.get_image(0, 0, 48, 48),
                            self.idle_sheet.get_image(48, 0, 48, 48),
                            self.idle_sheet.get_image(96, 0, 48, 48),
                            self.idle_sheet.get_image(144, 0, 48, 48)]
        for frame in self.idle_frames:
            frame.set_colorkey(BLACK)
            self.idle_frames_l.append(pygame.transform.flip(frame, True, False))

        self.run_frames_r = [self.run_sheet.get_image(0, 0, 48, 48),
                             self.run_sheet.get_image(48, 0, 48, 48),
                             self.run_sheet.get_image(96, 0, 48, 48),
                             self.run_sheet.get_image(144, 0, 48, 48),
                             self.run_sheet.get_image(192, 0, 48, 48),
                             self.run_sheet.get_image(240, 0, 48, 48)]
        for frame in self.run_frames_r:
            frame.set_colorkey(BLACK)
            self.run_frames_l.append(pygame.transform.flip(frame, True, False))

        self.attack_frames = [self.attack_sheet.get_image(0, 0, 48, 48),
                              self.attack_sheet.get_image(48, 0, 48, 48),
                              self.attack_sheet.get_image(96, 0, 48, 48),
                              self.attack_sheet.get_image(144, 0, 48, 48),
                              self.attack_sheet.get_image(192, 0, 48, 48),
                              self.attack_sheet.get_image(240, 0, 48, 48)]
        for frame in self.attack_frames:
            frame.set_colorkey(BLACK)
            self.attack_frames_l.append(pygame.transform.flip(frame, True, False))

        self.death_frames = [self.death_sheet.get_image(0, 0, 48, 48),
                             self.death_sheet.get_image(48, 0, 48, 48),
                             self.death_sheet.get_image(96, 0, 48, 48),
                             self.death_sheet.get_image(144, 0, 48, 48),
                             self.death_sheet.get_image(192, 0, 48, 48),
                             self.death_sheet.get_image(240, 0, 48, 48)]
        for frame in self.death_frames:
            frame.set_colorkey(BLACK)

    def animate(self):
        now = pygame.time.get_ticks()

        if self.vel.x != 0 and not self.attacking:
            self.running = True
            self.idle = False
        elif self.vel.x == 0 and not self.attacking:
            self.running = False
            self.idle = True

        if self.idle:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames)
                if self.right_face:
                    self.image = self.idle_frames[self.current_frame]
                else:
                    self.image = self.idle_frames_l[self.current_frame]
        if self.running:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.run_frames_r)
                if self.vel.x > 0:
                    self.image = self.run_frames_r[self.current_frame]
                else:
                    self.image = self.run_frames_l[self.current_frame]
        if self.attacking:
            if now - self.last_update > 150:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.attack_frames)
                if self.right_face:
                    self.image = self.attack_frames[self.current_frame]
                else:
                    self.image = self.attack_frames_l[self.current_frame]

        if self.dying:
            if now - self.last_update > 150:
                self.count += 1
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.death_frames)
                self.image = self.death_frames[self.current_frame]
            if self.count > 4:
                self.dying = False
                self.respawn()

    def update(self, left_key, right_key, up_key, attack_key, secs):
        keys = pygame.key.get_pressed()

        self.animate()
        self.acc = vec(0, 0.5)

        if keys[left_key] and not self.dying:
            self.acc.x = -PLAYER_ACC
            self.right_face = False
        if keys[right_key] and not self.dying:
            self.acc.x = PLAYER_ACC
            self.right_face = True

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == attack_key:
                    self.attack(True)
                if event.key == pygame.K_w:
                    self.jump()
            if event.type == KEYUP:
                if event.key == attack_key:
                    self.attack(False)

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

    def jump(self):
        self.vel.y = -15

    def attack(self, num):
        if num == 1:
            self.attacking = True
            self.running = False
            self.idle = False

        elif num == 0:
            self.attacking = False
            self.idle = True

    def death(self):
        self.dying = True
        self.running = False
        self.idle = False
        self.attacking = False
        self.vel = vec(0, 0)

    def respawn(self):
        self.lives -= 1
        # self.start_time = pygame.time.get_ticks()
        self.pos = vec(2000, 2000)
        self.idle = True
        # now = pygame.time.get_ticks()
        # while self.start_time + 2000 > now:
        #    now = pygame.time.get_ticks()

        self.pos = vec(SCREEN_WIDTH / 2, 500)
        self.count = 0

    def next_level(self):
        self.pos = vec(SCREEN_WIDTH / 2, 500)

    def get_lives(self):
        return self.lives
