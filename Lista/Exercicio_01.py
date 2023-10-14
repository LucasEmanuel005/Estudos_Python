#1 Crie um programa que verifica se um número inteiro informado pelo usuário é divisível por 3.

#Apresentação do programa
print("Programa para informar se o numero digitado é divisivel por 3. ")

#Coleta de informação (numero)
n = input("Digite um número: ")   

#Funcao que contar quantos algarismos o número digitado tem
c=len(n)   

#Iniciando variavel que guardará a soma dos algarismos.
con=0  

  
#Loop para percorer e contar os algarismos  
for i in range (0,c):  
    #soma dos algarismos
    con=int(n[i])+con  

#Validação se é divisível por 3
if (con%3 == 0):  
    #Impressao do resultado, caso sim
    print(n, "é divisível por 3.")  
else:  
    #Impressao do resultado, caso nao
    print(n, "não é divisível por 3.")  