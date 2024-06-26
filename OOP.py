# OOP

# Object Oriented Programming Refresher

# Python does not requier you to use objects or classes
# Complex programs are hard to keep organized
# Object-oriented programming organizes and structures code
#       Groups together data and behavior into one place
#       Promotes modularization of programs
#       Isolates different parts of the program from each other
# Terms:
#           Class- a blueprint for creating objects of a particular type
#           Methods- regular functions that are part of a class
#           Attributes- variables that hold data that are part of a class
#           Object- a specific instance of a class
#           Inheritance- means by which a class can inherit capabilities from another
#           Composition- means of building complex objects out of other objects

# Basic class definitions:
# To-dos: Create a basic class, create instances of the class, print the class and property
# The init function is called when the intance is created and ready to be initialized
'''
class Book:
    def __init__(self, title):
        self.title = title

book1 = Book("Brave New World")
book2 = Book("War and Peace")

print(book1)
print(book1.title)
'''
# Instance methods and attributes:
# Using instance methods and attributes
# To-dos: add properties, print the price of book1, try setting the discount, 
# and properties with double underscores are hidden by the interpretor

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"

    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
        
    # Using underscores doesn't let other attributes in other classes be given the same name
    
    def setdiscount(self, amount):
        self._discount = amount

b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

print(b1.getprice())
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())

# Line below gives error
#print(b2.__secret)
# Line below 
print(b2._Book__secret)
