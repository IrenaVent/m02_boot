lista = [1, 3, -1, 15, 9]

listaDobles = map(lambda x: x*2, lista)
print (list(listaDobles))

# map a cada elemento de la lista se le aplica una transformación, actua sobre cada uno de ellos
#"lambda x: x*2" = qué es lo que queremos que haga con cada valor de la lista
# "lista" = dónde o con qué lista queremos que lo haga

listaPares = filter(lambda x: x % 2 == 0, lista)
print (list(listaPares))

# "filter" va a filtrar los valores de la lista que cumplen la sigueinte condición:
#"lambda x: x % 2 == 0" = la condición a cumplir para que lo saque en en "list"