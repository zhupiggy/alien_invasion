import pygame
from pygame.sprite import Group

from setting import Settings
import game_functions as gf
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


def run_game():
    """初始化pygame、设置和屏幕"""
    pygame.init()
    gui_setting = Settings()
    screen = pygame.display.set_mode(
        (gui_setting.screen_width, gui_setting.screen_height))

    pygame.display.set_caption("Alien Invasion")
    play_button = Button(gui_setting, screen, "PLAY")
    stats = GameStats(gui_setting)
    sb = ScoreBoard(gui_setting, screen, stats)
    # 创建飞船、子弹、外星人
    ship = Ship(screen, gui_setting)

    bullets = Group()

    aliens = Group()
    # 创建一群外星人
    gf.creat_aliens(gui_setting, screen, aliens)

    # 开始游戏主循环
    while True:
        gf.check_events(gui_setting, screen, ship, bullets, stats, play_button, aliens, sb)
        if stats.game_active == True:
            ship.update()
            gf.update_bullets(gui_setting, screen, bullets, aliens, sb, stats)
            gf.update_alien(gui_setting, stats, screen, ship, aliens, bullets, sb)
        gf.update_screen(gui_setting.bg_color, gui_setting, screen, stats, ship, bullets, aliens,
                         play_button, sb)


run_game()
