import pygame
from random import random
pygame.init()

win_width = 1000
win_height = 600

win = pygame.display.set_mode((win_width, win_height))

width = 64
height = 64
x = 60
y = win_height - height - 100
speed = 5

y_constant = y

jumpSpeed = 100
jump = False

red = 255
green = 255
blue = 100

left = False
right = False
up = False

#Keep delayLimit even number
delayLimit = 28
delay = -delayLimit


pygame.display.set_caption("Fast Legs")
radius= 128
cx=win_width
cy= y_constant - (128/3)

score = 0
high_score = 0
speed_base = 3
speed_multiplier = 2
s = int(random()*speed_multiplier+speed_base)

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
stand = pygame.image.load('standing.png')
leftCount = 0
rightCount = 0

run_t = True
Circles = []
Clouds = []
class Circle:
    def __init__(self,radius, dx, x, y):
        self.radius = radius
        self.dx = dx
        self.x = x
        self.y = y
    def draw_circle(self):
        win.blit(pygame.image.load('b.png'), (self.x, self.y))
        self.reset_circle()
        self.x -= self.dx
    def add_circle(self):
        Circles.append(self)
    def reset_circle(self):
        if self.x + 128 < 0:
            global score
            global speed_base
            global s
            score += 1
            self.x = cx
            self.dx = int(random()*speed_multiplier+speed_base)
            s = self.dx
            if score%3==0 and score<=55:
                speed_base +=1


cloud_x = win_width
cloud_y = 0
cloud_length = 0
cloud_width = 0



class Cloud:
    def __init__(self, x, y, length, width, cloud_speed):

        self.x=x
        self.y=y
        self.length = length
        self.width = width
        self.cloud_speed = cloud_speed
        self.generate_values()
    def generate_values(self):
        while (self.length <= 50):
            self.length = int(random() * 350)
        while (self.width <= 10):
            self.width = int(random() * 55)
        self.y = int((random()*300)+1)
    def draw_cloud(self):
        pygame.draw.ellipse(win,(255,255,255),[self.x,self.y,self.length,self.width])
        self.x -= s
    def add_cloud(self):
        Clouds.append(self)


temp = Circle(radius, s, cx, cy)
temp.add_circle()

cloud = Cloud(cloud_x,cloud_y,cloud_length,cloud_width,s)
cloud.add_cloud()

font = pygame.font.SysFont(None, 200)
font2 = pygame.font.SysFont(None, 50)
def text_score():
    screen_text = font.render(str(score),True,(0,0,0))
    win.blit(screen_text,[win_width/2,win_height/4])

    screen_text2 = font2.render(str(high_score), True, (0, 255, 0))
    win.blit(screen_text2, [win_width -50, 50])

run = True

while run:
    pygame.time.delay(7)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()

    if (key[pygame.K_LEFT] or key[pygame.K_a]):
            x -= speed
            left = True
    if (key[pygame.K_RIGHT] or key[pygame.K_d]):
            x += speed
            right = True


    #For Jumping mechanics
    if key[pygame.K_UP] or key[pygame.K_w]:
        jump = True

    if jump:
        if delay < 0:
            y -= (delay*delay)/50
            delay += 1

        elif delay == 0:
            delay += 1

        elif delay <= delayLimit:
            y += (delay*delay)/50
            delay += 1
        elif delay == delayLimit+1:
            jump = False
            delay = -delayLimit


    win.fill((0, 0, 0))

    #sky
    pygame.draw.rect(win, (46, 132, 244), (0, 0, win_width, y_constant + height))
    # Background ground
    pygame.draw.rect(win, (2, 204, 18), (0, y_constant + height - 5, win_width, 10))
    pygame.draw.rect(win, (97, 26, 9), (0, y_constant + height - 5 +10, win_width, win_height))
    # obstacle

    for i in range(len(Circles)):
        Circles[i].draw_circle()

    for i in range(len(Clouds)):
            Clouds[i].draw_cloud()

    if(random()>0.99):
        cloud = Cloud(cloud_x, cloud_y, cloud_length, cloud_width, s)
        cloud.add_cloud()

    #Rectangle character
    if(left):
        win.blit(walkLeft[leftCount], (x, y))
        leftCount +=1
    elif(right):
        win.blit(walkRight[rightCount], (x, y))
        rightCount+=1
    else:
        win.blit(stand, (x, y))

    left = False
    right = False

    text_score()

    if(leftCount>8):
        leftCount=0
    if (rightCount > 8):
        rightCount = 0
    if x>=Circles[0].x-35 and x<=(Circles[0].x+Circles[0].radius-35) and y>=Circles[0].y:
        explosion = [pygame.image.load('regularExplosion00.png'),pygame.image.load('regularExplosion01.png'),pygame.image.load('regularExplosion02.png'),pygame.image.load('regularExplosion03.png'),pygame.image.load('regularExplosion04.png'),pygame.image.load('regularExplosion05.png'),pygame.image.load('regularExplosion06.png'),pygame.image.load('regularExplosion07.png'),pygame.image.load('regularExplosion08.png')]

        for i in range(9):
            win.blit(explosion[i], (x, y))
            pygame.time.delay(100)
            if i == 8:
                run_t = False
                leave = font.render("D:", True, (int(random()*255), int(random()*255), int(random()*255)))
                win.blit(leave, (win_width/2, win_height / 2))
                score = 0
                run_t = True
                Circles[0].x = win_width
                x = 60
            if run_t:
                pygame.display.update()





    if score>= high_score:
        high_score = score
    pygame.display.update()
pygame.quit()


