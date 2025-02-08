# 2
nota1 = int ((input ("Digite a primeira nota: ")))
nota2 = int ((input ("Digite a segunda nota: ")))

media = (nota1 + nota2) / 2

if media >= 7: 
    print ("Aprovado")
else:
    print ("Reprovado")

# 3 

nota1 = int ((input ("Digite a primeira nota: ")))
nota2 = int ((input ("Digite a segunda nota: ")))

media = (nota1 + nota2) / 2

if media >= 7:
    print ("Aprovado")
elif media >= 5 and media < 7:
    print ("recuperar nota")
else:
    print ("Reprovado")
