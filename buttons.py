import pygame
from pygame.locals import *
import SP_configuration as Cfg


class Button:
    def __init__(self,image,destination,location):
        self.image = image
        self.rect_ = image.get_rect()
        self.destination = destination
        self.rect_.left, self.rect_.top = location[0],location[1]
        self.location = location
        self.active = True
        self.greyed_out = Cfg.BUTTON_GREY_OUT
        
    def display(self,Surface):
        if self.active == True:
            Surface.blit(self.image,self.location)
        else:
            Surface.blit(self.image,self.location)
            Surface.blit(self.greyed_out,self.location)

    def highlight(self,Surface):
        # expand button
        if self.active == True:    
            highlighted = self.rect_.copy()
            highlighted.width = self.rect_.width * Cfg.MAGNIFICATION
            highlighted.height = self.rect_.height * Cfg.MAGNIFICATION
            highlighted.centerx, highlighted.centery = self.rect_.centerx, self.rect_.centery
            highlight_img = pygame.transform.scale(
                self.image,(highlighted.width,highlighted.height))

            Surface.blit(highlight_img,highlighted)

    def indicate(self,Surface,indicator):
        # set button border
        if self.active == True:
            indicator_rect = indicator.get_rect()
            indicator_rect.centerx = self.rect_.centerx
            indicator_rect.centery = self.rect_.centery

            Surface.blit(indicator,indicator_rect)
            Surface.blit(self.image,self.rect_)
       

    def select(self):
        if self.active == True:
            pygame.event.post(pygame.event.Event(self.destination))
        else:
            pygame.event.post(pygame.event.Event(Cfg.INVALID))
    
    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False

    def indicate_at_loc(self,surface,indicator,location):
        if self.active == True:
            indicator_rect = indicator.get_rect()
            indicator.x, indicator.y = location[0], location[1]

            surface.blit(indicator,indicator_rect)



class Icon:
    def __init__(self,image,location):
        self.image = image
        self.location = location
        self.rect_ = image.get_rect()

    def display(self,Surface):
        Surface.blit(self.image,self.location)


class Node:
    def __init__(self,name,node,neighbours):
        self.name = name
        self.node = node
        self.neighbours = neighbours 

        self.left, self.right = neighbours[0], neighbours[1]
        self.up, self.down = neighbours[2], neighbours[3]
        

class Graph:
    def __init__(self,nodes):
        GraphGrid = {}
        for i in nodes:
            GraphGrid[i.node] = i.neighbours
        self.grid = GraphGrid
        self.nodes = nodes
        
        self.selected = nodes[0].node
    
    def move(self,node_2_move):
        self.selected = node_2_move

        