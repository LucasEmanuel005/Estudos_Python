#12. Faça um programa que leia um número natural N e calcule a soma abaixo (lembre-se de que tanto as divisões 
#quanto o resultado devem ser decimais). Utilize o laço que lhe for mais conveniente.
# S = 1 - 1/2 + 1/3 - 1/4 + 1/5 - ... + 1/N

#Apresentação do programa
print("Programa para resolver a expressão: S = 1 - 1/2 + 1/3 - 1/4 + 1/5 - ... + 1/N ")
  
#Iniciando a variavel que armazenara a resposta.
resp=0 
#Iniciando o contador.
c=1 
#Coletando o 'n'
n=int(input("Digite um número")) 

#Loop 
while(c<=n): 
    #Validação se será uma soma ou um subtração.
    if(c%2 == 0): 
        resp = resp - (1/c)
    else: 
        resp= resp + (1/c) 
    #Incrementando no contador.
    c+=1
    
#Mostrando o resultado de S
print("S = ", resp) 
