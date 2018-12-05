import pygame
from random import *
from Square import Square
from Board import Board
from Tile import Tile
from Player import Player
import pygame.locals as loc
from copy import deepcopy

SQUARE_SIDE = 40
BOARD_SIDE = 40 * 15
display_width = 1200
display_height = 734
player_1_score = 00
player_2_score = 00
player_3_score = 00
player_4_score = 00
remaining_tiles = 93

pygame.display.set_caption('Our Scrabble Game')
background = pygame.image.load('./images/background_3.png')
blank_board = pygame.image.load('./images/blank_board.png')
SCREEN = pygame.display.set_mode((display_width,display_height))
blank_square = pygame.image.load('./images/blank_square_2.png')
double_letter = pygame.image.load('./images/double_letter.png')
triple_letter = pygame.image.load('./images/triple_letter.png')
pygame.display.set_icon(pygame.image.load('images/icon_scrabble.png'))

x =  (display_width * 0.0)
y =  (display_height * 0.0)

running = True
finished = False
holding = False

rack_dict = {}
tile = ['t1', 't27', 't27', 't27', 't27', 't27', 't27', 't27', 't27', 't27', 't27', 't27', 't2', 't3', 't27', 't4', 't5', 't27', 't6', 't27', 't7', 't8', 't27', 't9', 't10', 't11', 't27', 't12', 't27', 't13', 't14', 't27', 't15', 't16', 't17', 't18', 't19', 't20', 't21', 't22', 't23', 't24', 't25', 't26', 't27']
button_grid = ((90, 130), (565, 605)), ((150, 190), (565, 605)), ((210, 250), (565, 605)), ((270, 310), (565, 605)), ((330, 370), (565, 605)), ((390, 430), (565, 605)), ((450, 490), (565, 605)), ((160, 320), (40, 660)), ((360, 520), (40, 660)), ((560, 720), (40, 660)), ((760, 920), (40, 660))
rack_grid = (((90, 130), (565, 605)), ((150, 190), (565, 605)), ((210, 250), (565, 605)), ((270, 310), (565, 605)), ((330, 370), (565, 605)), ((390, 430), (565, 605)), ((450, 490), (565, 605)))
test_rack = [('O','value'), ('U','value'), ('R','value'), ('G','value'), ('A','value'), ('M','value'), ('E','value')]
score_items = ('SCORE BOARD','PLAYER  A', 'PLAYER  B', 'PLAYER  C', 'PLAYER  D', 'TILES REMAINING')

b = Board()
# (b)
b.make_board()
b1 = deepcopy(b)
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
        't27': Tile('#', 0),
        }

tile_dict = {'A': (pygame.image.load('./images/A_1.png'),1,'A'),
             'B': (pygame.image.load('./images/B_1.png'),3,'B'),
             'C': (pygame.image.load('./images/C_1.png'),3,'C'),
             'D': (pygame.image.load('./images/D_1.png'),2,'D'),
             'E': (pygame.image.load('./images/E_1.png'),1,'E'),
             'F': (pygame.image.load('./images/F_1.png'),4,'F'),
             'G': (pygame.image.load('./images/G_1.png'),2,'G'),
             'H': (pygame.image.load('./images/H_1.png'),4,'H'),
             'I': (pygame.image.load('./images/I_1.png'),1,'I'),
             'J': (pygame.image.load('./images/J_1.png'),8,'J'),
             'K': (pygame.image.load('./images/K_1.png'),5,'K'),
             'L': (pygame.image.load('./images/L_1.png'),1,'L'),
             'M': (pygame.image.load('./images/M_1.png'),3,'M'),
             'N': (pygame.image.load('./images/N_1.png'),1,'N'),
             'O': (pygame.image.load('./images/O_1.png'),1,'O'),
             'P': (pygame.image.load('./images/P_1.png'),3,'P'),
             'Q': (pygame.image.load('./images/Q_1.png'),10,'Q'),
             'R': (pygame.image.load('./images/R_1.png'),1,'R'),
             'S': (pygame.image.load('./images/S_1.png'),1,'S'),
             'T': (pygame.image.load('./images/T_1.png'),1,'T'),
             'U': (pygame.image.load('./images/U_1.png'),1,'U'),
             'V': (pygame.image.load('./images/V_1.png'),4,'V'),
             'W': (pygame.image.load('./images/W_1.png'),4,'W'),
             'X': (pygame.image.load('./images/X_1.png'),8,'X'),
             'Y': (pygame.image.load('./images/Y_1.png'),4,'Y'),
             'Z': (pygame.image.load('./images/Z_1.png'),10,'Z'),
             '#': (pygame.image.load('./images/blank_square_2.png'),0,'#'),
            }

