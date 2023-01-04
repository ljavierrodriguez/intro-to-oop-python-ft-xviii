# DRY = Dont Repeat Yourself

from classes import Dog, Person, Student, Teacher, ClassRoom
from functions import suma
from datetime import datetime
from math import sqrt, ceil, floor

from libs.utils import saludo

firulai = Dog("Firulai", "male", "Buldog", 1) # creando una instancia 
firulai.run()

sasha = Dog("Sasha", "female", "Puddle", 2)
sasha.eat()


p1 = Person("John", "Doe")
p2 = Person("Jane", "Doe")


s1 = Student("John", "Doe", "MIT")
print(s1.greet())

s2 = Student("Jane", "Doe", "Harvard")
s2.name = "Jane Anna"
print(s2.greet())


t1 = Teacher("Sam", "Smith", "Technology")
print(t1.greet())


print(suma(10, 10))

print(datetime.now())

print(sqrt(9))
print(ceil(1.2))
print(floor(1.6))
print(round(1.5))


c1 = ClassRoom()
c1.get_students()
# print(c1.get_all_students())
students = c1.get_all_students()
names = [student["name"] for student in students]
print(names)

saludo()