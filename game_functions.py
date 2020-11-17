import sys

import pygame

from bullet import Bullet


def fire_bullets(gui_setting, screen, ship, bullets):
    if len(bullets) < gui_setting.bullets_allowed:
        new_bullet = Bullet(gui_setting, screen, ship)
        bullets.add(new_bullet)


def check_keydown_events(event, gui_setting, screen, ship, bullets):
    """相应案件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(gui_setting, screen, ship, bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(gui_setting, screen, ship, bullets):
    """相应鼠标和键盘指令"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, gui_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(bg_color, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(bg_color)
    # 在飞船和外星人后边重绘所有自担
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    """更新子单位置、 并删除已经在屏幕消失的子弹"""
    bullets.update()

    # 删除在屏幕消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
