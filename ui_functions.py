from buttons import Button, Icon
import SP_configuration as Cfg

import pygame, sys
from pygame.locals import *

MainClock = pygame.time.Clock()

def HomeScreen(Surface,homeBg):

    StartButton = Button(Cfg.STARTBUTTON,Cfg.SELECTSIDES,(384,278))
    ExitButton = Button(Cfg.EXITBUTTON,QUIT,(384,359))
    SettingsButton = Button(Cfg.SETTINGSBUTTON,Cfg.SETTINGS,(768,418))

    HOMESCREEN_GRID = (StartButton,ExitButton,SettingsButton)

    pointer = 3
    
    Active = True

    while Active:
               
        Surface.blit(homeBg,(0,0))
        Surface.blit(Cfg.SPACESHOOTER_NAME,(299,71))

        for button in HOMESCREEN_GRID:
            button.display(Surface)

        indicator = pointer % len(HOMESCREEN_GRID)
        HOMESCREEN_GRID[indicator].highlight(Surface)
    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type ==  KEYUP:
                if event.key == K_w or event.key == K_UP:
                    pointer -= 1
                
                if event.key == K_s or event.key == K_DOWN:
                    pointer += 1

                if event.key == K_SPACE or event.key == K_KP_ENTER:
                    HOMESCREEN_GRID[indicator].select()
                    Active = False                    
                    break
        
        pygame.display.update()
            
            

def get_mode(point1,point2):
    parallel = point1[0] == point2[0] #parallel when both x are equal
    point1_com = point1 == Cfg.P1_POSITIONS[1] # controller 1 is in the computer position
    point2_com = point2 == Cfg.P2_POSITIONS[1] # controller 2 is in the computer position
    if parallel and point1_com:
        return 'Com'
    elif not parallel and not point1_com and not point2_com:
        return '2P'
    elif not parallel and point2_com or point1_com:
        return '1P'
    elif parallel and not point1_com or point2_com:
        return 'Same'


def SelectSides(Surface,SelectSideBg,SelectSideEle,P1_p,P2_p):

    BackButton = Button(Cfg.BACKBUTTON,Cfg.HOMESCREEN,(381,428))
    SelectButton = Button(Cfg.SELECTBUTTON,Cfg.INVALID,(500,428))

    SELECTSIDE_GRID = (BackButton,SelectButton)
    
    SelectSide_pointer = 2
    
    Active = True

    game_parameter = []

    while Active:

        P1_indicator = P1_p % len(Cfg.P1_POSITIONS)
        P2_indicator = P2_p % len(Cfg.P2_POSITIONS)

        P1_controller = Icon(
        Cfg.P1_CONTROLLER_IMG,(Cfg.P1_POSITIONS[P1_indicator]),True
        )

        P2_controller = Icon(
        Cfg.P2_CONTROLLER_IMG,(Cfg.P2_POSITIONS[P2_indicator]),True
        )

        mode = get_mode(P1_controller.location,P2_controller.location)
        if mode == 'Com' or mode == 'Same':
            SelectButton.deactivate()
        elif mode == '1P':
            SelectButton.activate()
            SelectButton.destination = Cfg.SELECTSHIP_1P
        elif mode =='2P':
            SelectButton.activate()
            SelectButton.destination = Cfg.SELECTSHIP_2P

        
        Surface.blit(SelectSideBg,(0,0))
        Surface.blit(SelectSideEle,(126,79))

        SelectSide_indicator = SelectSide_pointer % len(SELECTSIDE_GRID)
        P1_controller.display(Surface)
        P2_controller.display(Surface)

        SELECTSIDE_GRID[SelectSide_indicator].indicate(Surface,Cfg.BUTTON_INDICATOR)
        for i in SELECTSIDE_GRID:
            i.display(Surface)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYUP:
                if event.key == K_d:
                    P1_p += 1
                if event.key == K_a:
                    P1_p -= 1
                
                if event.key == K_RIGHT:
                    P2_p += 1
                if event.key == K_LEFT:
                    P2_p -= 1
    
                if event.key == K_s or event.key == K_DOWN and mode == 'Com' or mode == 'Same':
                    pass

                elif event.key == K_s or event.key == K_DOWN:
                    SelectSide_pointer += 1

                if event.key == K_w or event.key == K_UP and mode == 'Com' or mode == 'Same':
                    pass

                elif event.key == K_w or event.key == K_UP:
                    SelectSide_pointer -= 1
                    
                if event.key == K_KP_ENTER or event.key == K_SPACE:                  
                    SELECTSIDE_GRID[SelectSide_indicator].select()
                    Active = False
                    break
         
        pygame.display.update()            
        if game_parameter:
            return game_parameter
              
        '''               
def SelectShip_1P():

    P1_SELECTSHIP_GRID = [
        [Ceader,Quraos,Ronir],
        [Vidite,Rhomos,Elous],
        [Backbutton,SettingsButton,Pass]
    ]

def SelectShip_2P():

    P2_SELECTSHIP_GRID = [
        [   [],
            [],
            []            
        ],
        [   [],
            [],
            []
        ]
    ]

def Settings():

    SETTINGS_GRID = ()

'''