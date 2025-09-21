class Tachka:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
        self.current_speed = 0


car = Tachka("Mitsubishi", "LALALALALANCERRRR", 2030)


print(f"Make: {car.make}")
print(f"Model: {car.model}")
print(f"Year: {car.year}")