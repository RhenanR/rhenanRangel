nume=int(input("qual o numero? "))
if(nume%3==0 and nume>0):
    print("este número é possitivo e multiplo de três.")
elif(nume>0 and nume%2==0):
    print("este número é possitivo e par.")
elif (nume<0 and not nume%2==0):
    print("este número é negativo e ímpar.")
elif(nume==0):
    print ("este é o número zero.")
else:
    print("este número não é nenhuma das possibilidades.")