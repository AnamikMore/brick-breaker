import sys, pygame
# from pygame.locals import *

pygame.init()
windowWidth = 1000
windowHeight = 500
window = pygame.display.set_mode(size=(windowWidth, windowHeight))
pygame.display.set_caption('briksbreak')
font = pygame.font.SysFont('Arial', 30)

#   defining brick colour
oBrick = (255, 100, 10)
gBrick = (0, 255, 0)
wBrick = (255, 255, 255)
black = (0,0,0)

gameRows = 6
gameColumns = 2
clock = pygame.time.Clock()
frameRate = 30
myBall = False
gameOver = 0
score = 0
class Ball():
    def __init__(self, x, y):
        self.radius = 10
        self.x = x - self.radius
        self.y = y - 50
        self.rect = pygame.Rect(self.x, self.y, self.radius*2, self.radius*2)
        self.xSpeed = 1
        self.ySpeed = -1
        self.maxSpeed = 5
        self.gameOver = 0

    def motion(self):
        collisionThreshold = 5
        blockObject = brick.bricks
        brickDestroyed = 1
        countRow = 0
        for row in blockObject:
            countItem = 0
            for item in row:
                if self.rect.colliderect(item[0] ):
                    if abs(self.rect.bottom - item[0].top) < collisionThreshold and self.ySpeed >0 :
                        self.ySpeed *= -1
                    if abs(self.rect.top - item[0].bottom) < collisionThreshold and self.ySpeed < 0:
                        self.ySpeed *= -1
                    if abs(self.rect.right - item[0].left) < collisionThreshold and self.xSpeed > 0:
                        self.xSpeed *= -1
                    if abs(self.rect.left - item[0].right) < collisionThreshold and self.xSpeed < 0:
                        self.xSpeed *= -1
                    if blockObject [countRow][countItem] [1] > 1:
                        blockObject[countRow][countItem] [1] -= 1
                    else:
                        blockObject[countRow][countItem] [0] = (0, 0, 0, 0)

                if blockObject [countRow][countItem] [0] != (0,0,0,0):
                    brickDestroyed = 0
                countItem +=1
            countRow +=1

        if brickDestroyed ==1:
            self.gameOver = 1

        # check for collision with bricks
        if self.rect.left <0 or self.rect.right > windowWidth:
            self.xSpeed *= -1
        if self.rect.top < 0 :
            self.ySpeed *= -1
        if self.rect.bottom > windowHeight:
            self.gameOver = -1

        # check for collision with base
        if self.rect.colliderect(userBasepad):
            if abs(self.rect.bottom - userBasepad.rect.top) < collisionThreshold and self.ySpeed >0:
                self.ySpeed *=-1
                self.xSpeed += userBasepad.direction
                if self.xSpeed > self.maxSpeed:
                    self.xSpeed = self.maxSpeed
                elif self.xSpeed <0 and self.xSpeed <- self.maxSpeed:
                    self.xSpeed = -self.maxSpeed
                else:
                    self.xSpeed *= -1

        self.rect.x += self.xSpeed
        self.rect.y += self.ySpeed


        return self.gameOver

    def draw(self):
        pygame.draw.circle( window, (0, 0, 255), (self.rect.x + self.radius, self.rect.y + self.radius), self.radius)
        pygame.draw.circle(window, (255, 255, 255), (self.rect.x + self.radius, self.rect.y + self.radius), self.radius, 1)

    def reset(self,x, y):
        self.radius = 10
        self.x = x - self.radius
        self.y = y- 50
        self.rect = pygame.Rect( self.x, self.y, self.radius*2, self.radius*2 )
        self.xSpeed = 4
        self.ySpeed = -4
        self.maxSpeed = 5
        self.gameOver = 0


    #   to create bricks
class Block:
    def __init__(self):
        self.width = windowWidth
        self.height = 40
        self.bricks = []

    def makeBrick(self):
        singleBricks = []
        for row in range(gameRows):
            brickRow = []
            for column in range(gameColumns):
                xBrick = column * self.width
                yBrick = row * self.height
                rect = pygame.Rect(xBrick, yBrick, self.width, self.height)

                #assign power to the bricks based on row
                if row < 2:
                    power = 3
                elif row < 4:
                    power = 2
                elif row < 6:
                    power = 1

                singleBricks = [rect, power]
                brickRow.append(singleBricks)

            self.bricks.append(brickRow)

    def drawBrick(self):
        for row in self.bricks:
            for brick in row:
                if brick[1] == 3:
                    brickColour = oBrick
                elif brick[1] == 2:
                    brickColour = wBrick
                elif brick[1] == 1:
                    brickColour = gBrick

                pygame.draw.rect(window, brickColour, brick[0])
                pygame.draw.rect(window, black, brick[0], 1)

class Base():

    def __init__(self):
        self.height = 20
        self.width = int( windowWidth/gameColumns )
        self.x = int(windowWidth/2 - self.width/2)
        self.y = windowHeight - self.height*2
        self.speed = 8
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = 0

    def slide(self):
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.x -= self.speed
            self.direction =-1
        if key[pygame.K_RIGHT] and self.rect.right < windowWidth:
            self.x += self.speed
            self.direction = 1

brick= Block()
brick.makeBrick()
brick.drawBrick()

userBasepad= Base()
ball= Ball(windowWidth/2,windowHeight)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    # screen.fill(black)
    # screen.blit(ball, ballrect)
    
    userBasepad.slide()

    ball.draw()
    ball.motion()

    pygame.display.flip()

