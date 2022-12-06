
"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
"""Bucle while"""
"""
q = 1 
while q <= 10:
    print("Ejecucion "+str(q))
    q=q+1
print("Termino la ejecucion")
"""
"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
"""edad = int(input('Introduce tu edad por favor:'))

while edad<5 or edad >100:
    print('Has introducido una edad negativa. vuelve a intentarlo')
    edad = int(input('Introduce tu edad por favor: '))
print('Gracias por calaborar puedes pasar ')
print(f'edad del aspirante: {edad} años.')"""

"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
"""Calculo de raiz cuadrada"""
import math


print('programa que calcula la raiz cuadrada')
numero= int(input('Introduce un numero por favor: '))

intentos = 0

while numero<0:
    print('La raiz cuadrada de un numero negativo no esta en el conjunto \n de los nuemeros reales el resultados pertenece a al conjunto de numeros imaginarios')

    if intentos ==2:
        print('Has consumido demasiados intentos. El programa ha finalizado')
        break;
    numero= int(input('Introduce un numero por favor: '))
    if numero<0:
        intentos=intentos+1
if intentos<2:
    solucion = math.sqrt(numero)
    print(f'La raiz cuadrada de: {numero} es= {solucion}')


