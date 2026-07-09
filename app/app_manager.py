import sys
import os

APP_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(APP_PATH)


from kivy.uix.screenmanager import ScreenManager, Screen

from screens.home_screen import HomeScreen
from screens.quests_screen import QuestsScreen
from screens.stats_screen import StatsScreen
from screens.achievements_screen import AchievementsScreen
from screens.shop_screen import ShopScreen



class HomePage(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(HomeScreen())



class QuestsPage(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(QuestsScreen())



class StatsPage(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(StatsScreen())



class AchievementsPage(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(AchievementsScreen())



class ShopPage(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(ShopScreen())



def create_manager():

    manager = ScreenManager()

    manager.add_widget(HomePage(name="home"))
    manager.add_widget(QuestsPage(name="quests"))
    manager.add_widget(StatsPage(name="stats"))
    manager.add_widget(AchievementsPage(name="achievements"))
    manager.add_widget(ShopPage(name="shop"))

    return manager
