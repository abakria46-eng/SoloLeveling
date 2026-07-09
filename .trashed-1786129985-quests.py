from rich.console import Console
from datetime import date

from save import save_player, load_player
from player import add_xp, add_coins
from stats import update_stats
from achievements import show_achievements

console = Console()


def get_daily_quests(level):

    if level < 5:
        return [
            {
                "id": 1,
                "name": "10  ",
                "difficulty": " ",
                "xp": 15,
                "coins": 5
            },
            {
                "id": 2,
                "name": "20 ",
                "difficulty": " ",
                "xp": 15,
                "coins": 5
            },
            {
                "id": 3,
                "name": " 30 ",
                "difficulty": " ",
                "xp": 20,
                "coins": 10
            },
            {
                "id": 4,
                "name": " 1 ",
                "difficulty": " ",
                "xp": 20,
                "coins": 10
            }
        ]

    elif level < 10:
        return [
            {
                "id": 1,
                "name": "20  ",
                "difficulty": " ",
                "xp": 20,
                "coins": 10
            },
            {
                "id": 2,
                "name": "30 ",
                "difficulty": " ",
                "xp": 20,
                "coins": 10
            },
            {
                "id": 3,
                "name": " 60 ",
                "difficulty": " ",
                "xp": 30,
                "coins": 15
            },
            {
                "id": 4,
                "name": "   2 ",
                "difficulty": " ",
                "xp": 35,
                "coins": 20
            }
        ]

    return [
        {
            "id": 1,
            "name": "40  ",
            "difficulty": " ",
            "xp": 40,
            "coins": 20
        },
        {
            "id": 2,
            "name": "60 ",
            "difficulty": " ",
            "xp": 40,
            "coins": 20
        },
        {
            "id": 3,
            "name": " 3 ",
            "difficulty": " ",
            "xp": 60,
            "coins": 35
        },
        {
            "id": 4,
            "name": " 5 ",
            "difficulty": " ",
            "xp": 70,
            "coins": 40
        }
    ]


def daily_quests():

    player = load_player()

    if player is None:
        console.print("   .", style="red")
        return

    today = str(date.today())

    if "completed_quests" not in player:
        player["completed_quests"] = []

    if player.get("last_daily_quest") != today:
        player["completed_quests"] = []
        player["last_daily_quest"] = today
        save_player(player)

    quests = get_daily_quests(player["level"])

    console.print("\n==========   ==========", style="bold cyan")

    completed = len(player["completed_quests"])

    for quest in quests:

        if quest["id"] in player["completed_quests"]:
            console.print(
                f" {quest['id']}. {quest['name']} ()",
                style="green"
            )
        else:
            console.print(
                f"{quest['id']}. {quest['difficulty']} | {quest['name']}"
            )
            console.print(
                f"       {quest['xp']} XP     {quest['coins']} Coins"
            )
                console.print(
        f"\n : {completed}/{len(quests)}",
        style="yellow"
    )

    try:
        choice = int(input("\n   : "))
    except ValueError:
        console.print("   .", style="red")
        return

    selected = next((q for q in quests if q["id"] == choice), None)

    if selected is None:
        console.print("   .", style="red")
        return

    if selected["id"] in player["completed_quests"]:
        console.print(
            "     .",
            style="yellow"
        )
        return

    add_xp(player, selected["xp"])
    add_coins(player, selected["coins"])

    update_stats(
        player,
        selected["name"],
        selected["xp"],
        selected["coins"]
    )

    player["completed_quests"].append(selected["id"])

    if player.get("last_training") != today:
        player["streak"] += 1
        player["last_training"] = today

    if len(player["completed_quests"]) == len(quests):

        console.print(
            "\n     !",
            style="bold green"
        )

        add_xp(player, 50)
        add_coins(player, 25)

        player["stats"]["total_xp"] += 50
        player["stats"]["total_coins"] += 25

        console.print(" +50 XP", style="yellow")
        console.print(" +25 Coins", style="yellow")

    show_achievements(player)

    save_player(player)

    console.print(
        "\n",
        style="cyan"
    )

    console.print(
        "    ",
        style="green"
    )

    console.print(
        f" XP : {player['xp']}/{player['max_xp']}"
    )

    console.print(
        f" Coins : {player['coins']}"
    )

    console.print(
        f" Streak : {player['streak']} "
    ) 