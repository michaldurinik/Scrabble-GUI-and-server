from random import *
import pygame
from Board import Board
from Tile import Tile
from Player import Player

b = Board()
# print(b)
b.make_board()
# print(b)
tiles = {'t1': Tile("A", 1),
        't2': Tile("B", 3),
        't3': Tile("C", 3),
        't4': Tile("D", 2),
        't5': Tile("E", 1),
        't6': Tile("F", 4),
        't7': Tile("G", 2),
        't8': Tile("H", 4),
        't9': Tile("I", 1),
        't10': Tile("J", 8),
        't11': Tile("K", 5),
        't12': Tile("L", 1),
        't13': Tile("M", 3),
        't14': Tile("N", 1),
        't15': Tile("O", 1),
        't16': Tile("P", 3),
        't17': Tile("Q", 10),
        't18': Tile("R", 1),
        't19': Tile("S", 1),
        't20': Tile("T", 1),
        't21': Tile("U", 1),
        't22': Tile("V", 4),
        't23': Tile("W", 4),
        't24': Tile("X", 8),
        't25': Tile("Y", 4),
        't26': Tile("Z", 10),
        't27': Tile('BL', 0),
        }

tile = ['t1', 't27', 't27', 't27', 't27', 't27', 't27', 't27', 't27', 't27', 't27', 't27', 't2', 't3', 't27', 't4', 't5', 't27', 't6', 't27', 't7', 't8', 't27', 't9', 't10', 't11', 't27', 't12', 't27', 't13', 't14', 't27', 't15', 't16', 't17', 't18', 't19', 't20', 't21', 't22', 't23', 't24', 't25', 't26', 't27']
for i in range(15):
    for j in range(15):
        b.place_tile((i, j), tiles[choice(tile)])

# grid_coor = square.get_position()
# print(grid_coor)
# sq_colour = square.get_colour()
# print(sq_colour)
# for square in b:
#     print(square.get_position())
#     if square.is_occupied():
#         print(square.get_tile().get_letter(), square.get_tile().get_value())
#         # print(square.get_tile().get_value())
#     else:
#         print('Its a blank')




pygame.init()

BOARD_SIDE = 40 * 15
SQUARE_SIDE = 40
display_width = 1200
display_height = 734
rack_x =  (display_width * 0.0745) 
rack_y =  (display_height * 0.73)
player_1_score = 0
player_2_score = 780
player_3_score = 50
player_4_score = 100
remaining_tiles = 25





##############################################################################################################################################################################################################################
#                                                                   IT easy really to test, just fill the tuples with the values as shown to place letters                                                                   #
##############################################################################################################################################################################################################################


test_rack = [('T','value'), ('O','value'), ('R','value'), ('T','value'), ('U','value'), ('R','value'), ('E','value')]



tile_dict = {'A': pygame.image.load('./images/A_1.png'),
             'B': pygame.image.load('./images/B_1.png'),
             'C': pygame.image.load('./images/C_1.png'),
             'D': pygame.image.load('./images/D_1.png'),
             'E': pygame.image.load('./images/E_1.png'),
             'F': pygame.image.load('./images/F_1.png'),
             'G': pygame.image.load('./images/G_1.png'),
             'H': pygame.image.load('./images/H_1.png'),
             'I': pygame.image.load('./images/I_1.png'),
             'J': pygame.image.load('./images/J_1.png'),
             'K': pygame.image.load('./images/K_1.png'),
             'L': pygame.image.load('./images/L_1.png'),
             'M': pygame.image.load('./images/M_1.png'),
             'N': pygame.image.load('./images/N_1.png'),
             'O': pygame.image.load('./images/O_1.png'),
             'P': pygame.image.load('./images/P_1.png'),
             'Q': pygame.image.load('./images/Q_1.png'),
             'R': pygame.image.load('./images/R_1.png'),
             'S': pygame.image.load('./images/S_1.png'),
             'T': pygame.image.load('./images/T_1.png'),
             'U': pygame.image.load('./images/U_1.png'),
             'V': pygame.image.load('./images/V_1.png'),
             'W': pygame.image.load('./images/W_1.png'),
             'X': pygame.image.load('./images/X_1.png'),
             'Y': pygame.image.load('./images/Y_1.png'),
             'Z': pygame.image.load('./images/Z_1.png'),
             'BL': pygame.image.load('./images/blank_square_2.png'),
             'doubleL': pygame.image.load('./images/double_letter.png'),
             'tripleL': pygame.image.load('./images/double_word.png'),
             'doubleW': pygame.image.load('./images/triple_letter.png'),
             'tripleW': pygame.image.load('./images/triple_word.png'),
             'default': pygame.image.load('./images/blank_square_2.png'),
             }

SCREEN = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Scrabble')
pygame.display.set_icon(pygame.image.load('images/icon_scrabble.png'))
background = pygame.image.load('./images/background_2.png')
# background = (18,131,86)
blank_board = pygame.image.load('./images/blank_board.png')
blank_square = pygame.image.load('./images/blank_square_2.png')
double_letter = pygame.image.load('./images/double_letter.png')
triple_letter = pygame.image.load('./images/triple_letter.png')

x =  (display_width * 0.0)
y = (display_height * 0.0)
LEFT = 1
running = True
finished = False
# clock = pygame.time.Clock()
def screen_background():
    SCREEN.blit(pygame.transform.scale(background, (display_width,display_height)), (0,0))
    # SCREEN.fill(background)

