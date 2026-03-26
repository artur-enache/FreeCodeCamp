# Python Course Notes

## Docstrings

- Docstrings are enclosed in triple double quotes, and are placed as the first statement in a class/function.
- Docstrings can be accessed through the __doc__ attribute, and this attribute defaults to None. Ex: print(test.__doc__)

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
