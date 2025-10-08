#Inheritance
#Use when classes have very similar methods and can be generalized 

#Parent/ Upper level class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} year(s) old')

    #This will be overridden in child classes
    def speak(self):
        print("I dont know what to say")

#Inherits Pet class
class Cat(Pet):
    def __init__(self, name, age, color):
        #Calling super class's (inherited from class) method __init__ and pass arguments
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("I Meow")

    #adding color, changing show() method 
    def show(self):
        print(f"I am {self.name} and I am {self.age} year(s) old and I am {self.color}")
    
#Inherits Pet class
class Dog(Pet):
    def speak(self):
        print("I Bark")

#Because there is no speak defined in here, it will use speak() from the parent/ upper level class
class Fish(Pet):
    pass
    

pet1 = Pet("Will", 14)
pet1.show()

#These will inherite the properies of the Pet class which is why its able to use show()
pet2 = Cat("Shadow", 11, "Black")
pet2.show()
pet2.speak()

pet3 = Cat("Girl", 3, "Grey")
pet3.show()
pet3.speak()

pet4 = Dog("Sedona", 20)
pet4.show()
pet4.speak()

pet5 = Fish("Nemo", 2)
pet5.show()
#Shows importance of having two speak classes
pet5.speak()