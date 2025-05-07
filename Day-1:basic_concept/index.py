# Variable
name = "Sothea"
age = 25
height = 1.75
is_student = True

print(age)
#Display output (print command)

print("hello "+name)
#Take user input (input command)

inputnumber  = (input("Enter user Number : "))
print("wellcome : "+inputnumber)

#Conditionals

# give label to user age : 
# if, elif, else
age = int(input("Enter age : "))

if age < 18:
    print("Minor")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# and, or
if age > 18 and age < 30:
    print("Young Adult")

if age < 18 or age > 65:
    print("Needs guardian")

# not
logged_in = False
if not logged_in:
    print("Please log in")

# in
if "apple" in ["banana", "apple", "cherry"]:
    print("Found!")

# is
x = None
if x is None:
    print("x has no value")
