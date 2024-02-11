import pygame
from sys import exit
import numpy as np

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height), 0, 32)
#pygame.display.set_caption("CompGraph_Midterm - Indra Imanuel Gunawan - 20195118")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

margin = 8
pts = []
count = 0

# https://kite.com/python/docs/pygame.Surface.blit
clock = pygame.time.Clock()


done = False
screen.fill(WHITE)
while not done:
    time_passed = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill(WHITE)
            # add point
            count += 1
            x, y = pygame.mouse.get_pos()
            pygame.draw.rect(screen, BLUE, (x - margin, y - margin, 2 * margin, 2 * margin), 2)      
            pts.append([x, y])

            if 2<=count: # edge exists

                #lagrange core
                for t in np.arange(0, len(pts)-1, 0.01): # is this drawing 100 *num_points !!!!
                    ptPlt = np.zeros(2, float)
                    for i in range(len(pts)):
                        num, den = 1, 1
                        for j in range(len(pts)):
                            if j != i:
                                num = num * (t - j)
                                den = den * (i - j)
                        ptPlt = ptPlt + np.dot(pts[i], num/den)
                    pygame.draw.circle(screen, RED, ptPlt.astype(int), 3)

                #Line and rects
                for p1,p2 in zip(pts,pts[1:]):pygame.draw.line(screen, 'GREEN', p1, p2, 2)
                for x,y in pts:pygame.draw.rect(screen, BLUE, (x-margin, y-margin, 2*margin, 2*margin), 2)

        elif event.type == pygame.QUIT:             done = True

    pygame.display.update()
pygame.quit()