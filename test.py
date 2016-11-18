import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Collision Detection")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 25, 25)

clock = pygame.time.Clock()


def detectCollisions(x1, y1, w1, h1, x2, y2, w2, h2):
    if (x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 >= y2):
        return True
    elif (x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2):
        return True
    elif (x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 + h1 >= y2):
        return True
    elif (x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 + h1 >= y2):
        return True
    else:
        return False

def Collide(x1, y1, w1 ,h1, x2, y2, w2, h2,x_direction, y_direction):
    if x1 + w1 >= x2 and x1 + w1 <= x2 + w2 or x1 <= x2 + w2 and x1 > x2:
        x_direction *= -1
        if y1 + h1 >= y2 and y1 + h1 <= y2 + h2 or y1 <= y2 + h2 and y1 >= y2:
            y_direction *= -1
    return True

''''#collision code
if x1 > (x2-w2) and x1 < (x2+w2) or (x1+w1) > (x2-w2) and (x1+w1) < (x2+w2):
    x_direction *= -1
    if y > (p2-MAGNET_SIZE[1]) and y < (p2+MAGNET_SIZE[1]) and y+BALL_SIZE[1] > (p2-MAGNET_SIZE[1]) and y+BALL_SIZE[1]< (p2+MAGNET_SIZE[1]):
        y_direction *= -1

if x > (pos1-TARGET_SIZE[0]) and x < (pos1+TARGET_SIZE[0]) or (x+BALL_SIZE[0]) > (pos1-TARGET_SIZE[0]) and (x+BALL_SIZE[0]) < (pos1+TARGET_SIZE[0]):
    if y > (pos2-TARGET_SIZE[1]) and y < (pos2+TARGET_SIZE[1]) and y+BALL_SIZE[1] > (pos2-TARGET_SIZE[1]) and y+BALL_SIZE[1]< (pos2+TARGET_SIZE[1]):
        screen.fill([0,0,0])
        screen.blit(Text, (400,300)'''

class Sprite:
    def __init__(self, x, y, width, height):

        self.x = x

        self.y = y

        self.width = width

        self.height = height

    def render(self, collision):

        if (collision == True):

            pygame.draw.rect(window, red, (self.x, self.y, self.width, self.height))

        else:

            pygame.draw.rect(window, black, (self.x, self.y, self.width, self.height))


Sprite1 = Sprite(100, 50, 100, 100)
Sprite2 = Sprite(300, 50, 100, 100)

moveX, moveY = 0, 0

gameLoop = True
while gameLoop:

    for event in pygame.event.get():

        if (event.type == pygame.QUIT):
            gameLoop = False

        if (event.type == pygame.KEYDOWN):

            if (event.key == pygame.K_LEFT):
                moveX = -4

            if (event.key == pygame.K_RIGHT):
                moveX = 4

            if (event.key == pygame.K_UP):
                moveY = -4

            if (event.key == pygame.K_DOWN):
                moveY = 4

        if (event.type == pygame.KEYUP):

            if (event.key == pygame.K_LEFT):
                moveX = 0

            if (event.key == pygame.K_RIGHT):
                moveX = 0

            if (event.key == pygame.K_UP):
                moveY = 0

            if (event.key == pygame.K_DOWN):
                moveY = 0

    window.fill(white)

    Sprite1.x += moveX

    Sprite1.y += moveY

    collisions = detectCollisions(Sprite1.x, Sprite1.y, Sprite1.width, Sprite1.height, Sprite2.x, Sprite2.y,
                                  Sprite2.width, Sprite2.height)

    Sprite1.render(collisions)

    Sprite2.render(False)

    pygame.display.flip()

    clock.tick(50)

pygame.quit()