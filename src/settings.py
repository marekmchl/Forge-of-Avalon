from json import dumps, loads

def load_settings():
    try:
        file = open("current_settings.json", "r")
        settings_dict = loads(file.read())
        file.close()
        return settings_dict
    except Exception:
        file = open("default_settings.json", "r")
        new_file = open("current_settings.json", "x")
        new_file.write(file.read())
        new_file.close()
        file.close()
        file = open("current_settings.json", "r")
        settings_dict = loads(file.read())
        file.close()
        return settings_dict


def save_settings(settings_dict):
    file = open("current_settings.json", "w")
    file.write(dumps(settings_dict))
    file.close()

settings = load_settings()
