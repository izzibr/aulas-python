#função sem retorno e sem passagem de parâmetro
def ola_mundo():
    """Função que mostra uma mensagem padrão na tela."""
    print("Olá mundo!")

ola_mundo()

#função sem retorno e com passagem de parâmetro
def ola_mundo(name):
    """Função que mostra um texto customizado na tela."""
    print (f"Olá mundo, seu nome é {name}")

name = input ("Qual o seu nome?")
ola_mundo(name)

#função com retorno e com passagem de parâmetro
def soma(a,b):
    """Função que recebe dois números e realiza a soma entre eles"""
    return a+b

resultado = soma (3,4)
print (resultado)

