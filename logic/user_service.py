from data.database import (
    insert_user,
    get_users,
    insert_category,
    get_users_by_email,
    update_user,
    delete_user
)

##########################new section
# CREATE USER

def create_user(profile):

    if not profile.get("email"):
        raise ValueError("Email is required")

    if not profile.get("name"):
        raise ValueError("Name is required")

    insert_user(profile)

##########################new section
# SEARCH USERS

def search_users(category, subcategory):
    return get_users(category, subcategory)

##########################new section
# ADD CATEGORY

def add_category(category, subcategory):
    return insert_category(category, subcategory)

##########################new section
# FIND BY EMAIL

def find_users_by_email(email):
    return get_users_by_email(email)

##########################new section
# UPDATE USER

def update_user_profile(user_id, profile):
    return update_user(user_id, profile)

##########################new section
# DELETE USER

def delete_user_profile(user_id):
    return delete_user(user_id)