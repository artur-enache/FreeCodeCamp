"""https://www.freecodecamp.org/learn/python-v9/lab-user-configuration-manager/build-a-user-configuration-manager"""

def add_setting(settings, setting_tuple):
    key, value = setting_tuple
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f'Setting \'{key}\' already exists! Cannot add a new setting with this name.'
    else:
        settings[key] = value
        return f'Setting \'{key}\' added with value \'{value}\' successfully!'

def update_setting(settings, setting_tuple):
    key, value = setting_tuple
    key = key.lower()
    value = value.lower()

    if key in settings:
        settings[key] = value
        return f'Setting \'{key}\' updated to \'{value}\' successfully!'
    else:
        return f'Setting \'{key}\' does not exist! Cannot update a non-existing setting.'

def delete_setting(settings, key):
    key = key.lower()
    if settings.pop(key, "Missing") != "Missing":
        return f'Setting \'{key}\' deleted successfully!'
    else:
        return 'Setting not found!'

def view_settings(settings):
    if not settings:
        return 'No settings available'
    else:
        lines = '\n'.join(f'{key.capitalize()}: {value}' for key, value in settings.items())
        return f'Current User Settings:\n{lines}\n'


