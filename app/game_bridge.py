import os
import sys

# الرجوع إلى مجلد المشروع الرئيسي
PROJECT_PATH = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.append(PROJECT_PATH)


from save import load_player
from player import get_rank, get_streak_rank


def get_player_data():

    player = load_player()

    if player is None:
        return {
            "name": "Unknown",
            "level": 1,
            "xp": 0,
            "max_xp": 100,
            "rank": "E",
            "streak": 0,
            "streak_rank": "🌱 مبتدئ",
            "coins": 0
        }


    return {
        "name": player["name"],
        "level": player["level"],
        "xp": player["xp"],
        "max_xp": player["max_xp"],
        "rank": get_rank(player),
        "streak": player["streak"],
        "streak_rank": get_streak_rank(player),
        "coins": player["coins"]
    }
