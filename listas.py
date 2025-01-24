"""
frutas = ["Fresa","Papaya","Manzana","Pera","Papaya"]
valoresDeVerdad = [True, True, False, True]
edades = [52,63,98,15]
evaluaciones = [3.5,9.3,2.8]
ensayis = ["Carlos",[1,6,8],52,True]
print(frutas[5])
# ordenadas, mutables, permiten duplicados
print(len(frutas)) #abreviatura de lenght-longitud
print(type(frutas))

nombre = "Carlos"
print(type(nombre))


frutas = ["manzana","papaya","pera","piña","guanabana"]

#print(frutas[1:3])


print("manzana" in frutas)


frutas = ["manzana","papaya","pera","piña","guanabana"]
frutas.append("naranja")
print(frutas)
#frutas.clear()
#print(frutas)
frutas2 = frutas.copy()
frutas2.append("mandarina")
print(frutas2)
print(frutas)

frutas = ["manzana","papaya","pera","piña","guanabana"]
frutasotro = frutas
frutasotro.append("fresa")
print(frutasotro)
print(frutas)
print(frutas.index("papaya"))
frutas.insert(1,"guayaba")
print(frutas)
print(frutas.count("papaya"))

frutas = ["manzana","papaya","pera","piña","papaya","guanabana"]
frutasmalucas = ["chontaduro","marañon"]

frutas.insert(1,frutasmalucas)
print(frutas[1][1])

frutas = ["manzana","papaya","pera","piña","papaya","guanabana"]
frutas[1] = "toronja"
print(frutas)

frutas = ["manzana","papaya","pera","piña","papaya","guanabana"]
frutas.pop(1)
print(frutas)

frutas = ["manzana","papaya","pera","piña","papaya","guanabana"]


frutas.pop(2)
print(frutas)
frutas.reverse()
print(frutas)
frutas.sort()
print(frutas)
frutas.remove("papaya")
print(frutas)
"""