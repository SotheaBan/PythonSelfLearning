# 1. Odd or even
# Tags: variable, int,  input, print

# Welcome a user then ask them for a number between 1 and 1000.

# When the user gives you the number, you check if it's odd or even and then you print a message letting them know. 

print(" Wellcome ")
num = int(input("Please enter from 1 to 1000 : "))

if 1<num>1000: 
    
    print("wrong number")

else: 
    if num % 2 == 0 : 
        print("even")
    else: 
        print('odd')