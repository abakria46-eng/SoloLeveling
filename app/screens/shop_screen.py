from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from shop import get_shop_items, buy_item
from save import load_player


class ShopScreen(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(
            orientation="vertical",
            spacing=15,
            padding=20,
            **kwargs
        )

        title = Label(
            text="[ 🛒 SHOP ]",
            font_size=35,
            color=(0, 0.8, 1, 1)
        )

        self.add_widget(title)

        self.status = Label(
            text="اختر مكافأتك",
            font_size=20
        )

        self.add_widget(self.status)

        self.coins_label = Label(
            font_size=22
        )

        self.add_widget(self.coins_label)

        self.rest_label = Label(
            font_size=20
        )

        self.add_widget(self.rest_label)

        for item in get_shop_items():

            button = Button(
                text=f"{item['name']}  |  {item['price']} 🪙",
                size_hint=(1, 0.12)
            )

            button.bind(
                on_press=lambda instance, x=item:
                self.buy(x["id"])
            )

            self.add_widget(button)

        self.update_info()

    def buy(self, item_id):

        success, message = buy_item(item_id)

        self.status.text = message

        self.update_info()

    def update_info(self):

        player = load_player()

        if player:

            self.coins_label.text = (
                f"🪙 العملات: {player.get('coins', 0)}"
            )

            self.rest_label.text = (
                f"🌴 أيام الراحة: {player.get('rest_days', 0)}"
            )
