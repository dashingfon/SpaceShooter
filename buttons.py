import pygame
from pygame.locals import *
import SP_configuration as Cfg


class Button():
    def __init__(self,image,destination,location):
        self.image = image
        self.rect_ = image.get_rect()
        self.destination = destination
        self.rect_.left, self.rect_.top = location[0],location[1]
        self.location = location

    def display(self,Surface):
        Surface.blit(self.image,self.location)

    def highlight(self,Surface):
        # expand button
        highlighted = self.rect_.copy()
        highlighted.width = self.rect_.width * Cfg.MAGNIFICATION
        highlighted.height = self.rect_.height * Cfg.MAGNIFICATION
        highlighted.centerx, highlighted.centery = self.rect_.centerx, self.rect_.centery
        highlight_img = pygame.transform.scale(
            self.image,(highlighted.width,highlighted.height))

        Surface.blit(highlight_img,highlighted)

    def indicate(self,Surface,indicator):
        # set button border
        indicator_rect = indicator.get_rect()
        indicator_rect.centerx = self.rect_.centerx
        indicator_rect.centery = self.rect_.centery

        Surface.blit(indicator,indicator_rect)
        Surface.blit(self.image,self.rect_)

    def select(self):
        pygame.event.post(pygame.event.Event(self.destination))
        
class Icon(Button):
    def __init__(self,image,location,mobile):
        self.image = image
        self.location = location
        self.mobile = mobile

    def display(self,Surface):
        Surface.blit(self.image,self.location)

    def move(self,destination):
        if self.mobile == True:
            self.location.left, self.location.top = destination[0], destination[1]



