# Check a phone number network service name in Cambodia. - hits
# Prompt: Input your phone number for checking:
# Input: 012456123
# Output: Your phone number is Cellcard


network_service = {
    "012" : "Celcard",
    "016" : "Smart",
    "097" : "Metphone"
}

user = input("Enter your mobile phone : ")
splitnumber = user[:3]
for i,service in network_service.items():
    if splitnumber == i : 
        print(f"Your phone number is {service}")
        break
else : 
    print("Sorry your number input doesn't belong to the mobile service in Cambodia.")