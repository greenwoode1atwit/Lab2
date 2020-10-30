import pygame
import math

BKGRND_COLOR = (25,25,25)

class Ball:
    def __init__(self, screen, HEIGHT, BORDER, radius=10, color=((255,255,255)), x=0, y=0, velocity=-1, angle=0):
        self.screen = screen
        self.HEIGHT = HEIGHT
        self.BORDER = BORDER
        self.RADIUS = radius
        self.color = color
        self.x = x
        self.y = y
        self.vx = -velocity
        self.vy = velocity * math.tan(angle)
        self.angle = angle


    def show(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.RADIUS)

    def update(self):



        pygame.draw.circle(self.screen, BKGRND_COLOR, (int(self.x), int(self.y)), self.RADIUS)
        self.x += self.vx
        self.y += self.vy


        colY = False
        colX = False
        #CHECK FOR COLIISIONS
        if (self.y < self.BORDER + self.RADIUS) or (self.y > (self.HEIGHT - (self.BORDER + self.RADIUS))):
            colY = True
        if (self.x < self.BORDER + self.RADIUS):
            colX = True

        if (colY or colX) is True:
            #if would draw in wall, instead back out in reflected directions
            if colY == True:
                self.vy = -self.vy
                self.y += self.vy
            if colX == True:
                self.vx = -self.vx
                self.x += self.vx

        self.show()
    
    def update_vel(self, velocity):
        self.vx = -velocity
        self.vy = velocity * math.tan(self.angle)

        
        
