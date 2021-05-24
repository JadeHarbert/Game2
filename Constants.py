"""
Constants.py - file that holds Constants for Game2
Jade Harbert
CSC 235
5-19-21
"""
import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 625
MUSIC_FILENAME = "Sounds/Undertale - Megalovania.wav"
LOSE_LIFE_FILE = "Sounds/Microsoft Windows XP Error - Sound Effect (HD).wav"
GAME_OVER_FILE = "Sounds/Game Over sound effect.wav"
WINNER_FILE = "Sounds/Winner Sound Effect.wav"
BACKGROUND_FILENAME = "Images/Joust_Background_Updated.jpg"
FONT_NAME = pygame.font.match_font('arial')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

CHAR_IDLE_FILENAME = "Images/Biker_idle.png"
CHAR_DEATH_FILENAME = "Images/Biker_death.png"
CHAR_ATTACK_FILENAME = "Images/Biker_attack1.png"
CHAR_JUMP_FILENAME = "Images/Biker_jump.png"
CHAR_RUN_FILENAME = "Images/Biker_run.png"

CYBORG_DEATH_FILENAME = "Images/Cyborg_death.png"
CYBORG_IDLE_FILENAME = "Images/Cyborg_idle.png"
CYBORG_RUN_FILENAME = "Images/Cyborg_run.png"

PLATFORM_FILENAME = "Images/Platform Spritesheet.png"

PLATFORM_LIST = {"mid": (281, 203, 344, 24), "midLeft": [0, 180, 157, 23], "midRight": (875, 180, 125, 20),
                 "botMid": (344, 381, 250, 23), "botLeft": (0, 336, 188, 23), "botRight": (719, 314, 188, 23),
                 "main": [0, 526, 1000, 100], "midRight2": (875, 336, 125, 23)}
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.10
CYBORG_ACC = 0.2
PLAYER_LIVES = 3
