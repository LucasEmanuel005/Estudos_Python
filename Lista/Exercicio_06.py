#6  Escreva um programa que leia um conjunto de 10 números inteiros positivos. Seu programa deve determinar e
#imprimir o maior deles. Use o laço FOR.

#Apresentação do programa
print("Programa para ler 10 números é mostrar o maior.")


#Iniciando a variavel que conterá o maior valor.
num_a=0 

#Loop para ler 10 números.
for n in range (0,10): 
	#Coletando numero
    num=int(input("Digite um número")) 
	#Validacao do maior numero
    if (num > num_a): 
		#Armazenando maior numero
        num_a = num 
		
#Impressao maior numero.
print ("O maior número digitado foi ", num_a) 
