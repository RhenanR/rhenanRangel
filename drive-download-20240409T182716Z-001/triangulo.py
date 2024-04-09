c1=float(input("qual o primeiro comprimento? "))
c2=float(input("qual o segundo comprimento? "))
c3=float(input("qual o terceiro comprimento? "))
if((c1+c2>c3)and(c1+c3>c2)and(c2+c3>c1)):
    print("é um triangulo")
    if((c1==c2)and(c1==c3)):
        print("triangulo equilatero")
    elif((c1==c2)and(not c1==c3)):
        print("triangulo isosceles")
    elif((c1==c3)and(not c1==c2)):
        print("triangulo isosceles")
    elif((c2==c3)and(not c2==c1)):
        print("triangulo isosceles")
    else:
        print("triangulo escaleno")
else:
    print("não é um triangulo")