import __future__

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
        f'----- Характеристики смартфона -----\n'
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


