'''
Ejercicio 2: Definir una función denominada imprimir_mensaje que imprima el siguiente
mensaje en pantalla: “Estudiando Fundamentos de Informática en la UNAJ”. No recibe
ninguna información por lo tanto no tiene ningún parámetro formal.

def imprimir_mensaje():
    print("Estudiando Fundamentos de Informática en la UNAJ")

imprimir_mensaje()
'''
'''
Ejercicio 3: Definir una función denominada retorno_mensaje que retorne siguiente
mensaje: “Estudiando Fundamentos de Informática en la UNAJ”.
A. ¿Cómo hago para mostrar ese mensaje en pantalla?
B. ¿Qué diferencia encuentra con el ejercicio anterior?
C. Si tuvieras que imprimir mensajes como “Estudiando Matemática I en la UNAJ“ y
“Estudiando Python en la UNAJ” utilizando la misma función ¿Cómo la modificarías?

def retorno_mensaje():
    return ("Estudiando Fundamentos de Informática en la UNAJ")

mensaje = retorno_mensaje()
print(mensaje)
'''
'''
Ejercicio 4: Definir una función denominada imprimo_fecha que reciba tres cadenas de
caracteres como parámetros formales, que representan un día, un mes y un año e imprima
la fecha de la siguiente manera: “ 21 de septiembre de 2021”.

def imprimo_fecha(day, month, year):
    return (day + " de " + month + " de " + year)

print(imprimo_fecha("31", "Agosto","1988"))
'''
'''
Ejercicio 5: Definir una función denominada cuantos_dias que reciba el número de mes
como parámetro y retorne la cantidad de días que posee. Ejemplo: cuantos_dias(1),
debería retornar 31. Ayuda: Pensar en tener una lista de la siguiente manera: [[“enero”,31],
[“febrero”, 28], ...]

def cuantos_dias(num):
    meses = [
        ["enero", 31],
        ["febrero", 28],
        ["marzo", 31],
        ["abril", 30],
        ["mayo", 31],
        ["junio", 30],
        ["julio", 31],
        ["agosto", 31],
        ["septiembre", 30],
        ["octubre", 31],
        ["noviembre", 30],
        ["diciembre", 31]
    ]
    if num < 1 or num > 12:
        return "Error: El número debe estar entre 1 y 12"

    for mes in meses:
        if meses.index(mes) + 1 == num:
            return mes[1]

print(cuantos_dias(8))
'''
'''
Ejercicio 6: Definir una función que reciba un número como parámetro y mostrar la tabla de
multiplicar de dicho número.

def tabla_mul(num):
    print(f"La tabla de multiplicar del número {num} es: ")

    for i in range(1, 11):
        resultado = num * i
        print(f"{num} * {i} = {resultado}")

tabla_mul(2)
'''
'''
Ejercicio 7: Definir una función que calcule el área de un círculo, otra que calcule el área de
un rectángulo y otra que calcule el área de un cuadrado. Analice qué parámetros deberían
recibir dichas funciones.

def area_circle(radio):
    area = 3.14 * (radio ** 2)
    return area

print(area_circle(2))

def area_rectangle(base, altura):
    area = base * altura
    return area

print(area_rectangle(2, 6))

def area_square(lado):
    area = lado ** 2
    return area

print(area_square(4))
'''
'''
Ejercicio 8: Definir una función llamada calculo_rebaja que reciba dos números, uno con
el precio anterior y otro para el precio rebajado y devuelva un número que represente el
porcentaje rebajado.

def calculo_rebaja(precio_ant, precio_rebaj):
    rebaja = precio_ant - precio_rebaj
    descuento = rebaja * 100 / precio_ant
    return descuento

print(calculo_rebaja(1000, 800))
'''
'''
Ejercicio 9
Pedir el ingreso por teclado de dos palabras de 4 letras cada una, luego armar una nueva
palabra con la primera letra de la primera palabra y la primera letra de la segunda palabra
y así sucesivamente hasta la cuarta letra. Luego imprimir dicha nueva palabra. Por ejemplo 
si ingresa "Hola" y "Chau", la impresión debe ser de la forma: "HCohlaau".

palabra1 = input("Por favor, ingrese una palabra de 4 letras: ")
palabra2 = input("Por favor, ingrese nuevamente una palabra de 4 letras: ")

if len(palabra1) == 4 and len(palabra2) == 4:
    nueva_palabra = ""
    for i in range(4):
        nueva_palabra += palabra1[i] + palabra2[i]
    print(f"La palabra formada es: {nueva_palabra}")
else:
    print("Una o ambas palabras no cumplen con la consigna de tener 4 letras")
'''
'''
Ejercicio 10
Pedir el ingreso de 4 textos por teclado, luego agregar a una lista la última letra de cada texto.
Por ejemplo, si ingresa "UNAJ", "es", "una" y "Universidad", la lista deberá quedar de la forma
["J", "s", "a", "d"].

texto1 = input("Ingrese el primer texto: ")
texto2 = input("Ingrese el segundo texto: ")
texto3 = input("Ingrese el tercer texto: ")
texto4 = input("Ingrese el cuarto texto: ")

nueva_lista = []
nueva_lista.append(texto1[-1])
nueva_lista.append(texto2[-1])
nueva_lista.append(texto3[-1])
nueva_lista.append(texto4[-1])

print(nueva_lista)
'''
'''
Ejercicio 11: Definir una función llamada armo_cartel que reciba una cadena de caracteres
(para el nombre del producto) y dos números (el precio anterior y el otro para el precio
rebajado) e imprima un cartel de la siguiente forma:
*************************************
Atención!!! Gran rebaja para el producto nombre (recibido como parámetro)
Antes: precio anterior (dato recibido como parámetro)
Ahora: precio rebajado (dato recibido como parámetro)
'''
def armo_cartel(nombre_producto, precio_anterior, precio_rebajado):
    print("*" * 37)
    print("Atención!!! Gran rebaja para el producto", nombre_producto)
    print("Antes:", precio_anterior)
    print("Ahora:", precio_rebajado)
    print("*" * 37)

