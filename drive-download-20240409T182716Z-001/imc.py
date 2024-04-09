a=float(input("qual tua altura? "))
p=float(input("qual teu peso? "))
a4=a**2
r=p/a4
if(r<18.5):
    print("você ta magro")
elif((r>18.6)and(r<25)):
    print("você está saudavel")
elif((r>24.9)and(r<30)):
    print("você está com soprepeso")
elif((r>29.9)and(r<40)):
    print("você é obeso")
else:
    print("você está com obesidade grave")