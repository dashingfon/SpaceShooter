from buttons import Button, Graph, Icon, Node
import SP_configuration as Cfg

import json
import pygame, sys
from pygame.locals import *

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

    while Active:

        P1_indicator = P1_p % len(Cfg.P1_POSITIONS)
        P2_indicator = P2_p % len(Cfg.P2_POSITIONS)

        P1_controller = Icon(
        Cfg.P1_CONTROLLER_IMG,(Cfg.P1_POSITIONS[P1_indicator]))

        P2_controller = Icon(
        Cfg.P2_CONTROLLER_IMG,(Cfg.P2_POSITIONS[P2_indicator]))

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

        P1_controller.display(Surface)
        P2_controller.display(Surface)

        SelectSide_indicator = SelectSide_pointer % len(SELECTSIDE_GRID)

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
                    if SELECTSIDE_GRID[SelectSide_indicator].active == True:  
                        Active = False
         
        pygame.display.update()            
    return [mode,P1_p,P2_p]
              
def get_new_ships():

    with open('GameSettings.json') as GS:
        GameSettings = json.load(GS)
        new_ships = GameSettings['Game_Settings']['New_Ships']
    
    return new_ships

def get_available_ships():

    with open('GameSettings.json') as GS:
        GameSettings = json.load(GS)
        available_ships = GameSettings['Game_Settings']['Available_Ships']
    
    return available_ships
    
def SelectShip_1P(Surface,SelectSideBg):

    ShipIcon = Icon(Cfg.SHIP_ICON,(474,63))

    CeaderButton = [Button(Cfg.CEADER_BUTTON_IMG,Cfg.SELECTSTAGE,(119,154)),'Ceader']
    ViditeButton = [Button(Cfg.VIDITE_BUTTON_IMG,Cfg.SELECTSTAGE,(289,154)),'Vidite']
    QuraosButton = [Button(Cfg.QURAOS_BUTTON_IMG,Cfg.SELECTSTAGE,(119,279)),'Quraos']
    RhomosButton = [Button(Cfg.RHOMOS_BUTTON_IMG,Cfg.SELECTSTAGE,(289,279)),'Rhomos']
    ElousButton = [Button(Cfg.ELOUS_BUTTON_IMG,Cfg.SELECTSTAGE,(119,397)),'Elous']
    RonirButton = [Button(Cfg.RONIR_BUTTON_IMG,Cfg.SELECTSTAGE,(289,397)),'Ronir']

    BackButton = Button(Cfg.BACKBUTTON,Cfg.SELECTSIDES,(426,473))
    SettingsButton = Button(Cfg.SETTINGSBUTTON,Cfg.SETTINGS,(524,473))

    ShipButtons = [
        CeaderButton,
        ViditeButton,
        QuraosButton,
        RhomosButton,
        ElousButton,
        RonirButton]

    ControlButtons = [
        BackButton,
        SettingsButton]

    CeaderNode = Node(CeaderButton[1],CeaderButton[0],[
        ElousButton[0],
        QuraosButton[0],
        BackButton,
        ViditeButton[0]])
    ViditeNode = Node(ViditeButton[1],ViditeButton[0],[
        RonirButton[0],
        RhomosButton[0],
        CeaderButton[0],
        BackButton])
    QuraosNode = Node(QuraosButton[1],QuraosButton[0],[
        CeaderButton[0],
        ElousButton[0],
        SettingsButton,
        RhomosButton[0]])
    RhomosNode = Node(RhomosButton[1],RhomosButton[0],[
        ViditeButton[0],
        RonirButton[0],
        QuraosButton[0],
        BackButton])
    ElousNode = Node(ElousButton[1],ElousButton[0],[
        QuraosButton[0],
        CeaderButton[0],
        SettingsButton,
        RonirButton[0]])
    RonirNode = Node(RonirButton[1],RonirButton[0],[
        RhomosButton[0],
        ViditeButton[0],
        ElousButton[0],
        SettingsButton])

    Nodes = [
        CeaderNode,
        ViditeNode,
        QuraosNode,
        RhomosNode,
        ElousNode,
        RonirNode]

    P1_SELECTSHIP_GRID = Graph(Nodes)

    new_ships = get_new_ships()
    available_ships = get_available_ships()

    Active = True

    while Active:
        Surface.blit(SelectSideBg,(0,0))
        ShipIcon.display(Surface)

        P1_SELECTSHIP_GRID.selected.indicate(Surface,Cfg.SHIP_INDICATOR0)

        for Ship in ShipButtons:
            if Ship[1] in available_ships:
                Ship[0].active = True
                Ship[0].display(Surface)
            else:
                Ship[0].active = False
                Ship[0].display(Surface)

            if Ship[1] in new_ships:
                Ship[0].indicate_at_loc(
                    Surface,Cfg.NEW_TAG,(Ship.rect_.left - 2,Ship.rect_.top - 65))
        
        for button in ControlButtons:
            button.display(Surface)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_a:
                    P1_SELECTSHIP_GRID.move(P1_SELECTSHIP_GRID.selected.left)

                if event.key == K_d:
                    P1_SELECTSHIP_GRID.move(P1_SELECTSHIP_GRID.selected.right)

                if event.key == K_w:
                    P1_SELECTSHIP_GRID.move(P1_SELECTSHIP_GRID.selected.up)

                if event.key == K_s:
                    P1_SELECTSHIP_GRID.move(P1_SELECTSHIP_GRID.selected.down)

                if event.key == K_SPACE:
                    P1_SELECTSHIP_GRID.selected.node.select()
                    if P1_SELECTSHIP_GRID.selected.node.active == True:
                        Active = False

        pygame.display.update()
    return P1_SELECTSHIP_GRID.selected.name
'''
def SelectShip_2P():

    P2_SELECTSHIP_GRID = [
        [   [Ceader,Vidite],
            [Quraos,Rhomos],
            [Elous,Ronir],
            [Backbutton,SettingsButton]           
        ],
        [   [Ceader,Vidite],
            [Quraos,Rhomos],
            [Elous,Ronir],
            [Backbutton,SettingsButton]
        ]
    ]
 
def Settings():

    SETTINGS_GRID = (GameSettings,Moves,HighScores,Achievement,Backbutton)

'''
