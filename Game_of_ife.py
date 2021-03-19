import pygame
from pygame.locals import *

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 640))
pygame.display.set_caption('Life')

# macro definitions
FPS = 30
pause = True
cell_check = (0, 0)
cell_check1 = (0, 0)
cell_check2 = (0, 0)
cell_check3 = (0, 0)
cell_check4 = (0, 0)
cell_check5 = (0, 0)
cell_check6 = (0, 0)
cell_check7 = (0, 0)
cell_check8 = (0, 0)
cell_around = 0
cell_set = (-10, -10)
cell_count = 0
cell_pos = (-10, -10)
cell = pygame.Surface((10, 10))
cell.fill((0, 0, 0))
cell1 = pygame.Surface((10, 10))
cell1.fill((20, 20, 20))
cells = []
cellspast = []
cellspast += cells

# main loop
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        # reacting to touch
        if event.type == MOUSEBUTTONDOWN:
            mouse_width, mouse_height = pygame.mouse.get_pos()
            cell_pos = (round(mouse_width / 10)) * 10, (round(mouse_height / 10)) * 10
            if mouse_width > 650:
                if not pause:
                    pause = True
                else:
                    pause = False
            elif cell_count == 0:
                cells.append(cell_pos)
                cell_count = cell_count + 1
            # adding or deleting cells
            else:
                for i in range(0, cell_count):
                    cell_set = cell_pos
                    if cells.count(cell_set) != 0:
                        cell_remove = cell_set
                        cells.remove(cell_remove)
                        cell_count = cell_count - 1
                        break
                    else:
                        cells.append(cell_set)
                        cell_count = cell_count + 1
                        break

        # printing
        screen.fill((255, 255, 255))
        if cells:
            for i in range(0, cell_count):
                screen.blit(cell, cells[i])

        for x in range(0, 640, 10):  # Draw vertical lines
            pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 640))
        for y in range(0, 640, 10):  # Draw vertical lines
            pygame.draw.line(screen, (40, 40, 40), (0, y), (640, y))

        pygame.display.update()

    # logic of game

    if not pause:
        for i in range(0, 65):
            for j in range(0, 65):
                #  -1 1     0 1   1 1
                #  -1 0     0 0   1 0
                #  -1 -1    0 -1  1 -1
                cell_check = (j * 10, i * 10)
                cell_check1 = (j * 10 - 10, i * 10 - 10)
                cell_check2 = (j * 10, i * 10 - 10)
                cell_check3 = (j * 10 + 10, i * 10 - 10)
                cell_check4 = (j * 10 + 10, i * 10)
                cell_check5 = (j * 10 + 10, i * 10 + 10)
                cell_check6 = (j * 10 - 10, i * 10)
                cell_check7 = (j * 10 - 10, i * 10 + 10)
                cell_check8 = (j * 10, i * 10 + 10)
                # print(cell_check1, cell_check2, cell_check3, cell_check4, cell_check5, cell_check6, cell_check7,
                # cell_check8)

                if cellspast.count(cell_check1) != 0:
                    cell_around = cell_around + 1

                if cellspast.count(cell_check2) != 0:
                    cell_around = cell_around + 1

                if cellspast.count(cell_check3) != 0:
                    cell_around = cell_around + 1

                if cellspast.count(cell_check4) != 0:
                    cell_around = cell_around + 1

                if cellspast.count(cell_check5) != 0:
                    cell_around = cell_around + 1

                if cellspast.count(cell_check6) != 0:
                    cell_around = cell_around + 1

                if cellspast.count(cell_check7) != 0:
                    cell_around = cell_around + 1

                if cellspast.count(cell_check8) != 0:
                    cell_around = cell_around + 1

                if cell_around < 2 or cell_around > 3:
                    if cellspast.count(cell_check) != 0:
                        cells.remove(cell_check)
                        cell_count = cell_count - 1

                if cell_around == 3:
                    if cellspast.count(cell_check) == 0:
                        cells.append(cell_check)
                        cell_count = cell_count + 1
                cell_around = 0

        cellspast = []
        cellspast += cells
        # printing
        screen.fill((255, 255, 255))
        if cells:
            for i in range(0, cell_count):
                screen.blit(cell, cells[i])

        for x in range(0, 640, 10):  # Draw vertical lines
            pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 640))
        for y in range(0, 640, 10):  # Draw vertical lines
            pygame.draw.line(screen, (40, 40, 40), (0, y), (640, y))

        pygame.display.update()
