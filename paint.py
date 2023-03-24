# Juego de pintar basado en la colección de FreeGames
# donde se hicieron modificaciones para una mejor experiencia
# de juego.
# Autores: Regina Luna, A01655821
#          Diego Samperio, A01662935
#          Abigail Curiel, A01655892
# Fecha: 23/03/2023

# Se importan las librerías que se utilizarán.
from turtle import *
from freegames import vector
import math

# Función que dibuja una línea desde un punto de 
# comienzo hasta un punto de fin.
# Toma como parámetro dos coordenadas de tipo 
# (x, y), una de inicio y otra de fin de la figura.
# No hay valor de retorno.
def line(start, end):
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

# Función que dibuja un cuadrado desde un punto de 
# comienzo hasta un punto de fin.
# Toma como parámetro dos coordenadas de tipo 
# (x, y), una de inicio y otra de fin de la figura.
# No hay valor de retorno.
def square(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

# Función que dibuja un círculo desde un punto de 
# comienzo hasta un punto de fin, el cual será
# el radio del círculo.
# Toma como parámetro dos coordenadas de tipo 
# (x, y), una de inicio y otra de fin de la figura.
# No hay valor de retorno.
def makeCircle(start, end):
    radius = math.sqrt(pow(end.x - start.x, 2)+pow(end.y - start.y, 2))
    up()
    goto(start.x, start.y)
    down()

    begin_fill()
    circle(radius)
    end_fill()

# Función que dibuja un rectángulo desde un punto de 
# comienzo hasta un punto de fin como su diagonal.
# Toma como parámetro dos coordenadas de tipo 
# (x, y), una de inicio y otra de fin de la
# diagonal de la figura.
# No hay valor de retorno.
def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    lado1 = (end.x - start.x)
    lado2 = (end.y - start.y)

    for count in range(2):
        forward(lado1)
        left(90)
        forward(lado2)
        left(90)

    end_fill()

# Función que dibuja un triángulo desde un punto 
# de comienzo hasta un punto de fin que define 
# la base y apotema.
# Toma como parámetro dos coordenadas de tipo 
# (x, y), una de inicio del triángulo y otra que
# define la base y el apotema.
# No hay valor de retorno.
def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    goto(end.x, start.y)
    goto(start.x + (end.x - start.x)/2, end.y)
    end_fill()

# Función que almacena un punto de inicio
# o una forma de dibujo.
# Toma como parámetro una coordenada de tipo 
# (x, y).
# No hay valor de retorno.
def tap(x, y):
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

# Función que almacena un valor en un estado
# de una llave/tecla particular.
# Toma como parámetro un valor y la llave/tecla
# en la que se guardará.
# No hay valor de retorno.
def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()

# Se deshace una acción.
onkey(undo, 'u')

# Se agrega la posibilidad de usar distintos
# colores para dibujar las formas de acuerdo
# con una llave/tecla particular.
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
# Se agregó el color amaillo
onkey(lambda: color('yellow'),'Y')

# Se dibujan las distintas formas de acuerdo
# con una llave/tecla particular.
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', makeCircle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()