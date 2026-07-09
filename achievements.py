from rich.console import Console
from save import save_player
from player import add_xp, add_coins

console = Console()


def check_achievements(player):

    achievements = [

        {
            "id": "level_5",
            "condition": player["level"] >= 5,
            "name": "⭐ المستوى 5 - بداية التطور",
            "xp": 50,
            "coins": 25
        },

        {
            "id": "level_10",
            "condition": player["level"] >= 10,
            "name": "🔥 المستوى 10 - لاعب متقدم",
            "xp": 100,
            "coins": 50
        },

        {
            "id": "streak_7",
            "condition": player["streak"] >= 7,
            "name": "📅 7 أيام استمرارية",
            "xp": 100,
            "coins": 50
        },

        {
            "id": "streak_30",
            "condition": player["streak"] >= 30,
            "name": "🏆 30 يوم انضباط",
            "xp": 300,
            "coins": 150
        },

        {
            "id": "streak_100",
            "condition": player["streak"] >= 100,
            "name": "👑 100 يوم استمرارية",
            "xp": 1000,
            "coins": 500
        },

    ]

    return achievements


def show_achievements(player):

    console.print("\n========== الإنجازات ==========", style="bold cyan")

    unlocked = False

    for achievement in check_achievements(player):

        if not achievement["condition"]:
            continue

        if achievement["id"] not in player["unlocked_achievements"]:

            player["unlocked_achievements"].append(
                achievement["id"]
            )

            add_xp(player, achievement["xp"])
            add_coins(player, achievement["coins"])

            console.print(
                f"\n🏆 {achievement['name']}",
                style="bold green"
            )

            console.print(
                f"⭐ +{achievement['xp']} XP"
            )

            console.print(
                f"🪙 +{achievement['coins']} Coins"
            )

            unlocked = True

        else:

            console.print(
                f"✅ {achievement['name']}",
                style="green"
            )

    if not unlocked and len(player["unlocked_achievements"]) == 0:

        console.print(
            "لا توجد إنجازات بعد 🌱",
            style="yellow"
        )

    save_player(player)