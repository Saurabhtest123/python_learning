#def myfunction():               #calling a function
#    print("Hello from a function")

#myfunction() 

#def my_function(name):             #Arguments
#    print(name + " Bana")

#my_function("Saurabh")
#my_function("Kapil")
#my_function("Gaurav")
#my_function("Mohit")

#def my_function(fname, mname, lname):      #number of arguments
#    print(fname + " " + mname + " " + lname)

#my_function("Dhananjay", "Singh", "Bana")    

#def my_function(*fname):                     # *args(argument)
#    print("your youngest kid name is" + " " + fname[2])
#    print("your eldest kid name is " + fname[-2])

#my_function("Jonu", "Ojas", "Dhananjay")


#def my_function(child1, child2, child3):              #keyword arguments
#    print("the youngest son is " + child2)

#my_function(child1= "Raja", child2= "Agrawal", child3= "Ankur")


#def my_function(**kid):                # **kwargs (key word arguments)
#    print("His last name is " + kid["lname"])
#    print("His first name is " + kid["fname"])

#my_function(fname = "Saurabh", lname = "Bana")


#def my_function(country = "Australia"):          #default parameter value
#    print("my country name is " + country)

#my_function("India")
#my_function()
#my_function("Swedan")
#my_function("America")

#def my_function(food):                      #Passing a list as an arguments
#    for x in food:
#        print(x)

#fruits = ["Apple", "Banana", "Cherry"]

#my_function(fruits)

#def my_function(x):                       #Return value
#    return 5 * x

#print(my_function(4))
#print(my_function(5))
#print(my_function(6))
#print(my_function(7))


def outer():
    x = 5
    def inner():
        nonlocal x
        x +=10
        print(x)
    inner()
    print(x)

outer()