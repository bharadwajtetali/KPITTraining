import pygame, random, sys
from pygame.locals import *

#List of possibilities where snake can collide the apple/itself
#x1,y1 = co-ordinates of snake
#x2,y2 = can be co-ordinates of snake/apple
#w1,w2,h1,h2 = width and height of snake/apple  
def collide(x1, x2, y1, y2, w1, w2, h1, h2):
    if x1 + w1 > x2 and x1 < x2 + w2 and y1 + h1 > y2 and y1 < y2 + h2:
        return True
    else:
        return False

#When the player dies, this function is called
def die(screen, score):
    f = pygame.font.SysFont('Arial', 30)
    t = f.render('Your score was: ' + str(score), True, (0, 0, 0))
    screen.blit(t, (10, 270))
    pygame.display.update()
    pygame.time.wait(2000)
    sys.exit(0)

#Initial snake location
xs = [290, 290, 290, 290, 290]
ys = [290, 270, 250, 230, 210]

#snake direction
sdir = 0
#Initial score
score = 0
#apple position using random function
applepos = (random.randint(0, 590), random.randint(0, 590))
pygame.init()
s = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake!!!')
#Apple image and color
appleimage = pygame.Surface((10, 10))
appleimage.fill((0, 255, 0))
#Snake image and color
img = pygame.Surface((20, 20))
img.fill((255, 0, 0))
f = pygame.font.SysFont('Arial', 20)
clock = pygame.time.Clock()
#Setting up the directions
while True:
    clock.tick(10)
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit(0)
        elif e.type == KEYDOWN:
            if e.key == K_UP and sdir != 0:
                sdir = 2
            elif e.key == K_DOWN and sdir != 2:
                sdir = 0
            elif e.key == K_LEFT and sdir != 1:
                sdir = 3
            elif e.key == K_RIGHT and sdir != 3:
                sdir = 1
    i = len(xs) - 1
	#If the snake collides to itself
    while i >= 2:
        if collide(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20): die(s, score)
        i -= 1
	#If the snake collides the apple, increase the score and position the apple somewhere else
    if collide(xs[0], applepos[0], ys[0], applepos[1], 20, 10, 20, 10): score += 1;xs.append(700);ys.append(
        700);applepos = (random.randint(0, 590), random.randint(0, 590))
	#If the snake touches the ends of the screen, it should die
    if xs[0] < 0 or xs[0] > 580 or ys[0] < 0 or ys[0] > 580: die(s, score)
    i = len(xs) - 1
	#loop for snake movement
    while i >= 1:
        xs[i] = xs[i - 1]
        ys[i] = ys[i - 1]
        i -= 1
    if sdir == 0:
        ys[0] += 20
    elif sdir == 1:
        xs[0] += 20
    elif sdir == 2:
        ys[0] -= 20
    elif sdir == 3:
        xs[0] -= 20
    s.fill((255, 255, 255))
	#positioning the snake and apple on the screen using blit()
    for i in range(0, len(xs)):
        s.blit(img, (xs[i], ys[i]))
    s.blit(appleimage, applepos)
    t = f.render(str(score), True, (0, 0, 0))
    s.blit(t, (10, 10))
    pygame.display.update()





