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

pts = []
knots = []
count = 0
screen.fill(WHITE)

# https://kite.com/python/docs/pygame.Surface.blit
clock = pygame.time.Clock()

#Lagrange
def lagrange():
    
    screen.fill(WHITE)
    #Line and rects
    for i in range(count - 1):
        pygame.draw.line(screen, GREEN, pts[i], pts[i+1], 3)
    for i in range(count):
        pygame.draw.rect(screen, BLUE, (pts[i][0] - margin, pts[i][1] - margin, 2 * margin, 2 * margin), 5)


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
    for i in range(count - 1):
        pygame.draw.line(screen, color, pts[i], pts[i+1], thick)
    for i in range(count):
        pygame.draw.rect(screen, BLUE, (pts[i][0] - margin, pts[i][1] - margin, 2 * margin, 2 * margin), 5)
        if(count > 2):
            lagrange()

done = False
pressed = 0
margin = 6
old_pressed = 0
old_button1 = 0
old_button3 = 0

selectedPoint = -1

while not done:

    time_passed = clock.tick(30)

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = -1
            if count > 2:  lagrange()
                    
        elif event.type == pygame.MOUSEBUTTONUP:    pressed = 1
        elif event.type == pygame.QUIT:             done = True
        else:                                       pressed = 0

    button1, button2, button3 = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    pt = [x, y]

    if old_pressed == -1 and pressed == 1 and old_button1 == 1 and button1 == 0:
        print('mouse click')
        if x < 590:
            pts.append(pt)
            count += 1
            pygame.draw.rect(screen, BLUE, (pt[0] - margin, pt[1] - margin, 2 * margin, 2 * margin), 5)
    
    if len(pts) > 1:
        drawPolylines(GREEN, 3)

    pygame.display.update()
    old_button1 = button1
    old_pressed = pressed
    old_button3 = button3

pygame.quit()