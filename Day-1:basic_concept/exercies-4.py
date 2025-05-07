# Ask a user for their personal information one by one. 
# Then check that the information they entered is valid. 
# Finally, print a summary of all the information they entered back to them.
# Example: What is your name? If the user enters * you prompt them that the input is wrong. 
# And ask them to enter a valid name. At the end you print a summary like that looks like this:

# - Name: Rim Sovankiry
# - Date of birth: Jan 1, 1990
# - Address: 16BT Phnom Penh, Cambodia
# - Personal goals: To be the best programmer there ever was.

name = "ban sothea"
date = "jan 1, 1900"
address = "16bt phnom penh, cambodai"
personal_goals = "programar"
user_name = input("What is your name? ").lower()

if user_name==name :
    date_birth = input("Success!!  Input date birth : ")
    if date_birth == date:
        address_user = input("Success Input address: ").lower()
        if address_user==address : 
            personal = input("Success ! Enter Personal goal : ").lower()
            if personal == personal_goals: 
                print(f"Name : {name}")
                print(f"Date : {date}")
                print(f"Address: {address}")
                print(f'personal goal: {personal_goals}')
            else: 
                print("There are some problem with the personal goal!")
        else: 
            print("problem with the adress ")   
    else : 
        print("Wrong Date Birth!")
else: 
    print("somthing went wrong? ")

