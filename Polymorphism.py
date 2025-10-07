import csv

#main class
class Item:

    pay_rate = 0.8

    all = []

    def __init__(self, name: str, price: float, quantity=0):
        #Run validations to the recieved arguments 
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Price {price} is not greater than or equal to zero!"

        #assign sef to object 
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    def calc_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    #Class method
    @classmethod
    def instantiate_from_csv(cls):
        with open('Instance_Attributes.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')) ,
                quantity = item.get('quantity')
            )
    
    #Static method
    @staticmethod
    def is_integer(num):
        #checking if instance is float or integer
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
     
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price},{self.quantity})"
    
#Practicing Inheritance
class Phone(Item):
    all=[]

    def __init__(self, name: str, price: float, quantity=0, broken_phones = 0):

        # Call super function to have access to all attributes and methods
        super().__init__(
            name, price, quantity
        )

        #Run validations to the recieved arguments 
        assert broken_phones >= 0, f"Broken phones {price} is not greater than or equal to zero!"


        #assign sef to object 
        self.broken_phones = broken_phones

        #Actions to execute
        Item.all.append(self)


#instances of class
#assigning attributes
item1 = Item("Phone", 100, 1)
print(item1.name, item1.price, item1.quantity)

item2 = Item("laptop", 1000, 3)
print(item2.name, item2.price, item2.quantity)

#Printing each instance name 
for instance in Item.all:
    print(instance.name)

#Printing each instance from __repr__  
print(Item.all) 

#printing function cacl_total_price result
print(item1.calc_total_price())
print(item2.calc_total_price())

#same with the pay rate
print(Item.pay_rate)

#working on printing variable inside class Item
item1.apply_discount()
print(item1.price)

#and outside of the class Item 
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)


#Printing results from csv file 
Item.instantiate_from_csv()

#Calling from print statement 
print(Item.is_integer(7))

# Inhertitance: 2 instances of phones
phone1 = Phone("phonev10", 500, 5)
phone1.broken_phones = 1
phone2 = Phone("phonev2", 500, 5)
phone2.broken_phones = 1


