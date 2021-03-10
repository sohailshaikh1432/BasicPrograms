"""
Wind chill = 13.12 + 0.6215T – 11.37 (V^0.16) + 0.3965T (V^0.16)

T = Temperature in degrees Celsius
V = Wind velocity in kilometers per hour

"""

def calculate_wc():
    wind_chill = 35.74 + 0.6215 * temp - 35.75 * (wind_speed ** 0.16) + 0.4275 * temp * (wind_speed ** 0.16)
    return wind_chill


if __name__ == '__main__':
    temp = int(input("Enter 'temprature' value : "))
    wind_speed = int(input("Enter 'wind speed' value : "))
    print("Wind chill is : ", calculate_wc())
