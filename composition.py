class Battery:
    def power(self):
        return "Battery is ON!"


class Phone:
    def __init__(self):
        self.battery = Battery()  # Phone HAS A Battery

    def turn_on(self):
        return self.battery.power()


# Usage
my_phone = Phone()
print(my_phone.turn_on())  # Output: Battery is ON!