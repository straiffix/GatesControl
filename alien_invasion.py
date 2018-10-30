# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 23:46:43 2018

@author: strai
"""

import pygame
from pygame.sprite import Group
import game_functions as game
from settings import Settings as Sett
from ship import Ship
from enemy import Enemy

movingKeys = (pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN)

def run_game():
    pygame.init()
    ai_settings = Sett()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen.fill((255, 255, 255))
    
    pygame.display.set_caption("Gate Control")
   
    ship = Ship(screen, ai_settings)
    enemy = Enemy(ai_settings, screen)
    
    bullets = Group()
    enemies = Group()
    
    game.create_fleet(ai_settings, screen, ship, enemies)
    
    running = True #Change for autimatical end of the loop
    
    while running:
        game.check_events(ship, bullets, ai_settings, screen)
       # pygame.display.flip()
        game.update_bullets_and_remove(bullets) #Removing old bullets
      # ship.update()                
        game.update_screen(ship, bullets, ai_settings, screen, enemies)

run_game()
