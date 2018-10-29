#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 16:57:00 2018

@author: fractum
"""

import sys
import pygame

movingKeys = (pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN)

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(1)
        elif event.type == pygame.KEYDOWN:
            if event.key in movingKeys:
                ship.moving = True
             #   ship.move(event.key)
      #  elif event.type == pygame.KEYUP:
       #     if event.key in movingKeys:
       #         ship.moving = False
        
            

def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    pygame.display.flip()
    
    