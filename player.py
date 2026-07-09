from datetime import date, timedelta


def create_player(name):
    return {
        "name": name,

        "level": 1,
        "xp": 0,
        "max_xp": 100,

        "strength": 5,
        "speed": 5,
        "endurance": 5,
        "flexibility": 5,

        "streak": 0,

        "coins": 0,

        "rest_days": 2,
        "last_rest_day": "",
        "last_rest_reset": str(date.today()),

        "last_training": "",
        "last_daily_quest": "",

        "completed_quests": [],

        "unlocked_achievements": []
    }


def add_xp(player, amount):

    player["xp"] += amount

    while player["xp"] >= player["max_xp"]:

        player["xp"] -= player["max_xp"]

        player["level"] += 1

        player["strength"] += 1
        player["speed"] += 1
        player["endurance"] += 1
        player["flexibility"] += 1

        print("\n🎉 ارتفع مستواك!")
        print(f"⭐ المستوى الجديد: {player['level']}")

    return player


def remove_xp(player, amount):

    player["xp"] = max(0, player["xp"] - amount)

    return player


def add_coins(player, amount):

    player["coins"] += amount

    return player


def remove_coins(player, amount):

    player["coins"] = max(0, player["coins"] - amount)

    return player


def use_rest_day(player):

    today = date.today()

    if player["rest_days"] <= 0:
        return False, "❌ لا توجد أيام راحة متبقية."

    if player["last_rest_day"]:

        yesterday = str(today - timedelta(days=1))

        if player["last_rest_day"] == yesterday:
            return False, "❌ لا يمكنك أخذ يومي راحة متتاليين."

    player["rest_days"] -= 1
    player["last_rest_day"] = str(today)

    return True, "🌴 تم استعمال يوم الراحة."


def reset_weekly_rest_days(player):

    today = date.today()

    if "last_rest_reset" not in player:
        player["last_rest_reset"] = str(today)
        return

    last_reset = date.fromisoformat(player["last_rest_reset"])

    if (today - last_reset).days >= 7:
        player["rest_days"] = 2
        player["last_rest_reset"] = str(today)


def get_rank(player):

    level = player["level"]

    if level >= 100:
        return "SSS"
    elif level >= 80:
        return "SS"
    elif level >= 60:
        return "S"
    elif level >= 40:
        return "A"
    elif level >= 25:
        return "B"
    elif level >= 15:
        return "C"
    elif level >= 5:
        return "D"
    else:
        return "E"


def get_streak_rank(player):

    streak = player["streak"]

    if streak >= 365:
        return "🌌 أسطورة الانضباط"
    elif streak >= 180:
        return "👑 ملك الإرادة"
    elif streak >= 100:
        return "🔥 أسطوري"
    elif streak >= 60:
        return "⚔️ محارب"
    elif streak >= 30:
        return "💪 منضبط"
    elif streak >= 14:
        return "🌟 مثابر"
    elif streak >= 7:
        return "🚀 بداية قوية"
    else:
        return "🌱 مبتدئ"