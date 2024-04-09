#ano bissexto
ano=int(input("qual ano? "))
if(ano%4==0):
    if(ano%100==0):
        if(ano%400==0):
            print("esse ano ébissexto")
        else:
            ("esse ano não é bissexto")
    else:
        print("esse ano é bissexto")
else:
    print("esse ano não é bissexto")