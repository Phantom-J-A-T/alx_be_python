# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main Program
def main():
    try:
        # Ask user for temperature
        temp_input = input("Enter the temperature to convert:").strip()
        temperature = float(temp_input)  # Validate it's a number

        # Ask for unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

        if unit == 'c':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted:.2f}°F.")
        elif unit == 'f':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted:.2f}°C.")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Run the program
if __name__ == "__main__":
    main()
