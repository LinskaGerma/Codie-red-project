def setup_test_db():
    from data.database import save_database

    test_data = {
        "sport": {
            "tennis": [],
            "football": []
        },
        "music": {
            "guitar": []
        }
    }

    save_database(test_data)

from logic.user_service import (
    create_user,
    search_users,
    find_users_by_email,
    update_user_profile,
    delete_user_profile
)

from data.database import save_database


def setup_test_db():
    test_data = {
        "sport": {
            "tennis": []
        }
    }
    save_database(test_data)


def sample_user():
    return {
        "name": "Test User",
        "email": "test@mail.com",
        "category": "sport",
        "subcategory": "tennis",
        "level": "beginner",
        "city": "wroclaw",
        "days": ["Monday"],
        "time": "morning"
    }


##########################
# CREATE USER

def test_create_user():

    setup_test_db()

    create_user(sample_user())

    users = search_users("sport", "tennis")

    assert len(users) == 1
    assert users[0]["email"] == "test@mail.com"
    assert "id" in users[0]


##########################
# SEARCH USERS

def test_search_users_empty():

    setup_test_db()

    users = search_users("sport", "tennis")

    assert users == []


##########################
# FIND BY EMAIL

def test_find_users_by_email():

    setup_test_db()

    create_user(sample_user())

    results = find_users_by_email("test@mail.com")

    assert len(results) == 1
    assert results[0]["name"] == "Test User"


##########################
# UPDATE USER

def test_update_user():

    setup_test_db()

    create_user(sample_user())

    users = search_users("sport", "tennis")
    user = users[0]

    user["city"] = "krakow"

    success = update_user_profile(user["id"], user)

    assert success is True

    updated = search_users("sport", "tennis")[0]

    assert updated["city"] == "krakow"


##########################
# DELETE USER

def test_delete_user():

    setup_test_db()

    create_user(sample_user())

    user = search_users("sport", "tennis")[0]

    success = delete_user_profile(user["id"])

    assert success is True

    users = search_users("sport", "tennis")

    assert len(users) == 0