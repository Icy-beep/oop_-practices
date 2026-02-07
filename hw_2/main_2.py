from __future__ import annotations

import math

class ModelWindow:

   UP, DOWN, LEFT, RIGHT = 'up', 'down', 'left', 'right'
   COMMANDS = [UP, DOWN, LEFT, RIGHT]
   HEIGHT, WIDTH = 1960, 1080
   DISPLAY_BORDERS = [HEIGHT, WIDTH]
   GREEN, RED, YELLOW = 'green', 'red', 'yellow'
   COLORS = [GREEN, RED, YELLOW]
   X = 0
   Y = 1

   __title: str
   __left_up_corner_coord: list[int]
   __width: int
   __height: int
   __color: str
   __is_visible: bool
   __has_border: bool

   def __init__(self, title: str, color: str):
       self.__title = title
       self.__color = color


       self.__width = self.WIDTH
       self.__height = self.HEIGHT
       self.__has_border = True
       self.__is_visible = True
       self.__left_up_corner_coord = [0, 0]

   def __str__(self):
       visibility = 'visible' if self.__is_visible else 'hidden'
       border = 'with border' if self.__has_border else 'borderless'
       return(
           f'\nОкно: {self.__title}\n'
           f'Координаты левого верхнего угла: {self.__left_up_corner_coord}\n'
           f'Размер по горизонтали: {self.__width}\n'
           f'Размер по вертикали: {self.__height}\n'
           f'Цвет окна: {self.__color}\n'
           f'Видимость: {visibility}\n'
           f'С рамкой/без: {border}\n'
       )

   def get_title(self):
       return self.__title

   def get_width(self):
       return self.__width

   def get_height(self):
       return self.__height

   def get_color(self):
       return self.__color

   def get_is_visible(self):
       return self.__is_visible

   def get_left_up_corner_coord(self):
       return self.__left_up_corner_coord[:]

   def set_color(self, color):
       if color in self.COLORS:
           self.__color = color

   def set_is_visible(self, is_visible):
       self.__is_visible = is_visible


   def move_horizontal(self, x: int, command: str):
       if command in self.COMMANDS and self.__is_visible:
           if command == self.RIGHT:
               self.__left_up_corner_coord[self.X] += x
               if self.__left_up_corner_coord[self.X] >= self.__width:
                   self.__left_up_corner_coord[self.X] = 0
               elif self.__left_up_corner_coord[self.X] < 0:
                   self.__left_up_corner_coord[self.X] = 0
           if command == command == self.LEFT:
               self.__left_up_corner_coord[self.X] -= x
               if self.__left_up_corner_coord[self.X] < 0:
                   self.__left_up_corner_coord[self.X] = 0

   def move_vertical(self, y: int, command: str):
       if command in self.COMMANDS and self.__is_visible:
           if command == self.DOWN:
               self.__left_up_corner_coord[self.Y] += y
               if self.__left_up_corner_coord[self.Y] >= self.__height:
                   self.__left_up_corner_coord[self.Y] = 0
               if self.__left_up_corner_coord[self.Y] < 0:
                   self.__left_up_corner_coord[self.Y] = 0
           if command == self.UP:
               self.__left_up_corner_coord[self.Y] -= y
               if self.__left_up_corner_coord[self.Y] < 0:
                   self.__left_up_corner_coord[self.Y] = 0

   def resize(self, width: int, height: int):
       if width < self.WIDTH and self.__is_visible:
           self.__width = width
       if height < self.HEIGHT and self.__is_visible:
           self.__height = height


window = ModelWindow('Spotify', 'Green')

print(window)

window.set_is_visible(False)

print(window)

window.move_horizontal(600, 'left')

window.move_vertical(600, 'down')

print(window)

window.set_is_visible(True)

print(window)

window.move_horizontal(600, 'left')

window.move_vertical(600, 'down')

print(window)

window.resize(1240, 800)

print(window)

window.resize(20000, 200000)

print(window)

