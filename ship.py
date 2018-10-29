# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 23:01:43 2018

@author: strai
"""

import pygame

class Ship():
    
    def __init__(self, screen):
        self.screen = screen
        self.image=pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving = False
        
    def update(self):
        if self.moving:
            self.rect.centerx +=1
    
    def move(self, key):
        if self.moving:
            if key == pygame.K_RIGHT:
                self.rect.centerx +=1
            elif key == pygame.K_LEFT:
                self.rect.centerx -=1
            elif key == pygame.K_UP:
                self.rect.centery -=1
            elif key == pygame.K_DOWN:
                self.rect.centery +=1
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)