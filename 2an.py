class TemperatureSensor:
    def __init__(self, location, temperature):
        self.location = location
        self.temperature = temperature

    def increase_temperature(self):
        self.temperature += 1

    def decrease_temperature(self):
        self.temperature -= 1

    def show_temperature(self):
        print(f"{self.location}: {self.temperature} degrees")


sensor1 = TemperatureSensor("Kitchen", 20)
sensor2 = TemperatureSensor("Outside", 12)

sensor1.show_temperature()
sensor2.show_temperature()

sensor1.increase_temperature()
sensor1.increase_temperature()
sensor1.show_temperature()

sensor2.decrease_temperature()
sensor2.show_temperature()

