medida=str(input("qual tipo de metida quer que seja convertida? milhas, polegadas, pes, centimetros, metros ou quilometros? "))
valor=float(input("qual o valor da metida? "))
conversao=str(input("para qual você quer converter? milhas, polegadas, pes, centimetros, metros ou quilometros?  "))
if medida=="milhas":
    if conversao=="polegadas":
        valor_convertido=(valor*63360)
        print ("o valor em milhas foi convertido para "valor_convertido" polegadas")
    elif conversao=="pes":
        valor_convertido=(valor*5280)
        print("o valor em milhas foi convertido para "valor_convertido" pes")
    elif conversao=="centimetros":
        valor_convertido=(valor*160900)
        print("o valor em milhas foi convertido para "valor_convertido" centimetros")
    elif conversao=="metros":
        valor_convertido=(valor*1609)
        print("o valor em milhas foi convertido para "valor_convertido" metros")
    elif conversao=="quilometros":
        valor_convertido=(valor*1.609)
        print("o valor em milhas foi convertido para "valor_convertido" quilometros")
    else:
        print("conversão  invalida")
elif medida=="polegadas":
    if conversao=="milhas":
        valor_convertido=(valor/63360)
        print("o valor em polegadas foi convertido para "valor_convertido" milhas")
    elif conversao=="pes":
        valor_convertido=(valor/12)
        print("o valor em polegadas foi convertido para "valor_convertido" pes")
    elif conversao=="centimetros":
        valor_convertido=(valor*2.54)
        print("o valor em polegadas foi convertido para "valor_convertido" centimetros")
    elif conversao=="metros":
        valor_convertido=(valor/39.37)
        print("o valor em polegadas foi convertido para "valor_convertido" metros")
    elif conversao=="quilometros":
        valor_convertido=(valor/39370)
        print("o valor em polegadas foi convertido para "valor_convertido" quilometros")
    else:
        print("conversão  invalida")
elif medida=="pes":
    if conversao=="milhas":
        valor_convertido=(valor/5280)
        print("o valor em pes foi convertido para "valor_convertido" milhas")
    elif conversao=="polegadas":
        valor_convertido=(valor*12)
        print("o valor em pes foi convertido para "valor_convertido" polegadas")
    elif conversao=="centimetros":
        valor_convertido=(valor*30.48)
        print("o valor em pes foi convertido para "valor_convertido" centimetros")
    elif conversao=="metros":
        valor_convertido=(valor/3.281)
        print("o valor em pes foi convertido para "valor_convertido" metros")
    elif conversao=="quilometros":
        valor_convertido=(valor/3281)
        print("o valor em pes foi convertido para "valor_convertido" quilometros")
    else:
        print("conversão  invalida")
elif medida=="centimetros":
    if conversao=="milhas":
        valor_convertido=(valor/160900)
        print("o valor em centimetros foi convertido para "valor_convertido" milhas")
    elif conversao=="polegadas":
        valor_convertido=(valor/2.54)
        print("o valor em centimetros foi convertido para "valor_convertido" polegadas")
    elif conversao=="pes":
        valor_convertido=(valor/30.48)
        print("o valor em centimetros foi convertido para "valor_convertido" pes")
    elif conversao=="metros":
        valor_convertido=(valor/100)
        print("o valor em centimetros foi convertido para "valor_convertido" metros")
    elif conversao=="quilometros":
        valor_convertido=(valor/100000)
        print("o valor em centimetros foi convertido para "valor_convertido" quilometros")
    else:
        print("conversão  invalida")
elif medida=="metros":
    if conversao=="milhas":
        valor_convertido=(valor/1609)
        print("o valor em metros foi convertido para "valor_convertido" milhas")
     elif conversao=="polegadas":
        valor_convertido=(valor*39.37)
        print("o valor em metros foi convertido para "valor_convertido" polegadas")
    elif conversao=="pes":
        valor_convertido=(valor*3.281)
        print("o valor em metros foi convertido para "valor_convertido" pes")
    elif conversao=="centimetros":
        valor_convertido=(valor*100)
        print("o valor em metros foi convertido para "valor_convertido" centimetros")
    elif conversao=="quilometros":
        valor_convertido=(valor/1000)
        print("o valor em metros foi convertido para "valor_convertido" quilometros")
    else:
        print("conversão  invalida")
elif medida=="quilometros":
    if conversao=="milhas":
        valor_convertido=(valor/1.609)
        print("o valor em quilometros foi convertido para "valor_convertido" milhas")
    elif conversao=="polegadas":
        valor_convertido=(valor*39370)
        print("o valor em quilometros foi convertido para "valor_convertido" polegadas")
    elif conversao=="pes":
        valor_convertido=(valor*3281)
        print("o valor em quilometros foi convertido para "valor_convertido" pes")
    elif conversao=="centimetros":
        valor_convertido=(valor*100000)
        print("o valor em quilometros foi convertido para "valor_convertido" centimetros")
    elif conversao=="metros":
        valor_convertido=(valor*1000)
        print("o valor em quilometros foi convertido para "valor_convertido" metros")
    else:
        print("conversão  invalida")
else:
        print("conversão  invalida")