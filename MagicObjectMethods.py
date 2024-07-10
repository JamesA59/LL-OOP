# Magic Object Methods

# What are magic methods?:

# A set of methods that Python automatically associates with every class definition
# Customize object behavior and integrate with the language
# Degine how objects are represented as strings
# Control access to attirbute values, both for get and set
# Build in comparison and equality testing capabilities
# Allow objects to be called like functions
# Can make code more concise and readable
# Features like these are what Python its flexibility and power


# String Manipulation:

# Using the __str__ and __repr__ magic methods

# __str__ method is used to provide a user-friendly string description of the object and usually intended to be displayed to the user
# __repr__ method is used to generate a more developer facing string that ideally can be used to recreate the object in its current state
#       And is also commonly used for debugging purposes

# To-dos: use the __str__ method to return a string and use the __repr__ method to return an obj representation

'''
class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    def __repr__(self):
        return f"title={self.title},author={self.author},price={self.price}"
    


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

print(b1)
print(b2)
print(str(b1))
print(repr(b2))
'''

# Equality and comparison:

# By default, plain objects in in Python don't know how to compare themselves to each other
# But they can be taught using the equality and comparison magic methods

# To-dos: use __eq__ method ot check for equality between two objects, use __ge__ to establish >= relationship with another object,
#       use __le__ to establish <= relationship with another object, use __lt__ to establish < relationship with another object, 
#       use __gt__ to establish > relationship with another object, and sorting

# Now that less than calculation support has been added, can now sort
# Built-in sort feature uses less than

'''
class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")
        return (self.title == value.title and 
                self.author == value.author and
                self.price == value.price)

    # TODO: the __ge__ establishes >= relationship with another obj
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")
        return self.price >= value.price

    # TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")
        return self.price < value.price


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# Without __eq__ function b1 == b3 would return false even though all the values are the same, 
print(b1 == b3)
print(b1 == b2)
# Below line raises value errer due to __eq__ function
#print(b1 == 42)

print(b2 >= b1)
print(b2 < b1)

# Will sort by price because of __lt__ function 
books = [b1, b3, b2, b4]
# .sort() is a built-in feature
books.sort()
print([book.title for book in books])
'''

# Attribute access:

# Magic methods give you complete access over how an objects attributes are accessed

# To-dos: call __get__attribute__  when  an attribute is retrieved, call __setattr__ when an attribute value is set, 
#       and when __getattribute__ lookup fails call __getattr__. The last method can pretty much generate attributes on the fly

from typing import Any

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    # The __str__ function is used to return a user-friendly string representation of the object
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # Don't directly access the attr name otherwise a recursive loop is created
    def __getattribute__(self, name):
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(name)

    # Don't set the attr directly here otherwise a recursive loop causes a crash
    def __setattr__(self, name, value):
        if name == "price":
            if type(value) is not float:
                raise ValueError("The 'price' attr must be a float")
        return super().__setattr__(name,value)

    # This version only gets called if the __getattribute__ version hasn't been defined
    def __getattr__(self, name):
        return name + " is not here!"

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

b1.price = 38.95
print(b1.price)

b1.price = float(40)
print(b1)

print(b1.randomprop)