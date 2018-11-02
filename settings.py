# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 22:40:47 2018

@author: strai
"""


class Settings:
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        self.shipSpeed = 1
        
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        self.fleet_drop_speed = 10
        # 1 = right -1 = left
        self.fleet_direction = 1
         
        self.ship_limit = 3
        self.speedup_scale = 2
        
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.enemy_speed_factor = 1
        self.bullet_speed_factor = 2
        self.enemy_point = 50
        
        
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.enemy_speed_factor *= self.speedup_scale
    
    
        
        