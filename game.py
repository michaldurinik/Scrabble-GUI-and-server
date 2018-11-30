import pygame
from random import choice
pygame.init()

SQUARE_SIDE = 50

RED_CHECK          = (240, 150, 150)
WHITE              = (255, 255, 255)
BLUE_LIGHT         = (140, 184, 219)
BLUE_DARK          = (91,  131, 159)
GRAY_LIGHT         = (240, 240, 240)
GRAY_DARK          = (200, 200, 200)
CHESSWEBSITE_LIGHT = (212, 202, 190)
CHESSWEBSITE_DARK  = (100,  92,  89)
LICHESS_LIGHT      = (240, 217, 181)
LICHESS_DARK       = (181, 136,  99)
LICHESS_GRAY_LIGHT = (164, 164, 164)
LICHESS_GRAY_DARK  = (136, 136, 136)

BOARD_COLORS = [GRAY_LIGHT, GRAY_DARK,
                BLUE_LIGHT, BLUE_DARK,
                WHITE, BLUE_LIGHT,
                CHESSWEBSITE_LIGHT, CHESSWEBSITE_DARK,
                LICHESS_LIGHT, LICHESS_DARK,
                LICHESS_GRAY_LIGHT, LICHESS_GRAY_DARK]

CLOCK = pygame.time.Clock()
CLOCK_TICK = 15


pygame.display.set_caption("Scrabble")
pygame.display.set_icon(pygame.image.load('images/iconfinder_Scrabble-grey_190318.png'))

SCREEN = pygame.display.set_mode((15*SQUARE_SIDE, 15*SQUARE_SIDE))


def resize_screen(square_side_len):
    global SQUARE_SIDE
    global SCREEN
    SCREEN = pygame.display.set_mode((15*square_side_len, 15*square_side_len), pygame.RESIZABLE)
    SQUARE_SIDE = square_side_len


def print_empty_board():
    SCREEN.fill(BOARD_COLORS[2])
    # paint_dark_squares(BOARD_COLOR[1])


game_running = True
while game_running:
    CLOCK.tick(CLOCK_TICK)
    # pygame.time.delay(60)

    print_empty_board()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False


pygame.quit()
