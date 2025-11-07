######################################
# Trabajo de desarrollo sumativo: Unidad 1
# Universidad Mayor - Programacion Computacional
# Estudiantes: Catalina Ortuño y Dario Toro
######################################

# Diccionario de equivalencias 
equivalencias = {
    "1":"A", "2":"B", "3":"C", "4":"D", "5":"E", "6":"F", "7":"G", "8":"H", "9":"I",
    "10":"J", "11":"K", "12":"L", "13":"M", "14":"N", "15":"Ñ", "16":"O", "17":"P",
    "18":"Q", "19":"R", "20":"S", "21":"T", "22":"U", "23":"V", "24":"W", "25":"X",
    "26":"Y", "27":"Z"
}

# 1) Entrada: el usuario escribe números separados por espacios
mensaje = input("Ingrese el mensaje numérico (números del 1 al 27 separados por espacios): ")

# 2) Proceso: separar, convertir cada número a letra y armar el resultado
numeros = mensaje.split()
mensaje_descifrado = ""

for n in numeros:
    if str(n) in equivalencias:           # Convertimos a texto antes de buscar
        mensaje_descifrado += equivalencias[str(n)]
    else:
        mensaje_descifrado += "?"         # Si no existe, marca con "?"

# 3) Salida: mostrar el mensaje descifrado
print("Mensaje descifrado:", mensaje_descifrado)