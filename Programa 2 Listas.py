// Implemente um programa que leia vários números inteiros positivos guardando-os
em duas listas, uma pra pares e putra pra impares. Interrompa a entrada dos números
assim que o usuário digite uma informação para finalizar a digitação fica a seu critério.//

Lista=[[],[]]
Item = 0
SomaPar = 0
SomaImpar = 0
Conta_Meior_Par = 0
Conta_Meior_Impar= 0
MediaPar= 0.00 
MediaImpar = 0.00 

while 1==1: 
    Item = input("Digite -1 para encerrar o programa \n Entre com um valor: ")
    if Item == "-1" : 
        break 
    elif not Item.isnumeric():
        print ("Por Favor, digite um valor válido: ")
    else:
        Item = int(Item)
        if Item % 2 == 0: 
            Lista[0].append(Item)
            SomaPar += Item
        else: 
            Lista[1].append(Item)
            SomaImpar += Item
        
if len(Lista[0]) > 0: 
    MediaPar = SomaPar/len(Lista[0])
if len(Lista[1]) > 0: 
    MediaImpar = SomaImpar/len(Lista[1]) 
for i in Lista[0]:
    if i > MediaPar: 
        Conta_Meior_Par += 1 
for i in Lista[1]: 
    if i > MediaImpar: 
        Conta_Meior_Impar += 1 
print ("Os valores pares digitados foram:", sorted (Lista[0], reverse = True))
print ("Os valores impares digitados foram:", sorted (Lista[1], reverse = True))
print ("A Media Par é: ", MediaPar)
print ("A Media Impar é: ", MediaImpar)
print ("A quantidade acima da média Par é: ", Conta_Meior_Par)
print ("A quantidade acima da media Impar é: ", Conta_Meior_Impar)
