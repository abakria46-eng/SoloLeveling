
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from datetime import date

from save import load_player, save_player
from player import add_xp, add_coins


class QuestsScreen(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(
            orientation="vertical",
            spacing=15,
            padding=20,
            **kwargs
        )

        self.completed = False

        title = Label(
            text="[ DAILY QUESTS ]",
            font_size=35,
            color=(0, 0.8, 1, 1)
        )

        self.add_widget(title)

        self.message = Label(
            text="اختر المهام التي أنجزتها",
            font_size=20
        )

        self.add_widget(self.message)

        self.quests = [
            ("💪 تمرين 10 دقائق", 20, 10),
            ("📚 تعلم شيء جديد", 15, 5),
            ("🧹 ترتيب المكان", 10, 5),
            ("💧 شرب الماء", 10, 5)
        ]

        self.selected = []

        for index, quest in enumerate(self.quests):

            button = Button(
                text=quest[0],
                size_hint=(1, 0.12)
            )

            button.bind(
                on_press=lambda instance, i=index: self.select_quest(i)
            )

            self.add_widget(button)

        complete = Button(
            text="✅ استلام المكافأة",
            size_hint=(1, 0.15)
        )

        complete.bind(
            on_press=self.complete_quests
        )

        self.add_widget(complete)

    def select_quest(self, index):

        if index in self.selected:
           
            self.selected.remove(index)
        else:
            self.selected.append(index)

        self.message.text = f"تم اختيار {len(self.selected)} مهام"

    def complete_quests(self, instance):

        player = load_player()

        if player is None:
            self.message.text = "لا يوجد لاعب"
            return

        today = str(date.today())

        if player.get("last_quest") == today:
            self.message.text = "تم إنجاز مهام اليوم مسبقًا"
            return

        if len(self.selected) == 0:
            self.message.text = "اختر مهمة واحدة على الأقل"
            return

        total_xp = 0
        total_coins = 0

        for i in self.selected:
            quest = self.quests[i]
            total_xp += quest[1]
            total_coins += quest[2]

        player = add_xp(player, total_xp)
        player = add_coins(player, total_coins)

        player["streak"] += 1
        player["last_quest"] = today

        save_player(player)

        self.message.text = (
            f"✅ تم الإنجاز\n"
            f"⭐ +{total_xp} XP\n"
            f"🪙 +{total_coins} Coins"
        )

        self.selected.clear()
