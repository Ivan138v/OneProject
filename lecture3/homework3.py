Celsius = float(input("Enter a Temperature in Celsius: "))
Fahrenheit = ((9 * Celsius)/5) + 32
def convert(Celsius, Fahrenheit):
    """'convert' function takes 2 parameters, 'Celsius' & 'Fahrenheit' and
        completes the operation for the two variables"""
    print(Celsius, "in degrees Celsius is", Fahrenheit, "in degrees Fahrenheit")
    return Fahrenheit
convert(Celsius, Fahrenheit)
