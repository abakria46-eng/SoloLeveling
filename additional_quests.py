from rich.console import Console

from save import save_player, load_player
from player import add_xp, add_coins
from stats import update_stats
from data.additional_quest_data import ADDITIONAL_QUESTS

console = Console()


def additional_quests():

    player = load_player()

    if player is None:
        console.print("❌ لا يوجد لاعب")
        return


    console.print(
        "\n========== المهام الإضافية ==========\n",
        style="cyan"
    )


    for i, quest in enumerate(ADDITIONAL_QUESTS, 1):

        console.print(
            f"{i} - {quest['name']} "
            f"+{quest['xp']} XP "
            f"+{quest['coins']} Coins"
        )


    choice = input(
        "\nاكتب رقم المهمة التي أكملتها (أو 0 للخروج): "
    )


    if choice == "0":
        return


    try:
        index = int(choice) - 1
        quest = ADDITIONAL_QUESTS[index]

    except (ValueError, IndexError):

        console.print(
            "❌ اختيار غير صحيح"
        )
        return


    confirm = input(
        f"\nهل أكملت {quest['name']}؟ (y/n): "
    )


    if confirm.lower() != "y":

        console.print(
            "لم يتم استلام المكافأة"
        )
        return


    player = update_stats(
        player,
        quest["name"],
        quest["xp"],
        quest["coins"]
    )


    player = add_xp(
        player,
        quest["xp"]
    )


    player = add_coins(
        player,
        quest["coins"]
    )


    save_player(player)


    console.print(
        "\n[green]✅ تم إكمال المهمة الإضافية![/green]"
    )

    console.print(
        f"⭐ +{quest['xp']} XP"
    )

    console.print(
        f"🪙 +{quest['coins']} Coins"
    )
