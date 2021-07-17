# CLASE es el bloque de código define las características de un objeto determinado
            # la calse o el bloque de código está compuesto por:
            # funciones - a las que llamamos MËTODOS - los métodos fijan el corportamiento del objeto
            # variables - a las que llamamos ATRIBUTOS - los atributos fijan el estado
            # INSTANCIAS - son copias con unas determinadas características
            
class Dog(): #declaramos la clase siempre en MAYÜSCULAS
    def __init__(self, n, e, p):#esto siempre debemos incluirlo porque es la función constructora, para crear la instancias, de eso se encarga esta función
        self.nombre = n   #self = clase vacia, para instanciar la clase, es decir, crear las diferentes instaccias
        self.edad = e
        self.peso = p
        
    def ladrar(self): #por conveviencia se pone self, pero podríamos poner cualquier cosa
        if self.peso > 5:
            print ("GUAU, GUAU")
        else:
            print ("guau, guau")
    
    def __str__(self):
        return "Perro {}, e: {} años, p: {} kg".format(self.nombre, self.edad, self.peso) #para que nos devuelva los datos

def ladrar():
    print ("No tengo perro")
 

