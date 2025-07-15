nombre1 = ""
nombre2 = ""

print ("Entrez deux nombres")
nombre1 = input("Nombre 1 : ")
nombre2 = input("Nombre 2 : ")

if not (nombre1.isnumeric() and nombre2.isnumeric()):
    raise SystemExit("Fin du programme")
else :
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)

operation = input("Entrez l'opération (+, -, *, /) : ")

if operation == "+":
    print(f"{nombre1} + {nombre2} = {nombre1 + nombre2}")
elif operation == "-":
    print(f"{nombre1} - {nombre2} = {nombre1 - nombre2}")
elif operation == "*":
    print(f"{nombre1} * {nombre2} = {nombre1 * nombre2}")
elif operation == "/":
    if nombre2 == 0:
        raise SystemExit("Division par zéro n'est pas autorisée")
    else:
        print(f"{nombre1} / {nombre2} = round.{nombre1 / nombre2}")
else:
    raise SystemExit("Opération non reconnue")