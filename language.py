import json
import os

from save import load_player


LANG_PATH = "data/language"


def get_language():

    player = load_player()

    if player and "settings" in player:

        return player["settings"].get(
            "language",
            "ar"
        )

    return "ar"



def load_language():

    lang = get_language()

    file_path = os.path.join(
        LANG_PATH,
        f"{lang}.json"
    )


    if not os.path.exists(file_path):

        lang = "ar"

        file_path = os.path.join(
            LANG_PATH,
            "ar.json"
        )


    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def t(key):

    language = load_language()

    return language.get(
        key,
        key
    )
