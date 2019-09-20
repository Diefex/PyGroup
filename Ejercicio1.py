name = input("Cual es tu primer nombre?")
name += " " + input("Cual es tu segundo nombre?")
name += " " + input("Cual es tu primer apellido?")
name += " " + input("Cual es tu segundo apellido?")

year = input("En que año naciste?")

print("Hola " + name)
print("Probablemente tienes " + str(2019-int(year)) + " años")