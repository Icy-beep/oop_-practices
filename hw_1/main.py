"""
## **Задача №1.**

Сформировать класс "Animal" для представления сущности «Животное» в программе.
В качестве полей задаются: имя животного (строка), вид животного (строка), возраст (число).
Реализовать следующие операции: вывести звук, который издает животное (строка).
Реализовать метод вывода информации о животном на экран.
Метод вывода на экран должен аккумулировать состояние полей объекта.
"""

class Animal:

    name: str
    species: str
    age: int

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self, sound):
        print(f'{self.name}: {sound}')

    def display_your_info(self):
        print(f'Name: {self.name}\nSpecies: {self.species}\nAge: {self.age}\n')

dog = Animal('Bobik', 'dog', 10)
dog.make_sound('bark! bark!')
dog.display_your_info()

"""
## **Задача №2.**

Сформировать класс «Book» для представления сущности «Книга» в программе. 
В качестве полей задаются: наименование книги (строка), автор книги (строка), количество страниц (число). 
Реализовать операции: «отрыть» указанную страницу 
(на вход в метод передается номер страницы и выводится строка, открылась страница или нет). 
Реализовать метод вывода информации о книге на экран. 
Метод вывода на экран должен аккумулировать состояние полей объекта.
"""

class Book:

    title: str
    author: str
    pages: int

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def open_page(self, page):

        if page < 1:
            raise ValueError('Page must be greater than 0')

        print(f'Page open! Grats!\nPage: {page} | Pages in book: {self.pages}')

    def display_book_info(self):
        print(f'Title: {self.title} | Author: {self.author} | Pages: {self.pages}')

book = Book('The Adventures of Bobik', 'Bobik', 200)
#user_input = input('Enter a page: ')
user_input = 100
try:
    user_input = int(user_input)
    book.open_page(user_input)
except ValueError:
    print('Page not opened! Damn...')
book.display_book_info()

"""
## **Задача №3.**

Сформировать класс «**PassengerPlane**» для представления сущности «Пассажирский Самолет» в программе. 
В качестве полей задаются: производитель самолета, модель самолета, вместимость, пассажиров, текущая высота, текущая скорость. 
Реализовать следующие операции: взлет самолета, посадка самолета, изменение высоты, изменение скорости.  
Реализовать метод вывода информации о пассажирском самолете на экран. Метод вывода на экран должен аккумулировать состояние полей объекта.

Примечание:

Взлет самолета – операция, которая выводит сообщение на консоль «Самолет взлетел!».

Посадка самолета – операция, которая выводит сообщение на консоль «Самолет приземлился!».

Изменение высоты – операция, которая на вход принимает новое значение высоты и заменяет старое.
"""

class PassengerPlane:

    manufacturer: str
    model: str
    capacity: float
    passengers: int
    altitude: float
    speed: float

    def __init__(self, manufacturer, model, capacity, passengers, altitude, speed):
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = capacity
        self.passengers = passengers
        self.altitude = altitude
        self.speed = speed

    def takeoff(self):
        if self.speed == 0:
            self.speed = 300
            self.change_altitude(500)
            print('Самолет взлетел!')
        else:
            print("Самолет уже в воздухе!")

    def touchdown(self):
        if self.altitude > 0:
            self.altitude = 0.0
            self.speed = 0.0
            print('Самолет приземлился!')
        else:
            print("Самолет уже на земле!")

    def change_altitude(self, new_altitude: float):
        self.altitude = new_altitude

    def change_speed(self, new_speed: float):
        self.speed = new_speed

    def show_plane_info(self):
        print(f'Manufacturer: {self.manufacturer}\nModel: {self.model}\nCapacity: {self.capacity} kg\nPassengers: {self.passengers} seats\nAltitude: {self.altitude} m\nSpeed: {self.speed} km/h\n')

plane = PassengerPlane('Bobik – Engineering', 'Dogster', 15000, 150, 0, 0)
plane.takeoff()
plane.touchdown()
plane.show_plane_info()

"""
## **Задача №4.**

Сформировать класс «**MusicAlbum**» для представления сущности «Музыкальный Альбом» в программе. 
В качестве полей задаются: исполнитель, название альбома, жанр, список треков. 
Реализовать следующие операции: добавить трек в альбом, удалить трек из альбома, воспроизвести указанный трек. 
Реализовать метод вывода информации о музыкальном альбоме на экран. Метод вывода на экран должен аккумулировать состояние полей объекта.

Примечание:

Добавить трек в альбом – операция принимает на вход трек в формате строки и добавляет в список треков.

Удалить трек из альбома – операция, принимает на вход название трека в формате строки и удаляет трек, если он имеется.

Воспроизвести трек – операция, принимает на вход название трека и имитирует его воспроизведение выводом информации на консоль.
"""

class MusicAlbum:

    artist: str
    album_name: str
    genre: str
    track_list: list

    def __init__(self, artist, album_name, genre, track_list):
        self.artist = artist
        self.album_name = album_name
        self.genre = genre
        self.track_list = track_list

    def add_track(self, track: str):
        self.track_list.append(track)

    def delete_track(self, track: str):
        self.track_list.remove(track)

    def play_track(self, track: int):
        print(f'Играет: {self.track_list[track + 1]}')

    def show_album_info(self):
        print(f'Album: {self.album_name} | Genre: {self.genre} | Artist: {self.artist} | Tracks: {len(self.track_list)}')


album = MusicAlbum('Slipknot', 'Iowa', 'nu metal', ['(515)', 'People = Shit', 'Disasterpiece'])
album.add_track('My Plague')
album.add_track('111')
album.delete_track('111')
album.play_track(1)
album.show_album_info()

