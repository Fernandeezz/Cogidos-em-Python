a = float(input("Coeficiente a "))
b = float(input("Coeficiente b "))
c = float(input("Coeficiente c "))
if a !=0:
    d=b*b-4*a*c 
    print("Delta = %f" % d)
    if d < 0:
        print ("Impossivel calcular - N~so possui raiz exata")
    else:
        x1 = (-b+d**0.5)/(2*a)
        print("R1 = %.5f" % x1)
        if d> 0:
            x2=(-b-d**0.5)/(2*a)
        else:
            print("Possui sd taizes são iguais")
else:
    print("Impossivel calcular")
