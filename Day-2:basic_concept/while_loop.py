# Understand Python While Loops: You need to know when you should use while loop
# Understand The break, continue, pass  Statement
# What is the difference between for loop and while loop?

# using for iteration as for loop as well but it have before starting iterate each item 

# practies some exercies : 
Booklist = ["Python Basics", "Data Science 101"]
author = ["John Doe", "Jane Smith"]


while True:
    print("\n📋 Menu:")
    print("1. Book Listing")
    print("2. Book Authur")
    print("3. Borrow Book")
    print("4. Exit")
    choice = int(input("\nEnter number of menu : "))
    if choice == 1:
        for i in Booklist:
            print(f" - {i}")
    elif choice == 2:
        for i in author:
            print(f" - {i}")
    elif choice == 3:
        print("Soon!")
    elif choice == 4:
        break
    else:
        print("Invalid choice!")

print("👋 Goodbye!")

    