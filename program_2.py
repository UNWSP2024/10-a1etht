# Programmer: Alethea Lo
# Date: 3/31/25
# Title: Car Class

class Car:
    def __init__(self, year_model, make):
        """Initialize the car with year model, make, and speed set to 0."""
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        """Increase speed by 5."""
        self.__speed += 5

    def brake(self):
        """Decrease speed by 5, ensuring it doesn't go below 0."""
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0

    def get_speed(self):
        """Return the current speed of the car."""
        return self.__speed


def main():

    my_car = Car(2022, "Toyota")

    print("Accelerating...")
    for _ in range(5):
        my_car.accelerate()
        print(f"Current speed: {my_car.get_speed()} mph")

    print("\nBraking...")
    for _ in range(5):
        my_car.brake()
        print(f"Current speed: {my_car.get_speed()} mph")


if __name__ == "__main__":
    main()
