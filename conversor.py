def celsius_para_fahrenheit(celsius):
    """Converte temperatura de Celsius para Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    """Converte temperatura de Fahrenheit para Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_para_kelvin(celsius):
    """Converte temperatura de Celsius para Kelvin"""
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    """Converte temperatura de Kelvin para Celsius"""
    return kelvin - 273.15

def fahrenheit_para_kelvin(fahrenheit):
    """Converte temperatura de Fahrenheit para Kelvin"""
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)

def kelvin_para_fahrenheit(kelvin):
    """Converte temperatura de Kelvin para Fahrenheit"""
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)