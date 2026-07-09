from save import load_player, save_player
from player import add_xp
from datetime import date


def get_shop_items():

    return [
        {
            "id": "rest_day",
            "name": "🌴 يوم راحة إضافي",
            "price": 50,
            "type": "rest"
        },

        {
            "id": "xp_small",
            "name": "⚡ +50 XP",
            "price": 40,
            "type": "xp",
            "amount": 50,
            "limit": 3
        },

        {
            "id": "xp_large",
            "name": "🔥 +200 XP",
            "price": 150,
            "type": "xp",
            "amount": 200,
            "limit": 1
        }
    ]



def buy_item(item_id):

    player = load_player()

    if player is None:
        return False, "لا يوجد لاعب"



    if "coins" not in player:
        player["coins"] = 0


    if "rest_days" not in player:
        player["rest_days"] = 2


    if "shop_history" not in player:
        player["shop_history"] = {}



    today = str(date.today())



    if today not in player["shop_history"]:
        player["shop_history"] = {
            "date": today
        }



    item = None

    for shop_item in get_shop_items():

        if shop_item["id"] == item_id:
            item = shop_item
            break



    if item is None:
        return False, "العنصر غير موجود"



    if player["coins"] < item["price"]:
        return False, "🪙 العملات غير كافية"



    if item["type"] == "xp":

        key = item["id"]

        bought = player["shop_history"].get(key, 0)

        if bought >= item["limit"]:
            return False, "⛔ وصلت للحد اليومي لهذا العنصر"



        player["shop_history"][key] = bought + 1



    player["coins"] -= item["price"]



    if item["type"] == "rest":

        player["rest_days"] += 1



    elif item["type"] == "xp":

        player = add_xp(
            player,
            item["amount"]
        )



    save_player(player)


    return True, f"✅ تم شراء {item['name']}"
