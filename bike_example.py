class  Bike:  # classes should begin with a capital letter

    # the __init__ method special method is called a constructor
    # self is a reference to the current instance of the class
    def __init__(self, description, condition, sale_price, cost=0):
        self.description = description
        self.condition = condition
        self.sale_price = sale_price
        self.cost = cost
        self.sold = False
        print("Intializing a new bike")


    def update_sale_price(self):
        pass

    def sell(self):
        pass

    def service(self):
        pass


my_bike = Bike(description="Organge Africa", condition="bad", sale_price="100" ) # create an instance of the Bike class
print(type(my_bike))  # <class '__main__.Bike'>
print(my_bike)  # <__main__.Bike object at 0x000001E0B0E3F4C0>
print(my_bike.__class__)  # <class '__main__.Bike'>
print(my_bike.__class__.__name__)  # Bike
print(my_bike.__class__.__module__)  # __main__
print(my_bike.__class__.__module__ + '.' + my_bike.__class__.__name__)  # __main__.Bike
print(dir(my_bike))# print all methods of the class