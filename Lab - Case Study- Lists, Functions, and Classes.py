class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("\n--- Vehicle Details ---")
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Roof type: {self.roof}")

def main():
    Vehicle_type = "car"

    print("Please enter your car details:")
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")

    while True:
        doors = input("Number of doors (2 or 4): ")
        if doors in ["2", "4"]:
            break
        print("Invalid input. Please enter either 2 or 4.")

    while True:
        roof = input("Type of roof: ").strip().lower()
        if roof in ["solid", "sun roof"]:
            break
        print("Invalid input. Please enter 'solid' or 'sun roof'.")

    my_car = Automobile(Vehicle_type, year, make, model, doors, roof)
    my_car.display_info()

if __name__ == "__main__":
    main()