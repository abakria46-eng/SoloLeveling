from rich.console import Console
from save import save_player, load_player
from player import add_xp, add_coins

console = Console()


def side_quests():

    player = load_player()

    console.print("\n========== المهام الإضافية ==========", style="cyan")

    quests = [
        {"name": "قراءة 20 دقيقة", "xp": 15, "coins": 5},
        {"name": "تعلم شيء جديد 10 دقائق", "xp": 20, "coins": 8},
        {"name": "ترتيب المكان", "xp": 10, "coins": 5},
        {"name": "مساعدة شخص", "xp": 25, "coins": 10},
        {"name": "كتابة أهداف اليوم", "xp": 15, "coins": 5}
    ]

    for i, quest in enumerate(quests, start=1):
        console.print(
            f"{i}. {quest['name']} (+{quest['xp']} XP | +{quest['coins']} 🪙)"
        )

    choice = int(input("\nاختر المهمة التي أنجزتها: "))

    if 1 <= choice <= len(quests):

        selected = quests[choice - 1]

        player = add_xp(player, selected["xp"])
        player = add_coins(player, selected["coins"])

        save_player(player)

        console.print(
            "\n🎉 أحسنت! تم إكمال المهمة",
            style="green"
        )

        console.print(
            f"⚡ +{selected['xp']} XP",
            style="yellow"
        )

        console.print(
            f"🪙 +{selected['coins']} Coins",
            style="yellow"
        )

    else:
        console.print("\nاختيار غير صحيح", style="red")