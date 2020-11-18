class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, gui_setting):
        self.gui_setting = gui_setting
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        self.ships_left = self.gui_setting.ships_left
        self.score = 0
