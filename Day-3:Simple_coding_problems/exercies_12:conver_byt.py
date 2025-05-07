# 12. Create function convert bytes to kb to mb to gb to tb:
#       def format_pretty_bytes(size_bytes):
#     	     #Your code write here
#   	>>>> format_pretty_bytes(135000)
#   	135 kb
#   	>>>> format_pretty_bytes(250000000)
#   	250 mb
#   	>>>> format_pretty_bytes(1500000000)
#   	1.5 gb

# Unit	Value in Bytes
# 1 KB	1,024 Bytes
# 1 MB	1,024 KB = 1,048,576 B
# 1 GB	1,024 MB = 1,073,741,824 B

def format_pretty_bytes(size_bytes):
    if size_bytes >= 1_000_000_000:
        return f"{round(size_bytes / 1_000_000_000, 1)} gb"
    elif size_bytes >= 1_000_000:
        return f"{round(size_bytes / 1_000_000)} mb"
    elif size_bytes >= 1_000:
        return f"{round(size_bytes / 1_000)} kb"
    else:
        return f"{size_bytes} b"
    
    
while True: 

    print("Welcome to converter calculator")
    user_input = int(input("Enter byte to calculate : "))
    if user_input !="":
        print(format_pretty_bytes(user_input))
        print("PRess any key to break ")
    else:
        break
