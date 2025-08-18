"""
Para cada uno de los siguientes sistemas dados mas abajo:
    - Discretizar los siguientes sistemas de ecuaciones diferenciales para tE[0,5] usando el algoritmo de Euler con paso h.
    - Escribir un codigo para resolver numericamente el sistema discretizado.
    - Simular el sistema con paso h = 0.5 seg, h = 0.1 seg, h = 0.005 seg para aproximar la solucion del sistema de ecuaciones diferenciales en el t0 dado.
    - Hacer un cuadro con los resultados obtenidos para los distintos valores de h. 
"""

import os #Libreria necesaria para limpiar la pantalla
os.system("cls") #Esto es para que cuando corro el codigo se me borre lo anterior
import matplotlib.pyplot as plt #Libreria necesaria para graficar
import numpy as np #Libreria necesaria para trabajar con vectores

# ----------------------------------------------------- METODOS DE EULER PARA DISTINTOS CASOS -----------------------------------------------------
def euler(f, yo, to, tf, h): 
    t = np.arange(to, tf + h, h)
    y = np.zeros(len(t)) # Array de 0 de longitud t para rellenar paso a paso con los valores
    y[0] = yo

    for i in range (len(t)-1): # Pongo el menos 1 porque el "y" empieza en cero
        y[i+1] = y[i] + h * f(t[i], y[i])

    return t, y

def eulerGeneral(f, y0, t0, tf, h): # Metodo de Euler para sistemas de ecuaciones diferenciales, se usa para matrices de funciones 
    # y0 es el valor inicial
    # t0 el valor de tiempo inicial
    # h es el paso
    # tf el tiempo final
    t = np.arange(t0, tf + h, h) # Creo un vector de tiempo desde t0 hasta tf con paso h
    y = np.zeros((len(t), len(y0))) # Creo una matriz de ceros con el mismo numero de filas que t y columnas que y0
    y[0] = y0

    for i in range(len(t)-1): # Recorro el vector de tiempo
        y[i+1] = y[i] + h * f(t[i], y[i]) # Actualizo la matriz y usando el metodo de Euler

    return t, y

def eulerMatricial(M, y0, t0, tf, h): # Metodo de Euler para matriz de funciones de la forma dx = M * x
    # y0 es la matriz inicial
    # t0 el valor de tiempo inicial
    # h es el paso
    # tf el tiempo final

    t = np.arange(t0, tf + h, h) # Creo un vector de tiempo desde t0 hasta tf con paso h
    Y = np.zeros((len(t), len(y0))) # Creo una matriz de ceros con el mismo numero de filas que t y columnas que y0
    Y[0] = y0 # Asigno el valor inicial a la primera fila

    for i in range(len(t)-1): # Recorro el vector de tiempo
        Y[i+1] = Y[i] + h * (M @ Y[i]) # Actualizo la matriz y usando el metodo de Euler
        # : elige toda la fila
        # @ es el operador de producto matricial

    return t, Y
    
""" 
Puedo definir una funcion para graficar los resultados obtenidos por el metodo de Euler
Esta funcion recibe dos parametros: t y y
t es el vector de tiempo
y es el vector de resultados

def grafico(t, y):
    # Esta funcion grafica los resultados obtenidos por el metodo de Euler
    # t es el vector de tiempo
    # y es el vector de resultados

    plt.figure(1) #Genero otra ventana


    plt.plot(t,y,label='Funcion', linestyle='-',color='r') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
    plt.plot(t,y,label='Puntos',linestyle='',marker='o',color='y') #Genero un grafico llamado 'Puntos', sin linea de color amarillo
    plt.grid(True,linestyle='-') #Genero una grilla de linea 'punteada', tambien se le puede agregar color
    plt.title('Metodo de Euler') #Titulo del grafico
    plt.xlabel('y') #Titulo del eje
    plt.ylabel('t [s]') #Titulo del eje 
    plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')

    plt.tight_layout() #Ajusta las posiciones de los subplots para que no se superpongan
    plt.show() #Muestra los graficos

    return t, y

"""


