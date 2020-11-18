import pygame
import pygame.font


class Button():
    """docstring for Button"""

    def __init__(self, gui_setting, screen, msg):
        self.gui_setting = gui_setting
        self.screen = screen
        self.msg = msg
        self.screen_rect = self.screen.get_rect()

        # 字体设置
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 字体后框设置
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 渲染到surface
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制一个用颜色填充的按钮， 再绘制文本
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
