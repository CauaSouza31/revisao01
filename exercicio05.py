peso=float(input("Informe seu peso: "))
alt=float(input("Informe sua altura: "))

imc= peso/(alt**2)
if imc<18.6:
    print("abaixo do peso")
elif imc>=18.6 and imc <=24.9:
    print("peso ideal")
elif imc>=25.0 and imc <=29.9:
    print("Levemente acima do peso")
elif imc>=30.0 and imc <=34.9:
    print("Obsidade grau I")
elif imc>=35.0 and imc <=39.9:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")
