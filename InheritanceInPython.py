# with Inheritance one class can derive the properties of another class
class Vehicle:
    def __init__(self,milage,cost):
        self.milage=milage
        self.cost=cost
    

    def show_details(self):
        print("I am a vehicle")
        print("Milage of the Vehicle is :",self.milage)
        print("Cost of the vehicle is :",self.cost)

v1=Vehicle(500,500)
v1.show_details()

class Car(Vehicle):                         #Child class
    def show_car(self):
        print('I am a Car')


c1=Car(200,1200)
c1.show_details()                       #invoking parent  class method

c1.show_car()                           #invoking derive class method   

class car(Vehicle):
    def __init__(self,milage,cost,tyres,hp):
        super().__init__(milage,cost)         #overriding init method
        self.tyres=tyres
        self.hp=hp

    def show_car_details(self):
        print("I am a car")
        print("Number of Tyres are: ",self.tyres)
        print("Value of horse power is :",self.hp)

c1=car(20,12000,4,300)
c1.show_details()
c1.show_car_details()