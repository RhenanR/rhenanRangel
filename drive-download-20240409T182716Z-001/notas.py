nt=float(input("qual a sua nota? "))
if(nt>8.9):
    print("nota A")
elif((nt<9)and(nt>7.4)):
    print("nota B")
elif((nt<7.5)and(nt>5.9)):
    print("nota C")
elif((nt<6)and(nt>3.9)):
    print("nota D")
elif((nt<4)and(nt>2.9)):
    print("nota E")
else:
    print("nota F")