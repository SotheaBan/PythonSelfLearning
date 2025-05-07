#  Find a date into day in Khmer, format in date ISO YYYY-MM-DD
# Prompt: Please input the date for checking. 
# Input: 2021-01-05
# Output: ចន្ទ

from datetime import datetime
day_name_khmer = {
    "monday": "ចន្ទ",
    "tuesday": "អង្គារ",
    "wednesday": "ពុធ",
    "thursday": "ព្រហស្បតិ៍",
    "friday": "សុក្រ",
    "saturday": "សៅរ៍",
    "sunday": "អាទិត្យ"
}


while True : 
    choice =input("please date: ")
    if choice !="" : 
        date_object = datetime.fromisoformat(choice)
        day_name = date_object.strftime("%A")
        khmerday = day_name.lower()
        print(day_name_khmer[khmerday])
    else: 
        break