bonus_dict = {
             'CS': (pygame.image.load('./images/center_square.png'),0,'CS'),
             'doubleL': (pygame.image.load('./images/double_letter.png'),0,'#'),
             'tripleL': (pygame.image.load('./images/double_word.png'),0,'#'),
             'doubleW': (pygame.image.load('./images/triple_letter.png'),0,'#'),
             'tripleW': (pygame.image.load('./images/triple_word.png'),0,'#'),
             'default': (pygame.image.load('./images/blank_square_2.png'),0,'#'),
             }

for square in enumerate(b):
    pos = square.tile.get_position()
    (i, j) = (pos[0], pos[1]) 
    if (i, j) != (7, 7) and square.get_colour() != 'default':
        b.place_tile((i, j), Tile(tile_dict[square.get_colour()][0], bonus_dict[square.get_colour()][0]))

for i in range(15):
    for j in range(15):
        if (i, j) != (7, 7) and square.get_colour() == 'default':
            b.place_tile((i, j), Tile(tile_dict[square.get_colour()][0], bonus_dict[square.get_colour()][2][1]))

            
        else:
            b.place_tile((i, j), Tile('CS'))

pygame.init()

def draw_rack():
    i = 0
    while i < len(test_rack):
        if test_rack[i] == (0,0):
            rack_dict[test_rack[i]] = ()
        else:
            rack_dict[rack_grid[i]] = tile_dict[test_rack[i][0]]
            i+=1

draw_rack()
# clock = pygame.time.Clock()
def get_image(press_x, press_y):
    for (k, v) in rack_dict.items():
        if k[0][1] > press_x > k[0][0] and k[1][1] > press_y > k[1][0]:
            return v

def grab(press):
    image = get_image(press[0], press[1])
    holding = True
    print('Im holding an image')
    print(image)
    return image, holding

def drop():
    holding = False
    print('Ive dropped the image')

