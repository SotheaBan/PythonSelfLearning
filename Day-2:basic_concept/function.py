# Creating a Function to Python
# Calling a Function
# What is Arguments in function
# Arbitrary Arguments, *args
# What is Keyword Arguments
# Arbitrary Keyword Arguments, **kwargs
# Default Parameter Value
# Return Values



def hellowrold(): 
    print("hello!")

hellowrold()

#function with parameter : 

def addnumber(a,b): 
    c= a+b
    return c

number=addnumber(1,2)
print(number)

#Arbitrary Arguments :  this mean that it mostly 
print("Arbitrary function")

def printnumber(*a): 
    print(a)

printnumber(1,3,4,20,20)


#Keyword function: 
print("Keyword function")

def keyword(name , age ): 
    print (f"Hi I am {name} and I am {age} year old")

keyword(age="sothea", name="sothea")

#Arbitrary keyword functions : 
print("Arbitrary Keyword Arguments: **kwargs")

def userInfo(**info): 
   for keys,value in info.items(): 
       print(f"{keys} : {value}")

userInfo(name="sothea", age= 18 ,sport = "badminton")


# Return function return value : 
def addfun(a,b) : 
    c = a + b 

    return f" The result is {c}"


print(addfun(10,20))