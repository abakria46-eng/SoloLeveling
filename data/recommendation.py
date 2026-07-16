"""
recommendation.py

يجمع بين تحليل الجسم والتمارين والأطعمة
ولا يقوم بتعديل أي بيانات في اللاعب.
"""

from data.body_data import analyze_body
from data.workout_data import WORKOUT_DATA
from data.food_data import FOOD_DATA


def get_recommendation(age, height, weight, goal, training_level):

    analysis = analyze_body(
        age,
        height,
        weight,
        goal
    )

    age_group = analysis["age_group"]

    workout = {}

    if age_group in WORKOUT_DATA:

        if training_level in WORKOUT_DATA[age_group]:

            workout = WORKOUT_DATA[age_group][training_level].get(
                goal,
                {}
            )

    foods = {}

    if goal in FOOD_DATA:

        foods = FOOD_DATA[goal]

    return {
        "analysis": analysis,
        "workout": workout,
        "foods": foods
    }


def get_analysis(player):

    return get_recommendation(
        player.get("العمر", 0),
        player.get("الطول", 0),
        player.get("الوزن", 0),
        player.get("الهدف", ""),
        player.get("مستوى_التدريب", "مبتدئ")
    )
