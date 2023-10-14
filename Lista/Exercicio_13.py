#13Ler um número inteiro N e calcular e imprimir todos os seus divisores. Exemplo: para o número 6, temos os 
#seguintes divisores 1, 2, 3, 6. Utilize o laço que lhe for mais conveniente. 

#Apresentação do programa
print("Programa que informa os divisores do número digitado. ")  

  
#Coleta de informação (dividendo)
n=int(input("Digite um número"))

#Atribuindo o primeiro divisor
c=1 

  
#Vetor que armazenará os divisores
vet = [] 

  
#loop até que divisor seja igual ao dividendo
while(c<=n): 
    # Validação se é dividor ou nao.
    if(n%c == 0):     
        #Armazenando o divisor no vetor.
        vet.append(c)      
    #Incrementação do divisor
    c+=1 

     
#Imprimindo os divisores.
print("Os divisores de ", n , " são ", vet) 

 
