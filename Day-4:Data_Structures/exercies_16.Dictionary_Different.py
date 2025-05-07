# Tags: dict, set, compare

# Create a function that finds the difference between two dictionaries. After that the result will create a new dictionary with keys only different and value is type of list.
# First item of the list result is a value from the first dictionary.
# Second item of the list result is a value from the second dictionary.
def compare_dict_diff(d1,d2):   
    diff = {}
    allkey = d1.keys() | d2.keys()
    print(allkey)

    for key in allkey: 
       value1= d1.get(key,'')
       value2= d2.get(key,'')

       if value1 != value2 :
           print(f"{key} : {value1} different {key}  : {value2}")
 

d1 = {'a':1, 'b':5, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}

compare_dict_diff(d1,d2)