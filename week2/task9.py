#1. Define a class Person with attributes name and age. Create an instance of this class and print its attributes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person('Jack', 32)
person2 = Person('Sam', 28)
print(f'Name: {person1.name}, age: {person1.age}')
print(f'Name: {person2.name}, age: {person2.age}')



#2. Problem: Write a Python class named BankAccount with attributes like account_number, balance, and customer_name, and methods like deposit, withdraw, and check_balance.
class BankAccount:
    def __init__(self, account_number, balance, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.customer_name = customer_name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")
        return self.balance

account = BankAccount("12345", 5000, "John Doe")

account.check_balance()     # Current balance: 5000
account.deposit(1500)       # Deposited 1500. New balance: 6500
account.withdraw(2000)      # Withdrawn 2000. New balance: 4500
account.withdraw(8000)      # Insufficient balance!



#3. Create a class Book with a class method from_string() that creates a Book instance from a string. And print both attributes of the class
#book = Book.from_string("Python Programming, John Doe")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, book_string):
        title, author = book_string.split(", ")
        return cls(title, author)

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
book = Book.from_string("Python Programming, John Doe")
book.display()



#4. Create a base class Animal with a method sound(). Create subclasses Dog and Cat that overrides the sound() method and call those methods.
class Animal:
    def sound(self):
        print("This animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def sound(self):
        print("Cat says: Meow!")
dog = Dog()
cat = Cat()

dog.sound()
cat.sound()




#5. Write a code to perform multiple inheritance.
class Father:
    def skill(self):
        print("Father's skill: Driving")

class Mother:
    def talent(self):
        print("Mother's talent: Cooking")

class Child(Father, Mother):
    pass

# Create object of Child
c = Child()

c.skill()    # Inherited from Father
c.talent()   # Inherited from Mother





