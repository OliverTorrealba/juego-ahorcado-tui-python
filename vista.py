import os
import sys

# Arte ASCII del Zorrito completándose con cada fallo (de 0 a 6 fallos)
ETAPAS_ZORRO = [
    # 0 fallos: Terreno despejado (6 vidas)
    """
    
    
    
    
    
    
    ===========================
    """,
    # 1 fallo: Aparecen las orejitas puntiagudas (5 vidas)
    """
         /\\___/\\
        (       )
    
    
    
    
    ===========================
    """,
    # 2 fallos: Ojos curiosos y hocico (4 vidas)
    """
         /\\___/\\
        (  o o  )
        (  =^=  )
    
    
    
    ===========================
    """,
    # 3 fallos: Pecho y cuerpo del zorrito (3 vidas)
    """
         /\\___/\\
        (  o o  )
        (  =^=  )
         |     |
         |     |
    
    ===========================
    """,
    # 4 fallos: Patitas delanteras (2 vidas)
    """
         /\\___/\\
        (  o o  )
        (  =^=  )
        /|     |\\
       (_|     |_)
    
    ===========================
    """,
    # 5 fallos: Patitas traseras (1 vida)
    """
         /\\___/\\
        (  o o  )
        (  =^=  )
        /|     |\\
       (_|     |_)
         | | | |
    ===========================
    """,
    # 6 fallos: Zorrito completo con cola esponjosa y ojos de derrota (0 vidas)
    """
         /\\___/\\
        (  x x  )
        (  =^=  )
        /|     |\\   __
       (_|     |_) /  \\
         | | | |  / /\\ \\
         (_|_|_) (____/
    ===========================
    """
]

def limpiar_pantalla():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def pausar():
    input("\nPresiona [Enter] para continuar...")

def ver_menu():
    limpiar_pantalla()
    print("==============================")
    print("      JUEGO DEL AHORCADO      ")
    print("      (Edición Zorrito)       ")
    print("==============================")
    print("1. Nuevo juego")
    print("2. Cargar juego")
    print("3. Instrucciones")
    print("4. Salir")
    print("==============================")
    return input("Ingrese una opción (1-4): ").strip()

def mostrar_instrucciones():
    limpiar_pantalla()
    print("==================================================")
    print("                 INSTRUCCIONES                    ")
    print("==================================================")
    print("- Debes adivinar la palabra secreta letra por letra.")
    print("- Cada fallo va completando el dibujo del zorrito.")
    print("- Si el zorrito se completa (6 fallos), habrás perdido.")
    print("- Puedes escribir 'P' o 'PAUSA' en tu turno para")
    print("  pausar y guardar tu partida para continuar luego.")
    print("==================================================")
    pausar()

def ver_menu_pausa():
    limpiar_pantalla()
    print("==============================")
    print("        JUEGO EN PAUSA        ")
    print("==============================")
    print("1. Reanudar partida")
    print("2. Guardar partida")
    print("3. Volver al menú principal")
    print("==============================")
    return input("Ingrese una opción (1-3): ").strip()

def mostrar_tablero_juego(palabra_oculta, intentos_restantes, fallos, letras_usadas):
    limpiar_pantalla()
    print("==================================================")
    print("              JUEGO DEL AHORCADO                  ")
    print("     (Escribe 'P' en cualquier momento para PAUSA)")
    print("==================================================")
    
    # Dibujo del zorrito según la cantidad de fallos (máx 6)
    indice_etapa = min(fallos, len(ETAPAS_ZORRO) - 1)
    print(ETAPAS_ZORRO[indice_etapa])
    
    print(f"Vidas restantes : {intentos_restantes} / 6")
    print(f"Letras usadas   : {', '.join(letras_usadas) if letras_usadas else 'Ninguna'}")
    print("\nPalabra secreta : " + " ".join(palabra_oculta) + "\n")
    print("==================================================")

def pedir_jugada():
    return input("Ingresa una letra (o 'P' para pausar): ").strip().upper()

def mostrar_mensaje(mensaje):
    print(mensaje)

def mostrar_victoria(palabra):
    limpiar_pantalla()
    print("==================================================")
    print("             ¡FELICITACIONES!                     ")
    print("       ¡Has salvado al zorrito y ganado!          ")
    print("==================================================")
    print("""
         /\\___/\\
        (  ^ ^  )  * ¡Yip! *
        (  =^=  )
        /|     |\\   __
       (_|     |_) /  \\
         | | | |  / /\\ \\
         (_|_|_) (____/
    """)
    print(f"La palabra secreta era: {palabra}")
    print("==================================================")
    pausar()

def mostrar_derrota(palabra):
    limpiar_pantalla()
    print("==================================================")
    print("                 ¡HAS PERDIDO!                    ")
    print("          El zorrito se ha completado...          ")
    print("==================================================")
    print(ETAPAS_ZORRO[6])
    print(f"La palabra secreta era: {palabra}")
    print("==================================================")
    pausar()
