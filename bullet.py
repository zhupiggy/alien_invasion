# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """对飞船发射的子弹进行管理的类"""

    def __init__(self, gui_setting, screen, ship):
        """在飞船所处的位置创造一个子弹对象"""

        super().__init__()
        self.screen = screen

        # 在（0,0）处创建一个表示子弹的矩形， 再设置正确的位置
        self.rect = pygame.Rect(0, 0, gui_setting.bullet_width,
                                gui_setting.bullet_height)
