'''This code will create a very simplistic game '''

#import pygame
import pygame, sys
#initialise pygame
pygame.init()

#open screen
SCREEN_SIZE = [800, 600]
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Very Simple Game")

#hide mouse
pygame.mouse.set_visible(0)

clock = pygame.time.Clock()


BALL_SIZE = [22, 22]
MAGNET_SIZE = [100, 25]
TARGET_SIZE = [200, 200]

BALL = pygame.image.load("Ball.png").convert_alpha()
BALL.set_colorkey([255,255,255])
MAGNET= pygame.image.load("Magnet.png").convert_alpha()
MAGNET.set_colorkey([255,255,255])
TARGET = pygame.image.load("Target.png").convert_alpha()
TARGET.set_colorkey([255,255,255])



#define x and y
x,y = 0, 0

#define x and y directions
x_direction, y_direction = 1, 1
move_x, move_y= 0,0

#define position of magnet
p1=350
p2=275

#define position of target
pos1=700
pos2=400


myriadProFont=pygame.font.SysFont("Myriad Pro", 48)
Text=myriadProFont.render("YOU WIN",1,(255,255,255),(0,0,0))

'''test rotation code from http://stackoverflow.com/questions/25434990/
when-i-use-pygame-transform-rotate-it-moves-my-image-so-that-if-used-in-succ'''
def rotate45(gameObject, rotations={}):
    r = rotations.get(gameObject,0) + 45
    rotations[gameObject] = r
    return pygame.transform.rotate(gameObject, r)

angle=0

#main game loop
while 1:

    clock.tick(60)

    screen.fill([255,255,255])

    screen.blit(BALL, (x, y))
    screen.blit(MAGNET, (p1, p2))
    screen.blit(TARGET, (pos1, pos2))




    for event in pygame.event.get():
        if event.type==pygame.QUIT:sys.exit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_d and p1 + MAGNET_SIZE[0] < 800:
                move_x += 6
            else:
                move_x = 0
            if event.key==pygame.K_a and p1>0:
                move_x -= 6
            if event.key==pygame.K_s and p2 + MAGNET_SIZE[1] < 600:
                move_y += 6
            else:
                move_y = 0
            if event.key==pygame.K_w and p2 > 0:
                move_y -= 6
            if event.key==pygame.K_SPACE:
                ROT_MAG = pygame.transform.rotate(MAGNET, 45)
                screen.blit(ROT_MAG, (p1,p2))
                #angle = (angle + 45) % 360
                #rot_MAG=rotate45(MAGNET (p1,p2))
                #screen.blit(rot_MAG, (p1,p2))
                #screen.blit(pygame.transform.rotate((MAGNET, angle), (p1,p1)))
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_d:
                move_x = 0
            if event.key==pygame.K_a:
                move_x = 0
            if event.key==pygame.K_w:
                move_y = 0
            if event.key==pygame.K_s:
                move_y = 0

    p1 += move_x
    p2 += move_y

    x += 2*x_direction
    y += 2*y_direction

    if x + BALL_SIZE[0] >= 800 or x <= 0:
        x_direction *= -1
    if y + BALL_SIZE[1] >= 600 or y <= 0:
        y_direction *= -1

    if p1 + MAGNET_SIZE[0] >= 800 or p1 <= 0:
        move_x = 0
    if p2 + MAGNET_SIZE[1] >= 600 or p2 <= 0:
        move_y = 0

#collision code with magnet and ball:
    if p1 <= x + BALL_SIZE[0] <= p1 + MAGNET_SIZE[0] and p2 -MAGNET_SIZE[1] <= y <= p2 or p1 <= x + BALL_SIZE[0] <= p1 +MAGNET_SIZE[0] and p2 - MAGNET_SIZE[1] <= y -BALL_SIZE[1] <= p2:
        x_direction *= 1
        y_direction *= -1
    elif p1 <= x <= p1 +MAGNET_SIZE[0] and p2 -MAGNET_SIZE[1] <= y <= p2 or p1 <= x <= p1 +MAGNET_SIZE[0] and p2 - MAGNET_SIZE[1] <= y -BALL_SIZE[1] <= p2:
        x_direction *= 1
        y_direction *= -1

#ball and target
    if pos1 <= x + BALL_SIZE[0] <= pos1 +TARGET_SIZE[0] and pos2 -TARGET_SIZE[1] <= y <= pos2 or pos1 <= x + BALL_SIZE[0] <= pos1 +TARGET_SIZE[0] and pos2 - TARGET_SIZE[1] <= y -BALL_SIZE[1] <= pos2:
        screen.fill([0,0,0])
        screen.blit(Text, (400,300))
    elif pos1 <= x <= pos1 + TARGET_SIZE[0] and pos2 -TARGET_SIZE[1] <= y <= pos2 or pos1 <= x <= pos1 + TARGET_SIZE[0] and pos2 - TARGET_SIZE[1] <= y -BALL_SIZE[1] <= pos2:
        screen.fill([0,0,0])
        screen.blit(Text, (400,300))


    pygame.display.update()


#force for acceleration
#magnetic monopole radial force

