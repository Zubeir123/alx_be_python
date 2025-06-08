FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

temperature = input("Enter the temperature to convert: ")
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

try:
    temperature = float(temperature)
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")

if unit == "c":
    fahrenheit = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {fahrenheit}°F")
elif unit == "f":
    celsius = convert_to_celsius(temperature)
    print(f"{temperature}°F is {celsius}°C")
else:
    raise ValueError("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

