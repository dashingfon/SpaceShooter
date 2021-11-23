
import pygame, sys
from pygame.locals import *
import SP_configuration as Cfg
import ui_functions as UI

import json

pygame.init()

MainClock = pygame.time.Clock()

WindowSurface = pygame.display.set_mode((Cfg.WINDOWWIDTH,Cfg.WINDOWHEIGHT),0,32)
pygame.display.set_caption('Space Shooter')
pygame.mouse.set_visible(False)

Sound = False
Music = False

P1_pointer = 1
P2_pointer = 1

pygame.event.post(pygame.event.Event(Cfg.HOMESCREEN))

GameBoard = {}
GameBoard['Mode'] = ''

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == Cfg.HOMESCREEN:
            UI.HomeScreen(WindowSurface,Cfg.HOMESCREEN_BACKGROUND)

        if event.type == Cfg.SELECTSIDES:
            game_parameters = UI.SelectSides(
            WindowSurface,
            Cfg.SELECTSIDES_BACKGROUND,
            Cfg.SELECTSIDE_ELEMENT,
            P1_pointer,
            P2_pointer)
            
            if game_parameters:
                P1_pointer, P2_pointer = game_parameters[1], game_parameters[2]
                GameBoard['Mode'] = game_parameters[0]

        if event.type == Cfg.SELECTSHIP_1P:

            GameBoard['Player1_ship'] = UI.SelectShip_1P(
                WindowSurface,Cfg.SELECTSIDES_BACKGROUND)

            with open('GameSettings.json') as GS:
                GameSettings = json.load(GS)
                SelectedShips = GameSettings['Game_Settings']['Selected_Ships']
            
            if GameBoard['Player1_ship'] not in SelectedShips and GameBoard['Player1_ship']:
                GameSettings['Game_Settings']['Selected_Ships'].append(
                    GameBoard['Player1_ship'])
                
                with open('GameSettings.json','w') as GS:
                    json.dump(GameSettings, GS,indent = 2)
                
        if event.type == Cfg.SELECTSHIP_2P:
            Selected_ships = UI.SelectShip_2P(
                WindowSurface,Cfg.SELECTSIDES_BACKGROUND)

            if Selected_ships:
                GameBoard['Player1_ship'], GameBoard['Player2_ship'] = Selected_ships

                with open('GameSettings.json') as GS:
                    GameSettings = json.load(GS)
                    SelectedShips = GameSettings['Game_Settings']['Selected_Ships']
                
                if GameBoard['Player1_ship'] not in SelectedShips:
                    GameSettings['Game_Settings']['Selected_Ships'].append(
                        GameBoard['Player1_ship'])

                    with open('GameSettings.json','w') as GS:
                        json.dump(GameSettings, GS, indent = 2)

                if GameBoard['Player2_ship'] not in SelectedShips:
                    GameSettings['Game_Settings']['Selected_Ships'].append(
                        GameBoard['Player2_ship'])        
                    
                    with open('GameSettings.json','w') as GS:
                        json.dump(GameSettings, GS, indent = 2)

        if event.type == Cfg.SETTINGS:
            UI.Settings(GameBoard['Mode'],WindowSurface,Cfg.SETTINGS_BACKGROUND)

        if event.type == Cfg.SELECTSTAGE:
            Stage = UI.SelectStage(WindowSurface,Cfg.SELECTSIDES_BACKGROUND)
            if Stage:
                GameBoard['Stage'] = Stage

        if event.type == Cfg.MOVES:
            UI.Moves(WindowSurface,Cfg.SETTINGS_BACKGROUND)

    pygame.display.update()
    MainClock.tick(Cfg.FPS)


