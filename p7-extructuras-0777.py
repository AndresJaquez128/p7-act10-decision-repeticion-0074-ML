# JAQUEZ ANDRES 0074  2 EJEMPLOS POR CASO
# ============================================================
# TRABAJO DE PYTHON
# EJEMPLOS BASADOS EN W3SCHOOLS
#
# Se presentan 2 ejemplos por cada caso (link).
# Total: 5 casos x 2 ejemplos = 10 ejemplos.
# ============================================================


# ============================================================
# CASO 1
# TEMA: PYTHON CONDITIONS AND IF STATEMENTS
# LINK:
# https://www.w3schools.com/python/python_conditions.asp
# ============================================================


# ------------------------------------------------------------
# EJEMPLO 1 - Condición IF
# Descripción:
# Se verifica si el valor de una variable es mayor que otro.
# ------------------------------------------------------------

a = 33
b = 200

if b > a:
    print("Ejemplo 1: b es mayor que a")


# ------------------------------------------------------------
# EJEMPLO 2 - Comprobar si un número es positivo
# Descripción:
# Se utiliza una condición para determinar si un número
# es mayor que cero.
# ------------------------------------------------------------

numero = 15

if numero > 0:
    print("Ejemplo 2: El número es positivo")


# ============================================================
# CASO 2
# TEMA: PYTHON ELIF STATEMENT
# LINK:
# https://www.w3schools.com/python/python_if_elif.asp
# ============================================================


# ------------------------------------------------------------
# EJEMPLO 1 - Clasificación de una calificación
# Descripción:
# Se utilizan if, elif y else para determinar el resultado
# dependiendo de la calificación.
# ------------------------------------------------------------

calificacion = 85

if calificacion >= 90:
    print("Ejemplo 1: Excelente")
elif calificacion >= 70:
    print("Ejemplo 1: Aprobado")
else:
    print("Ejemplo 1: Reprobado")


# ------------------------------------------------------------
# EJEMPLO 2 - Determinar la edad
# Descripción:
# Se utilizan varias condiciones para clasificar una edad.
# ------------------------------------------------------------

edad = 25

if edad < 13:
    print("Ejemplo 2: Niño")
elif edad < 18:
    print("Ejemplo 2: Adolescente")
elif edad < 60:
    print("Ejemplo 2: Adulto")
else:
    print("Ejemplo 2: Adulto mayor")


# ============================================================
# CASO 3
# TEMA: PYTHON IF...ELSE STATEMENT
# LINK:
# https://www.w3schools.com/python/python_if_else.asp
# ============================================================


# ------------------------------------------------------------
# EJEMPLO 1 - Mayor o menor de edad
# Descripción:
# Si la edad es 18 o más, se considera mayor de edad.
# De lo contrario, es menor de edad.
# ------------------------------------------------------------

edad = 20

if edad >= 18:
    print("Ejemplo 1: Es mayor de edad")
else:
    print("Ejemplo 1: Es menor de edad")


# ------------------------------------------------------------
# EJEMPLO 2 - Número par o impar
# Descripción:
# Se utiliza el operador módulo (%) para determinar si un
# número es divisible entre 2.
# ------------------------------------------------------------

numero = 7

if numero % 2 == 0:
    print("Ejemplo 2: El número es par")
else:
    print("Ejemplo 2: El número es impar")


# ============================================================
# CASO 4
# TEMA: PYTHON FOR LOOPS
# LINK:
# https://www.w3schools.com/python/python_for_loops.asp
# ============================================================


# ------------------------------------------------------------
# EJEMPLO 1 - Recorrer una lista
# Descripción:
# El ciclo for recorre cada elemento de una lista y lo muestra.
# ------------------------------------------------------------

frutas = ["Manzana", "Plátano", "Naranja", "Uva"]

for fruta in frutas:
    print("Ejemplo 1:", fruta)


# ------------------------------------------------------------
# EJEMPLO 2 - Utilizar range()
# Descripción:
# El ciclo for se utiliza para repetir una acción varias veces.
# range(1, 6) genera los números del 1 al 5.
# ------------------------------------------------------------

for numero in range(1, 6):
    print("Ejemplo 2:", numero)


# ============================================================
# CASO 5
# TEMA: PYTHON WHILE LOOPS
# LINK:
# https://www.w3schools.com/python/python_while_loops.asp
# ============================================================


# ------------------------------------------------------------
# EJEMPLO 1 - Contador con while
# Descripción:
# El ciclo continúa mientras la condición sea verdadera.
# ------------------------------------------------------------

contador = 1

while contador <= 5:
    print("Ejemplo 1:", contador)
    contador += 1


# ------------------------------------------------------------
# EJEMPLO 2 - Cuenta regresiva
# Descripción:
# El ciclo while disminuye el valor hasta llegar a cero.
# ------------------------------------------------------------

numero = 5

while numero >= 1:
    print("Ejemplo 2:", numero)
    numero -= 1

print("Fin de la cuenta regresiva")


# ============================================================
print("Programa realizado por Jaquez andres 0074")