class GeometryUtils:
    PI = 3.141592653589793

    @staticmethod
    def calculate_circle_area(radius: float) -> float:
        if radius < 0:
            raise ValueError('radius cannot be negative')

        return GeometryUtils.PI * radius ** 2

    @staticmethod
    def calculate_circle_perimeter(radius: float) -> float:
        if radius < 0:
            raise ValueError('radius cannot be negative')

        return 2 * GeometryUtils.PI * radius

    @staticmethod
    def calculate_rectangle_area(width: int, height: int) -> float:
        if width < 0 or height < 0:
            raise ValueError('width and height cannot be negative')

        return width * height

    @staticmethod
    def calculate_rectangle_perimeter(width: int, height: int) -> float:
        if width < 0 or height < 0:
            raise ValueError('width and height cannot be negative')

        return 2 * (width + height)

    @staticmethod
    def calculate_triangle_area_heron(a: float, b: float, c:float) -> float:
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError('sides must be positive numbers')

        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError('that triangle doesnt exist')

        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))

        return area

class Vector:

    __x: float
    __y: float
    __z: float

    def __init__(self, x: float, y: float, z: float):
        self.__x = x
        self.__y = y
        self.__z = z

    def __str__(self) -> str:
        return f'({self.__x}, {self.__y}, {self.__z})'

    def __add__(self, other):
        return Vector(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)

    def __sub__(self, other):
        return Vector(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.__x * other.__x + self.__y * other.__y + self.__z * other.__z
        elif isinstance(other, (int, float)):
            return Vector(self.__x * other, self.__y * other, self.__z * other)
        else:
            raise TypeError('Умножение возможно только на число или другой вектор')

    def cross_product(self, other):
        if not isinstance(other, Vector):
            raise TypeError('Векторное произведение требует второй вектор')

        res_x = self.__y * other.__z - self.__z * other.__y
        res_y = self.__z * other.__x - self.__x * other.__z
        res_z = self.__x * other.__y - self.__y * other.__x

        return Vector(res_x, res_y, res_z)

    def norm(self) -> float:
        return math.sqrt(self.__x ** 2 + self.__y ** 2 + self.__z ** 2)

number = 3.5

vector = Vector(-1, 3, 5)
other_vector = Vector(3.5, 2, 3)

print(vector)

print(vector + other_vector)
print(vector - other_vector)
print(vector * other_vector)

print(vector.cross_product(other_vector))
print(vector.norm())

class Time:

    __hour: int
    __minute: int
    __second: int

    def __init__(self, hour: int, minute: int, second: int):
        total_seconds = hour * 3600 + minute * 60 + second
        h, remainder = divmod(total_seconds, 3600)
        m, s = divmod(remainder, 60)

        self.__hour = h % 24
        self.__minute = m
        self.__second = s

    def __str__(self):
        return f'\n{self.__hour:02}:{self.__minute:02}:{self.__second:02}\n'

    def __to_seconds(self) -> int:
        return self.__hour * 3600 + self.__minute * 60 + self.__second

    @classmethod
    def __from_seconds(cls, total_seconds:int):
        h, remainder = divmod(total_seconds, 3600)
        m, s = divmod(remainder, 60)

        h = h % 24

        return cls(h, m, s)

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError('складывать можно только с целым количеством секунд')

        new_seconds = self.__to_seconds() + other

        return self.__from_seconds(new_seconds)

    def __sub__(self, other):
        if not isinstance(other, int):
            raise TypeError('вычитать можно только целое количество секунд')

        new_seconds = self.__to_seconds() - other

        return self.__from_seconds(new_seconds)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        if not isinstance(other, int):
            raise TypeError('вычитать можно только целое количество секунд')

        new_seconds = other - self.__to_seconds()

        return self.__from_seconds(new_seconds)

    def __eq__(self, other):
        if not isinstance(other, Time):
            raise TypeError("сравнить можно только объекты класса Time")
        return self.__to_seconds() == other.__to_seconds()

    def __ne__(self, other):
        if not isinstance(other, Time):
            raise TypeError("сравнить можно только объекты класса Time")
        return self.__to_seconds() != other.__to_seconds()

    def __gt__(self, other):
        if not isinstance(other, Time):
            raise TypeError("сравнить можно только объекты класса Time")
        return self.__to_seconds() > other.__to_seconds()

    def __lt__(self, other):
        if not isinstance(other, Time):
            raise TypeError("сравнить можно только объекты класса Time")
        return self.__to_seconds() < other.__to_seconds()



    def get_hour(self):
        return self.__hour

    def get_minute(self):
        return self.__minute

    def get_second(self):
        return self.__second



real_time = Time(0, 0, 0)

print(real_time)

real_time += 3600

print(real_time)

real_time += -100

print(real_time)

real_time += 25

print(real_time)

