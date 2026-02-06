import __future__
import random


class Smartphone:

    brand: str
    model: str
    os: str
    storage: float
    ram: float
    power: float
    is_on: bool
    apps: list[str]

    def __init__(self, brand: str, model: str, os: str, storage: float, ram: float, power: float, is_on: bool, apps: list[str]):
        self.brand = brand
        self.model = model
        self.os = os
        self.storage = storage
        self.ram = ram
        self.power = power
        self.is_on = is_on
        self.apps = apps

    def __str__(self):
        status = 'Включен' if self.is_on else 'Выключен'
        return (
        f'\n----- Характеристики смартфона -----\n'
        f'      Марка: {self.brand}\n'
        f'      Модель: {self.model}\n'
        f'      Операционная система: {self.os}\n'
        f'      Объём памяти: {self.storage}\n'
        f'      Объём оперативной памяти: {self.ram}\n'
        f'      Уровень заряда: {self.power}\n'
        f'      Состояние: {status}\n'
        f'      Установленные приложения: {self.apps}\n'
        f'------------------------------------\n')


    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_os(self):
        return self.os

    def get_storage(self):
        return self.storage

    def get_ram(self):
        return self.ram

    def get_power(self):
        return self.power

    def get_is_on(self):
        return self.is_on

    def set_is_on(self) -> None:
        if self.power <= 0:
            raise ValueError('power must be positive')

        self.is_on = True

    def set_is_off(self) -> None:
        self.is_on = False


    def set_os(self, os: str) -> None:
        if self.is_on:
            self.os = os

    def install_app(self, app_name: str, size: float) -> str:
        if self.is_on and self.power > 0:
            if size < self.storage:
                self.storage -= size
                self.apps.append(app_name)

            return f'App installed: {app_name}'
        else:
            if self.power < 1 or not self.is_on:
                self.is_on = False
                return f'Smartphone off'
            else:
                return f'Error: File size is too big!'

    def uninstall_app(self, app_name: str) -> str:
        if self.is_on and self.power > 0:
            if app_name in self.apps:
                #self.storage += size
                self.apps.remove(app_name)

            return f'App uninstalled: {app_name}'
        else:
            if self.power < 1 or not self.is_on:
                self.is_on = False
                return f'Smartphone off'
            return f'App: {app_name} not find!'

    def set_power(self, power: float) -> None:
        self.power = power


my_smartphone = Smartphone('Xiaomi', 'Redmi Note 145', 'Android 25', 256000, 16000, 86, False, [])

print(my_smartphone.install_app('Game', 200))

print(my_smartphone)

my_smartphone.set_is_on()
print(my_smartphone.install_app('Game', 200))

print(my_smartphone)

my_smartphone.set_power(0)

print(my_smartphone.install_app('Not a Game', 2000))

my_smartphone.set_power(1)

print(my_smartphone)

print(my_smartphone.install_app('Not a Game', 2000))

my_smartphone.set_is_on()

print(my_smartphone)

print(my_smartphone.install_app('Not a Game', 2000))


class Potion:

    EFFECTS = ['restore_health', 'restore_magicka', 'fix_bones', 'repair']

    __name: str
    __ingredients: list[str]
    __difficulty: int
    __effect: str
    __state: bool

    def __init__(self, name: str, ingredients: list[str], difficulty: int | None, effect: str, state: bool):
        self.__name = name
        self.__ingredients = ingredients
        self.__difficulty = difficulty
        self.__effect = effect
        self.__state = state

    def __str__(self):
        return (
            f'\nName: {self.__name}\n'
            f'Ingredients: {self.__ingredients}\n'
            f'Difficulty: {self.__difficulty}\n'
            f'Effect: {self.__effect}\n'
            f'State: {self.__state}\n'
        )

    def get_name(self) -> str:
        return self.__name

    def get_ingredients(self) -> list[str]:
        return self.__ingredients[:]

    def get_difficulty(self) -> int:
        return self.__difficulty

    def get_effect(self) -> str:
        return self.__effect

    def get_state(self) -> bool:
        return self.__state

    def set_effect(self, effect: str) -> None:
        self.__effect = effect

    def set_difficulty(self, difficulty: int) -> None:
        if 1 <= difficulty <= 10:
            self.__difficulty = difficulty

    def set_state(self, state: bool) -> None:
        self.__state = state

    def add_ingredient(self, ingredient: str) -> None:
        if ingredient and ingredient.strip():
            self.__ingredients.append(ingredient)
        else:
            f'{ingredient} is not a valid ingredient!'

    def remove_ingredient(self, ingredient: str) -> None:
        if ingredient and ingredient.strip() and ingredient in self.__ingredients:
            self.__ingredients.remove(ingredient)
        else:
            f'{ingredient} is not a valid ingredient!'

    def craft_potion(self) -> None:
        if self.__ingredients and len(self.__ingredients) > 1:
            difficulty = random.randint(1, 10)
            self.set_difficulty(difficulty)
            difficult_roll = random.randint(1, 10)
            if difficult_roll >= self.__difficulty:
                effect_roll = random.randint(0, len(Potion.EFFECTS) - 1)
                self.set_effect(Potion.EFFECTS[effect_roll])
                self.set_state(True)
                self.__name = f'Potion of {self.__effect.replace("_", " ")}'


potion = Potion('', [], None, '', False)
print(potion)

potion.craft_potion()

print(potion)

potion.add_ingredient('Lavender')

print(potion)

potion.add_ingredient('Root of Earth')

print(potion)

potion.craft_potion()

print(potion)









