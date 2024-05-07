'''
Ejercicio 2: Definir una función denominada imprimir_mensaje que imprima el siguiente
mensaje en pantalla: “Estudiando Fundamentos de Informática en la UNAJ”. No recibe
ninguna información por lo tanto no tiene ningún parámetro formal.
'''
def imprimir_mensaje():
    print("Estudiando Fundamentos de Informática en la UNAJ")

imprimir_mensaje()
'''
Ejercicio 3: Definir una función denominada retorno_mensaje que retorne siguiente
mensaje: “Estudiando Fundamentos de Informática en la UNAJ”.
A. ¿Cómo hago para mostrar ese mensaje en pantalla?
B. ¿Qué diferencia encuentra con el ejercicio anterior?
C. Si tuvieras que imprimir mensajes como “Estudiando Matemática I en la UNAJ“ y
“Estudiando Python en la UNAJ” utilizando la misma función ¿Cómo la modificarías?
'''
def retorno_mensaje():
    return ("Estudiando Fundamentos de Informática en la UNAJ")

mensaje = retorno_mensaje()
print(mensaje)
'''
Ejercicio 4: Definir una función denominada imprimo_fecha que reciba tres cadenas de
caracteres como parámetros formales, que representan un día, un mes y un año e imprima
la fecha de la siguiente manera: “ 21 de septiembre de 2021”.
'''
def imprimo_fecha(day, month, year):
    return (day + " de " + month + " de " + year)

print(imprimo_fecha("31", "Agosto","1988"))
'''
Ejercicio 5: Definir una función denominada cuantos_dias que reciba el número de mes
como parámetro y retorne la cantidad de días que posee. Ejemplo: cuantos_dias(1),
debería retornar 31. Ayuda: Pensar en tener una lista de la siguiente manera: [[“enero”,31],
[“febrero”, 28], ...]
'''
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
Ejercicio 6: Definir una función que reciba un número como parámetro y mostrar la tabla de
multiplicar de dicho número.
'''
def tabla_mul(num):
    print(f"La tabla de multiplicar del número {num} es: ")

    for i in range(1, 11):
        resultado = num * i
        print(f"{num} * {i} = {resultado}")

tabla_mul(2)

'''
Ejercicio 7: Definir una función que calcule el área de un círculo, otra que calcule el área de
un rectángulo y otra que calcule el área de un cuadrado. Analice qué parámetros deberían
recibir dichas funciones.
'''
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
Ejercicio 8: Definir una función llamada calculo_rebaja que reciba dos números, uno con
el precio anterior y otro para el precio rebajado y devuelva un número que represente el
porcentaje rebajado.
'''
def calculo_rebaja(precio_ant, precio_rebaj):
    rebaja = precio_ant - precio_rebaj
    descuento = rebaja * 100 / precio_ant
    return descuento

print(calculo_rebaja(1000, 800))

'''
Ejercicio 9
Pedir el ingreso por teclado de dos palabras de 4 letras cada una, luego armar una nueva
palabra con la primera letra de la primera palabra y la primera letra de la segunda palabra
y así sucesivamente hasta la cuarta letra. Luego imprimir dicha nueva palabra. Por ejemplo 
si ingresa "Hola" y "Chau", la impresión debe ser de la forma: "HCohlaau".
'''
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
Ejercicio 10
Pedir el ingreso de 4 textos por teclado, luego agregar a una lista la última letra de cada texto.
Por ejemplo, si ingresa "UNAJ", "es", "una" y "Universidad", la lista deberá quedar de la forma
["J", "s", "a", "d"].
'''
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

