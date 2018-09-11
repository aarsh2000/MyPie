import pygame
pygame.init()

win_width = 1000
win_height = 600

win = pygame.display.set_mode((win_width, win_height))

width = 50
height = 100
x = 60
y = win_height - height - 100
speed = 3

y_constant =  y

jumpSpeed = 8
jump = False

#Keep delayLimit even number
delayLimit = 26
delay = -delayLimit

pygame.display.set_caption("Fast Legs")



run = True

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
            x -= speed
    if key[pygame.K_RIGHT]:
            x += speed


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
    # Background
    pygame.draw.rect(win, (2, 204, 18), (0, y_constant + height, win_width, win_height))
    pygame.draw.rect(win, (46, 132, 244), (0, 0, win_width, y_constant + height))

    pygame.draw.rect(win, (255, 255, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()


