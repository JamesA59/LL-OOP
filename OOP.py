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
'''
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
'''
# Checking Instance Types:
# To-dos: use type() to inspect the object type and compare two types together, 
# use isinstance to compare a specific instance to a known type
'''
class Book:
    def __init__(self, title):
        self.title = title

class Newspaper:
    def __init__(self,name):
        self.name = name

b1 = Book("The Catcher in the Rye")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")

print(type(b1))
print(type(n1))

print(type(b1) == type(b2))
print(type(b1) == type(n2))

print(isinstance(b1, Book))
print(isinstance(n1, Newspaper))
print(isinstance(n2, Book))
# isintance also works with inheritance, as shown below
print(isinstance(n2, object))
'''

# Class Methods and Members:
# To-do's: properties defined at the class level are shared by all instances,
#       double-underscore properties are hidden from other classes, create a class method, create a static method, 
#       access the class attribute

# Instance methods receive a specific object instance as an arguement and operate on data specific to that object instance
# Not many good uses of static methods, but one good use is to implement a singleton design pattern

class Book:

    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    __booklist = None
    

    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES
    
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype

print("Book types: ", Book.get_book_types())

b1 = Book("Title1", "HARDCOVER")
# Line below causes error because comic is not an accepted book type, will ignore it so code will run
#b2 = Book("Title1", "COMIC")
b2 = Book("Title1", "PAPERBACK")

thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)