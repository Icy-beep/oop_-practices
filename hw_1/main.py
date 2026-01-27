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
        print(f'Name: {self.name}\nSpecies: {self.species}\nAge: {self.age}')

dog = Animal('Bobik', 'dog', 10)
dog.make_sound('bark! bark!')
dog.display_your_info()

