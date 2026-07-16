from save import load_player, save_player
from player import add_xp
from data.shop_data import SHOP_ITEMS
from datetime import date
from language import t


def get_shop_items():
    return SHOP_ITEMS


def buy_item(item_id):

    player = load_player()

    if player is None:
        return False, t("no_player")


    if "coins" not in player:
        player["coins"] = 0

    if "rest_days" not in player:
        player["rest_days"] = 2

    if "shop_history" not in player:
        player["shop_history"] = {}


    today = date.today()


    item = None

    for shop_item in SHOP_ITEMS:

        if shop_item["id"] == item_id:
            item = shop_item
            break


    if item is None:
        return False, t("not_found")


    if player["coins"] < item["price"]:
        return False, t("not_enough_coins")


    history = player["shop_history"]


    if item["type"] == "xp":

        last_buy = history.get(item["id"] + "_date")


        if last_buy:

            last_date = date.fromisoformat(last_buy)

            days = (today - last_date).days

            if days < item["cooldown_days"]:

                remaining = item["cooldown_days"] - days

                return False, f"{t('wait_days')} {remaining} {t('days')}"


        history[item["id"] + "_date"] = str(today)



    elif item["type"] == "rest_day":

        if player["rest_days"] >= 4:

            return False, t("max_rest")


        week_count = history.get("rest_day_week", 0)


        if week_count >= item["weekly_limit"]:

            return False, t("weekly_limit")


        history["rest_day_week"] = week_count + 1



    player["coins"] -= item["price"]


    if item["type"] == "xp":

        player = add_xp(player, item["value"])


    elif item["type"] == "rest_day":

        player["rest_days"] += item["value"]


    save_player(player)


    name = t(item["name_key"])

    return True, f"{t('buy_success')} {name}"
