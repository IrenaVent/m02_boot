# CLASE es el bloque de código define las características de un objeto determinado
            # la calse o el bloque de código está compuesto por:
            # funciones - a las que llamamos MËTODOS - los métodos fijan el corportamiento del objeto
            # variables - a las que llamamos ATRIBUTOS - los atributos fijan el estado
            # INSTANCIAS - son copias con unas determinadas características
            
class Perro(): #creamos un construcctor en vacío solo con la instancia, e indicamos los atributos y los indicamos después
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None

    def ladrar(self):
        if peso == None:
            print ("Soy un fantasma")
        if self.peso > 5:
            print ("GUAU, GUAU")
        else:
            print ("guau, guau")

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

class Assistancedog(Dog): #definimos de que clase herada los atributos
    def __init__(self, nombre, edad, peso, amo):
        Dog.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False #esto es un atributo provado
        
    def __str__(self):
        return "Perro de asistencia {}".format(self.amo) # sobreescribimos un método, si no estña, buscará en el padre, abuelo, etc. donde esta y la ejecutará
    
    def pasear(self):
        print ("{} ayuda a su dueño, {} a pasear".format(self.nombre, self.amo))
        
    def ladrar(self):
        if self.__trabajando: #esto simula un método provado
            print ("shhhhh, no puedo ladrar")
        else:
            Dog.ladrar(self) # incovamos el método padre
            
    def trbajando (self, valor=None): #creamos un método para consultar o modificar el estado trabajando
        is valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor
            
        # Fly.trabajando() - Getter / método getter
        # Fly.trabajando(True) - Setter / método setter

def ladrar(): 
    print ("No tengo perro")
 