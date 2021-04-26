import pygame

pygame.init()

surface = pygame.display.set_mode((500, 500))
surface.fill((0, 0, 0))

pygame.display.set_caption("FelippoDev Sudoku Solver")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
