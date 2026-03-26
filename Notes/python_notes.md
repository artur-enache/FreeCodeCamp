# Python Course Notes

## Use Cases

- I can use Python in DevOps for writing CI/CD scripts, and managing infrastructure. I should research this.
- I can also use pytest for creating test suites. Otherwise, Python can also be used for server monitoring, log management, and other system-level tasks.

## Variables

- Variable names can only start with a letter or an underscore. They can only contain a-z A-Z 0-9 and _
- Variable names are case sensitive
- Snake case is preferrable.
- In Python type errors are only found during execution.

## Data Types

- Common data types: integer, float, string, boolean, set ("{4, 2, 0}" - unordered), dictionary (key value pairs; {'name' : 'John'}, tuple (immutable ordered collection (7, 8, 4)), range (range(5)), list (ordered collection of elements; supports different data types; ex [22, 'String', 2.2, True]), none (special value, basically null)
- Get the data type of a variable using the type() function.
- isinstance() checks if a variable matches a specific data type; returns bools

## Operators

- +=, -=, *= are called "augmented assignment" in Python

## Logical Operators

- "and" takes two operands, and returns the first operand if it is falsy; otherwise it returns the second operand; it is known as a short-circuit operator
- "or" returns the first if it is truthy, or the second if the first is falsy
- "or" is also known as a short-circuit operator
- Conditions joined with "and" are evaluated before conditions joined with "or"

## Strings

- Single and double quotes do not affect strings in Python
- Multiline strings can be defined using triple quotes (single or double)
- String interpolation in Python is handled via f-strings (ex: f'My name is {interpolate_this}')
- String slicing syntax: string[start:stop:step]
- str.maketrans is an interesting function for creating a translation table; it is used in string.translate(translation_table)
- Some useful functions for strings: str.startswith(prefix), str.endswith(suffix), str.find(substring), str.count(substring); the first two return bool values, the third returns an index of a substring (or -1), the fourth an int

## Lists

- Lists use zero based indexing, meaning the first element is at index 0
- list() can convert an iterable to a list; example:
```
developer = 'Jessica'
list(developer)
['J', 'e', 's', 's', 'i', 'c', 'a']
```
- To delete an element from a list: del my_list[index]
- Unpacking lists can assign their values to variables. Ex:
```
developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer
```
- You can also collect remaining elements from a list using the * operator. Ex:
```
developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer
```
- To append: my_list.append(element); if a list is passed, the entire list is added as a single nested element
- To append elements from a list to another: my_list.extend(new_list); unlike append(), extend() adds each element of the new list individually
- To insert at a specific index: my_list.insert(index, element)
- To remove the first occurrence of an item from a list: my_list.remove(element)
- To remove an element at a specific index: my_list.pop(index); if you don't specify an index, the last element is removed; pop() also removes and returns the element
- my_list.sort() sorts a list in place; to get a new sorted list, use: new_list = sorted(my_list)
- To clear a list: my_list.clear()
- my_list.reverse() reverses the list in place
- my_list.index(element) returns the index of the first occurrence of element in the list
- max() returns the largest item in an iterable; if two or more positional arguments are provided, it returned the largest of the positional arguments
- sum() returns the sum of all items in an iterable; it also accepts an optional start argument that sets the initial value for the summation. Ex: sum([5, 10, 15], 10) returns 40

## Tuples

- Tuples can be created from iterables using the tuple() constructor. Example:
```
developer = 'Jessica'
tuple(developer) # ('J', 'e', 's', 's', 'i', 'c', 'a')
```
- Items from a tuple can be unpacked same as with lists
- Same goes for collecting the remaining items from a tuple
- To find an item in a tuple, starting from index 2 and stopping at index 5 (excluding): programming_languages.index('Python', 2, 5)
- Tuples have no in-place sort method (unlike lists), so sorted() is the only option; ex. sorting by length: sorted(programming_languages, key=len)
- sorted() can also be reversed like so: sorted(programming_languages, reverse=True)

## Sets

- Set: An unordered collection of unique elements:

my_set_var = {7, 5, 8}

- Sets are a mutable and unordered data structure that cannot store duplicate values
- Because sets are unordered, they cannot be accessed via indices or keys
- An empty set must be defined with `set()`, not `{}` — curly braces without content create an empty dictionary
- To remove elements: `.remove(element)` raises a `KeyError` if not found; `.discard(element)` silently does nothing if not found
- `.issubset()` and `.issuperset()` check if a set is a sub- or superset of another
- `.isdisjoint()` checks if two sets share no elements in common
- `|` (union) returns a new set with all elements from both sets
- `&` (intersection) returns a new set with only elements common to both sets
- `-` (difference) returns a new set with elements in the first set that are not in the other
- `^` (symmetric difference) returns a new set with elements that are in either set, but not both
- All set operators have compound assignment equivalents (`|=`, `&=`, `-=`, `^=`), which update the first set in place

## Dictionaries

- To unpack & iterate over a dictionary, the items() method is required. Ex: "for key, value in level_count.items()"
- Dictionaries can be built using the `dict()` constructor. Ex: `pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])`
- The `.get()` method accesses a value by key, and accepts an optional default argument returned when the key doesn't exist: `dictionary.get(key, default)`
- `.keys()` and `.values()` return a view object containing the dictionary's keys or values respectively
- View objects do not create a copy of the data — they reflect the current state of the dictionary
- `.items()` returns a view object of key-value pairs
- `.pop(key, default)` removes a key-value pair and returns its value; if the key doesn't exist, returns the value passed to `default`
- In recent Python versions, `.popitem()` removes and returns the last inserted key-value pair
- `.update()` updates a dictionary with key-value pairs from another; if they share keys, the existing values are overwritten
- The `**` operator unpacks a dictionary into keyword arguments. Ex: `nums = {'a': 2, 'b': 3}`; given `def add(a, b): return a + b`, calling `add(**nums)` is equivalent to `add(a=2, b=3)`

## Falsy Values

- None, False, 0, 0.0, "" - these are all considered "falsy" values (they should evaluate to False in a logical context)

## Conditionals

- Conditionals: if, elif, else

## Loops

- Loops: break & continue can be used to stop the loop, and to skip the current iteration respectively
- Both for & while loops can be combined with an else clause; the else clause applies whenever the loop is not terminated by a break statement
- The range function can be used to generated lists of integers; example:
```
numbers = list(range(2, 11, 2))
print(numbers) # [2, 4, 6, 8, 10]
```
- To keep track of the index when iterating over iterables, you can: unpack the count and value from an enumerate object; ex:
```
for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')
```
- The enumerate() function also takes an optional "start" argument, defining from what integer the index should start from (default 0)
- zip() can be used to iterate over multiple iterables in parallel
- A negative step can be passed to range() to generate a sequence in decrementing order. Ex: range(40, 0, -10) generates 40, 30, 20, 10

## Functions

- When a function returns multiple values separated by commas without explicitly declaring a type, Python packages them into a tuple.

## Docstrings

- Docstrings are enclosed in triple double quotes, and are placed as the first statement in a class/function.
- Docstrings can be accessed through the __doc__ attribute, and this attribute defaults to None. Ex: print(test.__doc__)

## Variable Scopes

- Variables have multiple scopes: local, defined in functions or classes; enclosing scope, in enclosing or nested functions; global, at the top level of module/file; built-in scope, which are reserved names in Python
- The "nonlocal" keyword is used to make an enclosing variable modifiable
- "global" makes a locally scoped variable globally accessible
- "global" can also be used to edit a global value, inside of an enclosing scope

## List Comprehension & Higher Order Functions

- List comprehension allows you to create a new list in a single line by combining a loop and condition directly within square brackets.
- Two examples to demonstrate list comprehension. Without it:
```
even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)
```
With it:
```
even_numbers = [num for num in range(21) if num % 2 == 0]
```
- The filter() function can also create lists from iterables, and it takes in a function as an argument, and a list. It then iterates over the list, applies the function, and selects items that meet the condition.
- Filter example:
```
def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
```
- map() can be used to apply a function to each element of a list
- Map example:
```
def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
```
- lambda functions are anonymous, and very good to use in higher order functions (ex. as an argument for the function parameter in filter())
- Example lambda function:
```
def square(num):
    return num ** 2
```
Is equivalent to:
```
lambda num: num ** 2
```
Therefore, "squared_numbers = list(map(square, numbers))" is equivalent to "squared_numbers = list(map(lambda num: num ** 2, numbers))"; and "even_numbers = list(filter(lambda x: x % 2 == 0, numbers))" is an example of using a lambda with filter()
- Best practices for lambda functions: don't assign them to variables; don't make them overly complicated

## Classes and Objects

- Classes define shared behaviors, objects use those behaviors.
- Classes and their attributes (a.k.a. variables) are defined like so:
```
class ClassName:
    def __init__(self, name, age):
```
- Objects get created from classes like so: `object_1 = ClassName(attribute_1, attribute_2)`

## Attributes

- A class has two types of attributes: instance (unique to each object) and class (shared by all objects)

## Magic/Dunder Methods

- Special methods in Python (ex: `__init__()`) are called "magic methods" or "dunder methods"
- `len()`, `str()`, `==` are also dunder methods "behind the hood"; in order to use them on objects, they must be defined in the class body (ex: `def __len__(self): return self.pages`)

## Dynamic Attributes

- Python allows you to work with class attributes dynamically (at runtime, not at definition) using: `getattr()`, `setattr()`, `hasattr()`, and `delattr()`
- `dir()` lets you list all attribute names on an object

## OOP Principles

- OOP has four principles: encapsulation, inheritance, polymorphism and abstraction

## Encapsulation

- Encapsulation: internal (private) attributes (by convention named: _name) should only be accessible via "public" methods. Prefixing attributes with a single underscore is a convention, but a double underscore __name actually prevents them being accessible from outside their class.

## Properties

- Properties are a way to access methods with a dot notation, similar to accessing a normal attribute (without paranthesis). Properties are accessed using getters, setters, and deleters. These have to define inside a @property/@<propertyname>.setter/@<propertyname>.deleter decorator (a decorator modifies the functionality of a function, without changing its code). Here is a full example:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Getter
    @property
    def radius(self):
        return self._radius

    # Setter
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    # Deleter
    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self._radius
```

## Inheritance

- Inheritance allows you to reuse code from existing classes, as well as create clear hierarchies & customize behavior easily. An object can inherit from one, or multiple classes. Attributes from the parent class can be overriden in the child class, or extended using the super() function. Example code:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name} makes a sound'

class Dog(Animal):
    bark = 'woof! woof!! woof!!!'

    # Call Animal.sound(), then append bark
    def sound(self):
        base = super().sound()
        return f'{base}, then {self.name} barks {self.bark}'

jack = Dog('Jack')
print(jack.sound())  # Jack makes a sound, then Jack barks woof! woof!! woof!!!
```

- When inheriting from multiple classes, the child class can combine or override behavior from each.

## Polymorphism

- Polymorphism lets you interact with many objects using the same code. Methods in different classes can share the same name, but perform different tasks.
- Another kind of polymorphism is inheritance-based polymorphism, where objects inherit methods but override them.
- Name mangling is a process in which Python changes __attribute into _ClassName__attribute, to prevent accidental overriding in subclasses
- isinstance(obj, ClassName) returns True for both the class, and any of its subclasses, because it validates the entire inheritance chain

## Error Types

- SyntaxError - obvious; NameError - accessing an undefined variable/function; TypeError - try to perform an operation on incompatible data types; IndexError - access an index that is out of bounds; AttributeError - try to use a method/property that doesn't exist for that data type.

## Debugging

- Python has a built-in debugging tool called pdb. Ex: pdb.set_trace() allows you to step through the code

## Exception Handling

- Exception handling in Python is done using try, except, else, finally blocks. Try - code where an exception is expected; except - catch the exception; else - when there is no exception; finally - always runs.
- Multiple except clauses can be used at the same time.
- Multiple exception can be caught in the same except clause, by specifying them as a tuple: except (ValueError, ZeroDivisionError) as e
- The raise statement allows you to manually trigger exceptions in your code.
- raise can also be used to re-raise the current exception that's being handled in an except clause
- Exceptions with custom logic must be created via an exception class.
- The raise statement can also be used with the "from" keyword to chain exceptions; ex: raise ValueError('Configuration file is missing') from None
- Exceptions can also be raised conditionally using assert statements
- Python evaluates except clauses top to bottom; example exception inheritance: AppException > DetailedException > GranularException; except AppException: do something except DetailedException: do something else; in this example, if DetailException is raised, because it inherits from AppException then AppException will trigger the except clause & execute the code in it
