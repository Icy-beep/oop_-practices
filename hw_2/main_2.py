from __future__ import annotations

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


