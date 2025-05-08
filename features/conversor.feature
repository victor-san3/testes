# language: pt

Funcionalidade: Conversor de Temperatura
  Para estudantes de ciências
  Quero converter temperaturas entre diferentes escalas
  Para resolver problemas de física e química

  Cenário: Converter de Celsius para Fahrenheit
    Dado que eu tenho uma temperatura de 25 graus Celsius
    Quando eu converto para Fahrenheit
    Então o resultado deve ser 77 graus Fahrenheit

  Cenário: Converter de Fahrenheit para Celsius
    Dado que eu tenho uma temperatura de 98.6 graus Fahrenheit
    Quando eu converto para Celsius
    Então o resultado deve ser 37 graus Celsius

  Cenário: Converter de Celsius para Kelvin
    Dado que eu tenho uma temperatura de 0 graus Celsius
    Quando eu converto para Kelvin
    Então o resultado deve ser 273.15 Kelvin

  Cenário: Converter de Kelvin para Celsius
    Dado que eu tenho uma temperatura de 300 Kelvin
    Quando eu converto para Celsius
    Então o resultado deve ser 26.85 graus Celsius

  Cenário: Converter de Fahrenheit para Kelvin
    Dado que eu tenho uma temperatura de 32 graus Fahrenheit
    Quando eu converto para Kelvin
    Então o resultado deve ser 273.15 Kelvin

  Cenário: Converter de Kelvin para Fahrenheit
    Dado que eu tenho uma temperatura de 0 Kelvin
    Quando eu converto para Fahrenheit
    Então o resultado deve ser -459.67 graus Fahrenheit

  Cenário: Converter ponto de ebulição da água de Celsius para Fahrenheit
    Dado que eu tenho uma temperatura de 100 graus Celsius
    Quando eu converto para Fahrenheit
    Então o resultado deve ser 212 graus Fahrenheit

  Cenário: Converter zero absoluto de Kelvin para Celsius
    Dado que eu tenho uma temperatura de 0 Kelvin
    Quando eu converto para Celsius
    Então o resultado deve ser -273.15 graus Celsius

  Cenário: Converter temperatura corporal humana de Fahrenheit para Kelvin
    Dado que eu tenho uma temperatura de 98.6 graus Fahrenheit
    Quando eu converto para Kelvin
    Então o resultado deve ser 310.15 Kelvin

  Esquema do Cenário: Converter várias temperaturas de Celsius para Fahrenheit
    Dado que eu tenho uma temperatura de <celsius> graus Celsius
    Quando eu converto para Fahrenheit
    Então o resultado deve ser <fahrenheit> graus Fahrenheit

    Exemplos:
      | celsius | fahrenheit |
      | -40     | -40        |
      | 0       | 32         |
      | 10      | 50         |
      | 20      | 68         |
      | 30      | 86         |