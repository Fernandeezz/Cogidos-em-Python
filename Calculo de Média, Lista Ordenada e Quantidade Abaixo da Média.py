// Implemente um programa em Python que leia varios números inteiros positivos
guardando em uma lista ate que p usuario digite uma informação para finalizar a 
digitação.A forma de controle de fim de digitação fica a seu criterio. 
Informe ao final: 
  a) A Lista criada em ordem crescente;
  b) A Média;
  c) Quantos números digitados estão abaixo daa média dos números digitados.
//

Lista = []
item = 0 
Soma = 0 
Conta_Menor = 0 
Media = 0.00 

while 1==1:
    item= str(input("Digite um número menor igual a zero ou -1 para sair: "))
    if item == "-1": 
        break 
    elif not item.isnumeric():
        print ("Por favor, digite um valor válido: ")
    else: 
        item = int(item)
        Lista.append(item)
        Soma += item
if len(Lista) > 0:
    Media = Soma/len(Lista)
for i in Lista: 
    if i < Media : 
        Conta_Menor += 1 
print ("A Lista Ordenada: ", sorted(Lista))
print ("Média= ", Media)
print ("Quantidade abaixo da média= ",Conta_Menor)
