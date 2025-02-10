#Lista built-in 

mercado =["cebola", "alho", "macarrao"]
#acrescenta um elemento no final da lista
mercado.append ("molho")
print (mercado)

#conta quantas vezes um elemento se repete na lista
contagem = mercado.count ("molho")
print (contagem)

#retorna o índice de um elemento 
indice = mercado.index("macarrao")
print (indice)

#inserir um elemento em um índice
mercado.insert (1, "refrigerante")
print (mercado)

#colocar em ordem alfabética ou crescente se for numeros
mercado.sort()
print (mercado)

#colocar em ordem reversa 
mercado.reverse ()
print (mercado)

#strings são imutáveis 
#listas são mutáveis, consegue alterar valores individuais
lista = ["cachorro", "gato"]
lista [0] = "elefante"
print (lista)


