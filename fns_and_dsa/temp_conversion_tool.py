FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * FAHRENHEIT_TO_CELSIUS_FACTOR) + 32
    return fahrenheit

temperature = int(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

if unit == "C":
    fahrenheit = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {fahrenheit}°F")
elif unit == "F":
    celsius = convert_to_celsius(temperature)
    print(f"{temperature}°F is {celsius}°C")
else:
    print("Please enter either C or F")

