alg=int(input("Informe um valor: "))
if alg % 2 == 0:
    if alg<0:
        print(f"{alg} é par e é positivo")
    else:
        print(f"{alg} é impar e é positivo")
else:
    if alg%2==0:
        print(f"{alg} é par e é neagtivo")
    else:
        print(f"{alg} é impar e é negativo")