# ----------------------------------------------------- ITEM A ----------------------------------------------------- 

def fa(t, x):
    # Defino la funcion del sistema de ecuaciones diferenciales
    return np.sqrt(x)

ta1, fa1 = euler(fa, 2, 2, 5, 0.5)
ta2, fa2 = euler(fa, 2, 2, 5, 0.1)
ta3, fa3 = euler(fa, 2, 2, 5, 0.05)

"""
grafico(ta1, fa1)
grafico(ta2, fa2)
grafico(ta3, fa3) 
"""

plt.figure(figsize = (8,6)) #Genero otra ventana

# h = 0.5
plt.subplot(2,2,1)
plt.plot(ta1,fa1,label='Funcion', linestyle='-',color='r') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
plt.plot(ta1,fa1,label='Puntos',linestyle='',marker='o',color='grey') #Genero un grafico llamado 'Puntos', sin linea de color amarillo
plt.grid(True,linestyle='-') #Genero una grilla de linea 'punteada', tambien se le puede agregar color
plt.title('Item "a" con h = 0.5') #Titulo del grafico
plt.ylabel('Y') #Titulo del eje
plt.xlabel('t [s]') #Titulo del eje 
plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')

# h = 0.1
plt.subplot(2,2,2) # (2,2) es la posicion del segundo grafico
plt.plot(ta2,fa2,label='Funcion', linestyle='-',color='r') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
plt.plot(ta2,fa2,label='Puntos',linestyle='',marker='o',color='grey') #Genero un grafico llamado 'Puntos', sin linea de color amarillo
plt.grid(True,linestyle='-') #Genero una grilla de linea 'punteada', tambien se le puede agregar color
plt.title('Item "a" con h = 0.1') #Titulo del grafico
plt.ylabel('Y') #Titulo del eje
plt.xlabel('t [s]') #Titulo del eje 
plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')

# h = 0.005
plt.subplot(2,1,2) # Ocupa toda la fila
plt.plot(ta3,fa3,label='Funcion', linestyle='-',color='r') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
plt.plot(ta3,fa3,label='Puntos',linestyle='',marker='o',color='grey') #Genero un grafico llamado 'Puntos', sin linea de color amarillo
plt.grid(True,linestyle='-') #Genero una grilla de linea 'punteada', tambien se le puede agregar color
plt.title('Item "a" con h = 0.005') #Titulo del grafico
plt.ylabel('Y') #Titulo del eje
plt.xlabel('t [s]') #Titulo del eje 
plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')

plt.tight_layout() #Ajusta las posiciones de los subplots para que no se superpongan
plt.show() #Muestra los graficos



# ----------------------------------------------------- ITEM B -----------------------------------------------------
def fb(t, X): # Pongo la X mayuscula porque es una matriz
    # Defino la funcion del sistema de ecuaciones diferenciales
    # X es una matriz de 2x1
    # X[0] es la primera variable --> X[0] = x  
    # X[1] es la segunda variable --> X[1] = y
    x, y = X   
    return np.array([y, x-y])

tb1, yb1 = eulerGeneral(fb, np.array([1, 0]), 1, 5, 0.5)
tb2, yb2 = eulerGeneral(fb, np.array([1, 0]), 1, 5, 0.1)
tb3, yb3 = eulerGeneral(fb, np.array([1, 0]), 1, 5, 0.005)

"""
grafico(tb1, yb1)
grafico(tb2, yb2)
grafico(tb3, yb3)
"""

plt.figure(figsize = (8,6)) #Genero otra ventana

