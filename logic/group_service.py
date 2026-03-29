from data.database import load_database

def get_groups_matrix():

    database = load_database()

    levels = ["beginner", "middle", "advanced", "professional"]

    result = {}

    for category, subcats in database.items():

        result[category] = {}

        for subcategory, users in subcats.items():

            level_count = {level: 0 for level in levels}

            for user in users:
                if user["level"] in level_count:
                    level_count[user["level"]] += 1

            result[category][subcategory] = level_count

    return result