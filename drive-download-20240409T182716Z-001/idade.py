idd=int(input("qual a sua idade?"))
if(idd<13):
    print("você é uma criança")
elif((idd>12) and (idd<18)):
    print("você é um adolecente")
elif((idd>17) and (idd<60)):
    print("você é um adulto")
else:
    print("você é um idoso")