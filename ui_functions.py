from buttons import Button, Graph, Icon
import SP_configuration as Cfg

import copy
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
                if event.key == Cfg.P1_CONTROLS['up'] or event.key == Cfg.P2_CONTROLS['up']:
                    pointer -= 1
                
                if event.key == Cfg.P1_CONTROLS['down'] or event.key == Cfg.P2_CONTROLS['down']:
                    pointer += 1

                if event.key == Cfg.P1_CONTROLS['select'] or event.key == Cfg.P2_CONTROLS['select']:
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
                if event.key == Cfg.P1_CONTROLS['right']:
                    P1_p += 1
                if event.key == Cfg.P1_CONTROLS['left']:
                    P1_p -= 1
                
                if event.key == Cfg.P2_CONTROLS['right']:
                    P2_p += 1
                if event.key == Cfg.P2_CONTROLS['left']:
                    P2_p -= 1
    
                if event.key == Cfg.P1_CONTROLS['down'] or event.key == Cfg.P2_CONTROLS['down'] and mode == 'Com' or mode == 'Same':
                    pass

                elif event.key == Cfg.P1_CONTROLS['down']:
                    SelectSide_pointer += 1

                elif  event.key == Cfg.P2_CONTROLS['down']:
                    SelectSide_pointer += 1
                
                if event.key == Cfg.P1_CONTROLS['up'] or event.key == Cfg.P2_CONTROLS['up'] and mode == 'Com' or mode == 'Same':
                    pass

                elif event.key == Cfg.P1_CONTROLS['up']:
                    SelectSide_pointer -= 1

                elif event.key == Cfg.P2_CONTROLS['up']:
                    SelectSide_pointer -= 1    

                if event.key == Cfg.P1_CONTROLS['select'] or event.key == Cfg.P2_CONTROLS['select']:                  
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

    ShipIcon = Icon(Cfg.SHIP_ICON,(404,36))

    CeaderButton = Button(Cfg.CEADER_BUTTON_IMG,Cfg.SELECTSTAGE,(265,127))
    ViditeButton = Button(Cfg.VIDITE_BUTTON_IMG,Cfg.SELECTSTAGE,(265,266))
    QuraosButton = Button(Cfg.QURAOS_BUTTON_IMG,Cfg.SELECTSTAGE,(423,127))
    RhomosButton = Button(Cfg.RHOMOS_BUTTON_IMG,Cfg.SELECTSTAGE,(423,266))
    ElousButton = Button(Cfg.ELOUS_BUTTON_IMG,Cfg.SELECTSTAGE,(579,127))
    RonirButton = Button(Cfg.RONIR_BUTTON_IMG,Cfg.SELECTSTAGE,(579,266))

    BackButton = Button(Cfg.BACKBUTTON,Cfg.SELECTSIDES,(392,438))
    SettingsButton = Button(Cfg.SETTINGSBUTTON,Cfg.SETTINGS,(489,438))

    ShipButton = {
        CeaderButton : Cfg.CEADER,
        ViditeButton : Cfg.VIDITE,
        QuraosButton : Cfg.QURAOS,
        RhomosButton : Cfg.RHOMOS,
        ElousButton : Cfg.ELOUS,
        RonirButton : Cfg.RONIR 
        }
       

    ControlButton = [
        BackButton,
        SettingsButton
    ]

    P1_GRID = Graph(
        [
        [CeaderButton, [ElousButton,QuraosButton,BackButton,ViditeButton]],
        [ViditeButton, [RonirButton,RhomosButton,CeaderButton,BackButton]],
        [QuraosButton, [CeaderButton,ElousButton,BackButton,RhomosButton]],
        [RhomosButton, [ViditeButton,ElousButton,QuraosButton,SettingsButton]],
        [ElousButton, [QuraosButton,CeaderButton,SettingsButton,RonirButton]],
        [RonirButton, [RhomosButton,ViditeButton,ElousButton,SettingsButton]],
        [BackButton, [SettingsButton,SettingsButton,RhomosButton,CeaderButton]],
        [SettingsButton, [BackButton,BackButton,RhomosButton,ElousButton]]
        ]   
    )

    new_ships = get_new_ships()
    available_ships = get_available_ships()

    P1_Ship = ''

    Active = True

    while Active:
        Surface.blit(SelectSideBg,(0,0))
        ShipIcon.display(Surface)

        if P1_GRID.selected not in ControlButton:
            P1_GRID.selected.indicate(Surface,Cfg.SHIP_INDICATOR0)
        else:
            P1_GRID.selected.indicate(Surface,Cfg.BUTTON_INDICATOR)

        for Ship in ShipButton.keys():
            if ShipButton[Ship] in available_ships:
                Ship.active = True
                Ship.display(Surface)
            else:
                Ship.greyed_out = Cfg.PlAYER_GREY_OUT
                Ship.active = False
                Ship.display(Surface)

            if Ship in new_ships:
                Ship.indicate_at_loc(
                    Surface,Cfg.NEW_TAG,(Ship.rect_.left + 2,Ship.rect_.top - 65))
        
        for button in ControlButton:   
            button.display(Surface)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == Cfg.P1_CONTROLS['left'] and P1_GRID.grid[P1_GRID.selected][0].active == True:
                    P1_GRID.move_left()

                if event.key == Cfg.P1_CONTROLS['right'] and P1_GRID.grid[P1_GRID.selected][1].active == True:
                    P1_GRID.move_right()

                if event.key == Cfg.P1_CONTROLS['up'] and P1_GRID.grid[P1_GRID.selected][2].active == True:
                    P1_GRID.move_up()

                if event.key == Cfg.P1_CONTROLS['down'] and P1_GRID.grid[P1_GRID.selected][3].active == True:
                    P1_GRID.move_down()

                if event.key == Cfg.P1_CONTROLS['select']:
                    P1_GRID.selected.select()
                    if P1_GRID.selected.active == True:
                        if P1_GRID.selected not in ControlButton:
                            P1_Ship = ShipButton[P1_GRID.selected]
                        Active = False

        pygame.display.update()

    return P1_Ship

