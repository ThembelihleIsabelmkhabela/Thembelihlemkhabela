

def currency_converter():
    USD_TO_ZAR = 18.50  
    ZAR_TO_USD = 1 / USD_TO_ZAR

    print("Welcome to the Currency Converter!")
    print("1. Convert USD to ZAR")
    print("2. Convert ZAR to USD")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        try:
            usd = float(input("Enter amount in USD: "))
            zar = usd * USD_TO_ZAR
            print(f"${usd:.2f} USD = R{zar:.2f} ZAR")
        except ValueError:
            print("Invalid input! Please enter a number.")
    elif choice == "2":
        try:
            zar = float(input("Enter amount in ZAR: "))
            usd = zar * ZAR_TO_USD
            print(f"R{zar:.2f} ZAR = ${usd:.2f} USD")
        except ValueError:
            print("Invalid input! Please enter a number.")
    else:
        print("Invalid choice! Please select 1 or 2.")
currency_converter()

