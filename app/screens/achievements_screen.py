from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

import sys
import os

PROJECT_PATH = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

sys.path.append(PROJECT_PATH)

from save import load_player, save_player
from achievements import check_achievements


class AchievementsScreen(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(
            orientation="vertical",
            spacing=15,
            padding=20,
            **kwargs
        )


        title = Label(
            text="[ ACHIEVEMENTS ]",
            font_size=35,
            color=(0, 0.8, 1, 1)
        )

        self.add_widget(title)


        self.info = Label(
            font_size=20
        )

        self.add_widget(self.info)


        refresh = Button(
            text="🔄 تحديث الإنجازات",
            size_hint=(1, 0.12)
        )

        refresh.bind(
            on_press=self.update_screen
        )

        self.add_widget(refresh)


        self.update_screen()



    def update_screen(self, instance=None):

        player = load_player()


        if player is None:

            self.info.text = "لا يوجد لاعب"

            return


        achievements = check_achievements(player)


        text = ""


        for achievement in achievements:


            if achievement["id"] in player["unlocked_achievements"]:

                status = "✅"

            else:

                status = "🔒"


            text += (
                f"{status} {achievement['name']}\n"
                f"⭐ {achievement['xp']} XP   "
                f"🪙 {achievement['coins']}\n\n"
            )


        self.info.text = text

        save_player(player)
