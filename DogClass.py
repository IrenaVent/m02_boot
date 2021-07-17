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