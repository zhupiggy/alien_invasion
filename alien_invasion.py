import pygame

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

    # 创建一艘飞船
    ship = Ship(screen, gui_setting)

    # 开始游戏主循环
    while True:
        ship.update()
        gf.check_events(ship)
        gf.update_screen(gui_setting.bg_color, screen, ship)


run_game()