def SelectShip_2P(Surface,SelectSideBg):

    ShipIcon = Icon(Cfg.SHIP_ICON,(404,36))

    P1_ReadyIcon = Icon(Cfg.PLAYER_READY_IMG,(137,302))
    P2_ReadyIcon = Icon(Cfg.PLAYER_READY_IMG,(675,302))

    CeaderButton_P1 = Button(Cfg.CEADER_BUTTON_IMG,Cfg.PLAYGAME,(66,113))
    ViditeButton_P1 = Button(Cfg.VIDITE_BUTTON_IMG,Cfg.PLAYGAME,(236,113))
    QuraosButton_P1 = Button(Cfg.QURAOS_BUTTON_IMG,Cfg.PLAYGAME,(66,236))
    RhomosButton_P1 = Button(Cfg.RHOMOS_BUTTON_IMG,Cfg.PLAYGAME,(236,236))
    ElousButton_P1 = Button(Cfg.ELOUS_BUTTON_IMG,Cfg.PLAYGAME,(66,354))
    RonirButton_P1 = Button(Cfg.RONIR_BUTTON_IMG,Cfg.PLAYGAME,(236,354))

    BackButton = Button(Cfg.BACKBUTTON,Cfg.SELECTSIDES,(392,438))
    SettingsButton = Button(Cfg.SETTINGSBUTTON,Cfg.SETTINGS,(489,438))

    CeaderButton_P2 = Button(Cfg.CEADER_BUTTON_IMG,Cfg.PLAYGAME,(621,113))
    ViditeButton_P2 = Button(Cfg.VIDITE_BUTTON_IMG,Cfg.PLAYGAME,(787,113))
    QuraosButton_P2 = Button(Cfg.QURAOS_BUTTON_IMG,Cfg.PLAYGAME,(621,236))
    RhomosButton_P2 = Button(Cfg.RHOMOS_BUTTON_IMG,Cfg.PLAYGAME,(787,236))
    ElousButton_P2 = Button(Cfg.ELOUS_BUTTON_IMG,Cfg.PLAYGAME,(621,354))
    RonirButton_P2 = Button(Cfg.RONIR_BUTTON_IMG,Cfg.PLAYGAME,(787,354))

    ShipButton_P1 = {
        CeaderButton_P1 : Cfg.CEADER,
        ViditeButton_P1 : Cfg.VIDITE,
        QuraosButton_P1 : Cfg.QURAOS,
        RhomosButton_P1 : Cfg.RHOMOS,
        ElousButton_P1 : Cfg.ELOUS,
        RonirButton_P1 : Cfg.RONIR 
        }

    ShipButton_P2 = {
        CeaderButton_P2 : Cfg.CEADER,
        ViditeButton_P2 : Cfg.VIDITE,
        QuraosButton_P2 : Cfg.QURAOS,
        RhomosButton_P2 : Cfg.RHOMOS,
        ElousButton_P2 : Cfg.ELOUS,
        RonirButton_P2 : Cfg.RONIR 
        }   

    ControlButton = [
        BackButton,
        SettingsButton
    ]

    P1_GRID = Graph(
        [
        [CeaderButton_P1, [ViditeButton_P1,ViditeButton_P1,BackButton,QuraosButton_P1]],
        [ViditeButton_P1, [CeaderButton_P1,CeaderButton_P1,RhomosButton_P1,RonirButton_P1]],
        [QuraosButton_P1, [RhomosButton_P1,RhomosButton_P1,CeaderButton_P1,ElousButton_P1]],
        [RhomosButton_P1, [QuraosButton_P1,QuraosButton_P1,ViditeButton_P1,RonirButton_P1]],
        [ElousButton_P1, [RonirButton_P1,RonirButton_P1,QuraosButton_P1,BackButton]],
        [RonirButton_P1, [ElousButton_P1,ElousButton_P1,RhomosButton_P1,BackButton]],
        [BackButton, [SettingsButton,SettingsButton,RonirButton_P1,ViditeButton_P1]],
        [SettingsButton, [BackButton,BackButton,SettingsButton,SettingsButton]]
        ]   
    )

    P2_GRID = Graph(
        [
        [CeaderButton_P2, [ViditeButton_P2,ViditeButton_P2,SettingsButton,QuraosButton_P2]],
        [ViditeButton_P2, [CeaderButton_P2,CeaderButton_P2,RhomosButton_P2,RonirButton_P2]],
        [QuraosButton_P2, [RhomosButton_P2,RhomosButton_P2,CeaderButton_P2,ElousButton_P2]],
        [RhomosButton_P2, [QuraosButton_P2,QuraosButton_P2,ViditeButton_P2,RonirButton_P2]],
        [ElousButton_P2, [RonirButton_P2,RonirButton_P2,QuraosButton_P2,BackButton]],
        [RonirButton_P2, [ElousButton_P2,ElousButton_P2,RhomosButton_P2,BackButton]],
        [BackButton, [SettingsButton,SettingsButton,BackButton,BackButton]],
        [SettingsButton, [BackButton,BackButton,ElousButton_P2,CeaderButton_P2]]
        ]   
    )

    new_ships = get_new_ships()
    available_ships = get_available_ships()

    P1_Ship = ''
    P2_Ship = ''

    P1_Pointer, P1_Static = 2, 2
    P2_Pointer, P2_Static = 2, 2

    Active = True 

    while Active:
        Surface.blit(SelectSideBg,(0,0))
        ShipIcon.display(Surface)

        if P1_Ship:
            SelectedShip_P1 = copy.copy(P1_GRID.selected)
            SelectedShip_P1.location = (149,207)

            SelectedShip_P1.display(Surface)
            P1_ReadyIcon.display(Surface) 
        else:
            if P1_GRID.selected not in ControlButton:
                P1_GRID.selected.indicate(Surface,Cfg.SHIP_INDICATOR0)
            else:
                P1_GRID.selected.indicate(Surface,Cfg.BUTTON_INDICATOR)

            for Ship in ShipButton_P1.keys():
                if ShipButton_P1[Ship] in available_ships:
                    Ship.active = True
                    Ship.display(Surface)
                else:
                    Ship.greyed_out = Cfg.PlAYER_GREY_OUT
                    Ship.active = False
                    Ship.display(Surface)

                if Ship in new_ships:
                    Ship.indicate_at_loc(
                        Surface,Cfg.NEW_TAG,(Ship.rect_.left + 2,Ship.rect_.top - 65))

        if P2_Ship:
            SelectedShip_P2 = copy.copy(P2_GRID.selected)
            SelectedShip_P2.location = (687,207)

            SelectedShip_P2.display(Surface)
            P2_ReadyIcon.display(Surface)
        else:
            if P2_GRID.selected not in ControlButton:
                P2_GRID.selected.indicate(Surface,Cfg.SHIP_INDICATOR1)
            else:
                P2_GRID.selected.indicate(Surface,Cfg.BUTTON_INDICATOR0)

            for Ship in ShipButton_P2.keys():
                if ShipButton_P2[Ship] in available_ships:
                    Ship.active = True
                    Ship.display(Surface)
                else:
                    Ship.greyed_out = Cfg.PlAYER_GREY_OUT
                    Ship.active = False
                    Ship.display(Surface)

                if Ship in new_ships:
                    Ship.indicate_at_loc(
                        Surface,Cfg.NEW_TAG,(Ship.rect_.left + 2,Ship.rect_.top - 65))
        
        if P1_Ship and P2_Ship:
                break

        for button in ControlButton:   
            button.display(Surface)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == Cfg.P1_CONTROLS['left'] and P1_GRID.grid[P1_GRID.selected][0].active == True:
                    P1_GRID.move_left()

                if event.key == Cfg.P1_CONTROLS['right'] and P1_GRID.grid[P1_GRID.selected][1].active == True:
                    P1_GRID.move_right()

                if event.key == Cfg.P1_CONTROLS['up'] and P1_GRID.grid[P1_GRID.selected][2].active == True:
                    P1_GRID.move_up()

                if event.key == Cfg.P1_CONTROLS['down'] and P1_GRID.grid[P1_GRID.selected][3].active == True:
                    P1_GRID.move_down()

                if event.key == Cfg.P1_CONTROLS['select']:
                    if P1_GRID.selected.active == True:
                        if P1_GRID.selected not in ControlButton:
                            State1_P1, State2_P1 = '',ShipButton_P1[P1_GRID.selected]
                            P1_Ship = P1_GRID.selected.toggle(
                                P1_Ship,P1_Pointer,P1_Static,State1_P1,State2_P1)
                            P1_Pointer += 1
                        else:
                            P1_GRID.selected.select()                            
                            Active = False
    
                    
                if event.key == Cfg.P2_CONTROLS['left'] and P2_GRID.grid[P2_GRID.selected][0].active == True:
                    P2_GRID.move_left()

                if event.key == Cfg.P2_CONTROLS['right'] and P2_GRID.grid[P2_GRID.selected][1].active == True:
                    P2_GRID.move_right()

                if event.key == Cfg.P2_CONTROLS['up'] and P2_GRID.grid[P2_GRID.selected][2].active == True:
                    P2_GRID.move_up()

                if event.key == Cfg.P2_CONTROLS['down'] and P2_GRID.grid[P2_GRID.selected][3].active == True:
                    P2_GRID.move_down()

                if event.key == Cfg.P2_CONTROLS['select']:
                    if P2_GRID.selected.active == True:
                        if P2_GRID.selected not in ControlButton:
                            State1_P2, State2_P2 = '',ShipButton_P2[P2_GRID.selected]
                            P2_Ship = P2_GRID.selected.toggle(
                                P2_Ship,P2_Pointer,P2_Static,State1_P2,State2_P2)
                            P2_Pointer += 1
                        else:
                            P2_GRID.selected.select()

                            Active = False                
        
            

        pygame.display.update()

    if P2_Ship and P1_Ship:
        return [ShipButton_P1[P1_GRID.selected],ShipButton_P2[P2_GRID.selected]]

