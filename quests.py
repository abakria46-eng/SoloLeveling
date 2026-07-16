from rich.console import Console
from datetime import date

from save import save_player, load_player
from player import add_xp, add_coins
from stats import update_stats
from data.quest_data import QUESTS

console = Console()


def daily_quests():

    player = load_player()

    if player is None:
        console.print("❌ لا يوجد لاعب")
        return


    if "last_quest" not in player:
        player["last_quest"] = ""


    today = str(date.today())


    if player["last_quest"] == today:

        console.print(
            "\n[red]لقد أنجزت المهام اليومية اليوم بالفعل![/red]"
        )
        return


    console.print(
        "\n========== المهام اليومية ==========\n",
        style="cyan"
    )


    for i, quest in enumerate(QUESTS,1):

        console.print(
            f"{i} - {quest['name']} "
            f"+{quest['xp']} XP "
            f"+{quest['coins']} Coins"
        )


    confirm = input(
        "\nهل أكملت المهام اليوم؟ (y/n): "
    )


    if confirm.lower() != "y":

        console.print(
            "لم يتم استلام المكافآت"
        )
        return



    total_xp = 0
    total_coins = 0


    for quest in QUESTS:

        total_xp += quest["xp"]
        total_coins += quest["coins"]

        player = update_stats(
            player,
            quest["name"],
            quest["xp"],
            quest["coins"]
        )


    player = add_xp(player,total_xp)

    player = add_coins(player,total_coins)


    player["streak"] += 1

    player["last_quest"] = today


    save_player(player)


    console.print(
        "\n[green]✅ تم إكمال المهام اليومية![/green]"
    )

    console.print(
        f"⭐ +{total_xp} XP"
    )

    console.print(
        f"🪙 +{total_coins} Coins"
    )

    console.print(
        f"🔥 السلسلة: {player['streak']} يوم"
    )
