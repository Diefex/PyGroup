def is_even (k):
    if (k % 2):
        return False
    else:
        return True

if(is_even(int(input("ingresa un numero ")))):
    print("este es un numero par")
else:
    print("este es un numero impar")