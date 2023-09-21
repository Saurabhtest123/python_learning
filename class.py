#class Person:                              #__init__()  function
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#p1 = Person("Saurabh", 31)

#print(p1.name)
#print(p1.age)

#class admin:                                  #__str__() function
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#    def __str__(self):
#        return f"{self.name}({self.age})"
    
#p1 = admin("Bana", 31)

#print(p1)


#class person:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#    def myfunc(self):
#        print("Hello my name is " + self.name)

#p1 = person("Saurabh", 31)
#p1.myfunc()


class furkan:
    def __init__(ajij, name, age):
        ajij.name = name
        ajij.age = age

    def myfunc(xyz):
        print("Hello my name is " + xyz.name)

p1 = furkan("Bana", 31)

p1.age = 40
p1.myfunc()
print(p1.age)