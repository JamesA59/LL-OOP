# Data Classes

# Defining a data class:

# With the release of Python 3.7, the data class feature was introduced, which helps automate creation and management of classes
# Can still add methods the same way as before

# To-dos: print the book itself, compare two dataclasses, and change some fields

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