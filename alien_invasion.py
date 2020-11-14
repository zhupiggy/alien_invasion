import sys

import pygame

from setting import Settings
from ship import Ship


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    gui_setting = Settings()
    screen = pygame.display.set_mode(
            (gui_setting.screen_width, gui_setting.screen_height))
            
    pygame.display.set_caption("Alien Invasion")
    
    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()

        # 每次循环都重绘屏幕
        screen.fill(gui_setting.bg_color)
        ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()