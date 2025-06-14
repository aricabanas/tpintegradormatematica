# ----------------------------- IMPORTACIONES -----------------------------

from itertools import product  # Para producto cartesiano
from datetime import datetime  # Para obtener el año actual


# ----------------------------- FUNCIONES -----------------------------

# Función para ingresar múltiples DNIs desde teclado
def ingresar_dnis():
    cantidad = int(input("¿Cuántos DNIs desea ingresar? "))
    dnis = []
    for i in range(cantidad):
        dni = input(f"Ingrese el DNI #{i + 1} (solo números): ")
        while not dni.isdigit():
            dni = input("Entrada inválida. Ingrese solo números: ")
        dnis.append(dni)
    return dnis

# Convierte un DNI en un conjunto de dígitos únicos
def obtener_conjunto_digitos(dni):
    return set(dni)

# Realiza operaciones de conjuntos con la lista de conjuntos de dígitos
def operaciones_conjuntos(conjuntos):
    union = set.union(*conjuntos)
    interseccion = set.intersection(*conjuntos)
    diferencias = [conjuntos[0].difference(c) for c in conjuntos[1:]]
    diferencia_simetrica = set.symmetric_difference(*conjuntos)
    return union, interseccion, diferencias, diferencia_simetrica

# Cuenta la frecuencia de cada dígito del 0 al 9 en un DNI
def contar_frecuencias(dni):
    frecuencia = {str(i): 0 for i in range(10)}
    for digito in dni:
        frecuencia[digito] += 1
    return frecuencia

# Suma todos los dígitos del DNI
def suma_digitos(dni):
    return sum(int(d) for d in dni)

# Evalúa condiciones sobre los conjuntos de dígitos
def evaluar_condiciones(conjuntos):
    interseccion = set.intersection(*conjuntos)
    if interseccion:
        print("Dígito compartido:", interseccion)
    for i, conjunto in enumerate(conjuntos):
        if len(conjunto) > 6:
            print(f"DNI #{i+1}: Diversidad numérica alta")

# Analiza la paridad (pares/impares) de cada DNI
def analizar_paridad(dnis):
    pares_global = False
    impares_global = False
    for i, dni in enumerate(dnis):
        pares = sum(1 for d in dni if int(d) % 2 == 0)
        impares = sum(1 for d in dni if int(d) % 2 != 0)
        print(f"DNI #{i+1} ({dni}): {pares} pares, {impares} impares")
        if pares > impares:
            print("Predominan los pares.")
        elif impares > pares:
            print("Predominan los impares.")
        else:
            print("Cantidad igual de pares e impares.")
        if pares == len(dni):
            pares_global = True
        if impares == len(dni):
            impares_global = True
    if pares_global:
        print("Existe al menos un DNI compuesto solo por dígitos pares.")
    if impares_global:
        print("Existe al menos un DNI compuesto solo por dígitos impares.")

# Determina si un año es bisiesto
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


# ----------------------------- PROGRAMA PRINCIPAL -----------------------------

# ----- Ingreso de datos -----
dnis = ingresar_dnis()
conjuntos = [obtener_conjunto_digitos(dni) for dni in dnis]

# ----- Operaciones con conjuntos -----
print("\n--- Operaciones con Conjuntos de Dígitos ---")
union, interseccion, diferencias, diferencia_simetrica = operaciones_conjuntos(conjuntos)

print(f"Unión: {union}")
print(f"Intersección: {interseccion}")
for idx, diff in enumerate(diferencias, start=1):
    print(f"Diferencia del DNI #1 con el DNI #{idx+1}: {diff}")
print(f"Diferencia simétrica: {diferencia_simetrica}")

# ----- Frecuencia de dígitos -----
print("\n--- Frecuencia de Dígitos por DNI ---")
for idx, dni in enumerate(dnis):
    frec = contar_frecuencias(dni)
    print(f"DNI #{idx+1} ({dni}): {frec}")

# ----- Suma de dígitos -----
print("\n--- Suma de Dígitos por DNI ---")
for idx, dni in enumerate(dnis):
    suma = suma_digitos(dni)
    print(f"DNI #{idx+1} ({dni}): Suma = {suma}")

# ----- Evaluación de condiciones -----
print("\n--- Evaluación de Condiciones Lógicas ---")
evaluar_condiciones(conjuntos)

# ----- Análisis de paridad -----
print("\n--- Análisis de Paridad de Dígitos por DNI ---")
analizar_paridad(dnis)
####

# ----- Análisis de años de nacimiento -----
anios_nacimiento = [1999, 2002, 2004]  # Podés cambiar estos años
anios_pares = 0
anios_impares = 0
algun_bisiesto = False

for anio in anios_nacimiento:
    if anio % 2 == 0:
        anios_pares += 1
    else:
        anios_impares += 1
    if es_bisiesto(anio):
        algun_bisiesto = True

print("\n--- Operaciones con Años de Nacimiento ---")
print("Años ingresados:", anios_nacimiento)
print("Cantidad de años pares:", anios_pares)
print("Cantidad de años impares:", anios_impares)

if all(anio > 2000 for anio in anios_nacimiento):
    print("Grupo Z")
if algun_bisiesto:
    print("Tenemos un año especial")

# ----- Producto cartesiano año - edad -----
anio_actual = datetime.now().year
edades = [anio_actual - anio for anio in anios_nacimiento]
producto_cartesiano = list(product(anios_nacimiento, edades))

print("\nProducto cartesiano (Año, Edad):")
for par in producto_cartesiano:
    print(par)
