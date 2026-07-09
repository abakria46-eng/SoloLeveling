from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from save import load_player, save_player
from stats import initialize_stats


class StatsScreen(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(
            orientation="vertical",
            spacing=15,
            padding=20,
            **kwargs
        )

        self.info = Label(
            font_size=22
        )

        self.add_widget(
            Label(
                text="[ STATS ]",
                font_size=35,
                color=(0, 0.8, 1, 1)
            )
        )

        self.add_widget(self.info)

        refresh = Button(
            text="🔄 تحديث الإحصائيات",
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
            self.info.text = "لا يوجد لاعب محفوظ"
            return

        player = initialize_stats(player)
        save_player(player)

        stats = player["stats"]

        self.info.text = f"""
💪 الضغط: {stats['pushups']}
🦵 السكوات: {stats['squats']}
🤸 البلانك: {stats['plank_seconds']} ثانية
🏃 الجري: {stats['run_km']} كم

📅 المهام اليومية: {stats['daily_quests_completed']}
⭐ إجمالي XP: {stats['total_xp']}
🪙 إجمالي العملات: {stats['total_coins']}
"""
