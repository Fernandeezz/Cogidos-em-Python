n1 = float (input("Digite o primeiro valor: "))
n2 = float (input("Digite o segundo valor: "))
oper = int (input("Digite o numero da sua operação (1 - Soma, 2- Subtração, 3- multiplicação ou 4 - divisão): "))
if oper == 1 :
    result = n1+n2
    print ("O resultado da soma é: ", result)
else : 
    if oper == 2 :
        result = n1-n2
        print ("O resultado da subtração é: ", result)
    else : 
        if oper == 3 :
            result = n1*n2 
            print ("O resultado da multiplicação é: ", result)
        else :
            if oper == 4 :
                if n2 == 0 : 
                    print ("Impossivel dividir o valor por zero.")
                else :
                    result = n1/n2 
                    print ("O resultado da divisão é: ", result)
            else :
                print ("Opção invalida.")
