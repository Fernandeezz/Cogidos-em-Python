n=1 
while n>=1 and n<=3:
    n=int(input("1 - soma\n2 - subtrair\n3- multiplicar\ n4- sair"))
    if n==1:
        a=int(input("Valor 1? "))
        b=int(input("Valor 2? "))
        res=a+b 
        print("Soma %d" %res) 
    elif n==2:
        a=int(input("Valor 1? "))
        b=int(input("Valor 2? "))
        res=a-b 
        print("Subtração %d" %res) 
    elif n==3:
        a=int(input("Valor 1? "))
        b=int(input("Valor 2? "))
        res=a*b 
        print("Multiplicação %d" %res) 
