# A tuple is an ordered, immutable (unchangeable) collection:

# Understanding Python Tuples
# Access Tuples
# Update and Unpack Tuples
# Loop Tuples
# Join Tuples
# Resource:

brand =("BMW","mercedes","iphone")

print(brand[-1])

#update and unpack tuples

data = list(brand)
print (data)
data.append("Lan khmer ")
print(data)

# loop and unpack Tuples

for i in data : 
    print(i)

# Here is how to unpack tuples 
germany, england ,USA = brand
print (USA)


# join temple : 

animal=("cat","Dog")
c = brand+animal
print(c)