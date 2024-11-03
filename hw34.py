import random

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

        def get_job(self):
            if self.car and self.car.drive():
                self.job = Job(job_list)
                print(f"{self.name} now has a job: {self.job.job}.")
            else:
                print(f"{self.name} тhe car is not working properly and needs repairs.")
                self.to_repair()

        def get_home(self):
            if self.home is None:
                self.home = House()
                print(f"{self.name} now has a home")
            else:
                print(f" {self.name} already has a house")

        def get_car(self):
            if self.car is None:
                self.car = Auto(brand_of_cars)
                print(f"{self.name} now has a car: {self.car.brand}.")
            else:
                print(f" {self.name} already has a car: {self.car.brand}.")

        def eat(self):
            if self.home.food <= 0:
                print(f"{self.name} has no food at home. Needs to buy food.")
                self.shopping("food")
            else:
                self.satiety += 5
                self.home.food -= 1
                if self.satiety > 100:
                    self.satiety = 100
                print(f"{self.name} ate. Satiety: {self.satiety}, food at home: {self.home.food}")

        def work(self):
            if self.car and self.car.drive():
                self.money += self.job.salary
                self.gladness -= self.job.gladness
                self.satiety -= 4
                print(
                    f"{self.name} worked and earned {self.job.salary}. Money: {self.money}, Gladness: {self.gladness}, Satiety: {self.satiety}")
            else:
                print(f"{self.name} car can't drive. Checking for repairs.")
                self.to_repair()

        def shopping(self, manage):
            if self.car and not self.car.drive():
                if self.car.fuel <= 0:
                    print(f"{self.name} is out of fuel. Needs to buy fuel.")
                    manage = "fuel"
                else:
                    print(f"{self.name}'s car is broken, repairing it.")
                    self.to_repair()
                    return
            if manage == "food":
                if self.money >= 20:
                    self.money -= 20
                    self.home.food += 10
                    print(f"{self.name} bought food. Money: {self.money}, Food at home: {self.home.food}")
                else:
                    print(f"{self.name} doesn't have enough money to buy food.")
            elif manage == "fuel":
                if self.money >= 50:
                    self.money -= 50
                    self.car.fuel += 50
                    print(f"{self.name} bought fuel. Money: {self.money}, Fuel level: {self.car.fuel}")
                else:
                    print(f"{self.name} doesn't have enough money to buy fuel.")

        def chill(self):
            self.gladness += 10
            if self.home:
                self.home.mess += 5
                print(f"{self.name} relaxed. Gladness: {self.gladness}, Mess at home: {self.home.mess}")
            else:
                print(f"{self.name} has no home to relax in.")

        def clean_home(self):
            if self.home:
                self.gladness -= 5
                self.home.mess = 0
                print(f"{self.name} cleaned the home. Gladness: {self.gladness}, Mess at home: {self.home.mess}")
            else:
                print(f"{self.name} has no home to clean.")

        def to_repair(self):
            if self.car:
                self.car.strenght += 100
                self.money -= 50
                print(f"{self.name} repaired the car. Strength: {self.car.strenght}, Money: {self.money}")
            else:
                print(f"{self.name} has no car to repair.")

        def days_indexes(self, day):
            pass

        def is_alive(self):
            if (self.gladness < 0):
                print(f"{self.name} has depression...")
                return False
            if(self.satiety < 0):
                print(f"{self.name} is dead...")
                return False
            if (self.money < -500):
                print(f"{self.name} is bankrupt...")
                return False
            return True
        def live(self, day):
            pass

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strenght = brand_list[self.brand]['strenght']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strenght > 0 and self.fuel > 0 and self.consumption > 0:
             self.fuel -= self.consumption
             return True
        else:
            print("Car cant Move")
            return False

class House:
    def __init__(self):
        self.food = 0
        self.mess = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness = job_list[self.job]['gladness']

job_list = {
    "Java_Developer" :
        {"salary": 50, "gladness": 10},
    "Python_Developer" :
        {"salary": 100, "gladness": 10},
    "C++_Developer" :
        {"salary": 100, "gladness": 5},
    "Java_Developer" :
        {"salary": 50, "gladness": 3},
}


brand_of_cars = {
    "BMW" : {"fuel": 100, "strenght" : 100, "consumption" : 6},
    "Volvo" : {"fuel": 200, "strenght" : 120, "consumption" : 20},
    "Ferrari" : {"fuel": 80, "strenght" : 120, "consumption" : 8},
}

first_car=Auto(brand_of_cars)