# Understanding Python Dictionary 
# Access Dictionary Items
# Add/Change and Remove Dictionary items
# Loop dictionaries
# Nested Dictionaries
# Dictionary Methods | Optional


# Nested Dictionaries
person = {
    "Name": "sothea",
    "age" : "23",
    "email": "bansothea@gmail.com",
    "experience": {
        "Jobify": "software engineer",
        "Morakot": "Sotware developer",
    }
}

# Add/Change and Remove Dictionary items
person.update({
    "car": "BMW"
})
print(person)
print("world")

#Remove Dictionary items

print(person["experience"]["Jobify"])

# Loop dictionaries
for j in person["experience"].items():
    print(j)
print("--Vlaue--")
for i in person.values():
    print(i)

print("--keys--")
for i in person.keys():
    print(i)