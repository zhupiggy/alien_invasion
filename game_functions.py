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


def check_events(gui_setting, screen, ship, bullets, stats, play_button, aliens, sb):
    """相应鼠标和键盘指令"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, gui_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(gui_setting, screen, stats, sb, play_button, ship,
                              aliens, bullets, mouse_x, mouse_y)


def update_screen(bg_color, gui_setting, screen, stats, ship, bullets, aliens,
                  play_button, sb):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(bg_color)
    sb.show_score()

    # 在飞船和外星人后边重绘所有自担
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # 如果游戏处于非活动状态， 绘制play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(gui_setting, screen, bullets, aliens, sb, stats):
    """更新子单位置、 并删除已经在屏幕消失的子弹"""
    bullets.update()

    # 删除在屏幕消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # 检测子弹与外星人的碰撞， 并销毁碰撞的外星人
    check_bullet_alien_collisions(gui_setting, screen, aliens, bullets, sb, stats)


def check_bullet_alien_collisions(gui_setting, screen, aliens, bullets, sb, stats):
    """响应碰撞"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for alien in collisions.values():
            stats.score += gui_setting.alien_points
            sb.prep_score()
        check_highscore(stats, sb)

    if len(aliens) == 0:
        # 删除现有子弹并创建新的外星人
        stats.level += 1
        sb.prep_level()
        bullets.empty()
        gui_setting.increase_speed()
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
            alien.y = 2 * alien_height + 2 * a * alien_height
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


def update_alien(gui_setting, stats, screen, ship, aliens, bullets, sb):
    """更新外星人位置"""
    check_fleet_edges(gui_setting, aliens)
    aliens.update()

    # 检测外星人与飞船的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(gui_setting, stats, screen, ship, aliens, bullets, sb)
    check_aliens_bottom(gui_setting, stats, screen, ship, aliens, bullets, sb)


def ship_hit(gui_setting, stats, screen, ship, aliens, bullets, sb):
    # 飞船被撞减1
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()

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
        pygame.mouse.set_visible(True)


def check_aliens_bottom(gui_setting, stats, screen, ship, aliens, bullets, sb):
    """检查是否有外星人到了底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(gui_setting, stats, screen, ship, aliens, bullets, sb)
            break


def check_play_button(gui_setting, screen, stats, sb, play_button, ship, aliens, bullets,
                      mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        # 重置游戏设置
        gui_setting.init_speed()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重置统计信息
        stats.reset_stats()
        stats.game_active = True

        # 重置记分牌
        sb.prep_level()
        sb.prep_score()
        sb.prep_ships()

        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并让飞船居中
        creat_aliens(gui_setting, screen, aliens)
        ship.center_ship()


def check_highscore(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
