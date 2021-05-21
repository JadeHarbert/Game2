"""
Main.py
Jade Harbert
CSC 235
5-19-21
"""
from typing import Union, Any, Type

import pygame
from pygame.locals import *
from pygame.rect import RectType
from pygame.sprite import Group
from pygame.surface import SurfaceType, Surface
from pygame.time import Clock

import Constants
from CharacterSprite import CharacterSprite

screen: Union[Surface, SurfaceType]
background: Union[Surface, SurfaceType]
background_rect: Union[Rect, RectType, None]
clock: Clock
character: CharacterSprite
character_group: Type[Group]


# Function to initialize pygame base elements
def initialize():
    global screen, background, background_rect, clock
    global character_group, character

    pygame.init()
    pygame.mixer.init()
    # pygame.mixer.music.load(Constants.MUSIC_FILENAME)
    # pygame.mixer.music.play(loops=-1)
    # pygame.mixer.music.set_volume(1.0)

    screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT), 0, 32)
    background = pygame.image.load(Constants.BACKGROUND_FILENAME).convert()
    background_rect = background.get_rect()
    clock = pygame.time.Clock()

    character_group = pygame.sprite.Group()
    character = CharacterSprite()
    character_group.add(character)


# Function that displays the start screen and is responsible
# for handling the events on the start screen
def start_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "Insane Asylum Pong!", 64, Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT / 4)
    draw_text(screen, "Arrow keys move Player1, A/D keys move Player 2", 22,
              Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT / 2)
    draw_text(screen, "Press a key to begin", 18, Constants.SCREEN_WIDTH / 2, Constants.SCREEN_HEIGHT * 3 / 4)
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


# Function that simplifies drawing text on a screen\
def draw_text(surface, text, size, temp_x, temp_y):
    font = pygame.font.Font(Constants.FONT_NAME, size)
    text_surface = font.render(text, True, Constants.WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (temp_x, temp_y)
    surface.blit(text_surface, text_rect)


def update_groups(left_key, right_key, passed_time):
    character_group.clear(screen, background)
    character_group.update(left_key, right_key, passed_time)
    character_group.draw(screen)
    pygame.display.update()


def main():
    initialize()
    is_start_screen = True

    while True:
        if is_start_screen:
            start_screen()
            is_start_screen = False
            screen.blit(background, (0, 0))
        else:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()

            time_passed = clock.tick(60)
            time_passed_seconds = time_passed / 1000.0

            update_groups(pygame.K_LEFT, pygame.K_RIGHT, time_passed_seconds)


if __name__ == "__main__":
    main()
