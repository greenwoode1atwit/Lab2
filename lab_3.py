import pygame
import random
import math

from ball import Ball

def main():
    pygame.init()
    pygame.display.set_caption('pink pong')

    WIDTH = 800
    HEIGHT = 400
    FCAP=60
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((0, 0, 0))
    pygame.display.update()

    wcolor = pygame.Color("Pink")
    BORDER = 15
 
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0), (WIDTH, BORDER))) #top wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,(HEIGHT - BORDER)), (WIDTH, BORDER))) #bottom wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0), (BORDER, HEIGHT))) #left wall

    ballRad = 10

    #angle is in randians, modulo used to fit to +-45 degree window
    balls = list()
    for i in range(5000):
        balls.append(Ball(screen, HEIGHT, BORDER, radius=ballRad, x=WIDTH-ballRad, y=HEIGHT//2, velocity=2, angle=(random.uniform(-math.pi/4, math.pi/4)) ) )
    
    for i in balls:
        i.show()

    pygame.display.update()
    
    running = True
    clock = pygame.time.Clock()

    while running:
            # event handling, gets all event from the eventqueue
            for event in pygame.event.get():
                # only do something if the event if of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False
            for i in balls:
                i.update()
            pygame.display.update()
            clock.tick(FCAP)
            
if __name__=="__main__":
    # call the main function
    main()