#Program that will convert celisus into fahrenheit.
def converter(temp):
    convertedTemp=(temp*5)/2+32
    return convertedTemp

temperature_inc=float(input("Enter Temperature in Celsius"))
temperature_inf=converter(temperature_inc)
print(temperature_inf,type(temperature_inf))