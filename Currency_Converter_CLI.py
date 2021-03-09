import requests


def currency_converter():
    global content
    print('''--------------------------Currency Converter (Live)--------------------------''')
    try:
        # Requesting data
        api_key = "Your key here"
        print("[+] Getting currency updates...")
        response = requests.get(f"http://data.fixer.io/api/latest?access_key={api_key}&format=1")

    except requests.exceptions.ConnectionError:
        print("[-] Connection error : Please check your internet Connection")

    else:
        print("[+] Converting data to usable form...")
        content = response.json()
        print("[+] Ready to Start !\n")
        print("Currencies:Rate We support:")
        for i in content["rates"]:
            print(f"{i}:{content['rates'][i]}")

        base_currency, to_currency, input_amount = input_taking()

        # Converting to EUR currency first
        semi = (1 / content["rates"][base_currency]) * input_amount
        # Converting EUR to User desired currency
        converted_amount = semi * content["rates"][to_currency]

        print("[+] Converted Amount :", converted_amount)
        ask = input(">>> Do you want to run again ? (y,yes) : ")
        if ask in ("y", "yes"):
            currency_converter()
        else:
            quit()


def input_taking():
    try:
        input_amount = float(input("\n>>> Enter Amount to Convert : "))
    except ValueError:
        print("[-] Please Enter Valid Amount")
        input_taking()
    else:
        base_currency = input(">>> Enter Base Currency (Refer to above currencies): ")
        to_currency = input(">>> Enter currency you want to convert to (Refer to above currencies):")

        if base_currency not in content["rates"] or to_currency not in content["rates"]:
            print("[-] Please enter Valid Currency!")
            input_taking()
        else:
            return base_currency, to_currency, input_amount


currency_converter()
