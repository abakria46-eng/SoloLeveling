from save import load_player, save_player


def show_body_data():

    player = load_player()

    print("\n========== بيانات الجسم ==========")

    print(f"🎂 العمر: {player.get('العمر', 0)}")
    print(f"📏 الطول: {player.get('الطول', 0)}")
    print(f"⚖️ الوزن: {player.get('الوزن', 0)}")
    print(f"🎯 الهدف: {player.get('الهدف', '')}")
    print(f"🏋️ مستوى التدريب: {player.get('مستوى_التدريب', 'مبتدئ')}")



def edit_body_data():

    player = load_player()

    print("\n========== تعديل البيانات ==========")

    age = input("🎂 العمر: ")
    height = input("📏 الطول (سم): ")
    weight = input("⚖️ الوزن (كغ): ")


    print("\nاختر الهدف:")
    print("1- تضخيم")
    print("2- تنشيف")
    print("3- لياقة")
    print("4- زيادة وزن معتدلة")

    goal_choice = input("اختيار: ")


    goals = {
        "1": "تضخيم",
        "2": "تنشيف",
        "3": "لياقة",
        "4": "زيادة وزن معتدلة"
    }


    print("\nاختر مستوى التدريب:")
    print("1- مبتدئ")
    print("2- متوسط")
    print("3- متقدم")

    level_choice = input("اختيار: ")


    levels = {
        "1": "مبتدئ",
        "2": "متوسط",
        "3": "متقدم"
    }


    player["العمر"] = int(age)
    player["الطول"] = int(height)
    player["الوزن"] = int(weight)

    player["الهدف"] = goals.get(goal_choice, "")

    player["مستوى_التدريب"] = levels.get(
        level_choice,
        "مبتدئ"
    )

    save_player(player)

    print("\n✅ تم تحديث بيانات اللاعب")



def create_default_settings(player):

    if "settings" not in player:

        player["settings"] = {
            "sound": True,
            "vibration": True,
            "theme": "normal",
            "language": "ar"
        }


    return player



def show_settings():

    player = load_player()

    player = create_default_settings(player)

    save_player(player)


    print("\n========== إعدادات النظام ==========")

    print(f"🔊 الصوت: {'تشغيل' if player['settings']['sound'] else 'إيقاف'}")

    print(f"📳 الاهتزاز: {'تشغيل' if player['settings']['vibration'] else 'إيقاف'}")

    print(f"🎨 المظهر: {player['settings']['theme']}")

    print(f"🌐 اللغة: {player['settings']['language']}")



def edit_settings():

    player = load_player()

    player = create_default_settings(player)


    print("\n========== تعديل الإعدادات ==========")

    print("1- تشغيل/إيقاف الصوت")
    print("2- تشغيل/إيقاف الاهتزاز")
    print("3- تغيير المظهر")
    print("4- تغيير اللغة")
    print("0- رجوع")


    choice = input("اختيار: ")


    if choice == "1":

        player["settings"]["sound"] = not player["settings"]["sound"]


    elif choice == "2":

        player["settings"]["vibration"] = not player["settings"]["vibration"]


    elif choice == "3":

        if player["settings"]["theme"] == "normal":

            player["settings"]["theme"] = "dark"

        else:

            player["settings"]["theme"] = "normal"



    elif choice == "4":

        print("\nاختر اللغة:")
        print("1- العربية")
        print("2- English")


        lang = input("اختيار: ")


        if lang == "1":

            player["settings"]["language"] = "ar"


        elif lang == "2":

            player["settings"]["language"] = "en"


    else:

        return


    save_player(player)

    print("✅ تم تحديث الإعدادات")
