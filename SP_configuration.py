import pygame
from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

WINDOWWIDTH = 950
WINDOWHEIGHT= 540

FPS = 60

MAGNIFICATION = 1.3

# Events
HOMESCREEN = USEREVENT + 1
SELECTSIDES = USEREVENT + 2
SELECTSHIP_1P = USEREVENT + 3
SELECTSHIP_2P = USEREVENT + 4
SETTINGS = USEREVENT + 5
PLAYGAME = USEREVENT + 6
PAUSEGAME = USEREVENT + 7
GAMEEND = USEREVENT + 8
SELECTSTAGE = USEREVENT + 9
INVALID = USEREVENT + 10

HOMESCREEN_BACKGROUND = pygame.image.load(
    "Assets\Icons\HomeScreen\SpaceShooter_homeBackground.png")

SPACESHOOTER_NAME = pygame.image.load(
    "Assets\Icons\HomeScreen\SpaceShooter.png"
)

#HomeScreen Buttons
STARTBUTTON = pygame.image.load(
    "Assets\Icons\HomeScreen\StartButton.png"
)

EXITBUTTON = pygame.image.load(
    "Assets\Icons\HomeScreen\ExitButton.png"
)

SETTINGSBUTTON = pygame.image.load(
    "Assets\Icons\HomeScreen\SettingsButton.png"
)

#69 by 69 button indicator
BUTTON_INDICATOR = pygame.image.load(
    "Assets\Icons\SelectSide\P1_indicator.png"
)

#selectsides background
SELECTSIDES_BACKGROUND = pygame.image.load(
    "Assets\Icons\SelectSide\SelectSides_background.png"
)
SELECTSIDE_ELEMENT = pygame.image.load(
    "Assets\Icons\SelectSide\Elements.png"
)

#SelectSide Buttons
P1_CONTROLLER_IMG = pygame.image.load(
    "Assets\Icons\SelectSide\P1_Controller.png"
)

P2_CONTROLLER_IMG = pygame.image.load(
    "Assets\Icons\SelectSide\P2_Controller.png"
)

P1_POSITIONS = (
    (127,127), # left
    (446,127), # middle
    (767,127) # right
)
    
P2_POSITIONS = (
    (127,211), # left
    (446,211), # middle
    (767,211) # right
)


BACKBUTTON = pygame.image.load(
    "Assets\Icons\SelectSide\BackButton.png"
)

SELECTBUTTON = pygame.image.load(
    "Assets\Icons\SelectSide\SelectButton.png"
)

# Controller select button indicator
SHIP_INDICATOR = pygame.image.load(
    "Assets\Icons\SelectShip\P1_Ship_Indicator.png"
)

SHIPS = {
    'Buttons_IMG':{

    },
    'Weapons':{

    },
    'Speed':{

    },

}




