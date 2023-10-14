# 10. Escreva um programa que imprima todos os múltiplos de 7 menores que 200. Use o laço #WHILE.  

#Apresentação do programa
print("Programa para mostrar os multiplos de 7 menores que 200. ")

#Iniciando o multiplicador
m=1 

#Iniciando a variavel que guardará a resposta
resp=1

#Vetor que armazenará os multiplos
vet = [] 

#loop 
while (resp < 190): 
    #operacao
    resp = m*7
    #adicionando os multiplicadores no vetor
    vet.append(resp)
    #incrementando o multiplicador
    m+=1

#Mostrando o resultado.
print("Os multiplos de 7 menores que 200 são: ", vet) 

     
