"""Função que calcule o quadrado do numéro passado como parâmetro
se nenhum numero for passado use como padrão o numero 5.
"""
def quadrado(numero=5):
    return numero * numero

quadrado (4)

"""Função que recebe como parâmetro uma temperatura 
em graus fahrenheit e converta para graus celsius
"""
def temperatura (temp):
    celsius = (5/9)*(temp - 32)
    return celsius

print (temperatura (32))
print (temperatura(10))

"""Função que recebe dois parâmetros. o primeiro
será uma palavra, se ela for quadrado deverá calcular 
o quadrado do número passado como segundo parametro.
se a palavra for cubo, deverá realizar o calculo do
cubo do número passado
"""
def calculo (comando,numero):
    if comando == 'quadrado':
        return numero * numero
    else:
        return numero * numero * numero

print (calculo ('cubo', 2))
print (calculo ('quadrado',3))