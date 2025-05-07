# Project requirement

# Write your code in class python. Example class name "CurrencyConverter" 
# Create a class method for breakdown by functionality:
# Print table exchange rate.
# Exchange money  from KHR to another currency.
# Get request data from the web NBC exchange rate.
# Save exchange rate in file csv.
# Command-line interface for input and output. (Check in example).

# Using a pretty print format table in the console (Terminal) suggestion use tabulate.


from tabulate import tabulate
import csv

header = ["Currency","Symbol","unit","Bid","ask","Average"]
data = [
    ["United States Dollar", "USD/KHR", 1,    4100, 4120, 4110],
    ["Australian Dollar",    "AUD/KHR", 1,    3081, 3112, 3096.5],
    ["Canadian Dollar",      "CAD/KHR", 1,    3208, 3240, 3224],
    ["Switzerland Franc",    "CHF/KHR", 1,    4351, 4395, 4373],
    ["Off-shore CNY",        "CNH/KHR", 1,     618,  624,  621],
    ["China Yuan",           "CNY/KHR", 1,     619,  625,  622],
    ["European Euro",        "EUR/KHR", 1,    4803, 4851, 4827],
    ["Hong Kong Dollar",     "HKD/KHR", 1,     520,  525,  522.5],
    ["Indonesian Rupiah",    "IDR/KHR", 1000,  279,  282,  280.5],
    ["Myanmar Kyat",         "MMK/KHR", 100,   280,  283,  281.5],
    ["Malaysian Ringgit",    "MYR/KHR", 1,     979,  989,  984],
    ["New Zealand Dollar",   "NZD/KHR", 1,    2836, 2865, 2850.5],
    ["Philippine Peso",      "PHP/KHR", 100,  8327, 8410, 8368.5],
    ["Special Drawing",      "SDR/KHR", 1,    5766, 5823, 5794.5],
    ["Swedish Krona",        "SEK/KHR", 1,     470,  474,  472],
    ["Singapore Dollar",     "SGD/KHR", 1,    3017, 3048, 3032.5],
    ["Thai Baht",            "THB/KHR", 1,     129,  130,  129.5],
    ["Taiwan Dollar",        "TWD/KHR", 1,     142,  144,  143],
    ["Vietnamese Dong",      "VND/KHR", 1000,  175,  177,  176]
]


def ShowExchangeRate():
    print(tabulate(data, headers=header,tablefmt="grid"))


def currencyConverter(amount,exchange):

    for i in range(len(data)):
        if exchange == data[i][1]:   
            result = round(amount/data[i][5],2)
            return result
        else: 
            print("Currency do not have enough data!")


def saveIntoCSV(filename, headers, data):
    if not filename.endswith(".csv"):
        filename += ".csv"

    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)

        print("")
        print(f"File saved as '{filename}'")
        print("Download exchange rate from the website...")
        print("Process save csv file…")
        print("Exchange rate save successfully...")
        print("")

        
    except Exception as e:
        print(f" Failed to write file: {e}")




while True : 

    print("Welcome to Currency converter")
    print("")
    print("1. Show real-time exchange rate")
    print("2. Money Exchange")
    print("3. Save exchange rate in CSV ")
    print("")
    choice = input("Please choose one to produce : ")
    print("or type 'q' to exit ")

    if choice == '1': 
        while True: 

            ShowExchangeRate()
            choice = input("Do you want to continue? (y/n): ")
            if choice == 'y': 
                break
            elif choice == 'n': 
                print('See you later!')
                exit()
            else: 
                print("Invalid input")

    elif choice == '2':
        while True: 
            
            semi = "-"*20

            print(f"{semi}Welcome To  Currency Converter{semi}")
            amount= int(input("Please Type amount in khmer Reil: "))
            currency = input("currency you want to exchange : ").upper()    

            if currency !="":
                exchange = currency+"/"+"KHR"
                for i in range(len(data)):
                    if exchange == data[i][1]:   
                        print("Currency do not have enough data!")
                        print(f"{semi}SUMMARY CURRENCY EXCHANGE{semi}")     
                        print(f"{amount} Cambodian Riels ={currencyConverter(amount,exchange)} ")
            else: 
                print("Invalid exchange !")

            choice = input("Do you want to continue? (y/n): ")
            if choice == 'y': 
                break
            elif choice == 'n': 
                print('See you later!')
                exit()
            else: 
                print("Invalid input")


    elif choice =='3': 
        filename = input("file Name : ")
        saveIntoCSV(filename,header,data)

        choice = input("Do you want to continue? (y/n): ")
        if choice == 'y': 
            pass
        elif choice == 'n': 
            exit()
        else: 
            print("Invalid input")


    elif choice == "q": 
        break
    else : 
        print("Invalid input !")



    