# h = 0.5
plt.subplot(2,2,1)
plt.plot(tb1,yb1[:,0],label='Funcion', linestyle='-') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
plt.plot(tb1,yb1[:,1],label='Puntos',linestyle='',marker='o',color='grey') #Genero un grafico llamado 'Puntos', sin linea de color amarillo
plt.grid(True,linestyle='-') #Genero una grilla de linea 'punteada', tambien se le puede agregar color
plt.title('Item "b" con h = 0.5') #Titulo del grafico
plt.ylabel('Y') #Titulo del eje
plt.xlabel('t [s]') #Titulo del eje 
plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')

# h = 0.1
plt.subplot(2,2,2) # (2,2) es la posicion del segundo grafico
plt.plot(tb2,yb2[:,0],label='Funcion', linestyle='-') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
plt.plot(tb2,yb2[:,1],label='Puntos',linestyle='',marker='o',color='grey') #Genero un grafico llamado 'Puntos', sin linea de color amarillo
plt.grid(True,linestyle='-') #Genero una grilla de linea 'punteada', tambien se le puede agregar color
plt.title('Item "b" con h = 0.1') #Titulo del grafico
plt.ylabel('Y') #Titulo del eje
plt.xlabel('t [s]') #Titulo del eje 
plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')

# h = 0.005
plt.subplot(2,1,2) # Ocupa toda la fila
plt.plot(tb3,yb3[:,0],label='Funcion', linestyle='-') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
plt.plot(tb3,yb3[:,1],label='Puntos',linestyle='',marker='o',color='grey') #Genero un grafico llamado 'Puntos', sin linea de color amarillo
plt.grid(True,linestyle='-') #Genero una grilla de linea 'punteada', tambien se le puede agregar color
plt.title('Item "b" con h = 0.005') #Titulo del grafico
plt.ylabel('Y') #Titulo del eje
plt.xlabel('t [s]') #Titulo del eje 
plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')

plt.tight_layout() #Ajusta las posiciones de los subplots para que no se superpongan
plt.show() #Muestra los graficos



# ----------------------------------------------------- ITEM C -----------------------------------------------------
def fc(t, X):
    # Defino la funcion del sistema de ecuaciones diferenciales
    x1, x2 = X
    dx1 = x2
    dx2 = np.cos(10 * np.pi * x1)

    return np.array([dx1, dx2])

tc1, Yc1 = eulerGeneral(fc, np.array([0, 1]), 0, 5, 0.5)
tc2, Yc2 = eulerGeneral(fc, np.array([0, 1]), 0, 5, 0.1)
tc3, Yc3 = eulerGeneral(fc, np.array([0, 1]), 0, 5, 0.005)

"""
grafico(tc1, Yc1[:, 0])  # Graficar x1
grafico(tc2, Yc2[:, 0])
grafico(tc3, Yc3[:, 0])
"""

plt.figure(figsize = (8,6)) #Genero otra ventana

# h = 0.5
plt.subplot(2,2,1)
plt.plot(tc1,Yc1[:, 0],label='Funcion', linestyle='-',color='green') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
plt.plot(tc1,Yc1[:, 0],label='Puntos',linestyle='',marker='o',color='grey') #Genero un grafico llamado 'Puntos', sin linea de color amarillo
plt.grid(True,linestyle='-') #Genero una grilla de linea 'punteada', tambien se le puede agregar color
plt.title('Item "c" con h = 0.5') #Titulo del grafico
plt.ylabel('Y') #Titulo del eje
plt.xlabel('t [s]') #Titulo del eje 
plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')

# h = 0.1
plt.subplot(2,2,2) # (2,2) es la posicion del segundo grafico
plt.plot(tc2,Yc2[:, 0],label='Funcion', linestyle='-',color='green') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
plt.plot(tc2,Yc2[:, 0],label='Puntos',linestyle='',marker='o',color='grey') #Genero un grafico llamado 'Puntos', sin linea de color amarillo
plt.grid(True,linestyle='-') #Genero una grilla de linea 'punteada', tambien se le puede agregar color
plt.title('Item "c" con h = 0.1') #Titulo del grafico
plt.ylabel('Y') #Titulo del eje
plt.xlabel('t [s]') #Titulo del eje 
plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')

