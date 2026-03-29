import json
import uuid
import os

##########################new section
# DATABASE SETTINGS

DATABASE_FILE = "database.json"

DEFAULT_DATABASE = {
    "sport": {
        "tennis": [],
        "football": [],
        "volleyball": [],
        "kayaking": []
    },
    "hobby": {
        "pottery": [],
        "beading": [],
        "drawing": []
    },
    "music": {
        "guitar": [],
        "piano": [],
        "vocal": []
    }
}

##########################new section
# CORE DB

def load_database():

    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "w") as file:
            json.dump(DEFAULT_DATABASE, file, indent=4)

    with open(DATABASE_FILE, "r") as file:
        database = json.load(file)

    # ensure IDs
    updated = False

    for category, subcats in database.items():
        for subcategory, users in subcats.items():
            for user in users:
                if "id" not in user:
                    user["id"] = str(uuid.uuid4())
                    updated = True

    if updated:
        save_database(database)

    return database


def save_database(data):

    with open(DATABASE_FILE, "w") as file:
        json.dump(data, file, indent=4)

##########################new section
# OPERATIONS

def insert_user(profile):

    database = load_database()

    category = profile["category"]
    subcategory = profile["subcategory"]

    if category not in database:
        database[category] = {}

    if subcategory not in database[category]:
        database[category][subcategory] = []

    profile["id"] = str(uuid.uuid4())

    database[category][subcategory].append(profile)

    save_database(database)


def get_users(category, subcategory):

    database = load_database()

    if category in database and subcategory in database[category]:
        return database[category][subcategory]

    return []


def insert_category(category, subcategory):

    database = load_database()

    if category in database:

        if subcategory in database[category]:
            return "duplicate"

        database[category][subcategory] = []
        save_database(database)
        return "subcategory_added"

    database[category] = {subcategory: []}
    save_database(database)
    return "new_category_added"


def get_users_by_email(email):

    database = load_database()
    results = []

    for category, subcats in database.items():
        for subcategory, users in subcats.items():
            for user in users:
                if user["email"] == email:
                    results.append(user)

    return results


def update_user(user_id, updated_profile):

    database = load_database()

    for category, subcats in database.items():
        for subcategory, users in subcats.items():
            for i, user in enumerate(users):
                if user["id"] == user_id:

                    users[i] = updated_profile
                    save_database(database)
                    return True

    return False


def delete_user(user_id):

    database = load_database()

    for category, subcats in database.items():
        for subcategory, users in subcats.items():
            for user in users:
                if user["id"] == user_id:

                    users.remove(user)
                    save_database(database)
                    return True

    return False