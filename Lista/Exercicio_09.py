 #9 Faça um programa para ler e escrever dados de uma turma de 5 alunos. O programa deve pedir dados como
#nome, idade e sexo. O programa deve imprimir os dados do aluno mais velho. Use o laço WHILE.

#Iniciando variavel que contará maior idade
n=0  

#Vetor para armazenar os nomes
nome = []  
#Vetor para armazenar as idades
idade = []  
#Vetor para armazenar os sexos
sexo = []  

idad=0  

#Loop para iniciar a coleta e a validação dos 5 alunos.
while n<5: 
	#Armazenando nome
    nome.append(input("Digite seu nome: ")) 
	#Armazenando idade
    idade.append(int(input("Digite sua idade: "))) 
	#Armazenando sexo
    sexo.append(input("Digite seu sexo: ")) 

     
	#Validando maior idade
    if (idade[n] > idad):  
        #Adicionando dados do aluno de maior idade em variavel.
        nom = nome[n] 
        idad=idade[n] 
        se = sexo[n]
    elif(idade[n] == idad):
        nom2 = nome[n] 
        idad2 =idade[n] 
        se2 = sexo[n]
        verf=1
        

  
    #incrementando para o proximo aluno
    n+=1  

#Mostrando as informações dos alunos de maior idade
if(verf == 1):
    print("Os alunos de maior idade são o(a)", nom, ", idade ", idad, " e sexo ", se , " e o(a) ", nom2, " idade ", idad2, " e sexo ", se2)
#Mostrando as informações do aluno de maior idade
else:
    print("O aluno(a) de maior idade é o(a)", nom, ", idade ", idad, " e sexo ", se)  
