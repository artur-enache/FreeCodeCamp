"""https://www.freecodecamp.org/learn/python-v9/lab-polygon-area-calculator/build-a-polygon-area-calculator"""

from math import sqrt

class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @width.setter
    def width(self, new_width: int) -> None:
        self._width = new_width

    @height.setter
    def height(self, new_height: int) -> None:
        self._height = new_height

    def set_width(self, new_width: int) -> None:
        self.width = new_width

    def set_height(self, new_height: int) -> None:
        self.height = new_height

    def get_area(self) -> int:
        return self.height * self.width

    def get_perimeter(self) -> int:
        return 2 * (self.height + self.width)

    def get_diagonal(self) -> float:
        return sqrt(self.height ** 2 + self.width ** 2)

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        output = '\n'.join(self.height * ['*' * self.width]) + '\n'
        return output

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def get_amount_inside(self, object) -> int:
        return ( self.height // object.height ) * ( self.width // object.width )

class Square(Rectangle):
    def __init__(self, side: int) -> None:
        self._width = side
        self._height = side

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @width.setter
    def width(self, new_width: int) -> None:
        self._width = new_width

    @height.setter
    def height(self, new_height: int) -> None:
        self._height = new_height

    def set_width(self, new_side: int) -> None:
        self.width = new_side
        self.height = new_side

    def set_height(self, new_side: int) -> None:
        self.height = new_side
        self.width = new_side

    def set_side(self, new_side: int) -> None:
        self.height = new_side
        self.width = new_side

    def __str__(self):
        return f'Square(side={self.height})'

def main():
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(type(rect))
    print(rect.get_picture())
    sq = Square(5)
    print(type(sq))
    print(Rectangle(15,10).get_amount_inside(Square(5)))

if __name__ == '__main__':
    main()