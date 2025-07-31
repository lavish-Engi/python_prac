#  1. Class and Object

class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

# Create an object
p1 = Person("Lavish", 22)
p1.greet()

#  2. Encapsulation
class Account:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = Account(1000)
acc.deposit(500)
print(acc.get_balance())  # Output: 1500

# 3. Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # Inherited
d.bark()

# 4. Polymorphism
class Bird:
    def fly(self):
        print("Bird flies")

class Airplane:
    def fly(self):
        print("Airplane flies")

# Polymorphic behavior
for obj in [Bird(), Airplane()]:
    obj.fly()

# 5. Abstraction
from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass  # no body here — must be implemented in child class

# Concrete Class
class Car(Vehicle):
    def start(self):
        print("Car started")

class Bike(Vehicle):
    def start(self):
        print("Bike started")

# Create objects
c = Car()
b = Bike()
c.start()   # Car started
b.start()   # Bike started


#  Magic (Dunder) Methods in Python
# These are special methods that begin and end with double underscores (__).
#  Python automatically calls them in specific situations.

# 1️⃣ __init__(self, ...) → Constructor
# Called automatically when you create an object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Lavish", 22)
print(p.name)  # Output: Lavish

# 2️⃣ __str__(self) → What print(obj) shows
# Returns a human-readable string for the object when you use print(obj).

class Car:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f"This is a {self.model}"

c = Car("BMW")
print(c)  # Output: This is a BMW

# 3️⃣ __len__(self) → Custom behavior for len(obj)
# Lets you use len() on your own object.

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __len__(self):
        return self.pages

b = Book(350)
print(len(b))  # Output: 350

# 4️⃣ __add__(self, other) → Customize + between objects
# Used when you do obj1 + obj2.

class Box:
    def __init__(self, weight):
        self.weight = weight

    def __add__(self, other):
        return self.weight + other.weight

b1 = Box(5)
b2 = Box(10)
print(b1 + b2)  # Output: 15

# 5️⃣ __eq__(self, other) → Customize ==
# Used when you compare two objects with ==.


class Student:
    def __init__(self, roll):
        self.roll = roll

    def __eq__(self, other):
        return self.roll == other.roll

s1 = Student(101)
s2 = Student(101)
print(s1 == s2)  # Output: True

# ACCESS MODIFIERS

# ✅ 1. Public Members
# Accessible everywhere: inside and outside the class.

class Student:
    def __init__(self, name):
        self.name = name  # public

s = Student("Lavish")
print(s.name)  # ✅ Output: Lavish

# ✅ 2. Protected Members
# Meant for internal use in the class and subclasses. Indicated by one underscore _.

class Person:
    def __init__(self, name):
        self._name = name  # protected

class Employee(Person):
    def show(self):
        print(f"Employee name is {self._name}")

e = Employee("Lavish")
e.show()        # ✅ Allowed in subclass
print(e._name)  # ✅ Technically allowed, but not recommended


# ✅ 3. Private Members
# Indicated by two underscores __. Only accessible inside the class.

class Account:
    def __init__(self, balance):
        self.__balance = balance  # private

    def show_balance(self):
        print("Balance:", self.__balance)

acc = Account(1000)
acc.show_balance()          # ✅ OK
# print(acc.__balance)        # ❌ Error: AttributeError




import pymysql

# Connect to database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='your_db'
)

cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM users")

# Fetch results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close
cursor.close()
conn.close()


# Logging
# Logging is the process of recording messages that describe events or actions that happen when your code runs.

# Instead of using print() statements (which are not recommended for real applications), you use the logging module.
# basic logging example
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Program started")
logging.warning("Low disk space")
logging.error("Something went wrong")


import logging

# Step 1: Create a logger object
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)  # Minimum level to capture

# Step 2: Create handlers
console_handler = logging.StreamHandler()                 # Stream → console
file_handler = logging.FileHandler("app.log")             # File → app.log

# Step 3: Create formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Step 4: Set formatter to handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Step 5: Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Step 6: Log messages
logger.debug("Debugging app...")
logger.info("App started")
logger.warning("Warning: Check config")
logger.error("Error occurred")
logger.critical("Critical error! System down")


#All done for now
print("All done!!!")

print("testing last")

print("hello")
