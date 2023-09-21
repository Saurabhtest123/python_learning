#class person:
#    def __init__(self, fname, lname):
#        self.firstname = fname
#        self.lastname = lname

#    def printname(self):
#        print (self.firstname, self.lastname)

#x = person("Saurabh", "Bana")
#x.printname()


#class lmno:
#    def __init__(xyz, y, z):
#        xyz.firstname = y
#        xyz.lastname = z

#    def printname(xyz):
#        print (xyz.firstname, xyz.lastname)

#x = lmno("Saurabh", "Bana")
#x.printname()


#class person:
#    def __init__(self, fname, lname):
#        self.firstname = fname
#        self.lastname = lname

#    def printname(self):
#        print(self.firstname, self.lastname)

#class Student(person):
#    pass

#x = Student("Gaurav", "Bana")
#x.printname()



#class person:                      #child class with __init__
#    def __init__(self, fname, lname):
#        self.firstname = fname
#        self.lastname = lname

#    def printname(self):
#        print(self.firstname, self.lastname)

#class student(person):
#    def __init__(self, fname, lname):
#        person.__init__(self, fname, lname)

#x = student("Kapil", "Bana")
#x.printname()



#class person:                                 #super() funtion
#    def __init__(self, fname, lname):
#        self.firstname = fname
#        self.lastname = lname

#    def printname(self):
#        print(self.firstname, self.lastname)

#class student(person):
#    def __init__(self, fname, lname):
#        super().__init__(fname, lname)

#x = student("Gaurav", "Bana")
#x.printname()
        



#class person:                                 #super() funtion & add properties
#    def __init__(self, fname, lname):
#        self.firstname = fname
#        self.lastname = lname

#    def printname(self):
#        print(self.firstname, self.lastname)

#class student(person):
#    def __init__(self, fname, lname):
#        super().__init__(fname, lname)
#        self.graduationyear = 2018

#x = student("Gaurav", "Bana")
#print(x.graduationyear)


#N = range(4)
#for i in N:
#    print(i)



class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def you(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Dinesh", "Bana", 2011)
x.you()