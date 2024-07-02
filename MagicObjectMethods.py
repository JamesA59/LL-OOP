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