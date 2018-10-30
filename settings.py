# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 22:40:47 2018

@author: strai
"""
import pygame

class Settings:
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.shipSpeed = 1
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        