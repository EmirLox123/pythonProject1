class Engine:
    def __init__(self, power, fuel_type):
        self.power = power
        self.fuel_type = fuel_type

    def start(self):
        print("Двигатель запущен")

    def stop(self):
        print("Двигатель остановлен")


class Transmission:
    def __init__(self, gears, type):
        self.gears = gears
        self.type = type

    def shift_up(self):
        print("Передача переключена на следующую")

    def shift_down(self):
        print("Передача переключена на предыдущую")


class Body:
    def __init__(self, color, type):
        self.color = color
        self.type = type

    def open_doors(self):
        print("Двери открыты")

    def close_doors(self):
        print("Двери закрыты")


class Car:
    def __init__(self, engine, transmission, body):
        self.engine = engine
        self.transmission = transmission
        self.body = body

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

    def shift_up(self):
        self.transmission.shift_up()

    def shift_down(self):
        self.transmission.shift_down()

    def open_doors(self):
        self.body.open_doors()

    def close_doors(self):
        self.body.close_doors()
