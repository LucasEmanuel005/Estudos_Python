#8 Faça um programa para imprimir os números pares entre 100 e 1, em ordem decrescente, ou seja, o laço deve
#iniciar em 100 e encerrar em 1. Use o laço FOR.


#Apresentação do programa
print("Programa para mostrar os pares de 100 a 1, ordem decrescente. ")

#Loop de 100 a 1 em ordem decrescente.
for n in range (100,1,-1): 
	#Validando se é par ou nao.
    if(n%2 == 0): 
		#imprissão dos pares.
        print (n) 