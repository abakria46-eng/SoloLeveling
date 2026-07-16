from rich.console import Console
from language import t
from player import get_rank, get_streak_rank

console = Console()


def initialize_stats(player):

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


    console.print(
        f"\n========== {t('stats')} ==========",
        style="bold cyan"
    )


    console.print("\n🏋️ التمارين:")


    console.print(
        f"💪 {t('pushups')}: {player['stats']['pushups']}"
    )

    console.print(
        f"🦵 {t('squats')}: {player['stats']['squats']}"
    )

    console.print(
        f"🤸 {t('plank')}: {player['stats']['plank_seconds']} {t('seconds')}"
    )

    console.print(
        f"🏃 {t('running')}: {player['stats']['run_km']} {t('km')}"
    )


    console.print("\n📅 الإنجاز:")


    console.print(
        f"✅ {t('daily_quests_completed')}: {player['stats']['daily_quests_completed']}"
    )

    console.print(
        f"⭐ {t('total_xp')}: {player['stats']['total_xp']}"
    )

    console.print(
        f"🪙 {t('total_coins')}: {player['stats']['total_coins']}"
    )


    console.print("\n🔥 النظام:")


    console.print(
        f"🔥 {t('streak')}: {player.get('streak',0)} {t('day')}"
    )

    console.print(
        f"🏅 {t('rank')}: {get_rank(player)}"
    )

    console.print(
        f"🎖 {t('title')}: {get_streak_rank(player)}"
    )
