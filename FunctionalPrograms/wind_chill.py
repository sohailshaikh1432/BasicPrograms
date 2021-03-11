"""
Wind chill = 13.12 + 0.6215T – 11.37 (V^0.16) + 0.3965T (V^0.16)

T = Temperature in degrees Celsius
V = Wind velocity in kilometers per hour

"""

# DECLARE CONSTATNT

CONSTANT_1 = 35.74
CONSTANT_2 = 0.6215
CONSTANT_3 = 0.4275
VELOCITY_POWER = 0.16


def calculate_wc():
    wind_chill = CONSTANT_1 + CONSTANT_2 * temp - CONSTANT_1 * (wind_speed ** VELOCITY_POWER) + CONSTANT_3 * temp * (wind_speed ** VELOCITY_POWER)
    return wind_chill


if __name__ == '__main__':
    temp = int(input("Enter 'temprature' value : "))
    wind_speed = int(input("Enter 'wind speed' value : "))
    print("Wind chill is : ", calculate_wc())
