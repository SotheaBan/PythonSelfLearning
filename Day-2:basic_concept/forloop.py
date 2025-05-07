# Understand Python For Loops: You need to know when you should use for loop
# Understand The break, continue, pass  Statement
# For loop with range() Function
# Nested Loops

odd_number = []
even_number = []

for i in range(20) : 
    if i % 2 == 0 : 
        even_number.append(i)
    else : 
        odd_number.append(i)

print(odd_number)
print(even_number)
   