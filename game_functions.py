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
from time import sleep

movingKeys = (pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN)

def check_events(sb, ship, bullets, ai_settings, screen, stats, play_button, enemies):
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(sb, ai_settings, screen, stats, play_button, ship, enemies,
bullets, mouse_x, mouse_y)

def check_play_button(sb, ai_settings, screen, stats, play_button, ship, enemies,
bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        enemies.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, enemies)
        ship.center_ship()

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
                    
def update_bullets_and_remove(enemies, bullets, screen, ship, ai_settings, stats, sb):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            check_bullet_enemy_collision(ai_settings, screen, ship, enemies, bullets, stats, sb)
    
    
def check_bullet_enemy_collision(ai_settings, screen, ship, enemies, bullets, stats, sb):
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    if collisions:
        for enemies in collisions.values():
            stats.score += ai_settings.enemy_point * len(enemies)
        sb.prep_score()
        check_hight_score(stats, sb)
    if len(enemies) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        stats.level +=1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, enemies)

def update_screen(sb, ship, bullets, ai_settings, screen, stats, enemies, play_button):
    screen.fill(ai_settings.bg_color)
    if ship.moving:
        ship.move(ship.movingDirection)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    enemies.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
    

def ship_hit(ai_settings, stats, screen, ship, enemies, bullets, sb):
    if stats.ships_left > 0:
        stats.ships_left -=1
        sb.prep_ships()
        enemies.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, enemies)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
  

def update_enemies(ai_settings, enemies, ship, stats, screen, bullets, sb):
    check_fleet_edges(ai_settings, enemies)
    enemies.update()
    if pygame.sprite.spritecollideany(ship, enemies):
        print("Hit!")
        ship_hit(ai_settings, stats, screen, ship, enemies, bullets, sb)
    check_enemies_bottom(ai_settings, stats, screen, ship, enemies, bullets, sb)
    
def check_fleet_edges(ai_settings, enemies):
    for enemy in enemies.sprites():
        if enemy.check_edges():
            change_fleet_direction(ai_settings, enemies)
            break
        
def change_fleet_direction(ai_settings, enemies):
    for enemy in enemies.sprites():
        enemy.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_enemies_bottom(ai_settings, stats, screen, ship, enemies, bullets, sb):
    screen_rect = screen.get_rect()
    for enemy in enemies.sprites():
        if enemy.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, enemies, bullets, sb)
            break
    
def check_hight_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

    
