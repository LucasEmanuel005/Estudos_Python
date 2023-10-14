#14. Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de senha 
#incorreta informada, escrever a mensagem "Senha Invalida". Quando a senha for informada corretamente deve 
#ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha correta é o valor 
#2002. Utilize o laço que lhe for mais conveniente. 

  

#Apresentação do programa
print("Programa validador de acesso. ")

#Coleta de informação (senha)
p=int(input("Digite a senha "))  
  
#Loop equanto a senha estiver errada.
while(2002!=p): 
    #Informando que a senha está errada
    print("Senha Invalida") 
    #Coleta de informação (senha)
    p=int(input("Digite a senha "))  

     
#Informando que o acesso foi liberado.
print("Acesso Permitido") 
