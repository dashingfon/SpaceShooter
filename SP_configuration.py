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
ACHIEVEMENT = USEREVENT + 11
GAME_SETTINGS = USEREVENT + 12
HIGHSCORES = USEREVENT + 13
MOVES = USEREVENT + 14
DISPLAY_WINNER = USEREVENT + 15


HOMESCREEN_BACKGROUND = pygame.image.load(
    "Assets\Icons\HomeScreen\SpaceShooter_homeBackground.png")

SPACESHOOTER_NAME = pygame.image.load(
    "Assets\Icons\HomeScreen\SpaceShooter.png")

#HomeScreen Buttons
STARTBUTTON = pygame.image.load(
    "Assets\Icons\HomeScreen\StartButton.png")

EXITBUTTON = pygame.image.load(
    "Assets\Icons\HomeScreen\ExitButton.png")

SETTINGSBUTTON = pygame.image.load(
    "Assets\Icons\HomeScreen\SettingsButton.png")

#69 by 69 button indicator
BUTTON_INDICATOR = pygame.image.load(
    "Assets\Icons\SelectSide\P1_indicator.png")

#selectsides background
SELECTSIDES_BACKGROUND = pygame.image.load(
    "Assets\Icons\SelectSide\SelectSides_background.png")
SELECTSIDE_ELEMENT = pygame.image.load(
    "Assets\Icons\SelectSide\Elements.png")

#SelectSide Buttons
P1_CONTROLLER_IMG = pygame.image.load(
    "Assets\Icons\SelectSide\P1_Controller.png")

P2_CONTROLLER_IMG = pygame.image.load(
    "Assets\Icons\SelectSide\P2_Controller.png")

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
    "Assets\Icons\SelectSide\BackButton.png")

SELECTBUTTON = pygame.image.load(
    "Assets\Icons\SelectSide\SelectButton.png")

# Controller select button indicator
SHIP_INDICATOR0 = pygame.image.load(
    "Assets\Icons\SelectShip\P1_Ship_Indicator.png")

SHIP_INDICATOR1 = pygame.image.load(
    "Assets\Icons\SelectShip\P2_Ship_Indicator.png")

SHIP_ICON = pygame.image.load(
    "Assets\Icons\SelectShip\ShipLabel.png")

NEW_TAG = pygame.image.load(
    r"Assets\Icons\SelectShip\NewTag.png")

PLAYER_READY_IMG = pygame.image.load(
    "Assets\Icons\SelectShip\ReadyText.png")

BUTTON_GREY_OUT = pygame.image.load(
    "Assets\Icons\SelectShip\Button_grey_out.png")

PlAYER_GREY_OUT = pygame.image.load(
    "Assets\Icons\SelectShip\Player_grey_out.png")

# Ship buttons and images
CEADER_IMG = pygame.image.load(
    "Assets\Ships\Ceader\Ceader.png")
CEADER_BUTTON_IMG = pygame.image.load(
    "Assets\Icons\SelectShip\ceader_button.png")

VIDITE_IMG = pygame.image.load(
    r"Assets\Ships\Vidite\vidite_.png")
VIDITE_BUTTON_IMG = pygame.image.load(
    r"Assets\Icons\SelectShip\vidite_button.png")

QURAOS_IMG = pygame.image.load(
    "Assets\Ships\Quraos\Quraos.png")
QURAOS_BUTTON_IMG = pygame.image.load(
    "Assets\Icons\SelectShip\quraos_button.png")

RHOMOS_IMG = pygame.image.load(
    "Assets\Ships\Rhomos\Rhomos.png")
RHOMOS_BUTTON_IMG = pygame.image.load(
    r"Assets\Icons\SelectShip\rhomos_button.png")

ELOUS_IMG = pygame.image.load(
    "Assets\Ships\Elous\Elous.png")
ELOUS_BUTTON_IMG = pygame.image.load(
    "Assets\Icons\SelectShip\elous_button.png")

RONIR_IMG = pygame.image.load(
    r"Assets\Ships\Ronir\ronir.png")
RONIR_BUTTON_IMG = pygame.image.load(
    r"Assets\Icons\SelectShip\ronir_button.png")



'''
# Weapon images
BASICGUN_1 = pygame.image.load()
BASICGUN_2 = pygame.image.load()

BASIC_BOMB = pygame.image.load()
ADVANCEDBOMB = pygame.image.load()

CAPSULE_GUN = pygame.image.load()
WIDE_CAPSULE_GUN = pygame.image.load()

CRYSTALBOMB_1 = pygame.image.load()
CRYSTALBOMB_2 = pygame.image.load()
CRYSTALBOMB_3 = pygame.image.load()

CRYSTAL_GUN = pygame.image.load()

MISSILE_1 = pygame.image.load()
MISSILE_2 = pygame.image.load()
MISSILE_3 = pygame.image.load()
'''



'''
SHIPS = {
    'Weapons':{
        "Ceader": ,
        'Vidite': ,
        'Quraos': ,
        'Rhomos': ,
        'Elous': ,
        'Ronir': 

    },
    'Speed':{
        "Ceader": ,
        'Vidite': ,
        'Quraos': ,
        'Rhomos': ,
        'Elous': ,
        'Ronir': 

    }
}

WEAPONS = {
    'damage' :{

    },
    'speed' : {

    }
} 


'''