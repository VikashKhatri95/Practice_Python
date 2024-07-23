#Determine the weather based on Humidity and Temperature in Celcius

def weatherForecast(temp,humidity):
    if(temp>=30 and humidity>=90):
        print("Hot and Humid")
    elif(temp>=30 and humidity<90):
        print("Hot")
    elif(temp<30 and humidity>=90):
        print("Cold and Humid")
    elif(temp<30 and humidity<90):
        print("Cold")
    
temperature=float(input("Enter Temperature in Celcius "))
humidity=float(input("Enter Humidity in Celcius "))
weatherForecast(temperature,humidity)