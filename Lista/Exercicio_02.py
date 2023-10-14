#2. Criar um programa para identificar se um dia da semana (numerados de 1 a 7) é dia de semana, fim de semana 
#ou um dia inválido.

#Vetor com os dias da semana.
dia = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'] 

  
#Coleta de informação (numero)
n_dig = int(input("Digite um número entre 1 e 7 para verificar se é um dia da semana:")) 

  
#Ajustando para o mesmo intervalo do indice do vetor
n_dia = n_dig - 1 

  

  
#Verificando dias da semana
if(n_dig >= 1 and n_dig <= 5): 
    print("O número digitado foi ", n_dig, "o dia da semana é ", dia[n_dia]) 

#Verificando finais de semana
elif (n_dig == 6 or n_dig == 7): 

    print("O número digitado foi ", n_dig, "o dia do final de semana é ", dia[n_dia]) 

#Para numeros fora do intervalo
else: 

    print("Invalido") 