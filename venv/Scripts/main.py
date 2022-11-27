import sys, pygame
from pygame import *

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

gameRows = 12
gameColumns = 12
clock = pygame.time.Clock()
fps = 30
text_col=234,0,6

#Fuction for displaying text on window 
def draw_text(text, font, text_col, x,y):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))

class Ball():
    def __init__(self, x, y):
        self.radius = 10
        self.x = x - self.radius
        self.y = y- 50
        self.rect = pygame.Rect( self.x, self.y, self.radius*2, self.radius*2 )
        self.xSpeed = 4
        self.ySpeed = -4
        self.maxSpeed = 5
        self.gameOver = 0
        self.score=0
        self.myBall=False 


    def motion(self,score,wall,userBasepad):
        collisionThreshold = 5
        blockObject = wall.bricks
        wallDestroyed = 1
        countRow = 0
        for row in blockObject:
            countItem = 0
            for item in row:
                if self.rect.colliderect(item[0] ):
                    self.score+=5
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
                # check if brick destroyed
                if blockObject [countRow][countItem] [0] != (0,0,0,0):
                    wallDestroyed=0
                countItem +=1
            countRow +=1

        if wallDestroyed ==1:
            self.gameOver = 1

        # check for collision with window border
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
        self.__init__(x,y)

class Block:
    def __init__(self):
        self.width = windowWidth//gameColumns
        self.height = 10
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
        self.speed = 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = 0

    def slide(self):
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction =-1
        if key[pygame.K_RIGHT] and self.rect.right < windowWidth:
            self.rect.x += self.speed
            self.direction = 1

    def drawBase(self):
        pygame.draw.rect(window,(0,200,0),self.rect)
    
def main():
    ball= Ball(windowWidth/2,windowHeight-100)
    wall= Block()
    wall.makeBrick()
    ball.myBall =False          # \\
    userBasepad= Base()
    run=True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run=False# sys.exit()
    
        window.fill(black)
        userBasepad.drawBase()
        wall.drawBrick()
        ball.draw()
        if ball.myBall:
            userBasepad.slide()    
            ball.gameOver =  ball.motion(ball.score,wall,userBasepad)
            if ball.gameOver != 0:
                ball.myBall = False
            
 
    #Print player instructions
        if not ball.myBall:
            if ball.gameOver == 0:
                draw_text(' START', font , text_col, 100, windowHeight // 2 + 100)
            elif ball.gameOver == 1:
                draw_text('YOU WON', font , text_col, 240, windowHeight // 2 + 50)
                draw_text(' START', font , text_col, 100, windowHeight // 2 + 100)   
            elif ball.gameOver == -1:
                draw_text('YOU LOST', font , text_col, 240, windowHeight // 2 + 50)
                draw_text(' START', font , text_col, 100, windowHeight // 2 + 100)   
            
            keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
                ball.myBall = True
                ball.reset(userBasepad.x + (userBasepad.width//2), userBasepad.y - userBasepad.height)
                userBasepad.drawBase()
                wall.makeBrick()
        
        draw_text(f"{ball.score}", font , text_col, 50 , windowHeight - 50)        
        pygame.display.update()
    pygame.quit()

if __name__ =='__main__':
    main()


