import pygame
from sys import exit
import numpy as np

width = 800
height = 600
pygame.init()
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("CompGraph_Midterm - Indra Imanuel Gunawan - 20195118")

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

margin = 6
pts = []
knots = []
count = 0
screen.fill(WHITE)

# https://kite.com/python/docs/pygame.Surface.blit
clock = pygame.time.Clock()

#Lagrange
def lagrange():
    print('lagrange')
    #Line and rects
    for i in range(count - 1):        pygame.draw.line(screen, GREEN, pts[i], pts[i+1], 3)
    for i in range(count):        pygame.draw.rect(screen, BLUE, (pts[i][0] - margin, pts[i][1] - margin, 2 * margin, 2 * margin), 5)

    for t in np.arange(0, len(pts)-1, 0.01):
        ptPlt = np.zeros(2, float)
        for i in np.arange(0, len(pts), 1):
            num, den = 1, 1
            for j in np.arange(0, len(pts), 1):
                if j != i:
                    num = num * (t - j)
                    den = den * (i - j)
            ptPlt = ptPlt + np.dot(pts[i], num/den)
        pygame.draw.circle(screen, RED, ptPlt.astype(int), 3)

def drawPolylines(color='GREEN', thick=3):
    if (count < 2): return
    for i in range(count - 1):  pygame.draw.line(screen, color, pts[i], pts[i+1], thick)
    for i in range(count):      pygame.draw.rect(screen, BLUE, (pts[i][0] - margin, pts[i][1] - margin, 2 * margin, 2 * margin), 5)
    lagrange()

done = False
while not done:
    
    time_passed = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('mouse click')
            x, y = pygame.mouse.get_pos()
            pt = [x, y]
            if x < 590:
                pts.append(pt)
                count += 1
                
                pygame.draw.rect(screen, BLUE, (pt[0] - margin, pt[1] - margin, 2 * margin, 2 * margin), 5)      

            if len(pts) > 1:
                screen.fill(WHITE)
                drawPolylines(GREEN, 3)
        elif event.type == pygame.QUIT:             done = True

    pygame.display.update()
pygame.quit()