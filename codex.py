from exercise_data import EXERCISES


def get_all_exercises():

    return EXERCISES



def get_exercise(exercise_id):

    return EXERCISES.get(exercise_id)



def search_exercise(name):

    results = []

    for exercise_id, exercise in EXERCISES.items():

        if name.lower() in exercise["name"].lower():

            results.append(exercise)

    return results



def get_categories():

    categories = []

    for exercise in EXERCISES.values():

        if exercise["category"] not in categories:
            categories.append(exercise["category"])

    return categories
