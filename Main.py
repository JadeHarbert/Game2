"""
Main.py - Driver class for a platforming fighting game
Jade Harbert
CSC 235
5-19-21
"""
from typing import Union, Type
import pygame.sprite
from pygame.locals import *
from pygame.rect import RectType
from pygame.sprite import Group
from pygame.surface import SurfaceType, Surface
from pygame.time import Clock
from Constants import *
from CharacterSpriteNew import CharacterSprite
from CyborgSprite import CyborgSprite
from PlatformSprite import PlatformSprite

screen: Union[Surface, SurfaceType]
background: Union[Surface, SurfaceType]
background_rect: Union[Rect, RectType, None]
clock: Clock
character: CharacterSprite
character_group: Type[Group]
enemy: CyborgSprite
enemy_group: Type[Group]
platform_group: Type[Group]
mainPlatform: PlatformSprite
enemyList = []
temp_lives: int
current_level: int
is_level_clear: bool
lose_life_sound: type[pygame.mixer.Sound]
game_over_sound: type[pygame.mixer.Sound]
winner_sound: type[pygame.mixer.Sound]
enemy_speed: int


# Function to initialize pygame base elements
def initialize():
    global screen, background, background_rect, clock
    global character_group, character
    global enemy, enemy_group, enemyList
    global mainPlatform, platform_group
    global lose_life_sound, game_over_sound, winner_sound

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(MUSIC_FILENAME)
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.01)

    lose_life_sound = pygame.mixer.Sound(LOSE_LIFE_FILE)
    lose_life_sound.set_volume(0.03)

    game_over_sound = pygame.mixer.Sound(GAME_OVER_FILE)
    game_over_sound.set_volume(0.01)

    winner_sound = pygame.mixer.Sound(WINNER_FILE)
    winner_sound.set_volume(0.05)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    background = pygame.image.load(BACKGROUND_FILENAME).convert()
    background_rect = background.get_rect()
    clock = pygame.time.Clock()

    character_group = pygame.sprite.Group()
    character = CharacterSprite()
    character_group.add(character)

    platform_group = pygame.sprite.Group()

    enemy_group = pygame.sprite.Group()

    # Gets the values from the PLATFORM_LIST dictionary in Constants
    p = PLATFORM_LIST.get("main")
    mainPlatform = PlatformSprite(p[0], p[1], p[2], p[3])
    p = PLATFORM_LIST.get("midLeft")
    midLeftPlatform = PlatformSprite(p[0], p[1], p[2], p[3])
    p = PLATFORM_LIST.get("mid")
    midPlatform = PlatformSprite(p[0], p[1], p[2], p[3])
    p = PLATFORM_LIST.get("botLeft")
    botLeftPlatform = PlatformSprite(p[0], p[1], p[2], p[3])
    p = PLATFORM_LIST.get("botMid")
    botMidPlatform = PlatformSprite(p[0], p[1], p[2], p[3])
    p = PLATFORM_LIST.get("botRight")
    botRightPlatform = PlatformSprite(p[0], p[1], p[2], p[3])
    p = PLATFORM_LIST.get("midRight")
    midRightPlatform = PlatformSprite(p[0], p[1], p[2], p[3])
    p = PLATFORM_LIST.get("midRight2")
    midRight2Platform = PlatformSprite(p[0], p[1], p[2], p[3])

    platform_group.add(mainPlatform)
    platform_group.add(midLeftPlatform)
    platform_group.add(midPlatform)
    platform_group.add(botLeftPlatform)
    platform_group.add(botMidPlatform)
    platform_group.add(botRightPlatform)
    platform_group.add(midRightPlatform)
    platform_group.add(midRight2Platform)

    platform_group.draw(screen)

    respawn_enemies(0.2)


# Respawns the enemies with a speed of the speed argument
def respawn_enemies(speed):
    # Gets the values from the PLATFORM_LIST dictionary in Constants.py
    p = PLATFORM_LIST.get("midLeft")
    e = CyborgSprite(p[0] + (p[2] / 2), p[1], speed)
    enemy_group.add(e)
    enemyList.append(e)

    p = PLATFORM_LIST.get("mid")
    e = CyborgSprite(p[0] + (p[2] / 2), p[1], speed)
    enemy_group.add(e)
    enemyList.append(e)

    p = PLATFORM_LIST.get("botLeft")
    e = CyborgSprite(p[0] + (p[2] / 2), p[1], speed)
    enemy_group.add(e)
    enemyList.append(e)

    p = PLATFORM_LIST.get("botMid")
    e = CyborgSprite(p[0] + (p[2] / 2), p[1], speed)
    enemy_group.add(e)
    enemyList.append(e)

    p = PLATFORM_LIST.get("botRight")
    e = CyborgSprite(p[0] + (p[2] / 2), p[1], speed)
    enemy_group.add(e)
    enemyList.append(e)

    p = PLATFORM_LIST.get("midRight")
    e = CyborgSprite(p[0] + (p[2] / 2), p[1], speed)
    enemy_group.add(e)
    enemyList.append(e)

    p = PLATFORM_LIST.get("midRight2")
    e = CyborgSprite(p[0] + (p[2] / 2), p[1], speed)
    enemy_group.add(e)
    enemyList.append(e)

    enemy_group.draw(screen)


