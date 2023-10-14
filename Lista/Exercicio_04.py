#4 Faça um programa que mostre todos os números inteiros ÍMPARES de 1 a 50. Use o laço WHILE



#Apresentação do programa
print("Programa para mostrar todos os números inteiros ÍMPARES de 1 a 50.")

#iniciando contador 
n=0 

  
#Loop
while (n<50): 
    #Incrementando contador
    n+=1 
    #Validacao se é impar
    if (n%2 != 0): 
	#Impressao dos impares
        print(n) 
