from rich.console import Console
from data.recommendation import get_analysis

console = Console()


def show_health_report(player):

    report = get_analysis(player)

    analysis = report["analysis"]
    workout = report["workout"]
    foods = report["foods"]

    console.print("\n========== التقرير الصحي ==========", style="bold green")

    console.print(f"👤 العمر: {player.get('العمر', 0)} سنة")
    console.print(f"📏 الطول: {player.get('الطول', 0)} سم")
    console.print(f"⚖️ الوزن: {player.get('الوزن', 0)} كغ")

    console.print(f"\n📊 BMI: {analysis['bmi']}")
    console.print(f"✅ التصنيف: {analysis['bmi_category']}")
    console.print(f"🧑 الفئة العمرية: {analysis['age_group']}")

    console.print(f"\n💧 الماء المقترح: {analysis['water']} لتر/اليوم")
    console.print(f"🥩 البروتين المقترح: {analysis['protein']} غرام/اليوم")
    console.print(f"🏋️ أيام التدريب: {analysis['training_days']} أيام أسبوعيًا")
    console.print(f"🌴 أيام الراحة: {analysis['rest_days']} أيام أسبوعيًا")

    if workout:
        console.print("\n🏋️ البرنامج التدريبي:", style="cyan")

        for exercise in workout.get("sessions", []):
            console.print(f"• {exercise}")

    if foods:
        console.print("\n🍽️ أطعمة اقتصادية:", style="yellow")

        for food in foods.get("اقتصادي", []):
            console.print(f"• {food['name']}")

        console.print("\n🍗 أطعمة بميزانية متوسطة:", style="yellow")

        for food in foods.get("متوسط", []):
            console.print(f"• {food['name']}")
