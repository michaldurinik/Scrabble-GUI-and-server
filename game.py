import pygame
pygame.init()

window = pygame.display.set_mode((1024, 1024))
pygame.display.set_caption("Scrabble")

game_running = True
while game_running:
    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

pygame.quit()
