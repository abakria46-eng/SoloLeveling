ACHIEVEMENTS = [

    {
        "id": "level_5",
        "name": "⭐ المستوى 5 - بداية التطور",
        "xp": 50,
        "coins": 25,
        "condition": lambda player: player["level"] >= 5
    },

    {
        "id": "level_10",
        "name": "🔥 المستوى 10 - لاعب متقدم",
        "xp": 100,
        "coins": 50,
        "condition": lambda player: player["level"] >= 10
    },

    {
        "id": "level_20",
        "name": "⚔️ المستوى 20 - محارب قوي",
        "xp": 250,
        "coins": 100,
        "condition": lambda player: player["level"] >= 20
    },

    {
        "id": "level_50",
        "name": "👑 المستوى 50 - سيد النظام",
        "xp": 1000,
        "coins": 500,
        "condition": lambda player: player["level"] >= 50
    },

    {
        "id": "streak_7",
        "name": "📅 7 أيام استمرارية",
        "xp": 100,
        "coins": 50,
        "condition": lambda player: player["streak"] >= 7
    },

    {
        "id": "streak_30",
        "name": "🏆 30 يوم انضباط",
        "xp": 300,
        "coins": 150,
        "condition": lambda player: player["streak"] >= 30
    },

    {
        "id": "streak_100",
        "name": "🔥 100 يوم استمرارية",
        "xp": 1000,
        "coins": 500,
        "condition": lambda player: player["streak"] >= 100
    },

    {
        "id": "streak_365",
        "name": "🌌 أسطورة الانضباط",
        "xp": 5000,
        "coins": 2500,
        "condition": lambda player: player["streak"] >= 365
    }

]
