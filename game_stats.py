class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, gui_setting):
        self.gui_setting = gui_setting
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.gui_setting.ships_left