def respawn_character():
    character.next_level()


# Function that displays the start screen and is responsible
# for handling the events on the start screen
def start_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "Cyborg Domination!", 64, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6)
    draw_text(screen, "WASD keys move the Player, F to attack", 22,
              SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    draw_text(screen, "Defeat 10 waves of Cyborgs by attacking them or jumping on their heads", 22,
              SCREEN_WIDTH / 2, SCREEN_HEIGHT * 11 / 16)
    draw_text(screen, "Press a key to begin", 18, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.KEYUP:
                waiting = False


# Function that displays the end screen and based on the is_winner argument, will display
# different screens
def end_screen(is_winner):
    pygame.mixer.music.stop()
    screen.blit(background, background_rect)
    if is_winner:
        draw_text(screen, "Congratulations, you beat the game!!", 64, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6)
    else:
        draw_text(screen, "You ran out of lives! You made it to level " + str(current_level), 64, SCREEN_WIDTH / 2,
                  SCREEN_HEIGHT / 6)

    draw_text(screen, "Thank you for playing!", 22, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    draw_text(screen, "Press a key to quit", 18, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.KEYUP:
                pygame.quit()
                waiting = False
                quit()


# Function that simplifies drawing text on a screen
def draw_text(surface, text, size, temp_x, temp_y):
    font = pygame.font.Font(FONT_NAME, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (temp_x, temp_y)
    surface.blit(text_surface, text_rect)


# Function that updates all of the Sprite groups
# and draws them on the screen
def update_groups(left_key, right_key, up_key, down_key, passed_time, character_reference):
    character_group.clear(screen, background)
    character_group.update(left_key, right_key, up_key, down_key, passed_time)
    character_group.draw(screen)

    enemy_group.clear(screen, background)
    enemy_group.update(character_reference)
    enemy_group.draw(screen)

    platform_group.clear(screen, background)
    platform_group.draw(screen)

    pygame.display.update()


# Function that draws the player lives and level on the screen
def update_scores():
    screen.blit(background, background_rect)
    draw_text(screen, "Player Lives: " + str(character.get_lives()), 20, 65, 15)
    draw_text(screen, "Level: " + str(current_level), 20, SCREEN_WIDTH - 65, 15)


def main():
    global temp_lives, is_level_clear, current_level, enemy_speed
    initialize()
    is_start_screen = True
    is_level_clear = False
    current_level = 1
    enemy_speed = 0.2

    while True:
        if is_start_screen:
            start_screen()
            is_start_screen = False
            temp_lives = 3
            update_scores()
        else:
            if not is_level_clear:
                time_passed = clock.tick(60)
                time_passed_seconds = time_passed / 1000.0
                update_groups(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_f, time_passed_seconds, character)

                # Responsible for character and platform collision
                if character.vel.y >= 0:
                    hits = pygame.sprite.spritecollide(character, platform_group, False)
                    if hits:
                        character.pos.y = hits[0].rect.top
                        character.vel.y = 0

                # Responsible for enemy and platform collision
                for e in enemyList:
                    hits = pygame.sprite.spritecollide(e, platform_group, False)
                    if hits:
                        e.pos.y = hits[0].rect.top
                        e.vel.y = 0

                # Responsible for the collisions between character and the enemies
                hits = pygame.sprite.spritecollide(character, enemy_group, False)
                if hits:
                    if character.pos.y < hits[0].pos.y or character.attacking:
                        hits[0].death()

                    elif character.pos.y >= hits[0].pos.y and hits[0].get_done_dying and not character.attacking \
                            and not character.dying:
                        character.death()
                        lose_life_sound.play()

                # Determines whether or not all the enemies have been killed
                if len(enemy_group) == 0:
                    is_level_clear = True
                    current_level += 1
                    update_scores()

                # Displays the end_screen based on the ending condition
                if character.get_lives() < 1:
                    game_over_sound.play()
                    end_screen(False)
                elif current_level > 10:
                    winner_sound.play()
                    end_screen(True)

                # Updates the displayed scored if they're different
                if temp_lives != character.get_lives():
                    temp_lives = character.get_lives()
                    update_scores()
            else:
                is_level_clear = False
                enemy_speed += 0.1
                respawn_enemies(enemy_speed)
                respawn_character()


if __name__ == "__main__":
    main()
