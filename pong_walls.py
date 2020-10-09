import pygame

def main():
    pygame.init()
    pygame.display.set_caption('pink pong')

    WIDTH = 800
    HEIGHT = 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((0, 0, 0))
    pygame.display.update()

    wcolor = pygame.Color("Pink")
    BORDER = 15

    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0), (WIDTH, BORDER))) #top wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,(HEIGHT - BORDER)), (WIDTH, BORDER))) #bottom wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0), (BORDER, HEIGHT))) #left wall

    pygame.display.update()

    running = True

    while running:
            # event handling, gets all event from the eventqueue
            for event in pygame.event.get():
                # only do something if the event if of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False

if __name__=="__main__":
    # call the main function
    main()