# Ejemplo de uso:
nombre_producto = "Camiseta"
precio_anterior = 25.99
precio_rebajado = 19.99

armo_cartel(nombre_producto, precio_anterior, precio_rebajado)

'''
Ejercicio 12: Definir una función llamada calculo_litros que reciba tres números, el alto,
ancho y profundidad (en metros) de una pileta y devuelva la cantidad de litros que tiene.
'''
def calculo_litros(alto, ancho, profundidad):
    # Calcula el volumen en metros cúbicos
    volumen_metros_cubicos = alto * ancho * profundidad

    # Convierte el volumen a litros
    volumen_litros = volumen_metros_cubicos * 1000

    return volumen_litros

# Ejemplo de uso:
alto_pileta = 2.5  # metros
ancho_pileta = 4.0  # metros
profundidad_pileta = 1.5  # metros

litros_en_pileta = calculo_litros(alto_pileta, ancho_pileta, profundidad_pileta)
print("La pileta tiene", litros_en_pileta, "litros.")

'''
Ejercicio 13: Definir una función llamada a_pagar que reciba 4 números: la cantidad de
personas, el monto gastado en bebida, el monto gastado en comida y el del alquiler del
lugar, y retorne cuánto le toca pagar a cada uno.

def a_pagar(cantidad_personas, monto_bebida, monto_comida, monto_alquiler):
    # Calcula el gasto total
    gasto_total = monto_bebida + monto_comida + monto_alquiler

    # Calcula cuánto le toca pagar a cada persona
    monto_por_persona = gasto_total / cantidad_personas

    return monto_por_persona

# Ejemplo de uso:
cantidad_personas = 5
monto_bebida = 120.50
monto_comida = 200.75
monto_alquiler = 300.00

monto_por_persona = a_pagar(cantidad_personas, monto_bebida, monto_comida, monto_alquiler)
print("A cada persona le toca pagar:", monto_por_persona, "pesos.")
'''
'''
Ejercicio 14: Definir tres funciones llamadas convertir_a_dolar, convertir_a_euro y
convertir_a_real. Cada función recibe un parámetro que representa un monto en pesos y
devuelve su conversión respectiva.

def convertir_a_dolar(monto_pesos, tipo_cambio_dolar):
    monto_dolar = monto_pesos / tipo_cambio_dolar
    return monto_dolar

def convertir_a_euro(monto_pesos, tipo_cambio_euro):
    monto_euro = monto_pesos / tipo_cambio_euro
    return monto_euro

def convertir_a_real(monto_pesos, tipo_cambio_real):
    monto_real = monto_pesos / tipo_cambio_real
    return monto_real

# Ejemplo de uso:
monto_en_pesos = 1000  # Monto en pesos argentinos
tipo_cambio_dolar = 100  # Supongamos que 1 dólar equivale a 100 pesos
tipo_cambio_euro = 120  # Supongamos que 1 euro equivale a 120 pesos
tipo_cambio_real = 20   # Supongamos que 1 real equivale a 20 pesos

monto_en_dolar = convertir_a_dolar(monto_en_pesos, tipo_cambio_dolar)
monto_en_euro = convertir_a_euro(monto_en_pesos, tipo_cambio_euro)
monto_en_real = convertir_a_real(monto_en_pesos, tipo_cambio_real)

print("Monto en dólares:", monto_en_dolar)
print("Monto en euros:", monto_en_euro)
print("Monto en reales:", monto_en_real)
'''
'''
Ejercicio 15: Definir una función llamada calculo_dosis que reciba tres números. Uno para
la cantidad de días que debe suministrarse el remedio, el segundo dato para la cantidad de
veces por día que debe tomarlo, y el último dato para la cantidad de comprimidos que trae el
envase. La función debe devolver verdadero si el envase alcanza para ese tratamiento y
falso si no alcanza.
'''
def calculo_dosis(cantidad_dias, veces_por_dia, comprimidos_envase):
    dosis_total = cantidad_dias * veces_por_dia
    if dosis_total <= comprimidos_envase:
        return True
    else:
        return False

