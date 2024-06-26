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

class Book:
    def __init__(self, title):
        self.title = title

book1 = Book("Brave New World")
book2 = Book("War and Peace")

print(book1)
print(book1.title)