from abc import ABC, abstractmethod

class SmartDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def show_status(self):
        pass

class SmartLight(SmartDevice):
    def __init__(self):
        self.status = "OFF"

    def turn_on(self):
        self.status = "ON"

    def turn_off(self):
        self.status = "OFF"

    def show_status(self):
        print("Smart Light:", self.status)

class SmartFan(SmartDevice):
    def __init__(self):
        self.status = "OFF"

    def turn_on(self):
        self.status = "ON"

    def turn_off(self):
        self.status = "OFF"

    def show_status(self):
        print("Smart Fan:", self.status)

light = SmartLight()
fan = SmartFan()

devices = [light, fan]

for device in devices:
    device.turn_on()
    device.show_status()

for device in devices:
    device.turn_off()
    device.show_status()