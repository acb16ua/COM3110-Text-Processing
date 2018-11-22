# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 10:58:57 2018

@author: acb16ua
"""

# Converts temperature in celsius to fahrenheit and kelvin scale
def temperature_convert(celsius):
    fahrenheit = ((float(celsius) * (9/5)) + 32)
    kelvin = (float(celsius) + 273.15)
    print("Converting temperature from Celsius to Fahrenheit and Kelvin Scale:")
    print("Temperature in Celsius degrees:", celsius)
    print("Temperature in Fahrenheit degrees:", fahrenheit)
    print("Temperature in Kelvin Scale:", kelvin)