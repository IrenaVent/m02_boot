def normal (x):
    return x

def cuadrado(x):
    return x * x

def cubo (x):
    return x**3

def sumaTodos(limitTo, f):
    resultado = 0
    for i in range (limitTo+1):
        resultado += f(i)
    
    return (resultado)

if __name__=="__main__":
    #(para que no ejecute el print si es llamado/invocado desde otro programa/otra función
    print (sumaTodos(100,normal))
    print (sumaTodos (3,cuadrado))
else:
    print (__name__)