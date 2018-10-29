# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 23:46:43 2018

@author: strai
"""

import pygame
import game_functions as game
from settings import Settings as Settings
from ship import Ship

#movingKeys = (pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN)

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen.fill((255, 255, 255))
    pygame.display.set_caption("Alien Invasion")
   
    
  #  ship = Ship(screen)
    
    #done = False
    
  #  while True:
   #     game.check_events()
        #ship.update()                
    #    game.update_screen(ai_settings, screen, ship)

run_game()