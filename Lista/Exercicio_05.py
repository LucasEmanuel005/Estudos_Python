#5. Faça um programa que peça um número inteiro, verifique se é par ou ímpar e mostre a mensagem “O número
#X é par”, quando o número for par ou mostre a mensagem “O número X é ímpar”, quando o número entrado for
#ímpar. O número X mostrado na mensagem é o número que foi entrado. Em seguida o programa pede um novo
#número e repetirá este processo até que se entre o número 0 (zero), quando encerrará o programa. Use o laço WHILE.

  

#Apresentação do programa
print("Programa para identificar se é par ou nao.")

#Coletando o número
num=int(input("Digite um número para saber se é par ou impar ou digite 0 para encerrar:")) 

#Loop
while(num!=0): 
	#Validação se é par
    if(num%2 == 0): 
		#Mostra do resultado, caso par.
        print("O número ", num," é par.") 

    else: 
		#Mostra do resultado, caso impar.
        print("O número ", num," é impar.") 
		
	#Coletando o número
    num=int(input("Digite um número para saber se é par ou impar ou digite 0 para encerrar:")) 
	
	
#Finalizacao do programa
print("Programa encerrado.")