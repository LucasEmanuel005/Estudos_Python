#3. Construir um programa para identificar quantos dias há em um mês, sabendo o mês e o ano.

#Coleta de informação (ano)
ano_dig= input("Digite o ano")

#Coleta de informação (mes)
mes_dig = input("Digite o mes") 

#vetor que contem meses com trinta dias 
trinta = ["abril", "4", "junho", "6", "setembro", "9", "novembro", "11"]
#vetor que contem meses com trinta e um dias
trinta_um = ["janeiro","1", "março", "3", "maio", "5", "julho", "7", "agosto", "8", "outubro", "10", "dezembro", "12"] 
#vetor que contem mes com vinte nove e vinte oito dias
vint = ["fevereiro","2"] 
  

#Verificacao 1 - Se o ano é divisivel por 4
v1 = int(ano_dig)%4

#Verificacao 2 - Se o algarismo da dezena e unidade sao 0
for i in range (0,len(ano_dig)):
    dig_d = ano_dig[i-1]
    dig_u = ano_dig[i]
    
if dig_d == "0" and dig_u == "0":
    v2 = 1
else:
    v2 = 0
    
#Verificacao 3 - Se o ano é divisivel por 400 para anos com algarismo da dezena e unidade valendo 0
v3 = int(ano_dig)%400


#Verificacao para anos divisiveis por 4 e algarismos das dezenas e unidades iguais a 0
if (v1 == 0 and v2 == 1 ):
    if(v2 == 1 and v3 == 0):        
        v4=1
    else:        
        v4=0

#Verificacao para anos divisiveis por 4 e algarismos das dezenas e unidades diferente de 0    
elif (v1 == 0 and v2 == 0):    
    v4=1

#Verificacao para anos nao divisiveis por 4
else:    
    v4=0


#Classificando meses com seus respectivos dias 
if(v4 == 1):
    if mes_dig in trinta: 
        print("Mês digitado " , mes_dig , "contém 30 dias no ano de ", ano_dig) 
    elif mes_dig in trinta_um: 
	    print("Mês digitado " , mes_dig , "contém 31 dias no ano de ", ano_dig)        
    elif mes_dig in vint: 
        print("Mês digitado " , mes_dig , "contém 29 dias no ano de ", ano_dig)   
    else:
        print("Mês invalido") 
else:
    print("Não Bissexto") 
    if mes_dig in trinta: 
        print("Mês digitado " , mes_dig , "contém 30 dias no ano de ", ano_dig) 
    elif mes_dig in trinta_um: 
        print("Mês digitado " , mes_dig , "contém 31 dias no ano de ", ano_dig)        
    elif mes_dig in vint: 
        print("Mês digitado " , mes_dig , "contém 28 dias no ano de ", ano_dig)    
    else:
        print("Mês invalido") 
    
    