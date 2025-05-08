from behave import given, when, then
import sys
import os

# Adiciona o diretório pai ao caminho para importar o módulo conversor
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from conversor import (
    celsius_para_fahrenheit, 
    fahrenheit_para_celsius,
    celsius_para_kelvin,
    kelvin_para_celsius,
    fahrenheit_para_kelvin,
    kelvin_para_fahrenheit
)

@given('que eu tenho uma temperatura de {temperatura:g} graus Celsius')
def step_celsius(context, temperatura):
    context.temperatura = temperatura
    context.unidade_origem = 'Celsius'

@given('que eu tenho uma temperatura de {temperatura:g} graus Fahrenheit')
def step_fahrenheit(context, temperatura):
    context.temperatura = temperatura
    context.unidade_origem = 'Fahrenheit'

@given('que eu tenho uma temperatura de {temperatura:g} Kelvin')
def step_kelvin(context, temperatura):
    context.temperatura = temperatura
    context.unidade_origem = 'Kelvin'

@when('eu converto para Fahrenheit')
def step_converte_para_fahrenheit(context):
    if context.unidade_origem == 'Celsius':
        context.resultado = celsius_para_fahrenheit(context.temperatura)
    elif context.unidade_origem == 'Kelvin':
        context.resultado = kelvin_para_fahrenheit(context.temperatura)
    context.unidade_destino = 'Fahrenheit'

@when('eu converto para Celsius')
def step_converte_para_celsius(context):
    if context.unidade_origem == 'Fahrenheit':
        context.resultado = fahrenheit_para_celsius(context.temperatura)
    elif context.unidade_origem == 'Kelvin':
        context.resultado = kelvin_para_celsius(context.temperatura)
    context.unidade_destino = 'Celsius'

@when('eu converto para Kelvin')
def step_converte_para_kelvin(context):
    if context.unidade_origem == 'Celsius':
        context.resultado = celsius_para_kelvin(context.temperatura)
    elif context.unidade_origem == 'Fahrenheit':
        context.resultado = fahrenheit_para_kelvin(context.temperatura)
    context.unidade_destino = 'Kelvin'

@then('o resultado deve ser {resultado:g} graus Fahrenheit')
def step_resultado_fahrenheit(context, resultado):
    assert round(context.resultado, 2) == round(resultado, 2), f"Esperava {resultado}, mas obteve {context.resultado}"

@then('o resultado deve ser {resultado:g} graus Celsius')
def step_resultado_celsius(context, resultado):
    assert round(context.resultado, 2) == round(resultado, 2), f"Esperava {resultado}, mas obteve {context.resultado}"

@then('o resultado deve ser {resultado:g} Kelvin')
def step_resultado_kelvin(context, resultado):
    assert round(context.resultado, 2) == round(resultado, 2), f"Esperava {resultado}, mas obteve {context.resultado}"