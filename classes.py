import requests

class Dog:
    name = ""
    gender = ""
    race = ""
    age = 0

    def __init__(self, name, gender, race, age):
        self.name = name
        self.gender = gender
        self.race = race
        self.age = age

    def eat(self):
        print(self.name, " go to eat")

    def run(self):
        self.greet()
        print(self.name, " go to park")

    def greet(self):
        print("Hello")


class Person:
    name = ""
    lastanem = ""

    def __init__(self, name, lastname):
        self.name = name
        self.lastanem = lastname

    def greet(self):
        return self.name + " " + self.lastanem


class Student(Person):
    university = ""

    def __init__(self, name, lastname, university):
        super().__init__(name, lastname) # llamada al constructor de la clase padre
        self.university = university
    
    def greet(self):
        return self.name + " " + self.lastanem + " from " + self.university


class Teacher(Person):
    faculty = ""

    def __init__(self, name, lastname, faculty):
        super().__init__(name, lastname)
        self.faculty = faculty

    def greet(self):
        return self.name + " " + self.lastanem + " from " + self.faculty


class ClassRoom:
    students = []

    def get_students(self):
        resp = requests.get("https://jsonplaceholder.typicode.com/users")
        # print(resp.json())
        self.students = resp.json()


    def get_all_students(self):
        return self.students

