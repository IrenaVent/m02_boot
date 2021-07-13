from funciones1nivel import sumaTodos

# lambda x: x**3 es una función anónima

doble = lambda x: x * 2
triple = lambda x: x * 3

print (sumaTodos(3, doble))
print (sumaTodos(100, triple))


