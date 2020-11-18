class Settings():
    """存储外星人的所有设置类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # 外星人设置
        self.drop_speed = 10
        self.direction = 1

        # 飞船设置
        self.ships_left = 3

        # 游戏进程加速
        self.speed_scale = 1.1
        self.init_speed()

    def init_speed(self):
        self.ship_speed = 1.5
        self.bullet_speed = 1
        self.alien_speed = 0.5
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.alien_speed *= self.speed_scale
        self.alien_points = int(self.speed_scale * self.alien_points)
