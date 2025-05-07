# Find the largest number in a list
# Prompt: Please input a list of number for finding
# Input: 2, 3, 4, 8, 1, 100, 49.12, 50
# Output: The largest number is 100


def find_large_number(number):
    ans= sorted(number)
    print(ans[-1])
    
number= []

print("Enter listing of number: ")

while True : 
    userinput=input('Enter number:')
    if userinput != "":
        number.append(userinput)
    else:
        break

print(number)
find_large_number(number)