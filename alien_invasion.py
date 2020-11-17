import pygame
from pygame.sprite import Group

from setting import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """初始化pygame、设置和屏幕"""
    pygame.init()
    gui_setting = Settings()
    screen = pygame.display.set_mode(
        (gui_setting.screen_width, gui_setting.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # 创建飞船、子弹
    ship = Ship(screen, gui_setting)
    bullets = Group()

    # 开始游戏主循环
    while True:
        gf.check_events(gui_setting, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(gui_setting.bg_color, screen, ship, bullets)


run_game()
