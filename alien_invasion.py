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
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


movingKeys = (pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN)

def run_game():
    pygame.init()
    ai_settings = Sett()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen.fill((255, 255, 255))
    
    pygame.display.set_caption("Gate Control")
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, "Play")
    ship = Ship(screen, ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    
    bullets = Group()
    enemies = Group()
    
    game.create_fleet(ai_settings, screen, ship, enemies)
    
    running = True #Change for autimatical end of the loop
    
    while running:
        game.check_events(sb, ship, bullets, ai_settings, screen, stats, play_button, enemies)
        if stats.game_active:
           game.update_bullets_and_remove(enemies, bullets, screen, ship, ai_settings, stats, sb) #Removing old bullets
           game.update_enemies(ai_settings, enemies, ship, stats, screen, bullets, sb)              
        game.update_screen(sb, ship, bullets, ai_settings, screen, stats, enemies, play_button)

run_game()
