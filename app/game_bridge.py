import os
import sys

PROJECT_PATH = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_PATH not in sys.path:
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
        "name": player.get("name", "Unknown"),
        "level": player.get("level", 1),
        "xp": player.get("xp", 0),
        "max_xp": player.get("max_xp", 100),
        "rank": get_rank(player),
        "streak": player.get("streak", 0),
        "streak_rank": get_streak_rank(player),
        "coins": player.get("coins", 0)
    }
