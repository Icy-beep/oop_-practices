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

        print(f'Page open! Grats!\nPage: {page}')

    def display_book_info(self):
        print(f'Title: {self.title} | Author: {self.author} | Pages: {self.pages}')

book = Book('The Adventures of Bobik', 'Bobik', 200)
user_input = input('Enter a page: ')
try:
    user_input = int(user_input)
    book.open_page(user_input)
except ValueError:
    print('Page not opened! Damn...')

book.display_book_info()