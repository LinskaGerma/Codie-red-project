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
