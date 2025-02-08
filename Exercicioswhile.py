#fatorial de um número !5 = 5*4*3*2*1

numero = int (input ("Digite um numero inteiro"))
fatorial = numero
while numero >= 2:
    fatorial = fatorial * (numero - 1)
    numero -= 1   #numero = numero - 1
print (fatorial)


#simular cofre tres tentativas de senha 

senha = '0000'
tentativas = 3

while tentativas != 0: 
    tentativa = input ("Digite uma senha numerica de quattro digitos")

    if tentativa == senha:
        print ("Senha correta. Acesso concedido")
        break
    
    else:
        print ("Senha incorreta. Tente novamente")
        tentativas -= 1
