import dices


class Environment:
    def __init__(self):
        self.day = 0
        self.hour = 10
        self.part_of_day = 'Nappal'
        self.weather = 'Derült'
        self.weather_types = ['Derült', 'Felhős', 'Borult', 'Eső']

    def add_hour(self, hour):
        for i in range(hour):
            if self.hour < 23:
                self.hour += 1
            elif self.hour == 23:
                self.hour = 0
                self.day += 1
        if 8 <= self.hour <= 19:
            self.part_of_day = 'Nappal'
            if self.weather == 'Csillagos':
                self.weather = 'Derült'
        else:
            self.part_of_day = 'Éjszaka'
            if self.weather == 'Derült':
                self.weather = 'Csillagos'
        self.change_weather()

    def change_weather(self):
        def clear_sky():
            if self.part_of_day == 'Nappal':
                return 'Derült'
            elif self.part_of_day == 'Éjszaka':
                return 'Csillagos'

        if self.weather == clear_sky():
            self.weather = [clear_sky(), clear_sky(), clear_sky(), 'Felhős', 'Felhős', 'Felhős'][dices.roll_1D6() - 1]
        elif self.weather == 'Felhős':
            self.weather = [clear_sky(), clear_sky(), clear_sky(), 'Felhős', 'Felhős', 'Eső'][dices.roll_1D6() - 1]
        elif self.weather == 'Eső':
            self.weather = ['Felhős', 'Felhős', 'Felhős', 'Eső', 'Eső', 'Eső'][dices.roll_1D6() - 1]

    def print_enviroment(self):
        print('Nap: {}, Óra: {}, {}, {}'.format(self.day, self.hour, self.part_of_day, self.weather))


if __name__ == "__main__":
    enviroment = Environment()
    enviroment.print_enviroment()
    for i in range(48):
        enviroment.add_hour(1)
        enviroment.print_enviroment()
