# Inheritance and Composition

# Understanding inheritance:

# The original code here is messy because of how needlessly long it is, inheritance can make the code more concise
# Adding Publication and Periodical classes to become base classes to the other 3 classes and to comment out the unnecessary lines
'''
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Periodical(Publication):
    def __init__(self,title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        #self.title = title
        #self.price = price
        self.author = author
        self.pages = pages


class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)
        #self.title = title
        #self.price = price
        #self.period = period
        #self.publisher = publisher


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)
        #self.title = title
        #self.price = price
        #self.period = period
        #self.publisher = publisher


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
'''

# Abstract base classes:

# Abstract base classes are strictly supposed to be a blueprint for derived classes, 
# Should not be instances of abstract base classes, but want it to have attributes for the base classes
# Also want it to be extensible so derived classes can be added
# Can be a very useful tool for enforcing a set of constraints among the users of the (code) classes 

# will import abc model from the standard library
'''
from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    # Made this an abstract method after the imports
    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side


# with the other added lines, this creates an error
#g = GraphicShape()

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
'''

# Using multiple inheritance

'''
class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = "Class B"

# If you comment out the (A, B) line and uncomment the (B, A) line it will print Class B instead of Class A
class C(A, B):
#class C(B, A):
    def __init__(self):
        super().__init__()

    # When you call a method or access an attribute in Python, 
    # the interpretor uses Method Resolution Order (MRO)to look it up in the class. 
    # The lookup starts in the current class, which in this case, class c, doesn't define the name property. 
    # Then python looks in the super classes in the order they are defined left to right
    # In this cases it looks at class A first, since it is listed first, so it prints the name property from class A
    # That is why class B is not printed
    def showprops(self):
        print(self.prop1)
        print(self.prop2)
        print(self.name)


c = C()

# Can inspect the MRO by using __mro__
# Showing it goes class C -> class A -> class B -> object
print(C.__mro__)

c.showprops()

# The complexities of multiple inheritance are why it is not seen in many real world projects
# But it still has it uses in implenting a programming construct called interfaces
'''

# Interfaces:

# By implementing an interface, a particular class makes a contract to provide a certain kind of bahvior or capability

# I created a small focus class, JSONify, 
# to now use whenever I want another class to be able to indicate that it knows how to represent itself as JSON
# Didn't have to modify the base class, which gives flexibilityto aply this new class anywhere it's needed

# Interfaces are really useful for declaring that a class has a capability that it provides

from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

# creating an abstract base class to make classes use JSON
class Jsonify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

class Circle(GraphicShape, Jsonify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)
    
    def toJSON(self):
        return f"{{'Circle': {str(self.calcArea())}}}"


c = Circle(10)
print(c.calcArea())
print(c.toJSON())