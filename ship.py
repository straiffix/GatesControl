# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 23:01:43 2018

@author: strai
"""

import pygame

class Ship():
    
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.image=pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving = False
        self.movingDirection = None
        self.ai_settings = ai_settings
        
    def update(self):
        if self.moving:
            self.rect.centerx +=1
    
    def move(self, key):
        if self.moving:
            if key == pygame.K_RIGHT and self.rect.right != 1200:
                self.rect.centerx += self.ai_settings.shipSpeed
            elif key == pygame.K_LEFT and self.rect.left != 0 :
                self.rect.centerx -= self.ai_settings.shipSpeed
            elif key == pygame.K_UP and self.rect.top!=0:
                self.rect.centery -= self.ai_settings.shipSpeed
            elif key == pygame.K_DOWN and self.rect.bottom!=800:
                self.rect.centery += self.ai_settings.shipSpeed
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)