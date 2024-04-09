n1=float(input("primeiro número?"))
n2=float(input("segundo número?"))
n3=float(input("terceiro número?"))
if((n1>n2)and(n1>n3)):
    print(n1)
elif((n2>n1)and(n2>n3)):
    print(n2)
elif((n3>n1)and(n3>n2)):
    print(n3)
elif((n1==n2)and(n1>n3)):
    print(n2)
elif((n1==n3)and(n1>n2)):
    print(n3)
elif((n2==n3)and(n3>n1)):
    print(n2)
else:
    print("erro")