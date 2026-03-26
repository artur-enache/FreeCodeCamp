## User Configuration Manager — Requirements

### Setup
- Create a dictionary named `test_settings` with some user configuration preferences.

### `add_setting(settings, setting_tuple)`
- Takes a dictionary of settings and a tuple `(key, value)`.
- Converts both key and value to lowercase.
- If the key already exists: return `Setting '[key]' already exists! Cannot add a new setting with this name.`
- If the key doesn't exist: add the pair to the dictionary and return `Setting '[key]' added with value '[value]' successfully!`
- Returned messages use the lowercase key/value.

### `update_setting(settings, setting_tuple)`
- Takes a dictionary of settings and a tuple `(key, value)`.
- Converts both key and value to lowercase.
- If the key exists: update its value and return `Setting '[key]' updated to '[value]' successfully!`
- If the key doesn't exist: return `Setting '[key]' does not exist! Cannot update a non-existing setting.`
- Returned messages use the lowercase key/value.

### `delete_setting(settings, key)`
- Takes a dictionary of settings and a key string.
- Converts the key to lowercase.
- If the key exists: remove it from the dictionary and return `Setting '[key]' deleted successfully!`
- If the key doesn't exist: return `Setting not found!`
- Returned message uses the lowercase key.

### `view_settings(settings)`
- Takes a dictionary of settings.
- If the dictionary is empty: return `No settings available.`
- If non-empty: return a string starting with `Current User Settings:` followed by each key-value pair on a new line, with the key's first letter capitalized. Example output for `{'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}`:
  ```
  Current User Settings:
  Theme: dark
  Notifications: enabled
  Volume: high
  ```
- The output must end with a newline character.
