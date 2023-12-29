# Exercise with classes
#1 – Create a Car class (Name)
#2 – Create an Engine class (Name)
#3 – Create a Manufacturer (Name) class
#4 – Make the connection between Car has an Engine
# Note: One engine can be used in several cars
#5 – Make the connection between Car and a Manufacturer
# Note: A manufacturer can manufacture several cars
# Display car name, engine and manufacturer on screen
class Car:
    def __init__(self, name):
        self.name = name
        self._engine = None
        self._manufacturer = None

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, value):
        self._engine = value

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value


class Engine:
    def __init__(self, name):
        self.name = name


class Manufacturer:
    def __init__(self, name):
        self.name = name


beetle = Car('Beetle')
volkswagen = Manufacturer('Volkswagen')
engine_1_0 = Engine('1.0')
beetle.manufacturer = volkswagen
beetle.engine = engine_1_0
print(beetle.name, beetle.manufacturer.name, beetle.engine.name)

gol = Car('Gol')
gol.manufacturer = volkswagen
gol.engine = engine_1_0
print(gol.name, gol.manufacturer.name, gol.engine.name)

fiat_uno = Car('Uno')
fiat = Manufacturer('Fiat')
fiat_uno.manufacturer = fiat
fiat_uno.engine = engine_1_0
print(fiat_uno.name, fiat_uno.manufacturer.name, fiat_uno.engine.name)

focus = Car('Focus Titanium')
ford = Manufacturer('Ford')
engine_2_0 = Engine('2.0')
focus.manufacturer = ford
focus.engine = engine_2_0
print(focus.name, focus.manufacturer.name, focus.engine.name)