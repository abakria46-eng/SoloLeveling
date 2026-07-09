from rich.console import Console

console = Console()


def initialize_stats(player):
    """
    إنشاء الإحصائيات إذا لم تكن موجودة.
    """

    if "stats" not in player:
        player["stats"] = {
            "pushups": 0,
            "squats": 0,
            "plank_seconds": 0,
            "run_km": 0,
            "daily_quests_completed": 0,
            "weekly_quests_completed": 0,
            "total_xp": 0,
            "total_coins": 0
        }

    return player


def update_stats(player, quest_name, xp, coins):

    initialize_stats(player)

    name = quest_name.lower()

    if "ضغط" in name:
        player["stats"]["pushups"] += extract_number(quest_name)

    elif "سكوات" in name:
        player["stats"]["squats"] += extract_number(quest_name)

    elif "بلانك" in name:
        player["stats"]["plank_seconds"] += extract_number(quest_name)

    elif "كم" in name:
        player["stats"]["run_km"] += extract_number(quest_name)

    player["stats"]["daily_quests_completed"] += 1
    player["stats"]["total_xp"] += xp
    player["stats"]["total_coins"] += coins

    return player


def extract_number(text):
    """
    استخراج أول رقم من النص.
    """

    number = ""

    for char in text:
        if char.isdigit():
            number += char
        elif number:
            break

    if number == "":
        return 0

    return int(number)


def show_stats(player):

    initialize_stats(player)

    console.print("\n========== الإحصائيات ==========", style="bold cyan")

    console.print(f"💪 الضغط: {player['stats']['pushups']}")
    console.print(f"🦵 السكوات: {player['stats']['squats']}")
    console.print(f"🤸 البلانك: {player['stats']['plank_seconds']} ثانية")
    console.print(f"🏃 الجري: {player['stats']['run_km']} كم")
    console.print(f"📅 المهام اليومية: {player['stats']['daily_quests_completed']}")
    console.print(f"⭐ إجمالي XP: {player['stats']['total_xp']}")
    console.print(f"🪙 إجمالي العملات: {player['stats']['total_coins']}")