# Menu Driven Program
def cm_to_ft(number):
    value = number * 0.0328
    return value

def km_to_miles(number):
    value = number * 0.62
    return value

def usd_to_inr(number):
    value = number * 83.72
    return value

def main():
    print("***************************Main Menu****************************")
    print("\tChoose 1 to Convert cm to feet")
    print("\tChoose 2 to Convert km to miles")
    print("\tChoose 3 to Convert usd to inr")
    print("\tChoose 4 to Quit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid Entry: Please enter a number between 1 and 4.")
        return

    if choice == 4:
        print("Exiting the program.")
        return

    try:
        number = float(input("Enter the value you want to convert: "))
    except ValueError:
        print("Invalid Entry: Please enter a numeric value.")
        return

    # Replacement for Switch in Python is Dictionary
    switcher = {
        1: cm_to_ft,
        2: km_to_miles,
        3: usd_to_inr,
    }

    # Get the conversion function from the dictionary based on user choice
    conversion_func = switcher.get(choice, None)

    if conversion_func:
        result = conversion_func(number)
        print(f"The value after conversion is {result:.2f}")
    else:
        print("Invalid choice: Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
