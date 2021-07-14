import turtle

tortuguita = turtle.Turtle() #creamos un objeto del módulo turtle, los objetos la clase siempre va en mayúscula
otraTortuguita = turtle.Turtle()
#los Objetos son funciones de 1er nivel:
        #capaces de invocarse a sí mismas
        #y hacer copias de si misma
        #encapsular también propiedades (por ejemplo en un juego diferentes jugadores)

tortuguita.shape("turtle")
tortuguita.fd(50)

otraTortuguita.color("blue")
otraTortuguita.left(90)
otraTortuguita.fd(50)