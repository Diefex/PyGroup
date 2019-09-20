m = input("ingresa un numero ")
n = input("ingresa otro numero ")
if (int(m) < int(n)):
    print(n + " es mayor que " + m)
elif (int(n) < int(m)):
    print(m + " es mayor que " + n)
else:
    print("ambos numeros son iguales")