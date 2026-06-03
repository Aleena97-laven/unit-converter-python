import requests

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def kg_to_lbs(kg):
    return kg * 2.20462

def lbs_to_kg(lbs):
    return lbs / 2.20462

def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 5/9) * 5/9

def get_currency_rate(base, target):
    """Fetch live currency rate from free API"""
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{base}"
        response = requests.get(url, timeout=5)
        data = response.json()
        return data["rates"][target]
    except:
        return None

def currency_convert(amount, base, target):
    rate = get_currency_rate(base, target)
    if rate:
        return amount * rate
    else:
        return None

def main():
    while True:
        print("\n=== Unit Converter ===")
        print("1. KM to Miles")
        print("2. Miles to KM")
        print("3. KG to LBS")
        print("4. LBS to KG")
        print("5. Celsius to Fahrenheit")
        print("6. Fahrenheit to Celsius")
        print("7. USD to INR - Live Rate")
        print("8. INR to USD - Live Rate")
        print("9. Exit")

        choice = input("Choose option 1-9: ")

        if choice == '9':
            print("Thanks for using Unit Converter!")
            break

        try:
            if choice == '1':
                val = float(input("Enter KM: "))
                print(f"{val} KM = {km_to_miles(val):.2f} Miles")
            elif choice == '2':
                val = float(input("Enter Miles: "))
                print(f"{val} Miles = {miles_to_km(val):.2f} KM")
            elif choice == '3':
                val = float(input("Enter KG: "))
                print(f"{val} KG = {kg_to_lbs(val):.2f} LBS")
            elif choice == '4':
                val = float(input("Enter LBS: "))
                print(f"{val} LBS = {lbs_to_kg(val):.2f} KG")
            elif choice == '5':
                val = float(input("Enter Celsius: "))
                print(f"{val}°C = {c_to_f(val):.2f}°F")
            elif choice == '6':
                val = float(input("Enter Fahrenheit: "))
                print(f"{val}°F = {f_to_c(val):.2f}°C")
            elif choice == '7':
                val = float(input("Enter USD: "))
                result = currency_convert(val, "USD", "INR")
                if result:
                    print(f"${val} USD = ₹{result:.2f} INR")
                else:
                    print("Error: Could not fetch exchange rate. Check internet.")
            elif choice == '8':
                val = float(input("Enter INR: "))
                result = currency_convert(val, "INR", "USD")
                if result:
                    print(f"₹{val} INR = ${result:.2f} USD")
                else:
                    print("Error: Could not fetch exchange rate. Check internet.")
            else:
                print("Invalid option. Choose 1-9.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()