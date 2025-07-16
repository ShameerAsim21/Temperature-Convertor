# temperature_converter.py

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    if from_unit == "C":
        if to_unit == "F":
            return celsius_to_fahrenheit(value)
        elif to_unit == "K":
            return celsius_to_kelvin(value)

    elif from_unit == "F":
        if to_unit == "C":
            return fahrenheit_to_celsius(value)
        elif to_unit == "K":
            return fahrenheit_to_kelvin(value)

    elif from_unit == "K":
        if to_unit == "C":
            return kelvin_to_celsius(value)
        elif to_unit == "F":
            return kelvin_to_fahrenheit(value)

    else:
        raise ValueError("Invalid unit conversion.")

def main():
    print("=== Temperature Converter ===")
    try:
        value = float(input("Enter the temperature value: "))
        from_unit = input("Convert from (C/F/K): ").upper()
        to_unit = input("Convert to (C/F/K): ").upper()

        valid_units = {"C", "F", "K"}
        if from_unit not in valid_units or to_unit not in valid_units:
            print("Invalid unit. Please use 'C', 'F', or 'K'.")
            return

        result = convert_temperature(value, from_unit, to_unit)
        print(f"{value}°{from_unit} is equal to {result:.2f}°{to_unit}")
    except ValueError:
        print("Invalid input. Please enter numeric temperature value.")

if __name__ == "__main__":
    main()
# run using: python temperature_converter.py