# h = 0.005
plt.subplot(2,1,2) # Ocupa toda la fila
plt.plot(tc3,Yc3[:, 0],label='Funcion', linestyle='-',color='green') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
plt.plot(tc3,Yc3[:, 0],label='Puntos',linestyle='',marker='o',color='grey') #Genero un grafico llamado 'Puntos', sin linea de color amarillo
plt.grid(True,linestyle='-') #Genero una grilla de linea 'punteada', tambien se le puede agregar color
plt.title('Item "c" con h = 0.005') #Titulo del grafico
plt.ylabel('Y') #Titulo del eje
plt.xlabel('t [s]') #Titulo del eje 
plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')

plt.tight_layout() #Ajusta las posiciones de los subplots para que no se superpongan
plt.show() #Muestra los graficos

# ----------------------------------------------------- ITEM D -----------------------------------------------------
matrizD = np. array([ # Crear una matriz de 3x3 con valores específicos
    [0, 1, 0], # x1 = x2
    [0, 0, 1], # x2 = x3
    [-2, -3, -4]]) # x3 = -2 * x1 - 3 * x2 - 4

y0 = [2, 1, 0]  # Condiciones iniciales

td1, yd1 = eulerMatricial(matrizD, y0, 1, 5, 0.5)
td2, yd2 = eulerMatricial(matrizD, y0, 1, 5, 0.1)
td3, yd3 = eulerMatricial(matrizD, y0, 1, 5, 0.05)

"""
grafico(td1, yd1[:, 0])  # Graficar x1
grafico(td2, yd2[:, 0])
grafico(td3, yd3[:, 0])
"""

plt.figure(figsize = (8,6)) #Genero otra ventana

# h = 0.5
plt.subplot(2,2,1)
plt.plot(td1,yd1[:, 0],label='Funcion', linestyle='-',color='purple') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
plt.plot(td1,yd1[:, 0],label='Puntos',linestyle='',marker='o',color='grey') 
plt.grid(True,linestyle='-') #Genero una grilla de linea 'punteada', tambien se le puede agregar color
plt.title('Item "d" con h = 0.5') #Titulo del grafico
plt.ylabel('y') #Titulo del eje
plt.xlabel('t [s]') #Titulo del eje 
plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')

# h = 0.1
plt.subplot(2,2,2)
plt.plot(td2,yd2[:, 0],label='Funcion', linestyle='-',color='purple') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
plt.plot(td2,yd2[:, 0],label='Puntos',linestyle='',marker='o',color='grey') 
plt.grid(True,linestyle='-') #Genero una grilla de linea 'punteada', tambien se le puede agregar color
plt.title('Item "d" con h = 0.1') #Titulo del grafico
plt.ylabel('y') #Titulo del eje
plt.xlabel('t [s]') #Titulo del eje 
plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')

# h = 0.005
plt.subplot(2,1,2)
plt.plot(td3,yd3[:, 0],label='Funcion', linestyle='-',color='purple') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
plt.plot(td3,yd3[:, 0],label='Puntos',linestyle='',marker='o',color='grey') 
plt.grid(True,linestyle='-') #Genero una grilla de linea 'punteada', tambien se le puede agregar color
plt.title('Item "d" con h = 0.005') #Titulo del grafico
plt.ylabel('y') #Titulo del eje
plt.xlabel('t [s]') #Titulo del eje 
plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')

plt.tight_layout() #Ajusta las posiciones de los subplots para que no se superpongan
plt.show() #Muestra los graficos

""" 
Observando los graficos realizados, 
se puede ver que a medida que disminuye el paso h, 
el grafico es mas preciso y se asemeja mas a la solucion exacta del sistema de ecuaciones diferenciales.
"""