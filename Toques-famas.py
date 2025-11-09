#JUEGO Toques y Famas
#Realizado por Catalina Ortuño y Dario Toro
#06-11-2025


import random
import sys

def generar_secreto():    #Genera un número secreto de 4 dígitos no repetidos
    digitos = list('0123456789')
    random.shuffle(digitos)
    secreto = "".join(digitos[:4])
    return secreto

def calcular_toques_famas(secreto, intento): #Calcula y devuelve toquesy famas comarando intento con secreto
    """
    - Fama: mismo dígito en la misma posición.
    - Toque: dígito presente en secreto pero en distinta posición.
    """
    famas = 0
    toques = 0

    # Contar famas (posición y dígito iguales)
    for i in range(4):
        if secreto[i] == intento[i]:
            famas += 1

    # Contar toques (mismo dígito, distinta posición)
    for i in range(4):
        if intento[i] != secreto[i] and intento[i] in secreto:
            toques += 1

    return toques, famas

def validar_intento(intento): #Valida intento que sean 4 dígitos no repetidos
    if intento.lower() == "salir":
        return True, ""  # permite la palabra 'salir' como comando para abandonar

    if len(intento) != 4:
        return False, "Debe ingresar exactamente 4 cifras."
    if not intento.isdigit():
        return False, "La entrada debe contener solo dígitos (0-9)."
    if len(set(intento)) != 4:
        return False, "Los dígitos no pueden repetirse. Intente con 4 dígitos únicos."
    return True, ""

def explicar_reglas():
    print("===========================================")
    print("     BIENVENIDO A TOQUES Y FAMAS ")
    print("===========================================\n")
    print("El objetivo del juego es adivinar un número secreto de 4 cifras.\n")
    print("- FAMA: el número y su posición son correctos.")
    print("- TOQUE: el número está en el secreto, pero en otra posición.\n")
    print("Ganas cuando consigues 4 FAMAS.")
    print("Puedes escribir 'salir' en cualquier momento para abandonar el juego.\n")
    print("¡Buena suerte!\n")
    print("===========================================\n")

def jugar_toques_y_famas():
    explicar_reglas()  # mostramos las reglas antes de iniciar

    while True:
        numero_secreto = generar_secreto()
        intentos = 0
        max_intentos = None 

        while True:
            intentos += 1
            try:
                intento_jugador = input(f"Intento #{intentos}. Ingrese su número de 4 cifras: ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\n\nJuego interrumpido. Gracias por jugar.")
                print(f"El número secreto era: {numero_secreto}")
                sys.exit(0)

            # Permitir salir
            if intento_jugador.lower() == "salir":
                print(f"Has salido. El número secreto era: {numero_secreto}")
                break

            # Validar entrada
            valido, mensaje_error = validar_intento(intento_jugador)
            if not valido:
                print("Entrada inválida:", mensaje_error)
                intentos -= 1
                continue

            # Calcular resultado
            toques, famas = calcular_toques_famas(numero_secreto, intento_jugador)
            print(f"Resultado: {toques} Toques - {famas} Famas.\n")

            # Verificar victoria
            if famas == 4:
                print("------------------------------")
                print(f"¡FELICIDADES! Adivinaste el número secreto ({numero_secreto})")
                print(f"Lo lograste en {intentos} intentos.")
                print("------------------------------\n")
                break

        # Preguntar si desea jugar otra vez
        while True:
            respuesta = input("¿Deseas jugar otra vez? (s/n): ").strip().lower()
            if respuesta in ("s", "si"):
                print("\nIniciando nueva partida...\n")
                break
            elif respuesta in ("n", "no"):
                print("¡Gracias por jugar Toques y Famas! ¡Hasta la próxima!")
                return
            else:
                print("Respuesta no reconocida. Escribe 's' para sí o 'n' para no.")

if __name__ == "__main__":
    jugar_toques_y_famas()