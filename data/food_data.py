"""
food_data.py

قاعدة بيانات أولية للأطعمة.
القيم الغذائية تقريبية لكل 100 غرام (أو للوحدة الشائعة عند الحاجة).
"""

FOOD_DATA = {

    "تضخيم": {

        "اقتصادي": [

            {
                "name": "بيض",
                "protein": 13,
                "carbs": 1,
                "fat": 11,
                "calories": 155
            },

            {
                "name": "شوفان",
                "protein": 17,
                "carbs": 66,
                "fat": 7,
                "calories": 389
            },

            {
                "name": "أرز",
                "protein": 7,
                "carbs": 80,
                "fat": 1,
                "calories": 365
            },

            {
                "name": "عدس",
                "protein": 25,
                "carbs": 60,
                "fat": 1,
                "calories": 352
            },

            {
                "name": "بطاطا",
                "protein": 2,
                "carbs": 20,
                "fat": 0,
                "calories": 87
            }

        ],

        "متوسط": [

            {
                "name": "صدر دجاج",
                "protein": 31,
                "carbs": 0,
                "fat": 4,
                "calories": 165
            },

            {
                "name": "لحم بقري",
                "protein": 26,
                "carbs": 0,
                "fat": 15,
                "calories": 250
            },

            {
                "name": "تونة",
                "protein": 29,
                "carbs": 0,
                "fat": 1,
                "calories": 132
            }

        ]

    },

    "تنشيف": {

        "اقتصادي": [

            {
                "name": "بيض",
                "protein": 13,
                "carbs": 1,
                "fat": 11,
                "calories": 155
            },

            {
                "name": "عدس",
                "protein": 25,
                "carbs": 60,
                "fat": 1,
                "calories": 352
            },

            {
                "name": "خضروات متنوعة",
                "protein": 2,
                "carbs": 6,
                "fat": 0,
                "calories": 35
            }

        ],

        "متوسط": [

            {
                "name": "صدر دجاج",
                "protein": 31,
                "carbs": 0,
                "fat": 4,
                "calories": 165
            },

            {
                "name": "سمك",
                "protein": 24,
                "carbs": 0,
                "fat": 5,
                "calories": 140
            }

        ]

    },

    "لياقة": {

        "اقتصادي": [

            {
                "name": "موز",
                "protein": 1,
                "carbs": 23,
                "fat": 0,
                "calories": 89
            },

            {
                "name": "لبن",
                "protein": 3,
                "carbs": 5,
                "fat": 3,
                "calories": 60
            }

        ],

        "متوسط": [

            {
                "name": "زبادي يوناني",
                "protein": 10,
                "carbs": 4,
                "fat": 5,
                "calories": 97
            }

        ]

    },

    "زيادة وزن معتدلة": {

        "اقتصادي": [

            {
                "name": "زبدة الفول السوداني",
                "protein": 25,
                "carbs": 20,
                "fat": 50,
                "calories": 588
            },

            {
                "name": "تمر",
                "protein": 2,
                "carbs": 75,
                "fat": 0,
                "calories": 282
            }

        ],

        "متوسط": [

            {
                "name": "مكسرات",
                "protein": 20,
                "carbs": 22,
                "fat": 50,
                "calories": 600
            }

        ]

    }

}
