import turtle

tortuguita = turtle.Turtle() #creamos un objeto del módulo turtle, los objetos la clase siempre va en mayúscula
otraTortuguita = turtle.Turtle()
#los Objetos son funciones de 1er nivel:
        #capaces de invocarse a sí mismas
        #y hacer copias de si misma
        #encapsular también propiedades (por ejemplo en un juego diferentes jugadores)
        #.Turtle - pueden tener diferentes atributos, diferentes instancias
        # CLASE es el bloque de código define las características de un objeto determinado
            # la calse o el bloque de código está compuesto por:
            # funciones - a las que llamamos MËTODOS
            # variables - a las que llamamos ATRIBUTOS

tortuguita.shape("turtle")
tortuguita.fd(50)

otraTortuguita.color("blue") # color es una función a la que llamamos método
otraTortuguita.left(90)
otraTortuguita.fd(50)