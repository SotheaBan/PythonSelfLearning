# A set is an unordered collection of unique items (no duplicates) and is written with {}:
# Understanding Python Set
# Access, Add and Remove Set Items
# Set Methods | Optional

car = {"BMW", "Mercedes", "kDV"}

# acess the set 
# set cant access by index 

for i in car: 
    print(i)

# for add new item in set  
model={1}
model.add(5)
    
print(model)

# setting method 

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))         # {1, 2, 3, 4, 5}
print(a.intersection(b))  # {3}
print(a.difference(b))    # {1, 2}