def miFuncion(n):
    return len(n)

x = map(miFuncion, ("manzana", "banano", "cereza"))
for i in x:
    print(i)
