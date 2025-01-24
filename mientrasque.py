"""
i = 1
while i < 6:
    print("mi mamá me mima")
    i += 2

tabla = int(input("Cual tabla quiere que le muestre: "))
i = 1
while i < 11:
    
    print(i , "X", tabla, "=", i*tabla)
    if i == 6:
        break
    i += 1
print("Aquí ya salió del ciclo")

tabla = int(input("Cual tabla quiere que le muestre: "))
i = 0
while i < 11:
    i += 1   
    
    if i == 6:
        continue
    print(i , "X", tabla, "=", i*tabla)

print("Aquí ya salió del ciclo")

cadena = "3208567456"
for elemento in cadena:
    print(elemento)

cadena = "cosita"
posicion = 0
longitud =  len(cadena)
while posicion <= longitud:
    print(cadena[posicion])
    posicion += 1

for x in range(5):
    print(x+1)
print("Ya acabé")
"""
