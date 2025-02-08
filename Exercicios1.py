#calcule a soma dos números do 10 ao 14

soma = sum ([10,11,12,13,14])
print ("A soma é: ", soma)


#peça pra o usuário digitar duas notas do zero a dez e os pesos das notas
#e calcule a média ponderada entre eles 

nota1 = float(input("Digite a sua primeira nota: "))
peso1 = float(input("Digite o peso da primeira nota: "))

nota2 = float(input("Digite a sua segunda nota: "))
peso2 = float(input("Digite o peso da segunda nota: "))

pesos = peso1 + peso2
media = (nota1 * peso1 + nota2 * peso2) / pesos
print (f'A média final é: {media}')

#Qual o menor preço dessa lista?
#precos: R$100.20, R$34.90, r$31.50, R$18.95

menorPreco = min (100.20,34.90, 31.50, 18.95)
print (menorPreco)
