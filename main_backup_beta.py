from rich.console import Console

from save import save_player, load_player
from player import create_player, get_rank, get_streak_rank, use_rest_day
from quests import daily_quests
from shop import get_shop_items, buy_item
from achievements import show_achievements
from settings import (
    show_body_data,
    edit_body_data,
    show_settings,
    edit_settings
)
from stats import show_stats
from language import t


console = Console()


def pause():
    input(f"\n{t('back')}...")


def show_player(player):

    console.print(
        f"\n========== {t('player_data')} ==========",
        style="cyan"
    )

    console.print(f"👤 {t('name')}      : {player['name']}")
    console.print(f"🏅 {t('rank')}     : {get_rank(player)}")
    console.print(f"⭐ {t('level')}    : {player['level']}")
    console.print(f"⚡ {t('xp')}       : {player['xp']}/{player['max_xp']}")
    console.print(f"💪 {t('strength')} : {player['strength']}")
    console.print(f"🏃 {t('speed')}    : {player['speed']}")
    console.print(f"🛡 {t('endurance')}: {player['endurance']}")
    console.print(f"🤸 {t('flexibility')}: {player['flexibility']}")
    console.print(f"🔥 {t('streak')}   : {player['streak']} {t('day')}")
    console.print(f"🎖 {t('title')} : {get_streak_rank(player)}")
    console.print(f"🪙 {t('coins')}    : {player['coins']}")
    console.print(f"🌴 {t('rest_days')}: {player.get('rest_days', 0)}")


def open_shop():

    while True:

        console.print(
            f"\n========== {t('shop')} ==========",
            style="green"
        )

        for item in get_shop_items():

            console.print(
                f"{item['id']} | {t(item['name_key'])} | 🪙 {item['price']}"
            )

        console.print(f"0️⃣ {t('back')}")

        choice = input("\nID: ")

        if choice == "0":
            break

        success, message = buy_item(choice)

        console.print(message)

        pause()


def open_settings():

    while True:

        console.print(
            f"\n========== {t('settings')} ==========",
            style="green"
        )

        console.print("1️⃣ تعديل بيانات الجسم")
        console.print("2️⃣ عرض بيانات الجسم")
        console.print("3️⃣ استخدام يوم الراحة")
        console.print("4️⃣ عرض إعدادات النظام")
        console.print("5️⃣ تعديل إعدادات النظام")
        console.print(f"0️⃣ {t('back')}")

        choice = input("\nاختر: ")

        if choice == "1":

            edit_body_data()
            pause()

        elif choice == "2":

            show_body_data()
            pause()

        elif choice == "3":

            player = load_player()

            success, message = use_rest_day(player)

            console.print(message)

            save_player(player)

            pause()

        elif choice == "4":

            show_settings()
            pause()

        elif choice == "5":

            edit_settings()
            pause()

        elif choice == "0":

            break

        else:

            console.print("❌ اختيار غير صحيح")
            pause()


console.print(
    "╔══════════════════════════════╗",
    style="cyan"
)

console.print(
    "║    SOLO LEVELING SYSTEM     ║",
    style="bold green"
)

console.print(
    "╚══════════════════════════════╝",
    style="cyan"
)


player = load_player()


if player is None:

    name = input("\nاكتب اسم اللاعب: ")

    player = create_player(name)

    save_player(player)


while True:

    player = load_player()

    show_player(player)


    console.print(
        f"\n========== {t('menu')} ==========",
        style="green"
    )

    console.print(f"1️⃣  {t('daily_quests')}")
    console.print(f"2️⃣  {t('stats')}")
    console.print(f"3️⃣  {t('achievements')}")
    console.print(f"4️⃣  {t('shop')}")
    console.print(f"5️⃣  {t('settings')}")
    console.print(f"0️⃣  {t('exit')}")


    choice = input("\nاختر: ")


    if choice == "1":

        daily_quests()
        pause()


    elif choice == "2":

        show_stats(load_player())
        pause()


    elif choice == "3":

        show_achievements(load_player())
        pause()


    elif choice == "4":

        open_shop()


    elif choice == "5":

        open_settings()


    elif choice == "0":

        console.print("\n👋 إلى اللقاء.", style="red")
        break


    else:

        console.print("\n❌ اختيار غير صحيح")
        pause()
