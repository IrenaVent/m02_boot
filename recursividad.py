# contador hacia atras

def contador(e):
    print ("{},".format(e), end="")
    if e > 0:
        contador (e-1)
    
contador (-10)

# la recusividad es que la función se llama a sí misma
# siempre debe de haber una condicón de parada, igual que el while una condición que le haga parar
# es muy elegante pero poco eficiente

def sumatorio(n):
    if n >  0:
        return n + sumatorio(n-1)
    else:
        return 0
        
print (sumatorio (4))

def factorial(n):
    if n != 0:
        return n * factorial(n-1)
    if n == 0:
        return 1
    
print (factorial (5))