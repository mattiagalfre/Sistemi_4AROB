import sys, pygame
pygame.init()

width, height = 640, 480
size=(width, height)
speedUp = [0, -5]
speedDown = [0, 5]
speedRight = [5, 0]
speedLeft = [-5, 0]
black = (0, 0, 0)

screen = pygame.display.set_mode(size)

ball = pygame.image.load("./intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN: 
            if event.__dict__["unicode"] == "w":
                ballrect = ballrect.move(speedUp)
                if ballrect.top < 0:
                    ballrect = ballrect.move(speedDown)
            elif event.__dict__["unicode"] == "s":
                ballrect = ballrect.move(speedDown)
                if ballrect.bottom > height:
                    ballrect = ballrect.move(speedUp)
            elif event.__dict__["unicode"] == "d":
                ballrect = ballrect.move(speedRight)
                if ballrect.right > width:
                    ballrect = ballrect.move(speedLeft)
            elif event.__dict__["unicode"] == "a":
                ballrect = ballrect.move(speedLeft)
                if ballrect.left < 0:
                    ballrect = ballrect.move(speedRight)

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()