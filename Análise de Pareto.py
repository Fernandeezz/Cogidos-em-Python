dados = open("entrada.txt", "r") 
L1 = [] #lista bruta 
L2 = [] #Lista rol de dados 
L3 = [] #Lista de número de ocorrencias
L4 = [] #Lista de Frequencia
L5 = [] #Lista final
porcentagem = 0.00
L1=dados.readlines() #Ler as linhas
#Formatando TXT
for i in L1: 
      L2.append(i.rstrip()) 
#Adicionando apenas uma de cada ocorrencia na lista 3
for i in L2: 
      if i not in L3: 
          L3.append(i) 
#Print de "legenda"
print('{:<14} {:>11} {:>9} {:>16}'.format('Ocorrências', 'Nr de Ocorrências', 'FR(%)', 'FR acumulada')) 
#Contando a quantidade de cada ocorrencia
for i in L3: 
      L4.append(L2.count(i)) 
#Somando número de ocorrencia
for i in L4: 
       soma = sum(L4) 
#Juntando a lista L3 e L4 e unificando as ocorrencias com sua quantidade
for i in range (0, len(L3)):  
       L5.append([L4[i], L3[i], (L4[i]/soma*100)]) 
#Colocando do menor para o maior
L5 = sorted(L5)
#Leitura de listas e calulo de porcentagem para print
for i in range(0,len(L4)):
    porcentagem += L5[i][2]
    print(f"{L5[i][1]:>5}{L5[i][0]:>19}{L5[i][2]:>17.2f}%{porcentagem:>13.2f}%")
print('{:>7} {:>16} {:>16}%''{:>13}'.format('Total', soma, porcentagem, '-----'))
#FIM!
