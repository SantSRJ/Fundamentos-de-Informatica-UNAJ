'''
Ejercicio 1
Escribir un programa que lee un número ingresado por el usuario
y muestre si es positivo, negativo o cero.

# Solicitar al usuario que ingrese un número
numero = float(input("Por favor, ingrese un número: "))

# Verificar si el número es positivo, negativo o cero y mostrar el resultado
if numero > 0:
    print("El número ingresado es positivo.")
elif numero < 0:
    print("El número ingresado es negativo.")
else:
    print("El número ingresado es cero.")
'''
'''
Ejercicio 2
Escribir un programa que lee el nombre y apellido de una persona y 
muestra en pantalla si tiene la misma inicial o no

name = input("Ingrese su nombre: ")
surname = input("Ingrese su apellido: ")
if name[0] == surname[0]:
    print("Su nombre y apellido tienen la misma inicial")
else:
    print("Su nombre y apellido no tienen la misma inicial")
'''
'''
Ejercicio 3
Escribir un programa que me indique si un numero es divisible por 6. ¿Cómo
lo modificaria si se pide lo mismo pero que invoque una funcion definida por usted?
Esta funcion debe llamarse es_Divisible y debe recibir dos parametros "n" y "m" y retorna 
True si m es divisible por n, sino retorna False.

# Programa para saber si un numero es divisible por 6.
num = int(input("Ingrese un numero: "))
if num % 2 == 0 and num % 3 == 0:
    print(f"El numero {num} es divisible por 6")
else:
    print(f"El numero {num} NO es divisible por 6")

# Programa para saber si un numero es divisible por otro
def es_Divisible(m, n):
    if m % n == 0:
        print(f"El numero {m} es divisible por {n}")
    else:
        print(f"El numero {m} NO es divisible por {n}")

m = int(input("Ingrese un numero (dividendo): "))
n = int(input("Ingrese un numero (divisor): "))

es_Divisible(m, n)
'''
'''
Ejercicio 4
Diseñar un programa que dado un numero del 1 al 7 determine el dia de la semana que
representa: 1 - Domingo a  7 - Sabado. ¿Que pasa si ingreso un numero mayor que 7?

num_day = int(input("Ingrese un numero del 1 al 7: "))
if num_day == 1:
    print("Domingo")
elif num_day == 2:
    print("Lunes")
elif num_day == 3:
    print("Martes")
elif num_day == 4:
    print("Miercoles")
elif num_day == 5:
    print("Jueves")
elif num_day == 6:
    print("Viernes")
elif num_day == 7:
    print("Sabado")
else:
    print("El numero ingresado es incorrecto, debe ser del 1 al 7")
'''
'''
Ejercicio 5
Dada la siguiente tabla { "Transporte": "Bicicleta", "Moto", "Auto", "Camioneta", "Colctivo", "Avion"}
                        { "Pasajeros": 1, 2, 4, 12, 40, 200}
Escribir un programa que dada la cantidad de personas a viajar, recomiende el medio de transporte

cant_per = int(input("Ingrese la cantidad de personas que viajaran : "))
if cant_per == 1:
    print("Bicicleta")
elif cant_per == 2:
    print("Moto")
elif cant_per > 2 and cant_per <= 4:
    print("Auto")
elif cant_per > 4 and cant_per <= 12:
    print("Camioneta")
elif cant_per > 12 and cant_per <= 40:
    print("Colectivo")
elif cant_per > 40 and cant_per <= 200:
    print("Avion")
else:
    print("Crucero")
'''
'''
Ejercicio 6
Desarrollar un programa en el que se ingrese el año de nacimiento de una persona e indique si la persona
es bebé, menor, adolescente, adulto o adulto mayor.
        Tabla { "Tipo": "Bebe", "Menor", "Adolescente", "Adulto", "Adulto mayor" }
              { "Edad": "< 2 años", "> 2 y <= 12", "> 12 y <= 18", "> 18 y <= 60", "> 60" }

edad = int(input("Ingrese la edad de la persona: "))
if edad > 0 and edad <= 2:
    print("La persona es un bebé")
elif edad > 2 and edad <= 12:
    print("La persona es un menor")
elif edad > 12 and edad <= 18:
    print("La persona es un adolescente")
elif edad > 18 and edad <= 60:
    print("La persona es un adulto")
elif edad > 60 and edad <= 120:
    print("La persona es un adulto mayor")
else:
    print("La persona no puede tener esa edad")
'''
'''
Ejercicio 7
Dada la siguiente tabla: 
                        { "Categoria": "A", "B", "C" }
                        { "Antigüedad": "< 10 años", "entre 10 a 15", "> 15",
                                        "< 10 años", "entre 10 a 15", "> 15",
                                        "< 10 años", "entre 10 a 15", "> 15" }
                        { "Aumento": "5%", "10%", "15%",
                                     "10%", "15%", "20%",
                                     "15%", "20%", "25%" }
Escriba un programa que le solicite a una persona su nombre, apellido, sueldo basico, categoria y antigüedad.
El programa debe calcular el aumento de acuerdo a la tabla y mostrarle el sueldo anterior, el aumento y el
sueldo actualizado con dicho aumento. Resuelva utilizando funciones.

def procesar_persona():
    name = input("Ingrese el nombre de la persona: ")
    surname = input("Ingrese el apellido de la persona: ")
    salary = float(input("Ingrese el sueldo basico de la persona: "))
    category = input("Ingrese la categoria de la persona (A, B o C): ")
    antiquity = int(input("Ingrese la antigüedad de la persona: "))
    return [name, surname, salary, category, antiquity]

def calcular_aumento(persona):
    if persona[3] == "A":
        if persona[4] < 10:
            aumento = persona[2] * 5 / 100
        elif persona[4] > 10 and persona[4] <= 15:
            aumento = persona[2] * 10 / 100
        else:
            aumento = persona[2] * 15 / 100
    elif persona[3] == "B":
        if persona[4] < 10:
            aumento = persona[2] * 10 / 100
        elif persona[4] > 10 and persona[4] <= 15:
            aumento = persona[2] * 15 / 100
        else:
            aumento = persona[2] * 20 / 100
    elif persona[3] == "C":
        if persona[4] < 10:
            aumento = persona[2] * 15 / 100
        elif persona[4] > 10 and persona[4] <= 15:
            aumento = persona[2]* 20 / 100
        else:
            aumento = persona[2] * 25 / 100
    else:
        print("La persona no se encuentra comprendida dentro de las Categorias A, B o C")
        return 0
    return aumento

persona = procesar_persona()
aumento = calcular_aumento(persona)
new_salary = aumento + persona[2]
print(f"La persona {persona[0]} {persona[1]}, tenía un sueldo básico de ${persona[2]}, tendrá un aumento de ${aumento} y cobrará ${new_salary}")
'''
'''
Ejercicio 8
Diseña un programa que, dado un numero entero, determine si éste es el doble de un numero impar (Ejemplo: 14 es el doble de 7, que es 
impar.) Resuelva utilizando funciones.

def leer_num():
    num = int(input("Ingrese un numero entero: "))
    return num

def determinar_doble_impar(num):
    es_doble_impar = num % 2 == 0 and (num // 2) % 2 != 0
    if es_doble_impar:
        return f"El numero {num} es el doble de {num // 2}, que es impar."
    else:
        return f"El numero {num} no es el doble de un numero impar."

numero = leer_num()
print(determinar_doble_impar(numero))
'''
'''
Ejercicio 9
Diseñar un programa que dado un caracter imprima en pantalla si es una letra, 
un digito, un caracter especial u otro tipo de caracter.

def tipo_caracter(caracter):
    if caracter.isalpha():
        print("Es una letra.")
    elif caracter.isdigit():
        print("Es un dígito.")
    elif caracter in "!@#$%^&*()-_+=<>?/.,;:'\"":
        print("Es un caracter especial.")
    else:
        print("Es otro tipo de caracter.")

caracter = input("Ingrese un caracter: ")
tipo_caracter(caracter)
'''
'''
Ejercicio 10
Dadas 3 longitudes, decir mediante un mensaje si se forma o no un triangulo (cada lado 
tiene que ser menor que la suma de los otros dos).

long1 = float(input("Ingrese la primera longitud: "))
long2 = float(input("Ingrese la segunda longitud: "))
long3 = float(input("Ingrese la tercera longitud: "))

if long1 + long2 <= long3 or long1 + long3 <= long2 or long2 + long3 <= long1:
    print("Al menos una de las longitudes es muy corta y no se puede formar el triangulo")
else:
    print("Con las longitudes cargadas, se puede formar un triangulo")
'''
'''
Ejercicio 11
Defina una funcion que reciba un caracter cualquiera desde el teclado, y muestre el mensaje
@Es una MAYUSCULA cuando el caracter sea una letra mayuscula y @Es una MINUSCULA cuando sea 
una minuscula. En cualquier otro caso, no mostrara mensaje alguno. (Considera unicamente las
letras del alfabeto)
Pista: aunque parezca una obviedad, recuerda que una letra es minuscula si esta entre la 'a'
y la 'z', y mayuscula si esta entre la 'A' y la 'Z', tambien debe hacer la correspondiente 
incovacion.
'''
'''
Ejercicio 12
Escribir un programa que dado un año determine si es bisiesto o no. Un año es bisiesto si es 
multiplo de 4. Los años multiplos de 100 no son bisiestos, salvo si ellos son tambien multiplo
de 400 (2000 es bisiesto, pero 1800 no lo es).
'''
'''
Ejercicio 13
Dado la duracion (en segundos) de una llamada telefonica, calcular su costo, de la siguiente
manera: El primer minuto $1.10, luego $0.25 por cada fraccion de 15 segundos (un cuarto de minuto).
'''
'''
Ejercicio 14
Calcular el numero de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio
aerobico; la formula que se aplica cuando el sexo es femenino es: (220-edad)/10; si el sexo es 
masculino es: (210-edad)/10. Resuelva utilizando funciones.
'''
'''
Ejercicio 15
A continuacion se detallan las temperaturas maximas y minimas de tres lugares de Argentina en un
dia del año:
USHUAIA: MAX: 13°C MIN: -5°C
BUENOS AIRES: MAX: 16°C MIN: 5°C
BASE MARAMBIO: MAX: 3°C MIN: -20°C
Defina una funcion que reciba dos temperaturas y que muestre el mensaje que indique la diferencia
entre ambas.
- Utilice la funcion anterior para mostrar la diferencia de temperaturas minimas entre Buenos Aires
y Ushuaia.
- Utilice la funcion anterior para mostrar la diferencia de temperaturas minimas entre Base Marambio
y Ushuaia.
- Si la temperatura de la Base Marambio bajo 7°C, que diferencia tendra con la temperatura minima.
- Utilice la funcion anterior para mostrar la diferencia entre la temperatura maxima de Buenos Aires 
y la minima.
Si los datos se ingresaran desde el teclado, ¿Que cambios debe hacer en su programa?
Fundamente su respuesta
'''
'''
Ejercicio 16
La aplicacion de la tarjeta SUBE permite revisar los saldos dia a dia y Marcos decidio ver sus saldos
de la semana  y anoto lo siguiente:
Lunes: $15 | Martes: $-21 | Miercoles: -$41 | Jueves: $109 | Viernes: $109 
Teniendo en cuenta el registro, definir 3 funciones que permitan mostrar lo siguiente:
a) ¿Cuanto gasto de lunes a martes?¿De martes a miercoles?
b) ¿Cuanto dinero cargo el miercoles para tener el saldo del jueves?
c) Calcule el promedio gastado en los 5 dias.
'''
'''
Ejercicio 17
Definir una funcion que permita ingresar dos numeros enteros y que calcule que porcentaje representa
el primer numero del segundo.
Por ejemplo, si la funcion recibe 25 y 200, debera retornar 50, ya que el 25% de 200 es 50.
Complete usando la funcion anterior: 
El 25% de 890 =
El 10% de 12600 =
El 35% de 12600 =
El 125% de 890 =  
'''
'''
Ejercicio 18
Una carniceria paso de cobrar el vacio de $810 a $1040,90, ¿se puede saber de cuanto fue el porcentaje
de aumento? Si es asi, calculalo.
Definir una funcion que reciba dos numeros y que retorne cual es el porcentaje de aumento.
'''
'''
Una persona compro 4 kilogramos de vacio en esta carniceria y por pago en efectivo le hicieron un descuento 
del 5%, ¿cuanto dinero gasto?
Definir una funcion que reciba dos numeros, que representan el porcentaje de descuento y el monto total,
y retorne el monto con el descuento aplicado.
'''
'''
Ejercicios complenarios:
Ejercicio 20
Implementar un programa que muestre un menu de opciones e invoque las funciones desarrolladas en la Practica 3.
Para que funcione debe importar los archivos donde se encuentran las definiciones o redefinirlas. El programa
deberia mostrar los siguientes mensajes:
'Bienvenido al programa con menu de opciones'
'Elija una opcion del siguiente menu, ingresando del 1 al 5'
1 - Calculo dosis
2 - Calculo litros
3 - Calculo nuevo precio
4 - Calculo transporte
5 - Salir
'''
'''
Ejercicio 21
Analizar el siguiente programa y completar el codigo que falta.
#Zona de definiciones de funciones
def cargarDatos():
    #pide nombre, apellido, edad y sueldo a una persona, arma una lista y la retorna
    ...
def esMayorDeEdad(pers):
    #retorna verdadero True si es mayor de 18 años, sino retorna falso False
    ...
def personaMejorSueldo(pers1, pers2):
    #retorna el nombre y apellido de la persona que gana mas
    ...
def personaMasJoven(pers1, pers2):
    #retorna el nombre y apellido de la persona mas joven de edad
    ...
#Zona del programa principal
print("Bienvenidos/as al programa sobre datos de personas")
print("Se solicitara datos de 2 personas y se mostrara informacion sobre ellas")
#Utilizar la funcion para cargar datos de dos personas
...
...
print("La persona que gana mas es:", ..........)
print("La persona mas chica es:" , ..........0)
#Imprimir si la persona mayor es la que mas gana o sea que mayor sueldo tiene.

'''