class Figure:
    sides_count = 0
    filled = False
    __sides = []
    __color = []

    def __init__(self, color, *sides):
        self.__color = color
        if self.__is_valid_side(*sides):
            self.__sides = tuple(sides)
        else:
            if len(sides) == 1 and sides[0] > 0:
                self.__sides = [sides[0]]*self.sides_count
            else:
                self.__sides = [1]*self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, *rgb):
        _flag = True
        for color in rgb:
            if color < 0 or color > 255:
                _flag = False
        return _flag

    def set_color(self, *rgb):
        if self.__is_valid_color(*rgb):
            self.__color = rgb

    def __is_valid_side(self, *sides):
        _flag = True
        if self.sides_count == len(sides):
            for side in sides:
                if not isinstance(side, int) or side < 0:
                    _flag = False
        else:
            _flag = False
        return _flag

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *sides):
        if self.__is_valid_side(*sides):
            self.__sides = sides


class Circle(Figure):
    sides_count = 1
    __radius = 0

    def __init__(self, *args):
        Figure.__init__(self, *args)
        self.__radius = self._Figure__sides[0]/2*3.14

    def get_square(self):
        return 3.14 * self.__radius**2


class Triangle(Figure):
    sides_count = 3
    __S = 0
    __height = 0

    def __init__(self, *args):
        Figure.__init__(self, *args)
        self.__height = 2 * self.get_square() / max(self._Figure__sides)

    def get_square(self):
        __p = sum(self._Figure__sides) / 2
        return (__p*(__p - self._Figure__sides[0])*(__p - self._Figure__sides[1])*(__p - self._Figure__sides[2]))**(1/2)


class Cube(Figure):
    sides_count = 12

    def get_volume(self):
        return self._Figure__sides[0]**3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())