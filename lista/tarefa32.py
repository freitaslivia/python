# lista com todas as letras da matriz
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']

matriz = []  


for i in range(5):
    linha = []  
   
    for j in range(4):
        letra = letras.pop(0) 
        linha.append(letra)  
    matriz.append(linha)  

print(matriz)  
