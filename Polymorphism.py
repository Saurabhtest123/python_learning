class car:                                         #class polymorphism
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Slowly!")

class plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fast!")

car1 = car("Ford", "Mustang")
boat1 = boat("Abc", "xyz")
plane1 = plane("Boeing", 747)

for x in (car1, boat1, plane1):
    x.move()







class Vehicle:                                            #Inheritance class Polymorphism
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("A")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("B")

class Plane(Vehicle):
  def move(self):
    print("C")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Maruti", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()
  print(x.brand)
  print(x.model)
  #x.move()
