import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien


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
    elif event.key == pygame.K_q:
        sys.exit()


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


def update_screen(bg_color, screen, ship, bullets, aliens):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(bg_color)

    # 在飞船和外星人后边重绘所有自担
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(gui_setting, screen, bullets, aliens):
    """更新子单位置、 并删除已经在屏幕消失的子弹"""
    bullets.update()

    # 删除在屏幕消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # 检测子弹与外星人的碰撞， 并销毁碰撞的外星人
    check_bullet_alien_collisions(gui_setting, screen, aliens, bullets)


def check_bullet_alien_collisions(gui_setting, screen, aliens, bullets):
    """响应碰撞"""
    colisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # 删除现有子弹并创建新的外星人
        bullets.empty()
        creat_aliens(gui_setting, screen, aliens)


def creat_aliens(gui_setting, screen, aliens):
    """创建一群外星人"""
    # 计算可以容纳的外星人 行数、 列数
    alien = Alien(gui_setting, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    space_x = gui_setting.screen_width - 2 * alien_width
    space_y = gui_setting.screen_height * 3 / 5

    num_x = int(space_x / (2 * alien_width))
    num_y = int(space_y / (2 * alien_height))

    # 创建行、列 外星人
    for a in range(num_y):
        for b in range(num_x):
            alien = Alien(gui_setting, screen)
            alien.y = alien_height + 2 * a * alien_height
            alien.rect.y = alien.y
            alien.x = alien_width + 2 * b * alien_width
            alien.rect.x = alien.x
            aliens.add(alien)


def check_fleet_edges(gui_setting, aliens):
    """外星人到达屏幕边缘时采取措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_direction(gui_setting, aliens)
            break


def change_direction(gui_setting, aliens):
    """外星人整体下移，并改变移动方向"""
    for alien in aliens.sprites():
        alien.rect.y += gui_setting.drop_speed
    gui_setting.direction *= -1


def update_alien(gui_setting, stats, screen, ship, aliens, bullets):
    """更新外星人位置"""
    check_fleet_edges(gui_setting, aliens)
    aliens.update()

    # 检测外星人与飞船的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit
    check_aliens_bottom(gui_setting, stats, screen, ship, aliens, bullets)


def ship_hit(gui_setting, stats, screen, ship, aliens, bullets):
    # 飞船被撞减1
    if stats.ships_left > 0:
        stats.ships_left -= 1

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建新的外星人， 并将飞船放置在屏幕底端中央
        creat_aliens(gui_setting, screen, aliens)
        ship.center_ship()

        # 暂停
        sleep(1)
    else:
        stats.game_active = False


def check_aliens_bottom(gui_setting, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到了底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(gui_setting, stats, screen, ship, aliens, bullets)
            break
