from kivy.app import App
from kivy.core.window import Window

from app_manager import create_manager


Window.clearcolor = (0.02, 0.02, 0.05, 1)


class SoloLevelingApp(App):

    def build(self):

        return create_manager()



if __name__ == "__main__":
    SoloLevelingApp().run()