# Ejemplo de uso:
cantidad_dias_tratamiento = 10
veces_por_dia = 2
comprimidos_envase = 30

if calculo_dosis(cantidad_dias_tratamiento, veces_por_dia, comprimidos_envase):
    print("El envase alcanza para el tratamiento.")
else:
    print("El envase no alcanza para el tratamiento.")
'''
Ejercicio 16: Definir una función llamada precio_con_iva que agrega el IVA (21%) de un
producto dado su precio de venta sin IVA.
'''
def calculo_nuevo_precio(precio_sin_iva):
    iva = precio_sin_iva * 0.21
    precio_con_iva = precio_sin_iva + iva
    return precio_con_iva

# Ejemplo de uso:
precio_sin_iva = 100.00

precio_con_iva_final = calculo_nuevo_precio(precio_sin_iva)
print("El precio con IVA es:", precio_con_iva_final)

'''
Ejercicios Complementarios
Ejercicio 17:
a) Definir una función que reciba como parámetro una lista de números y retorne la
suma del primer elemento con el último.
#Zona de definiciones de funciones
def sumaPrimUlt(lis):
#retorna la suma entre el primer elemento de la lista con el ultimo
….
def promedioPrimUlt(lis):
#retorna el promedio entre el primer elemento de la lista con el ultimo
….
#Zona del programa principal
#solicitar al usuario 3 numeros, armar la lista e invocar las funciones anteriores mostrando los
#resultados
…..
# Zona de definiciones de funciones
def sumaPrimUlt(lis):
    # Retorna la suma entre el primer elemento de la lista con el ultimo
    if len(lis) < 1:
        return "La lista está vacía"
    else:
        return lis[0] + lis[-1]

# Zona de definiciones de funciones
def sumaPrimUlt(lis):
    # Retorna la suma entre el primer elemento de la lista con el ultimo
    if len(lis) < 1:
        return "La lista está vacía"
    else:
        return lis[0] + lis[-1]

def promedioPrimUlt(lis):
    # Retorna el promedio entre el primer elemento de la lista con el ultimo
    if len(lis) < 1:
        return "La lista está vacía"
    else:
        return (lis[0] + lis[-1]) / 2

# Zona del programa principal
# Solicitar al usuario 3 números, armar la lista e invocar las funciones anteriores mostrando los resultados
numeros = []

for i in range(3):
    numero = float(input("Ingrese un número: "))
    numeros.append(numero)

suma = sumaPrimUlt(numeros)
promedio = promedioPrimUlt(numeros)

print("La suma del primer y último elemento de la lista es:", suma)
print("El promedio del primer y último elemento de la lista es:", promedio)
'''
'''
Ejercicio 18: En este código una fracción está representada por una lista de dos elementos,
el numerador y el denominador. Por ejemplo la fracción ¾ seria la lista (3,4). Complete el
código según corresponda.
#Zona de definiciones de funciones
def cargarFraccion():
#Solicita al usuario el numerador y denominador. Arma la fraccion como una lista y la retorna
…
.
def numeradorFraccion(x):
#Retorna el numerador que se encuentra en la fraccion x, representada como una lista
….
def denominadorFraccion(x):
#Retorna el denominador que se encuentra en la fraccion x, representada como una lista
….
def sumaFracciones(x, y):
#Retorna la suma de las fracciones, representadas como listas
….
def restaFracciones(x, y):
#Retorna la resta de las fracciones, representadas como listas
….
def divisionFracciones(x, y)
#Retorna la division de las fracciones, representadas como listas:
….
def multiplicacionFracciones(x, y):
#Retorna la multiplicacion fracciones, representadas como listas
….
#Zona del programa principal
print (“Bienvenidos/as a cuentas con Fracciones”)
a=cargarFraccion()
b=cargarFraccion()
print (“El denominador de la primera fraccion es:”, …..)
print (“El numerador de la segunda fraccion es:”, …..)
print (“La suma de dichas fracciones es:”, …..)
print (“La resta de dichas fracciones es:”, …..)
print (“La multiplicacion de dichas fracciones es:”, …..)
print (“La division es:”, …..)

# Zona de definiciones de funciones
def cargarFraccion():
    numerador = int(input("Ingrese el numerador de la fracción: "))
    denominador = int(input("Ingrese el denominador de la fracción: "))
    return [numerador, denominador]

def numeradorFraccion(x):
    return x[0]

def denominadorFraccion(x):
    return x[1]

def sumaFracciones(x, y):
    numerador_suma = x[0]*y[1] + y[0]*x[1]
    denominador_suma = x[1]*y[1]
    return [numerador_suma, denominador_suma]

def restaFracciones(x, y):
    numerador_resta = x[0]*y[1] - y[0]*x[1]
    denominador_resta = x[1]*y[1]
    return [numerador_resta, denominador_resta]

def divisionFracciones(x, y):
    numerador_division = x[0]*y[1]
    denominador_division = x[1]*y[0]
    return [numerador_division, denominador_division]

def multiplicacionFracciones(x, y):
    numerador_multiplicacion = x[0]*y[0]
    denominador_multiplicacion = x[1]*y[1]
    return [numerador_multiplicacion, denominador_multiplicacion]

# Zona del programa principal
print("Bienvenidos/as a cuentas con Fracciones")
a = cargarFraccion()
b = cargarFraccion()
print("El denominador de la primera fracción es:", denominadorFraccion(a))
print("El numerador de la segunda fracción es:", numeradorFraccion(b))
print("La suma de dichas fracciones es:", sumaFracciones(a, b))
print("La resta de dichas fracciones es:", restaFracciones(a, b))
print("La multiplicación de dichas fracciones es:", multiplicacionFracciones(a, b))
print("La división es:", divisionFracciones(a, b))
'''