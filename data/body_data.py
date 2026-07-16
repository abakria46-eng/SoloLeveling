"""
body_data.py

تحليل بيانات الجسم والتوصيات الأساسية.
لا يقوم هذا الملف بتعديل بيانات اللاعب.
"""

def calculate_bmi(height_cm, weight_kg):
    """حساب مؤشر كتلة الجسم."""
    if height_cm <= 0 or weight_kg <= 0:
        return 0

    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)


def bmi_category(bmi):
    """تصنيف BMI."""

    if bmi == 0:
        return "غير معروف"

    if bmi < 18.5:
        return "نقص وزن"

    elif bmi < 25:
        return "وزن طبيعي"

    elif bmi < 30:
        return "زيادة وزن"

    else:
        return "سمنة"


def age_group(age):
    """الفئة العمرية."""

    if age < 12:
        return "طفل"

    elif age <= 17:
        return "مراهق"

    elif age <= 29:
        return "شاب"

    elif age <= 39:
        return "بالغ"

    elif age <= 59:
        return "متوسط العمر"

    else:
        return "كبير السن"


def recommended_training_days(age):

    if age <= 17:
        return 3

    elif age <= 39:
        return 5

    elif age <= 59:
        return 4

    else:
        return 3


def recommended_rest_days(age):

    if age <= 17:
        return 2

    elif age <= 39:
        return 2

    elif age <= 59:
        return 3

    else:
        return 4


def recommended_protein(weight, goal):

    if goal == "تضخيم":
        return round(weight * 1.8)

    elif goal == "تنشيف":
        return round(weight * 2)

    elif goal == "زيادة وزن معتدلة":
        return round(weight * 1.6)

    else:
        return round(weight * 1.2)


def recommended_water(weight):
    """كمية الماء باللتر يومياً تقريباً."""
    return round(weight * 0.035, 1)


def analyze_body(age, height, weight, goal):

    bmi = calculate_bmi(height, weight)

    return {
        "bmi": bmi,
        "bmi_category": bmi_category(bmi),
        "age_group": age_group(age),
        "training_days": recommended_training_days(age),
        "rest_days": recommended_rest_days(age),
        "protein": recommended_protein(weight, goal),
        "water": recommended_water(weight)
    }
