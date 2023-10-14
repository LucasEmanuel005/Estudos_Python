#15. Escreva um programa capaz de ler o saldo inicial de uma conta bancária e um número indeterminado de 
#operações de depósito e saque. O usuário deve digitar “1” para realizar um depósito, “2” para realizar um saque e 
#“0” para encerrar o programa apresentando o saldo final e uma mensagem “Programa encerrado”. 

  
#Apresentação do programa
print("Programa bancário para deposito, saque e saldo. ")
  
#Coleta de informação (saldo)
s=float(input("Digite o seu saldo:"))

#Coleta de operação
o=int(input("Digite o numero da operação desejada:  1 -  depósito; 2 - Saque; 3 - Saldo; 0 - Encerrar")) 

#Loop 
while(o!=0):  
    #Validação de operação (deposito)
    if(o==1): 
        m=float(input("Digite o valor do deposito:")) 
        s=s+m
    #Validação de operação (saque)
    elif(o==2): 
        m=float(input("Digite o valor do saque:")) 
        s=s-m
    #Validação de operação (Saldo)
    elif(o==3): 
        print("Saldo R$",s)
    #Validação de operações invalidas
    else: 
        print("Operação invalida!")          
    #Coleta de operação
    o=int(input("Digite o numero da operação desejada:  1 -  depósito; 2 - Saque; 3 - Saldo; 0 - Encerrar")) 

     
#Informando encerramento do programa
print("Programa encerrado! Volte sempre!") 

         