def board_grid(press_x, press_y):
    x =  (display_width * 0.48)
    y =  (display_height - 714)
    i = ((press_x - x) // 40)
    j = ((press_y - y) // 40)
    return (i, j)

def screen_background():
    SCREEN.blit(pygame.transform.scale(background, (display_width,display_height)), (0,0))

def letter_rack(x,y):
    x =  (display_width * 0.0745) 
    y =  565
    for i in range(7):
        if test_rack[i] != (0,0):
            SCREEN.blit(pygame.transform.scale(tile_dict[test_rack[i][0]][0], (SQUARE_SIDE,SQUARE_SIDE)), (x,y))
        x = x + 60

def in_play_board(b, initial=True):
    x =  (display_width * 0.48)
    y =  (display_height - 714)
    for square in b:
        sq_colour = square.get_colour()
        pos = square.get_position()
        # print(pos = square.get_position())
        dy = y + (40 * pos[0])
        dx = x + (40 * pos[1])
        if square.is_occupied():
            if sq_colour == 'default':
                letter = square.get_tile().get_letter()
                # print(letter)
                if letter[0] == '#':
                    SCREEN.blit(pygame.transform.scale(tile_dict['#'][0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))
                else:
                    SCREEN.blit(pygame.transform.scale(tile_dict[letter][0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))
                # print(sq_colour)
            else:
                if initial:
                    pos = square.get_position()
                    if pos == [7, 7]:
                        SCREEN.blit(pygame.transform.scale(tile_dict['CS'][0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))
                    else:
                        SCREEN.blit(pygame.transform.scale(tile_dict[sq_colour][0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))
                    initial = False
                
                else:
                    letter = square.get_tile().get_letter()
                    # print(letter[0])
                    SCREEN.blit(pygame.transform.scale(tile_dict[letter[0]][0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))
                

def score_board():
    def scoreboard():
        x = 50
        y = 20
        i = 0
        for letter in score_items[0]:
            dx = x + (40 * i)
            if letter == ' ':
                pass
            else:
                SCREEN.blit(pygame.transform.scale(tile_dict[letter][0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,y))
            i+=1
      
    def players():
        y = 100
        i = 0
        for player in score_items[1:5]:
            j = 0
            dy = y + (70 * i)
            for letter in player:
                dx = x + (40 * j)
                if letter == ' ':
                    pass
                else:
                    SCREEN.blit(pygame.transform.scale(tile_dict[letter][0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))
                j+=1
            i+=1

    def remaining():
            x = 50
            y = 420
            i = 0
            for letter in score_items[-1]:
                dx = x + (40 * i)
                if letter == ' ':
                    y = 460
                    i = -1
                else:
                    SCREEN.blit(pygame.transform.scale(tile_dict[letter][0], (SQUARE_SIDE,SQUARE_SIDE)), (dx,y))
                i+=1

    def button_print():
        buttons = ('RESET','SWAP','SKIP','QUIT','CONFIRM')
        x = -40
        y = 660
        i = 0 
        j = 0   
        for button in buttons:
            x = x + 40
            for letter in button:
                # print(letter)
                x = x + 40 
                SCREEN.blit(pygame.transform.scale(tile_dict[letter][0], (SQUARE_SIDE,SQUARE_SIDE)), (x,y))
                i+=1
            j+=1

    scoreboard()
    remaining()
    players()
    button_print()
    
    pygame.font.init()
    myfont = pygame.font.SysFont('Times New Roman', 50)
    textsurface = myfont.render('{:>d}'.format(player_1_score), False, (0, 0, 0))
    SCREEN.blit(textsurface,(450,90))
    textsurface = myfont.render('{:>d}'.format(player_2_score), False, (0, 0, 0))
    SCREEN.blit(textsurface,(450,159))
    textsurface = myfont.render('{:>d}'.format(player_3_score), False, (0, 0, 0))
    SCREEN.blit(textsurface,(450,230))
    textsurface = myfont.render('{:>d}'.format(player_4_score), False, (0, 0, 0))
    SCREEN.blit(textsurface,(450,299))
    textsurface = myfont.render('{:>d}'.format(remaining_tiles), False, (0, 0, 0))
    SCREEN.blit(textsurface,(450,452))


pygame.init()
while running:      
    pos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            rack_copy = test_rack
            press = pygame.mouse.get_pos()

            if  680 + 160 > pos[0] > 680 and 660 + 40 > pos[1] > 660:
                print('PRESSED QUIT BUTTON')
                running = False
                quit()

            if 90 + 40 > press[0] > 90 and 565 + 40 > press[1] > 565:
                this_is = 0
                print('PRESSED TILE 1')
                if holding == False:
                    image, holding = grab(press)
                elif holding:
                    holding = False
                    print('Ive dropped the image')
                                                              

            elif 150 + 40 > press[0] > 150 and 565 + 40 > press[1] > 565:
                this_is = 1
                print('PRESSED TILE 2')
                if holding == False:
                    image, holding = grab(press)
                elif holding:
                    holding = False
                    print('Ive dropped the image')

            elif 210 + 40 > press[0] > 210 and 565 + 40 > press[1] > 565:
                this_is = 2
                print('PRESSED TILE 3')
                if holding == False:
                    image, holding = grab(press)
                elif holding:
                    holding = False
                    print('Ive dropped the image')

            elif 270 + 40 > press[0] > 270 and 565 + 40 > press[1] > 565:
                this_is = 3
                print('PRESSED TILE 4')
                if holding == False:
                    image, holding = grab(press)
                elif holding:
                    holding = False
                    print('Ive dropped the image')

            elif 330 + 40 > press[0] > 330 and 565 + 40 > press[1] > 565:
                this_is = 4
                print('PRESSED TILE 5')
                if holding == False:
                    image, holding = grab(press)
                elif holding:
                    holding = False
                    print('Ive dropped the image')

            elif 390 + 40 > press[0] > 390 and 565 + 40 > press[1] > 565:
                this_is = 5
                print('PRESSED TILE 6')
                if holding == False:
                    image, holding = grab(press)
                elif holding:
                    holding = False
                    print('Ive dropped the image')

            elif 450 + 40 > press[0] > 450 and 565 + 40 > press[1] > 565:
                this_is = 6
                print('PRESSED TILE 7')
                if holding == False:
                    image, holding = grab(press)
                elif holding:
                    holding = False
                    print('Ive dropped the image')
            
            elif 40 + 200 > press[0] > 40 and 660 + 40 > press[1] > 660:
                test_rack = rack_copy
                b = b1
                print('PRESSED  RESET BUTTON')

            elif 280 + 160 > press[0] > 280 and 660 + 40 > press[1] > 660:
                print('PRESSED  SWAP BUTTON')

            elif 480 + 160 > press[0] > 480 and 660 + 40 > press[1] > 660:
                print('PRESSED SKIP BUTTON')

            elif 680 + 160 > press[0] > 680 and 660 + 40 > press[1] > 660:
                print('PRESSED QUIT BUTTON')

            elif 880 + 280 > press[0] > 880 and 660 + 40 > press[1] > 660:
                print('PRESSED CONFIRM BUTTON')

            elif 1175 > press[0] > 576 and 620 > press[1] > 20:
                i = int(board_grid(press[0], press[1])[0]) 
                j = int(board_grid(press[0], press[1])[1]) 
                print('YOU PRESSED SQUARE ROW {} COLUMN {}'.format(i+1, j+1))
                if holding == True:
                    for k,v in tile_dict.items():
                        if v[0] == image[0]:
                            b.place_tile((j,i), Tile(v[2],v[1]))
                            print('I placed the image')
                            test_rack[this_is] = (0,0)
                            holding = False

        elif event.type == pygame.MOUSEBUTTONUP:
            release = pygame.mouse.get_pos()
            # print('Mouse button released', release)
     
    screen_background()
    score_board()
    letter_rack(x,y)

    in_play_board(b)
   
    pygame.display.update()
    # clock.tick(60print

            

pygame.quit()
quit()

# Pygame Drag'n'Drop Example

# """


# def main():
#     # standard init stuff
#     pygame.init()
#     screen = pygame.display.set_mode((640, 400))
#     pygame.display.set_caption("pygame drag'n'drop example - by jug")
#     clock = pygame.time.Clock()

#     # create a rect as simple object to drag'n'drop
#     rect = pygame.Rect(10,10,50,50)

#     # in this variable we will save the offset from the topleft of our rect
#     # to the mouse pointer
#     offset = None

#     # start the mainloop
#     while 1:
#         # limit fps to 40
#         clock.tick(40)

#         # handle events
#         for event in pygame.event.get():
#             # standard events to exit the program
#             if event.type == loc.QUIT:
#                 return
#             elif event.type == loc.KEYDOWN:
#                 if event.key == loc.K_ESCAPE:
#                     return
#             # if a button is pressed above the rect,
#             # save the offset and start dragging
#             elif (event.type == loc.MOUSEBUTTONDOWN
#                   and rect.collidepoint(event.pos)):
#                 mouse_x, mouse_y = event.pos
#                 my_x, my_y = rect.topleft
#                 offset = mouse_x - my_x, mouse_y - my_y
#         # if no button is pressed anymore, stop dragging
#         # I use mouse.get_pressed and not MOUSEBUTTONUP here to make sure
#         # we don't lose the mouse release
#         if not any(pygame.mouse.get_pressed()):
#             offset = None
#         # if we have an offset, ie if we are dragging, calculate the new
#         # position with the current mouse position and our offset
#         if offset:
#             mouse_x, mouse_y = pygame.mouse.get_pos()
#             off_x, off_y = offset
#             rect.topleft = mouse_x - off_x, mouse_y - off_y

#         # fill the screen, draw the rect and flip it
#         screen.fill((200,200,200))
#         screen.fill((0,0,0), rect)
#         pygame.display.flip()

# if __name__ == '__main__': 
#     main()
from random import *
import pygame
from Board import Board
from Tile import Tile
from Player import Player
import pygame.locals as loc

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
        't27': Tile('#', 0),
        }

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
             '#': pygame.image.load('./images/blank_square_2.png'),
             'CS': pygame.image.load('./images/center_square.png'),
             'doubleL': pygame.image.load('./images/double_letter.png'),
             'tripleL': pygame.image.load('./images/double_word.png'),
             'doubleW': pygame.image.load('./images/triple_letter.png'),
             'tripleW': pygame.image.load('./images/triple_word.png'),
             'default': pygame.image.load('./images/blank_square_2.png'),
             }
tile = ['t1', 't27', 't27', 't27', 't27', 't27', 't27', 't27', 't27', 't27', 't27', 't27', 't2', 't3', 't27', 't4', 't5', 't27', 't6', 't27', 't7', 't8', 't27', 't9', 't10', 't11', 't27', 't12', 't27', 't13', 't14', 't27', 't15', 't16', 't17', 't18', 't19', 't20', 't21', 't22', 't23', 't24', 't25', 't26', 't27']
for i in range(15):
    for j in range(15):
        # b.place_tile((i, j), tiles[choice(tile)])
        b.place_tile((i, j), tiles['t27'])

pygame.init()

BOARD_SIDE = 40 * 15
SQUARE_SIDE = 40
display_width = 1200
display_height = 734
rack_x = (display_width * 0.0745) 
rack_y = (display_height * 0.73)
player_1_score = 00
player_2_score = 00
player_3_score = 00
player_4_score = 00
remaining_tiles = 100
rack_1 = ((90, 130),(565, 605))# print('PRESSED TILE 1')
rack_2 = ((150, 190),(565, 605))# print('PRESSED TILE 2')
rack_3 = ((210, 250),(565, 605))# print('PRESSED TILE 3')
rack_4 = ((270, 310),(565, 605))# print('PRESSED TILE 4')
rack_5 = ((330, 370),(565, 605))# print('PRESSED TILE 5')
rack_6 = ((390, 430),(565, 605))# print('PRESSED TILE 6')
rack_7 = ((450, 490),(565, 605))# print('PRESSED TILE 7')
swap = ((160, 320), (40, 660))#  print('PRESSED  SWAP BUTTON')
skip = ((360, 520), (40, 660))# print('PRESSED SKIP BUTTON')
quit = ((560, 720), (40, 660))# print('PRESSED QUIT BUTTON')
confirm = ((760, 920), (40, 660))# print('PRESSED CONFIRM BUTTON')

button_grid = ((90, 130), (565, 605)), ((150, 190), (565, 605)), ((210, 250), (565, 605)), ((270, 310), (565, 605)), ((330, 370), (565, 605)), ((390, 430), (565, 605)), ((450, 490), (565, 605)), ((160, 320), (40, 660)), ((360, 520), (40, 660)), ((560, 720), (40, 660)), ((760, 920), (40, 660))

rack_dict = {}
rack_grid = (((90, 130), (565, 605)), ((150, 190), (565, 605)), ((210, 250), (565, 605)), ((270, 310), (565, 605)), ((330, 370), (565, 605)), ((390, 430), (565, 605)), ((450, 490), (565, 605)))
test_rack = [('O','value'), ('U','value'), ('R','value'), ('G','value'), ('A','value'), ('M','value'), ('E','value')]
i = 0
while i < len(test_rack):
    rack_dict[rack_grid[i]] = tile_dict[test_rack[i][0]]
    i+=1


# for item in 
# print(rack_dict)
# print(tile_dict)






SCREEN = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Our Scrabble Game')
pygame.display.set_icon(pygame.image.load('images/icon_scrabble.png'))
background = pygame.image.load('./images/background_3.png')
# background = (18,131,86)
blank_board = pygame.image.load('./images/blank_board.png')
blank_square = pygame.image.load('./images/blank_square_2.png')
double_letter = pygame.image.load('./images/double_letter.png')
triple_letter = pygame.image.load('./images/triple_letter.png')


x =  (display_width * 0.0)
y =  (display_height * 0.0)

LEFT = 1
running = True
finished = False
offset = None

# clock = pygame.time.Clock()
def get_image(press_x, press_y):   #rack_1 = ((90, 130),(565, 605))# print('PRESSED TILE 1')
    for (k, v) in rack_dict.items():
        if k[0][1] > press_x > k[0][0] and k[1][1] > press_y > k[1][0]:
            return v


def board_grid(press_x, press_y):
    x =  (display_width * 0.48)
    y =  (display_height - 714)

    i = ((press_x - x) // 40)
    j = ((press_y - y) // 40)
    return (i, j)

def screen_background():
    SCREEN.blit(pygame.transform.scale(background, (display_width,display_height)), (0,0))
    # SCREEN.fill(background)

def letter_rack(x,y):
    x =  (display_width * 0.0745) 
    y =  565
    for i in range(7):
        SCREEN.blit(pygame.transform.scale(tile_dict[test_rack[i][0]], (SQUARE_SIDE,SQUARE_SIDE)), (x,y))
        x = x + 60


def in_play_board(board):
    x =  (display_width * 0.48)
    y =  (display_height - 714)
    for square in board:
        sq_colour = square.get_colour()
        pos = square.get_position()
        # print(pos = square.get_position()pos)
        dy = y + (40 * pos[0])
        dx = x + (40 * pos[1])
        if square.is_occupied():
            if sq_colour == 'default':
                # pass
                # print('occupied')
                letter = square.get_tile().get_letter()
                SCREEN.blit(pygame.transform.scale(tile_dict[letter], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))
                # print(sq_colour)
            else:
                pos = square.get_position()

                if pos == [7, 7]:
                    SCREEN.blit(pygame.transform.scale(tile_dict['CS'], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))
                # print('unoccupied')
                # if sq_colour != 'default':
                else:
                    SCREEN.blit(pygame.transform.scale(tile_dict[sq_colour], (SQUARE_SIDE,SQUARE_SIDE)), (dx,dy))

def score_board():
    items = ('SCORE BOARD','PLAYER  A', 'PLAYER  B', 'PLAYER  C', 'PLAYER  D', 'TILES REMAINING')
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
    for letter in items[-1]:
        dx = x + (40 * i)
        if letter == ' ':
            y = 460
            i = -1
        else:
            SCREEN.blit(pygame.transform.scale(tile_dict[letter], (SQUARE_SIDE,SQUARE_SIDE)), (dx,y))
        i+=1

    buttons = ('SWAP','SKIP','QUIT','CONFIRM')
    x = 80
    y = 660
    i = 0 
    j = 0   
    for button in buttons:
        x = x + 40
        for letter in button:
            # print(letter)
            x = x + 40 
            SCREEN.blit(pygame.transform.scale(tile_dict[letter], (SQUARE_SIDE,SQUARE_SIDE)), (x,y))
            i+=1
        j+=1
    
    pygame.font.init()
    myfont = pygame.font.SysFont('Times New Roman', 50)
    textsurface = myfont.render('{:>d}'.format(player_1_score), False, (0, 0, 0))
    SCREEN.blit(textsurface,(450,90))
    textsurface = myfont.render('{:>d}'.format(player_2_score), False, (0, 0, 0))
    SCREEN.blit(textsurface,(450,159))
    textsurface = myfont.render('{:>d}'.format(player_3_score), False, (0, 0, 0))
    SCREEN.blit(textsurface,(450,230))
    textsurface = myfont.render('{:>d}'.format(player_4_score), False, (0, 0, 0))
    SCREEN.blit(textsurface,(450,299))
    textsurface = myfont.render('{:>d}'.format(remaining_tiles), False, (0, 0, 0))
    SCREEN.blit(textsurface,(450,452))

while running:      
    # initial_board(b)
    while not finished:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
                # create a rect as simple object to drag'n'drop
            # rect = pygame.Rect(40,40,40,40)


            if event.type == pygame.QUIT:
                pygame.quit()
                # quit()
                running = False
                finished = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                press = pygame.mouse.get_pos()
                print(press)
                

                if 90 + 40 > press[0] > 90 and 565 + 40 > press[1] > 565:
                    # print('PRESSED TILE 1')
                    print(get_image(press[0], press[1]))

                elif 150 + 40 > press[0] > 150 and 565 + 40 > press[1] > 565:
                    print('PRESSED TILE 2')
                    print(get_image(press[0], press[1]))

                elif 210 + 40 > press[0] > 210 and 565 + 40 > press[1] > 565:
                    print('PRESSED TILE 3')
                    print(get_image(press[0], press[1]))

                elif 270 + 40 > press[0] > 270 and 565 + 40 > press[1] > 565:
                    print('PRESSED TILE 4')
                    print(get_image(press[0], press[1]))

                elif 330 + 40 > press[0] > 330 and 565 + 40 > press[1] > 565:
                    print('PRESSED TILE 5')
                    print(get_image(press[0], press[1]))

                elif 390 + 40 > press[0] > 390 and 565 + 40 > press[1] > 565:
                    print('PRESSED TILE 6')
                    print(get_image(press[0], press[1]))

                elif 450 + 40 > press[0] > 450 and 565 + 40 > press[1] > 565:
                    print('PRESSED TILE 7')
                    print(get_image(press[0], press[1]))

                elif 160 + 160 > press[0] > 160 and 660 + 40 > press[1] > 660:
                    print('PRESSED  SWAP BUTTON')

                elif 360 + 160 > press[0] > 360 and 660 + 40 > press[1] > 660:
                    print('PRESSED SKIP BUTTON')

                elif 560 + 160 > press[0] > 560 and 660 + 40 > press[1] > 660:
                    print('PRESSED QUIT BUTTON')

                elif 760 + 280 > press[0] > 760 and 660 + 40 > press[1] > 660:
                    print('PRESSED CONFIRM BUTTON')

                elif 1175 > press[0] > 576 and 620 > press[1] > 20:
                    i = int(board_grid(press[0], press[1])[0]) + 1
                    j = int(board_grid(press[0], press[1])[1]) + 1
                    print('YOU PRESSED SQUARE ROW {} COLUMN {}'.format(i, j))

            if event.type == pygame.MOUSEBUTTONUP:
                release = pygame.mouse.get_pos()
                print('Mouse button released', release)
         

                # if event.type == loc.KEYDOWN:
                #     if event.key == loc.K_ESCAPE:
                #         return
                # if a button is pressed above the rect,
                # save the offset and start dragging
            # if (event.type == loc.MOUSEBUTTONDOWN and rect.collidepoint(event.pos)):
            #     mouse_x, mouse_y = event.pos
            #     my_x, my_y = rect.topleft
            #     offset = mouse_x - my_x, mouse_y - my_y
            # # if no button is pressed anymore, stop dragging
            # # I use mouse.get_pressed and not MOUSEBUTTONUP here to make sure
            # # we don't lose the mouse release
            # if not any(pygame.mouse.get_pressed()):
            #     offset = None
            # # if we have an offset, ie if we are dragging, calculate the new
            # # position with the current mouse position and our offset
            # if offset:
            #     mouse_x, mouse_y = pygame.mouse.get_pos()
            #     off_x, off_y = offset
            #     rect.topleft = mouse_x - off_x, mouse_y - off_y

            

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


# # test_board = [[(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), ('I','value'), ('T','value'), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), ('O','value'), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), ('O','value'), (           ), ('A','value'), (           ), (           ), ('W','value'), ('H','value'), ('I','value'), ('L','value'), ('E','value'), (           ), (           )],
# #               [(           ), (           ), (           ), ('K','value'), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), ('I','value'), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), ('B','value'), ('U','value'), ('T','value'), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), ('S','value'), ('C','value'), ('R','value'), ('A','value'), ('B','value'), ('B','value'), ('L','value'), ('E','value'), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), ('I','value'), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), ('T','value'), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), ('C','value'), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), ('H','value'), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), ('E','value'), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), ('S','value'), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )]]

# # test_board = [[(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), ('I','value'), (           ), ('C','value'), ('A','value'), ('N','value'), (           ), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )],
# #               [(           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           ), (           )]]

                # if 90 + 40 > press[0] > 90 and 565 + 40 > press[1] > 565:
                #     print('PRESSED TILE 1')

                # elif 150 + 40 > press[0] > 150 and 565 + 40 > press[1] > 565:
                #     print('PRESSED TILE 2')

                # elif 210 + 40 > press[0] > 210 and 565 + 40 > press[1] > 565:
                #     print('PRESSED TILE 3')

                # elif 270 + 40 > press[0] > 270 and 565 + 40 > press[1] > 565:
                #     print('PRESSED TILE 4')

                # elif 330 + 40 > press[0] > 330 and 565 + 40 > press[1] > 565:
                #     print('PRESSED TILE 5')

                # elif 390 + 40 > press[0] > 390 and 565 + 40 > press[1] > 565:
                #     print('PRESSED TILE 6')

                # elif 450 + 40 > press[0] > 450 and 565 + 40 > press[1] > 565:
                #     print('PRESSED TILE 7')

                # elif 160 + 160 > press[0] > 160 and 660 + 40 > press[1] > 660:
                #     print('PRESSED  SWAP BUTTON')

                # elif 360 + 160 > press[0] > 360 and 660 + 40 > press[1] > 660:
                #     print('PRESSED SKIP BUTTON')

                # elif 560 + 160 > press[0] > 560 and 660 + 40 > press[1] > 660:
                #     print('PRESSED QUIT BUTTON')

                # elif 760 + 280 > press[0] > 760 and 660 + 40 > press[1] > 660:
                #     print('PRESSED CONFIRM BUTTON')

# """
# Pygame Drag'n'Drop Example

# """


# def main():
#     # standard init stuff
#     pygame.init()
#     screen = pygame.display.set_mode((640, 400))
#     pygame.display.set_caption("pygame drag'n'drop example - by jug")
#     clock = pygame.time.Clock()

#     # create a rect as simple object to drag'n'drop
#     rect = pygame.Rect(10,10,50,50)

#     # in this variable we will save the offset from the topleft of our rect
#     # to the mouse pointer
#     offset = None

#     # start the mainloop
#     while 1:
#         # limit fps to 40
#         clock.tick(40)

#         # handle events
#         for event in pygame.event.get():
#             # standard events to exit the program
#             if event.type == loc.QUIT:
#                 return
#             elif event.type == loc.KEYDOWN:
#                 if event.key == loc.K_ESCAPE:
#                     return
#             # if a button is pressed above the rect,
#             # save the offset and start dragging
#             elif (event.type == loc.MOUSEBUTTONDOWN
#                   and rect.collidepoint(event.pos)):
#                 mouse_x, mouse_y = event.pos
#                 my_x, my_y = rect.topleft
#                 offset = mouse_x - my_x, mouse_y - my_y
#         # if no button is pressed anymore, stop dragging
#         # I use mouse.get_pressed and not MOUSEBUTTONUP here to make sure
#         # we don't lose the mouse release
#         if not any(pygame.mouse.get_pressed()):
#             offset = None
#         # if we have an offset, ie if we are dragging, calculate the new
#         # position with the current mouse position and our offset
#         if offset:
#             mouse_x, mouse_y = pygame.mouse.get_pos()
#             off_x, off_y = offset
#             rect.topleft = mouse_x - off_x, mouse_y - off_y

#         # fill the screen, draw the rect and flip it
#         screen.fill((200,200,200))
#         screen.fill((0,0,0), rect)
#         pygame.display.flip()

# if __name__ == '__main__': 
#     main()
