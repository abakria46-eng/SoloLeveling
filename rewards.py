def level_up_rewards(player):

    rewards = []

    level = player["level"]

    # كل مستويين: 10 عملات
    if level % 2 == 0:
        player["coins"] += 10
        rewards.append("🪙 +10 Coins")

    # كل 5 مستويات: يوم راحة إضافي
    if level % 5 == 0:
        player["rest_days"] += 1
        rewards.append("🌴 +1 Rest Day")

    return player, rewards