def letter_rack(x,y):
    x =  (display_width * 0.0745) 
    y =  (display_height * 0.73)
    for i in range(7):
        SCREEN.blit(pygame.transform.scale(tile_dict[test_rack[i][0]], (SQUARE_SIDE,SQUARE_SIDE)), (x,y))
        x = x + 60


def in_play_board(board):
    x =  (display_width * 0.48)
    y =  (display_height - 714)
    for square in board:
        sq_colour = square.get_colour()
        pos = square.get_position()
        dy = y + (40 * pos[0])
        dx = x + (40 * pos[1])
        if square.is_occupied():
            if sq_colour == 'default':
                # print('occupied')
                letter = square.get_tile().get_letter()
                SCREEN.blit(pygame.transform.scale(tile_dict[letter], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))
                # print(sq_colour)
            else:
                # print('unoccupied')
                # if sq_colour != 'default':
                SCREEN.blit(pygame.transform.scale(tile_dict[sq_colour], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))

def score_board():
    items = ('SCORE BOARD','PLAYER  A', 'PLAYER  B', 'PLAYER  C', 'PLAYER  D', 'TILES REMAINING', 'SWAP','SKIP','QUIT','CONFIRM')
    x = 50
    y = 20
    i = 0
    for letter in items[0]:
        dx = x + (40 * i)
        if letter == ' ':
            pass
        else:
            SCREEN.blit(pygame.transform.scale(tile_dict[letter], (SQUARE_SIDE,SQUARE_SIDE)), (dx,y))
        i+=1
      
    x = 50
    y = 100
    i = 0
    for player in items[1:5]:
        
        j = 0
        dy = y + (70 * i)
        for letter in player:
            dx = x + (40 * j)
            if letter == ' ':
                pass
            else:
                SCREEN.blit(pygame.transform.scale(tile_dict[letter], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))
            
            j+=1
        i+=1

    x = 50
    y = 420
    i = 0
    for letter in items[-5]:
        dx = x + (40 * i)
        if letter == ' ':
            y = 460
            i = -1

        else:
            SCREEN.blit(pygame.transform.scale(tile_dict[letter], (SQUARE_SIDE,SQUARE_SIDE)), (dx,y))
        i+=1

    x = 90
    y = 640
    i = 0 
    j = 0   
    for button in items[-4:]:
        dx = x + (100 * j)
        i = 0 
        for letter in button:
            
            SCREEN.blit(pygame.transform.scale(tile_dict[letter], (SQUARE_SIDE,SQUARE_SIDE)), (dx,y))
            dx = x + (40 * i)
            i+=1
        j+=1

    
    pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
    myfont = pygame.font.SysFont('Times New Roman', 50)
    textsurface = myfont.render('{:^d}'.format(player_1_score), False, (0, 0, 0))
    SCREEN.blit(textsurface,(450,90))
    textsurface = myfont.render('{:^d}'.format(player_2_score), False, (0, 0, 0))
    SCREEN.blit(textsurface,(450,159))
    textsurface = myfont.render('{:^d}'.format(player_3_score), False, (0, 0, 0))
    SCREEN.blit(textsurface,(450,230))
    textsurface = myfont.render('{:^d}'.format(player_4_score), False, (0, 0, 0))
    SCREEN.blit(textsurface,(450,299))
    textsurface = myfont.render('{:^d}'.format(remaining_tiles), False, (0, 0, 0))
    SCREEN.blit(textsurface,(450,452))

while running:      
    # initial_board(b)
    while not finished:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                running = False
                finished = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                press = pygame.mouse.get_pos()

                if 90 + 40 > press[0] > 90 and 535 + 40 > press[1] > 535:
                    print('PRESSED TILE 1')

                elif 150 + 40 > press[0] > 90 and 535 + 40 > press[1] > 535:
                    print('PRESSED TILE 2')

                elif 210 + 40 > press[0] > 90 and 535 + 40 > press[1] > 535:
                    print('PRESSED TILE 3')

                elif 270 + 40 > press[0] > 90 and 535 + 40 > press[1] > 535:
                    print('PRESSED TILE 4')

                elif 330 + 40 > press[0] > 90 and 535 + 40 > press[1] > 535:
                    print('PRESSED TILE 5')

                elif 390 + 40 > press[0] > 90 and 535 + 40 > press[1] > 535:
                    print('PRESSED TILE 6')

                elif 450 + 40 > press[0] > 90 and 535 + 40 > press[1] > 535:
                    print('PRESSED TILE 7')

            if event.type == pygame.MOUSEBUTTONUP:
                release = pygame.mouse.get_pos()
                print('Mouse button released', release)

            screen_background()
            score_board()
            # initial_board(b)
            letter_rack(x,y)

            in_play_board(b)
            # buttons()


        
            pygame.display.update()
            # clock.tick(60)

            

pygame.quit()
quit()


# test_board = [[(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), ('I','value'), ('T','value'), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), ('O','value'), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), ('O','value'), (           ), ('A','value'), (           ), (           ), ('W','value'), ('H','value'), ('I','value'), ('L','value'), ('E','value'), (           ), (           )],
#               [(           ), (           ), (           ), ('K','value'), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), ('I','value'), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), ('B','value'), ('U','value'), ('T','value'), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), ('S','value'), ('C','value'), ('R','value'), ('A','value'), ('B','value'), ('B','value'), ('L','value'), ('E','value'), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), ('I','value'), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), ('T','value'), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), ('C','value'), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), ('H','value'), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), ('E','value'), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), ('S','value'), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )]]

# test_board = [[(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), ('I','value'), (           ), ('C','value'), ('A','value'), ('N','value'), (           ), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
#               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )]]
