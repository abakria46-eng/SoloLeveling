from rich.console import Console
from save import save_player, load_player
from player import create_player, get_rank, get_streak_rank
from quests import daily_quests

console = Console()


def pause():
    input("\nاضغط Enter للعودة إلى القائمة...")


def show_player(player):
    console.print("\n========== بيانات اللاعب ==========", style="cyan")

    console.print(f"👤 الاسم      : {player['name']}")
    console.print(f"🏅 الرتبة     : {get_rank(player)}")
    console.print(f"⭐ المستوى    : {player['level']}")
    console.print(f"⚡ الخبرة     : {player['xp']}/{player['max_xp']}")
    console.print(f"💪 القوة      : {player['strength']}")
    console.print(f"🏃 السرعة     : {player['speed']}")
    console.print(f"🛡 التحمل     : {player['endurance']}")
    console.print(f"🤸 المرونة    : {player['flexibility']}")
    console.print(f"🔥 السلسلة    : {player['streak']} يوم")
    console.print(f"🎖 لقب السلسلة: {get_streak_rank(player)}")
    console.print(f"🪙 العملات    : {player['coins']}")


console.print("╔══════════════════════════════╗", style="cyan")
console.print("║    SOLO LEVELING SYSTEM     ║", style="bold green")
console.print("╚══════════════════════════════╝", style="cyan")


player = load_player()

if player is None:
    name = input("\nاكتب اسم اللاعب: ")
    player = create_player(name)
    save_player(player)


while True:

    player = load_player()

    show_player(player)

    console.print("\n========== القائمة ==========", style="green")
    console.print("1️⃣  المهام اليومية")
    console.print("2️⃣  الإحصائيات")
    console.print("3️⃣  الإنجازات (قريبًا)")
    console.print("4️⃣  المتجر (قريبًا)")
    console.print("5️⃣  الإعدادات (قريبًا)")
    console.print("0️⃣  خروج")

    choice = input("\nاختر: ")


    if choice == "1":
        daily_quests()
        pause()

    elif choice == "2":
        show_player(load_player())
        pause()

    elif choice == "3":
        console.print("\n🚧 سيتم إضافتها قريبًا.", style="yellow")
        pause()

    elif choice == "4":
        console.print("\n🚧 سيتم إضافته قريبًا.", style="yellow")
        pause()

    elif choice == "5":
        console.print("\n🚧 سيتم إضافتها قريبًا.", style="yellow")
        pause()

    elif choice == "0":
        console.print("\n👋 إلى اللقاء.", style="red")
        break

    else:
        console.print("\n❌ اختيار غير صحيح.", style="bold red")
        pause()