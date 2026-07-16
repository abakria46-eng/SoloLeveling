from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from app.game_bridge import get_player_data


class HomeScreen(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(
            orientation="vertical",
            spacing=15,
            padding=20,
            **kwargs
        )

        player = get_player_data()

        title = Label(
            text="[ SYSTEM ]",
            font_size=40,
            color=(0, 0.8, 1, 1)
        )

        self.add_widget(title)


        info = Label(
            text=f"""
👤 الاسم: {player['name']}

⭐ المستوى: {player['level']}
⚡ XP: {player['xp']} / {player['max_xp']}
🏅 الرتبة: {player['rank']}

🔥 السلسلة: {player['streak']} يوم
🎖 اللقب: {player['streak_rank']}

🪙 العملات: {player['coins']}
""",
            font_size=22
        )

        self.add_widget(info)


        buttons = [
            ("⚔️ المهام اليومية", "quests"),
            ("📖 دليل الصياد", "codex"),
            ("📊 الإحصائيات", "stats"),
            ("🏆 الإنجازات", "achievements"),
            ("🛒 المتجر", "shop")
        ]


        for text, page in buttons:

            button = Button(
                text=text,
                size_hint=(1, 0.12)
            )

            button.bind(
                on_press=lambda instance, p=page: self.open_page(p)
            )

            self.add_widget(button)


    def open_page(self, page):

        if self.parent:
            self.parent.manager.current = page
