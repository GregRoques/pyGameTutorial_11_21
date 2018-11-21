from pygame.sprite import Sprite
import pygame

class Arrow(Sprite): #Call the Super Class
    def __init__(self, theHero): # initialize the Super Class
        super(Arrow,self).__init__()
        self.x = theHero.x
        self.y = theHero.y
        self.speed = 30
        self.rect = pygame.Rect(0,0,64,64)
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def update_me(self):
        self.x += self.speed
        self.rect.centerx = self.x
        self.rect.centery = self.y
 
