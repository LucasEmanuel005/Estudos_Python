#11. Faça um programa que calcule e imprima o resultado da soma abaixo (lembre-se de que tanto as divisões  
#quanto o resultado devem ser decimais). Utilize o laço que lhe for mais conveniente.
# S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/20

#Apresentação do programa
print("Programa para resolver a expressão: S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/20 ")
  
#Iniciando a variavel que armazenara a resposta.
resp=1 

#Loop de 1  até 20 (denominador)
for n in range (2,21):
    #Soma
    resp= resp + (1/n) 

#Apresentando o resultado.
print(" S= ",resp) 

 
