# Data Classes

# Defining a data class:

# With the release of Python 3.7, the data class feature was introduced, which helps automate creation and management of classes
# Can still add methods the same way as before

# To-dos: print the book itself, compare two dataclasses, and change some fields
'''
from dataclasses import dataclass

# Instead of this:
#class Book:
    #def __init__(self, title, author, pages, price):
        #self.title = title
        #self.author = author
        #self.pages = pages
        #self.price = price

# Do this:      
@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def bookinfo(self):
        return f"{self.title} by {self.author}"

# The dataclass decorator code will rewrite theis class 
#       to automatically add in the init function where each of the attributes will be initialized on the object instance
# Another benefit of data classes than the concise code declaration is it 
#       automatically implements both the __repr__ and __eq__ magic methods

b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

print(b1.title)
print(b2.author)

print(b1)

print(b1 == b3)
print(b1 == b2)

b1.title = "Anna Karenina"
b1.pages = 864
print(b1.bookinfo())
'''

# Using Post Initialization:

# Can create attributes based on the value of other attributes

# To-dos: use the __post_init__ function to customize additional properties after the object has been initialized via built-in __init__
#       and use the description attribute created in the __post_init__ function

'''
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"

b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

print(b1.description)
print(b2.description)
'''


# Using Default Values

# Data classes provide the ability to define default values for their attributes, subject to some rules
# you can define default values when attributes are declared
# Attributes without default values have to come (be listed) first

# Another way of defining a default value is by using the field function

from dataclasses import dataclass, field

# for price_func
import random

def price_func():
    return float(random.randrange(20,40))

@dataclass
class Book:
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    # The line below can't be a default value beacuse there are line before it that are default values and code won't work
    # price: float
    # price: float = 0.0
    # Line below is another way of setting a default value, field() offers other uses and flexibility
    # price: float = field(default=10.0)
    # line below uses price_func function to generate a random price for the book
    # Each time it is ran in will generate a different price
    price: float = field(default_factory=price_func)

b1 = Book()
print(b1)

b2 = Book("War and Peace", "Leo Tolstoy", 1225)
b3 = Book("The Catcher in the Rye", "JD Salinger", 234)
print(b2)
print(b3)