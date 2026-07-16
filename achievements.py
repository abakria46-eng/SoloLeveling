from save import save_player
from data.achievement_data import ACHIEVEMENTS
from player import add_xp
from language import t


def show_achievements(player):

    print(f"\n========== {t('achievements')} ==========")

    if "unlocked_achievements" not in player:
        player["unlocked_achievements"] = []

    new_unlock = False


    for achievement in ACHIEVEMENTS:

        achievement_id = achievement["id"]


        if achievement_id in player["unlocked_achievements"]:

            status = "✅"

        else:

            if achievement["condition"](player):

                player["unlocked_achievements"].append(
                    achievement_id
                )

                player = add_xp(
                    player,
                    achievement["xp"]
                )


                player["coins"] += achievement["coins"]


                print(f"\n🎉 {achievement['name']}")
                print(f"⭐ +{achievement['xp']} XP")
                print(f"🪙 +{achievement['coins']} {t('coins')}")


                new_unlock = True
                status = "✅"

            else:

                status = "🔒"


        print(f"{status} | {achievement['name']}")


    if new_unlock:

        save_player(player)
