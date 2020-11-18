import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, gui_setting, screen):
        """外星人：初始化、位置确定"""
        super().__init__()
        self.screen = screen
        self.gui_setting = gui_setting

        # 加载外星人，设置其rect属性
        self.image = pygame.image.load("ship.png")
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """移动外星人"""
        self.x += self.gui_setting.alien_speed * self.gui_setting.direction
        self.rect.x = self.x

    def check_edges(self):
        """检测外星人是否靠近屏幕边缘"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
