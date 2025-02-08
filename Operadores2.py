#Operadores lógicos 

#Maior que
resultado = 8 > 4
print (resultado)

#Maior ou igual 
resultado = 8 >= 8
print (resultado)

#Menor 
resultado = 10 < 20 
print (resultado)

#Menor ou igual 
resultado = 20 <= 20
print (resultado)

#Igualdade 
resultado = 5 == 6 
print (resultado)

#Diferente 
resultado = 5 != 6
print (resultado)



# Programa que verifica se uma pessoa pode votar (idade >= 16) e dirigir (idade >= 18)

idade = 17
pode_votar = idade >= 16 
pode_dirigir = idade >= 18 
print ("Pode votar?", pode_votar)
print ("Pode dirigir?", pode_dirigir)


# Programa que verifica se o nome de usuário é "admin" e a senha é "1234"

usuario = input ("Digite o nome do usuário: ")
senha = input ("Digite a senha: ")

if usuario == "admin" and senha == "1234": 
    print ("Login bem-sucedido!")
else: ("Usuário ou senha incorretos")