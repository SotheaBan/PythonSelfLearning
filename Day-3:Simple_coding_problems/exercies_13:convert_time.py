# Create functions that convert seconds to minutes,  hours or days.
#  def format_pretty_sec(second):
#     	     #Your code write here

#   	>>>> format_pretty_sec(2300)
#   	38.33 minutes
#   	>>>> format_pretty_sec(23701)
#   	6.58 Hours
#   	>>>> format_pretty_sec(172800)
#       2 Days

# Unit	Formula
# Minutes	seconds / 60
# Hours	seconds / 3600 (60 × 60)
# Days	seconds / 86400 (24 × 3600)


def convertfun(time):

    if time >= 86400: 
        result = int(time/86400)
        return f"{result} Days"
    elif time >=3600: 
        result = (time/3600)
        return f"{result} hours"
    elif time >=60: 
        result = time/60
        return f"{result} Minutes"
    else:
        return f"{result} Second"
    

while True: 

    print("wecome to time Convertor ")
    user= int(input("Insert time : "))

    if user != "":
        print(convertfun(user))
    else: 
        break