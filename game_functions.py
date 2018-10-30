#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 16:57:00 2018

@author: fractum
"""
from enemy import Enemy
from bullet import Bullet
import sys
import pygame

movingKeys = (pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN)

def check_events(ship, bullets, ai_settings, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(1)
        elif event.type == pygame.KEYDOWN:
            if event.key in movingKeys: #Mowing
                ship.moving = True
                ship.movingDirection = event.key
            elif event.key == pygame.K_SPACE: #Shooting
                fire_bullet(ai_settings, screen, ship, bullets)
            elif event.key == pygame.K_q:
                sys.exit(1)
        elif event.type == pygame.KEYUP:
             if event.key in movingKeys:
                 ship.moving = False

def get_number_rows(ai_settings, ship_height, enemy_height):
    available_space_y = (ai_settings.screen_height - (3 * enemy_height) - ship_height)
    number_rows = int(available_space_y / (2 * enemy_height))
    return number_rows

def get_number_enemies_x(ai_settings, enemy_width):
    available_space_x = ai_settings.screen_width - 2 * enemy_width
    number_enemies_x = int(available_space_x / (2 * enemy_width))
    return number_enemies_x

def create_enemy(ai_settings, screen, enemies, enemy_number, row_number):
    enemy = Enemy(ai_settings, screen)
    enemy_width = enemy.rect.width
    enemy.x = enemy_width + 2 * enemy_width * enemy_number
    enemy.rect.x = enemy.x
    enemy.rect.y = enemy.rect.height + 2 * enemy.rect.height * row_number
    enemies.add(enemy)
            
def create_fleet(ai_settings, screen,ship,  enemies):
    enemy = Enemy(ai_settings, screen)
    number_enemies_x = get_number_enemies_x(ai_settings, enemy.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, enemy.rect.height)
    for row_number in range(number_rows):
        for enemy_number in range(number_enemies_x):
            create_enemy(ai_settings, screen, enemies, enemy_number, row_number)
         
            
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
                    newBullet = Bullet(ai_settings, screen, ship)
                    bullets.add(newBullet)
                    
def update_bullets_and_remove(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_screen(ship, bullets, ai_settings, screen, enemies):
    screen.fill(ai_settings.bg_color)
    if ship.moving:
        ship.move(ship.movingDirection)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    enemies.draw(screen)
    pygame.display.flip()
    
