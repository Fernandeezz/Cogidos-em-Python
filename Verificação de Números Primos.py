#pedido de valores das variaveis
n = int (input("Entre com um número de  2 (dois) a 1000 (mil): "))
cont = 0
i = 0 

#while verifica se é o número é menor que dois ou maior que mil (se for ira repetir até que o valor esteja dentro dos criterios)
while n < 2 or n > 1000 : 
    n = int(input("\n Por favor insira outro número entre 32 (dois) e 1000 (mil): "))
#este while verifica e faz os calculos para verificar se o numero é primo
while i <= n or cont < 2:
    i = i + 1 
    resto = n % i 
    if resto == 0 : 
        cont = cont + 1 
#aqui usamos o if para verificar se o numero de vezes que o numero foi dividido e se se adequa aos numeros primos
if cont <= 2 :
    print("Seu número é primo!")
else: 
    print ("Seu número não é primo!")
