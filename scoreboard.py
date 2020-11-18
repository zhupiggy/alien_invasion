import pygame.font
from pygame.sprite import Group

from ship import Ship


class ScoreBoard():
    """显示得分信息"""

    def __init__(self, gui_setting, screen, stats):
        self.gui_setting = gui_setting
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats

        # 字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 30)

        # 准备初始得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        rounded_score = int(round(self.stats.score, - 1))
        score_str = 'Score: ' + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # 安置在右上角
        self.rect = self.score_image.get_rect()
        self.rect.right = self.screen_rect.right - 20
        self.rect.top = 0

    def prep_high_score(self):
        high_score = int(round(self.stats.score, - 1))
        high_score_str = "HighScore: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        # 安置在中上
        self.high_rect = self.high_score_image.get_rect()
        self.high_rect.centerx = self.screen_rect.centerx
        self.high_rect.top = 0

    def prep_level(self):
        msg = 'Level: ' + str(self.stats.level)
        self.level_image = self.font.render(msg, True, self.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 30

    def prep_ships(self):
        self.ships = Group()
        for ship_num in range(self.stats.ships_left):
            ship = Ship(self.screen, self.gui_setting)
            ship.rect.x = 10 + ship_num * ship.rect.width
            ship.rect.y = 0
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image, self.rect)
        self.screen.blit(self.high_score_image, self.high_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
