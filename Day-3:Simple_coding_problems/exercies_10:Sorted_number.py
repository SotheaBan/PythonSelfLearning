# Sort list by alphabetical order
# Example 1: 
# Prompt: Please input a list of number or string
# Input: 14, 129, 120, 3, 12, 30
# Output: 3, 12, 14, 30, 120, 129

def sortednum(num): 
    aftersort = sorted(num)
    print(aftersort)

def funsort(numbers): 
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print(numbers)

def sortalphabet(word): 
    sortAlphabet = sorted(word)
    print(sortAlphabet)



listnum=[]
word=[]
while True : 

    print("1. Compare listing number")
    print("2. Compare Alphabet listing")
    print("3. exit")

    choice = input("please input : ")
    if choice == "1":
        while True: 
            number= input("Enter number ")
            if number !="":
                print("enter to exit ")
                listnum.append(number)
            else: 
                print("Result: ")
                sortednum(listnum)
                funsort(listnum)
                print("_________")
                break
    elif choice == "2": 
        while True : 
            alphabet= input("Enter Alphabet: ")
            if alphabet !="":
                print("enter to exit and see the result")
                word.append(alphabet)
            else: 
                print("Result!")
                funsort(word)
                print("_____")
                break
    elif choice =="3":
        break

    else: 
        print("Error input !")
