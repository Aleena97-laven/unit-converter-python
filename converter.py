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
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        print("\n=== Unit Converter ===")
        print("1. KM to Miles")
        print("2. Miles to KM") 
        print("3. KG to LBS")
        print("4. LBS to KG")
        print("5. Celsius to Fahrenheit")
        print("6. Fahrenheit to Celsius")
        print("7. Exit")
        
        choice = input("Pick an option 1-7: ")
        
        if choice == '7':
            print("Thanks for using Unit Converter!")
            break
            
        if choice not in ['1','2','3','4','5','6']:
            print("Invalid choice. Try again.")
            continue
            
        try:
            value = float(input("Enter value to convert: "))
        except ValueError:
            print("Please enter a number.")
            continue
            
        if choice == '1':
            print(f"{value} km = {km_to_miles(value):.2f} miles")
        elif choice == '2':
            print(f"{value} miles = {miles_to_km(value):.2f} km")
        elif choice == '3':
            print(f"{value} kg = {kg_to_lbs(value):.2f} lbs")
        elif choice == '4':
            print(f"{value} lbs = {lbs_to_kg(value):.2f} kg")
        elif choice == '5':
            print(f"{value}°C = {c_to_f(value):.2f}°F")
        elif choice == '6':
            print(f"{value}°F = {f_to_c(value):.2f}°C")

if __name__ == "__main__":
    main()