# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 17:43:55 2018

@author: strai
"""

import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load('images/enemy.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
    
    def update(self):
        self.x += (self.ai_settings.enemy_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    

    