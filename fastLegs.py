import pygame
from random import random
pygame.init()

win_width = 1000
win_height = 600

win = pygame.display.set_mode((win_width, win_height))

width = 50
height = 100
x = 60
y = win_height - height - 100
speed = 5

y_constant = y

jumpSpeed = 100
jump = False

#Keep delayLimit even number
delayLimit = 28
delay = -delayLimit


pygame.display.set_caption("Fast Legs")
radius= int(height / 3)
cx=win_width
cy=y_constant + height - radius

score = 0
speed_base = 3
speed_multiplier = 2
class Circle:
    def __init__(self,radius, dx, x, y):
        self.radius = radius
        self.dx = dx
        self.x = x
        self.y = y
    def draw_circle(self):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius, 0)
        self.reset_circle()
        self.x -= self.dx
    def add_circle(self):
        Circles.append(self)
    def reset_circle(self):
        if self.x < 0:
            global score
            global speed_base
            score += 1
            self.x = cx
            self.dx = int(random()*speed_multiplier+speed_base)
            if score%12 == 0 and score<=48:
                speed = int(random() * 9 + 1)
                temp = Circle(radius, speed, cx, cy)
                temp.add_circle()
            if score%48==0:
                speed_base +=2



Circles = []

for i in range(1):
    speed = int(random()*speed_multiplier+speed_base)
    temp = Circle(radius, speed, cx, cy)
    temp.add_circle()


run = True

while run:
    pygame.time.delay(10)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()

    if (key[pygame.K_LEFT] or key[pygame.K_a]):
            x -= speed
    if (key[pygame.K_RIGHT] or key[pygame.K_d]):
            x += speed


    #For Jumping mechanics
    if key[pygame.K_UP] or key[pygame.K_w]:
        jump = True

    if jump:
        if delay < 0:
            y -= (delay*delay)/80
            delay += 1

        elif delay == 0:
            delay += 1

        elif delay <= delayLimit:
            y += (delay*delay)/80
            delay += 1

        elif delay == delayLimit+1:
            jump = False
            delay = -delayLimit


    win.fill((0, 0, 0))
    # Background ground
    pygame.draw.rect(win, (2, 204, 18), (0, y_constant + height, win_width, win_height))
    #sky
    pygame.draw.rect(win, (46, 132, 244), (0, 0, win_width, y_constant + height))
    # obstacle
    pygame.draw.polygon(win, (255, 255, 0), ((0, 225), (25, 160), (400, 160), (425, 275)))


    for i in range(len(Circles)):
        Circles[i].draw_circle()


    #Rectangle character
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()



pygame.quit()


