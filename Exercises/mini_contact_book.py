# # Python Course Notes
#
# ## Use Cases
#
# - I can use Python in DevOps for writing CI/CD scripts, and managing infrastructure. I should research this.
# - I can also use pytest for creating test suites. Otherwise, Python can also be used for server monitoring, log management, and other system-level tasks.
#
# ## Variables
#
# - Variable names can only start with a letter or an underscore. They can only contain a-z A-Z 0-9 and _
# - Variable names are case-sensitive
# - Snake case is preferable.
# - In Python type errors are only found during execution.
#
# ## Data Types
#
# - Common data types: integer, float, string, boolean, set ("{4, 2, 0}" - unordered), dictionary (key value pairs; {'name' : 'John'}),
# tuple (immutable ordered collection (7, 8, 4)), range (range(5)),
# list (ordered collection of elements; supports different data types; ex [22, 'String', 2.2, True]), none (special value, basically null)
# - Get the data type of variable using the type() function.
# - isinstance() checks if a variable matches a specific data type; returns bools
#
# ## Strings
#
# - Single and double quotes do not affect strings in Python
# - Multiline strings can be defined using triple quotes (single or double)
# - String interpolation in Python is handled via f-strings (ex: f'My name is {interpolate_this}')
# - String slicing syntax: string[start:stop:step]
#
# ## Operators
#
# - +=, -=, *= are called "augmented assignment" in Python
from encodings.punycode import selective_find
from logging import exception

# ---
#   Mini Contact Book
#
#   Build a small contact book program that works in the terminal. It should:
#
#   1. Store contacts as a list of dictionaries, where each dictionary holds a name, age, email, and a tuple of phone numbers (since those don't change often).
#   2. Have a function that adds a contact — but before adding, it should validate the input:
#     - Use isinstance() to check that the name is a string, age is an integer, etc.
#     - Make sure the name isn't empty and the age is a reasonable number.
#   3. Have a function that displays all contacts using f-strings for clean formatting, e.g.:
#   Contact #1
#   Name: John Doe
#   Age: 30
#   Email: john@example.com
#   Phones: 555-1234, 555-5678
#   4. Have a function that searches contacts by name using string slicing or comparison (e.g., partial match — if I search "Jo", it finds "John").
#   5. Use augmented assignment somewhere meaningful (e.g., a counter tracking how many contacts were added).
#   6. Print the data type of each field when displaying a contact in a "debug mode."
#
#   ---

def add_contact(name, age, email, phone):
    global contacts_added

    type_checks = [
        # I didn't think of this solution myself, but claude did; why it works: if I know what input I will ask & accept,
        # then I can define my expectations. The list is a good idea to contain a collection of various types of data,
        # in this case tuples with variable value, type I need, and error message. Why a tuple? Because I don't want
        # this data to change at runtime.
        (name, str, "Name must be a string"),
        (age, int, "Age must be a number"),
        (email, str, "Email must be a string"),
        (phone, str, "Phone must be a string")
    ]

    for value, expected_type, error_message in type_checks:
        if not isinstance(value, expected_type):
            raise TypeError(error_message)

    if not name:
        print("Name cannot be empty")
        return

    if not age in range(0, 100):
        print("Age must be between 0 and 100")
        return

    contacts_added += 1

    contacts.append((contacts_added, name, age, email, phone))

def print_contacts(contact_list, is_debug=False):
    for contact in contact_list:
        fields = [ ('Name', contact[1]),
                   ('Age', contact[2]),
                   ('E-mail', contact[3]),
                   ('Phone number', contact[4])]

        for label, value in fields:
            line = f'{label}: {value}'
            if is_debug:
                line += f'{type(value)}'
            if label == 'Phone number':
                line += f'\n'
            print(line)


if __name__ == "__main__":
    contacts = []
    contacts_added = 0
    add_contact("123", 28, "email@test.com", "555-2312")
    add_contact('A', 99, '', "555-1211")

    print_contacts(contacts)