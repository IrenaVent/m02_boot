from functools import reduce

def doble(x):
    return x + x

lista = [1, 3, -1, 15, 9]

listaDobles = map(lambda x: x*2, lista)
print (list(listaDobles))

# map a cada elemento de la lista se le aplica una transformación, actua sobre cada uno de ellos
#"lambda x: x*2" = qué es lo que queremos que haga con cada valor de la lista
# "lista" = dónde o con qué lista queremos que lo haga

# ejemplo con una función declarada
listaDobles = map(doble,lista)
print (list(listaDobles))


listaPares = filter(lambda x: x % 2 == 0, lista)
print (list(listaPares))

# "filter" va a filtrar los valores de la lista que cumplen la sigueinte condición:
#"lambda x: x % 2 == 0" = la condición a cumplir para que lo saque en en "list"
# compara , esto es, la función debe devolver True o False 

sumaTodos = reduce (lambda x, y: x + y, lista)
print (sumaTodos)

suma100 = reduce (lambda x,y: x + y, range(101))
print (suma100)
