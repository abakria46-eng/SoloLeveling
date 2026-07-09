import json
import os
import shutil

FILE_NAME = "player.json"
BACKUP_FILE = "player_backup.json"


def save_player(player):

    # إنشاء نسخة احتياطية قبل الحفظ
    if os.path.exists(FILE_NAME):
        shutil.copy(FILE_NAME, BACKUP_FILE)

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(
            player,
            file,
            ensure_ascii=False,
            indent=4
        )


def load_player():

    if not os.path.exists(FILE_NAME):
        return None

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            player = json.load(file)

    except json.JSONDecodeError:

        # محاولة استرجاع النسخة الاحتياطية
        if os.path.exists(BACKUP_FILE):
            shutil.copy(BACKUP_FILE, FILE_NAME)

            with open(FILE_NAME, "r", encoding="utf-8") as file:
                player = json.load(file)

        else:
            return None


    defaults = {

        "level": 1,
        "xp": 0,
        "max_xp": 100,

        "strength": 5,
        "speed": 5,
        "endurance": 5,
        "flexibility": 5,

        "coins": 0,

        "streak": 0,

        "rest_days": 2,
        "last_rest_day": "",

        "last_training": "",
        "last_daily_quest": "",
        "last_quest": "",

        "completed_quests": [],

        "unlocked_achievements": []
    }


    updated = False

    for key, value in defaults.items():

        if key not in player:
            player[key] = value
            updated = True


    if updated:
        save_player(player)


    return player