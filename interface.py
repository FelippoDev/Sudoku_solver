import pygame
import Solver as s
import numpy as np

change = None
new_board = []

pygame.init()
surface = pygame.display.set_mode((700, 470))
pygame.display.set_caption('Sudoku Solver Created by FelippoDev')
font = pygame.font.Font(None, 60)


def background():
    surface.fill((255, 255, 255))
    pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(10, 10, 450, 450), 3)
    x, y = 10, 10
    n = 50
    for i in range(9):
        if i % 3 == 0:
            w = 2
        else:
            w = 1
        pygame.draw.line(surface, (0, 0, 0), (x, 10), (x, 458), width=w)
        pygame.draw.line(surface, (0, 0, 0), (10, y), (458, y), width=w)
        x += n
        y += n


def draw_num():
    posX = 25
    posY = 20
    d = 50
    for x in range(9):
        if x > 0:
            posY += d
            posX = 25
        for y in range(9):
            output = s.board[x][y]
            if output != 0:
                n_text = font.render(str(output), True, (0, 0, 0))
                surface.blit(n_text, (posX, posY))
            posX += d


def solving():
    posX = 25
    posY = 20
    d = 50
    for x in range(9):
        if x > 0:
            posY += d
            posX = 25
        for y in range(9):
            output = s.result[x][y]
            n_text = font.render(str(output), True, (0, 0, 0))
            surface.blit(n_text, (posX, posY))
            posX += d


def main():
    ans = False
    run = True
    while run:
        background()
        if ans == True:
            solving()
        else:
            draw_num()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ans = True
                    solving()
        pygame.display.update()


main()