def Settings(Mode,Surface,SettingsBg):

    GameSettingsButton = Button(Cfg.GAMESETTINGS_IMAGE,Cfg.GAME_SETTINGS,(339,60))
    AchievementButton = Button(Cfg.ACHIEVEMENT_IMAGE,Cfg.ACHIEVEMENT,(346,380))
    HighScoreButton = Button(Cfg.HIGHSCORE_IMAGE,Cfg.HIGHSCORES,(367,271))
    MovesButton = Button(Cfg.MOVES_IMAGE,Cfg.MOVES,(390,166))

    BackButton = Button(Cfg.BACKBUTTON,Cfg.HOMESCREEN,(117,432))

    if Mode and Mode == '1P':
        BackButton.destination = Cfg.SELECTSHIP_1P
    elif Mode and Mode == '2P':
        BackButton.destination = Cfg.SELECTSHIP_2P

    SettingsGrid = Graph ([
        [GameSettingsButton,[GameSettingsButton,GameSettingsButton,BackButton,MovesButton]],
        [MovesButton, [MovesButton,MovesButton,GameSettingsButton,HighScoreButton]],
        [HighScoreButton, [HighScoreButton,HighScoreButton,MovesButton,AchievementButton]],
        [AchievementButton, [AchievementButton,AchievementButton,HighScoreButton,BackButton]],
        [BackButton, [BackButton,BackButton,AchievementButton,GameSettingsButton]]
    ]
    )

    Active = True

    while Active:
        
        Surface.blit(SettingsBg,(0,0))

        for button in SettingsGrid.grid.keys():
            button.display(Surface)

        SettingsGrid.selected.highlight(Surface)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == KEYUP:
                if Mode == '1P':
                    if event.key == Cfg.P1_CONTROLS['up']:
                        SettingsGrid.move_up()
                    if event.key == Cfg.P1_CONTROLS['down']:
                        SettingsGrid.move_down()
                    
                    if event.key == Cfg.P1_CONTROLS['select']:
                        SettingsGrid.selected.select()
                        Active = False

                elif Mode == '2P' or not Mode:
                    if event.key == Cfg.P2_CONTROLS['up'] or event.key == Cfg.P2_CONTROLS['up']:
                        SettingsGrid.move_up()
                    if event.key == Cfg.P2_CONTROLS['down'] or event.key == Cfg.P2_CONTROLS['down']:
                        SettingsGrid.move_down()
                    
                    if event.key == Cfg.P2_CONTROLS['select'] or event.key == Cfg.P2_CONTROLS['select']:
                        SettingsGrid.selected.select()
                        Active = False

                

        pygame.display.update()           
                    
def SelectStage():




    Active = True

    while Active:


        pygame.display.update()


def Moves():


    Active = True

    while Active:

        pygame.display.update()


def HighScores():


    Active = True

    while Active:


        pygame.display.update()


def Achievement():


    Active = True


    while Active:


        pygame.display.update()


def GameSettings():


    Active = True


    while Active:


        pygame.display.update()

