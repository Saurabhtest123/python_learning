#mytuple = ("apple", "banana", "cherry")        #Iterator
#myit = iter(mytuple)

#print(next(myit))
#print(next(myit))
#print(next(myit))



#mystr = "Saurabh"                                 #Iterable
#myit = iter(mystr)

#print(next(myit))
#print(next(myit))
#print(next(myit))
#print(next(myit))
#print(next(myit))
#print(next(myit))
#print(next(myit))


#mytuple = ("apple", "banana", "cherry")      #loop through an iterator
#mystr = "Bana"

#for x in mytuple:
#for x in mystr:
#    print(x)



#class mynumbers:                 #create an Iterator
#    def __iter__(self):
#        self.a = 1
#        return self
    
#    def __next__(self):
#        x = self.a
#        self.a += 1
#        return x
    
#myclass = mynumbers()
#myiter = iter(myclass)

#print(next(myiter))
#print(next(myiter))
#print(next(myiter))
#print(next(myiter))
#print(next(myiter))
#print(next(myiter))
#print(next(myiter))
#print(next(myiter))




class mynumbers:                                                #StopIteration
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <=15:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration
        
myclass = mynumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)




