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
        return sqrt(self.height ** self.height + self.width ** self.width)

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        output = '\n'.join(self.height * ['*' * self.width])
        return output

def main():
    rect = Rectangle(8, 3)
    print(rect.get_picture())

if __name__ == '__main__':
    main()