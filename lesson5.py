# OOP
# class

# class Car:
#     color = "Grey"
#     wheels = 4
#
# car1 = Car()
# car2 = Car()
# car1.color = "Red"
# car2.color = "Blue"
# del car2.color
# print(Car.__dict__)
# print(car1.__dict__)
# print(car1.color, car2.color)

# class House:
#     foundation = "beton"
#
#     def __init__(self,
#                  count_window, count_room,
#                  count_door, color_house):
#         self.count_window = count_window
#         self.count_room = count_room
#         self.count_door = count_door
#         self.color_house = color_house
#         self.count_floor = 0
#
#     def get_info(self):
#         print(f"color {self.color_house}, floor {self.count_floor}")
#
#     def build_floors(self):
#         self.count_floor += 1
#
#
# house2 = House(5, 5, 5, "white")
# house2.build_floors()
# house2.build_floors()
# house2.get_info()

# class User:
#
#     def __init__(self, first_name, last_name, age, phone, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.phone = phone
#         self.email = email
#
#     def greet_user(self):
#         print(f"Hello {self.first_name} {self.last_name}")
#
#     def describe_user(self):
#         print(f"Name: {self.first_name}, Last name: {self.last_name},"
#               f" Age: {self.age}, Phone: {self.phone}, E-mail: {self.email}")
#
#
# user1 = User("Nurlan", "Ashyrov", 35, "772033040", "ashyrov.n@mail.ru")
# user1.describe_user()
# user1.greet_user()


class Car:
    def __init__(self, brand, model, color, price, avg_consume):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.avg_consume = avg_consume
        self.fuel = 0
        self.odometer = 0

    def car_info(self):
        print(f"Brand {self.brand}, Odometer {self.odometer}")

    def add_fuel(self, l: int):
        self.fuel += l

    def drive(self, km: int):
        if self.fuel == 0:
            print("The tank is empty")
        elif self.fuel >= self.avg_consume / 100 * km:
            self.odometer += km
        else:
            print(f"{self.fuel} is not enough")


car1 = Car("Toyota", "Camry", "Silver", 20000, 10)
car1.add_fuel(10)
car1.drive(100)
car1.drive(100)
car1.car_info()