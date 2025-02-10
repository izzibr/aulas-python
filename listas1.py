animais = ["cachorro", "gato", "elefante"]
print (type(animais))

print (animais [0]) #acessar elementos da lista
                    #retorna "cachorro" 

#somar elementos 
mais_animais = ["girafa", "pato", "macaco"]
nova_lista = animais + mais_animais
print (nova_lista)

#verififcar se tem na lista
print ("pato" in nova_lista)

#pode criar listas com string, inteiro, float
diversas = ["Texto", 3, 3.4]
print (diversas)

valores = [10,20,30,40]
print (min(valores))
print (max(valores))
print (sum(valores))


#substituir o segundo elemento por "amarelo".
cores = ["vermelho", "verde", "azul"]
cores [1] = "amarelo"
print (cores)