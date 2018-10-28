# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 23:46:43 2018

@author: strai
"""

import sys
import pygame
from settings import Settings as Sett
from ship import Ship

def run_game():
    pygame.init()
    ai_settings = Sett()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    ship = Ship(screen)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            screen.fill(ai_settings.bg_color)
            ship.blitme()
            pygame.display.flip()

run_game()