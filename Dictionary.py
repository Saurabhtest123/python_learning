thisdict = {
    "brand" : "Ford",
    "brand" : "Suzuki",
    "model" : "Omni",
    "model" : "Mustang",
    "year" : 1964,
    "year" : 2020,
    "year" : 1920
}
#x = thisdict["model"]
#print(thisdict["year"])
#print(x)
#print(thisdict)

car = {
    "brand" : "Maruti",
    "model" : "Ciaz",
    "year" : 2022,
}
#x = car.keys()
#print(x) #before the change
#car["color"] = "white"
#print(x)  #after the change
#y = car.values()
#print(y)

#if "color" in car:
 #   print("Yes")
#else:
#    print("No")
#car["year"] = 2023
#print(car)

#car.pop("model")
#del car["brand"]
#del car
#car.popitem()
#car.clear()
#for x in car:
#    print(x)
#  print(car[x])
#for x in car.values():
#for x in car.keys():
#   print(x)
#for x, y in car.items():
#    print(x,y)
#newcar = car.copy()
#newcar = dict(car)
#print(newcar)

#myfamily = {
#    "child1" : {
#        "name" : "Suraj",
#        "year" : 2004
#    },
#    "child2" : {
#        "name" : "Subham",
#        "year" : 2007
#    },
#    "child3" : {
#        "name" : "Shivani",
#        "year" : 2011
#    }
#}
#print(myfamily)

child1 = {
    "name" : "Love",
    "year" : 2002
}
child2 = {
    "name" : "Shalini",
    "year" : 2005
}
child3 = {
    "name" : "Jatin",
    "year" : 2009
}
myfamily = {
    "Beta" : child1,
    "Beti" : child2,
    "Pota" : child3
}
print(myfamily)
print(myfamily["Beti"]["name"])