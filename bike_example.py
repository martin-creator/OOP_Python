from enum import Enum
from tkinter import N

# Enum is a class in the standard library that allows you to create a set of constants that are represented by a name and a value.

class Condition(Enum):
    NEW = 0
    GOOD = 1
    OKAY = 2
    BAD = 3


class MethodNotAllowedError(Exception):
    pass

class  Bike:  # classes should begin with a capital letter


    num_wheels: int = 2 # class variable

    # the __init__ method special method is called a constructor
    # difference between Intializer and Constructor is that Intializer is called when an object is created and Constructor is called when an object is destroyed.
    # self is a reference to the current instance of the class
    def __init__(self, description, condition: Condition, sale_price, cost=0):
        self.description = description
        self.condition = condition
        self.sale_price = sale_price
        self.cost = cost
        self.sold = False
        print("Intializing a new bike")

    
    def __del__(self):
        print("Deleting a bike")


    def update_sale_price(self, new_sale_price):
        if self.sold:
            raise MethodNotAllowedError("Can't update sale price of a sold bike")
        self.sale_price = new_sale_price



    @property # this is a decorator that allows you to access the method as an attribute 
    def profit(self):
        if not self.sold:
            return None
        return int(self.sale_price) - int(self.cost)

    @sale_price.setter # this is a decorator that allows you to access the method as an attribute
    def sale_price(self, new_sale_price):
        if self.sold:
            raise MethodNotAllowedError("Can't update sale price of a sold bike")
        self.sale_price = new_sale_price
        

    def sell(self):
        self.sold = True
        profit = int(self.sale_price) - int(self.cost)
        return profit

    def service(self, cost, new_sale_price=None, new_condition=None):
        self.cost += cost
        if new_sale_price:
            self.update_sale_price(new_sale_price)
        if new_condition:
            self.condition = new_condition

    @staticmethod # this is a decorator that allows you to access the method as an attribute
    # static methods are methods that don't require an instance of the class to be called therefore they can be called on a class
    def get_test_bikes(self):
        Bike.test_count += 1
        return Bike("Test bike", Condition.GOOD, 100, 10)

    def __str__(self) -> str: # this is a special method that is called when you try to convert an object to a string
        return f"{self.description} bike for sale at {self.sale_price} with condition {self.condition.name}"

    def __repr__(self) -> str: # this is a special method that is called when you try to convert an object to a string
        return f"{self.description} bike for sale at {self.sale_price} with condition {self.condition.name}"


class Unicycle(Bike):
    num_wheels: int = 1

# my_bike = Bike(description="Organge Africa", condition="bad", sale_price="100" ) # create an instance of the Bike class
# my_bike.service(20, new_sale_price=200, new_condition=Condition.GOOD)
# my_bike.update_sale_price(200)
# print(my_bike.sale_price)

# print(type(my_bike))  # <class '__main__.Bike'>
# print(my_bike)  # <__main__.Bike object at 0x000001E0B0E3F4C0>
# print(my_bike.__class__)  # <class '__main__.Bike'>
# print(my_bike.__class__.__name__)  # Bike
# print(my_bike.__class__.__module__)  # __main__
# print(my_bike.__class__.__module__ + '.' + my_bike.__class__.__name__)  # __main__.Bike
# print(dir(my_bike))# print all methods of the class


if __name__ == '__main__': # this is the entry point of the program
    my_bike = Bike("Red Releigh cruiser", Condition.GOOD, 450, 50)
    print(my_bike)

    my_bike.update_sale_price(400)

    profit = my_bike.sell()

    print(my_bike.__dict__)

    print(profit)

    # del my_bike

    print("Program finished")

    # my_bike.update_sale_price(1000)



# List python class magic methods and their uses
# https://rszalski.github.io/magicmethods/
 # __init__ : Constructor
    # __del__ : Destructor
    # __repr__ : Evaluable string representation
    # __str__ : Readable string representation
    # __bytes__ : Bytes representation
    # __format__ : Custom formatting
    # __lt__ : Less than
    # __le__ : Less than or equal to
    # __eq__ : Equal to
    # __ne__ : Not equal to
    # __gt__ : Greater than

    # __ge__ : Greater than or equal to
    # __hash__ : Hashable
    # __bool__ : Boolean
    # __getattr__ : Accessing nonexistent attributes
    # __setattr__ : Assigning to attributes
    # __delattr__ : Deleting attributes
    # __dir__ : Listing attributes
    # __getattribute__ : Attribute access
    # __set__ : Descriptor access
    # __delete__ : Descriptor deletion
    # __set_name__ : Descriptor name rebinding
    # __slots__ : Restricting attribute creation
    # __len__ : Length
    # __length_hint__ : Length hint
    # __getitem__ : Indexing
    # __setitem__ : Assigning to indexed values
    # __delitem__ : Deleting indexed values
    # __missing__ : Default behavior for missing values
    # __iter__ : Iteration
    # __reversed__ : Reverse iteration
    # __contains__ : Membership
    # __call__ : Calling objects as functions
    # __enter__ : Context management support
    # __exit__ : Context management support
    # __await__ : Awaitable objects
    # __aiter__ : Asynchronous iteration
    # __anext__ : Asynchronous iteration
    # __aenter__ : Asynchronous context management support
    # __aexit__ : Asynchronous context management support
    # __index__ : Integer conversion
    # __trunc__ : Truncation
    # __floor__ : Flooring
    # __ceil__ : Ceiling
    # __round__ : Rounding

    # __add__ : Addition
    # __sub__ : Subtraction
    # __mul__ : Multiplication
    # __matmul__ : Matrix multiplication
    # __truediv__ : True division
    # __floordiv__ : Floor division
    # __mod__ : Modulo

    # __divmod__ : Divmod
    # __pow__ : Exponentiation
    # __lshift__ : Left bitwise shift
    # __rshift__ : Right bitwise shift
    # __and__ : Bitwise and
    # __xor__ : Bitwise xor
    # __or__ : Bitwise or

    # __radd__ : Addition with reflected operands
    # __rsub__ : Subtraction with reflected operands
