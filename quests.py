from rich.console import Console
from save import save_player, load_player
from datetime import date

console = Console()


def daily_quests():

    player = load_player()

    if player is None:
        console.print("\n[red]لا يوجد لاعب محفوظ! قم بإنشاء لاعب أولاً.[/red]")
        return

    if "xp" not in player:
        player["xp"] = 0

    if "coins" not in player:
        player["coins"] = 0

    if "streak" not in player:
        player["streak"] = 0

    if "last_quest" not in player:
        player["last_quest"] = ""

    today = str(date.today())

    if player["last_quest"] == today:
        console.print("\n[red]لقد أنجزت المهام اليومية اليوم بالفعل![/red]")
        return


    quests = [
        ("💪 تمرين 10 دقائق", 20, 10),
        ("📚 قراءة أو تعلم شيء جديد", 15, 5),
        ("🧹 ترتيب مكانك", 10, 5),
        ("💧 شرب كمية كافية من الماء", 10, 5)
    ]


    console.print("\n========== المهام اليومية ==========\n",
                  style="cyan")

    for i, (quest, xp, coins) in enumerate(quests, 1):
        console.print(
            f"{i} - {quest}  "
            f"[green]+{xp} XP[/green] "
            f"[yellow]+{coins} Coins[/yellow]"
        )


    confirm = input("\nهل أكملت المهام اليوم؟ (y/n): ")


    if confirm.lower() != "y":
        console.print("\n[yellow]لم يتم استلام المكافآت.[/yellow]")
        return


    total_xp = 0
    total_coins = 0

    for quest, xp, coins in quests:
        total_xp += xp
        total_coins += coins


    player["xp"] += total_xp
    player["coins"] += total_coins
    player["streak"] += 1
    player["last_quest"] = today


    save_player(player)


    console.print("\n[green]تم إكمال المهام اليومية![/green]")
    console.print(f"[cyan]+{total_xp} XP[/cyan]")
    console.print(f"[yellow]+{total_coins} Coins[/yellow]")
    console.print(
        f"[magenta]السلسلة: {player['streak']} يوم[/magenta]"
    )