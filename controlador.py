import sys
import modelo
import vista

def manejar_pausa(partida):
    """
    Gestiona el submenú de pausa.
    Retorna True si el usuario decide volver al menú principal, o False para reanudar.
    """
    while True:
        opcion = vista.ver_menu_pausa()

        if opcion == "1":
            # Reanudar partida
            return False
        elif opcion == "2":
            # Guardar partida actual
            guardado_ok = modelo.guardar_partida(partida)
            vista.limpiar_pantalla()
            if guardado_ok:
                vista.mostrar_mensaje("[✓] ¡Partida guardada exitosamente!")
            else:
                vista.mostrar_mensaje("[X] Error: No se pudo guardar la partida.")
            vista.pausar()
        elif opcion == "3":
            # Salir al menú principal
            return True
        else:
            vista.mostrar_mensaje("\n[!] Opción no válida.")
            vista.pausar()

def jugar(partida):
    """
    Bucle activo de una partida (nueva o cargada).
    """
    while True:
        # 1. Comprobar condiciones de fin de partida
        if partida.ha_ganado():
            vista.mostrar_victoria(partida.palabra_secreta)
            modelo.eliminar_partida_guardada()
            break

        if partida.ha_perdido():
            vista.mostrar_derrota(partida.palabra_secreta)
            modelo.eliminar_partida_guardada()
            break

        # 2. Renderizar el estado actual con el zorrito
        vista.mostrar_tablero_juego(
            partida.palabra_oculta,
            partida.intentos_restantes,
            partida.fallos,
            partida.letras_usadas
        )

        # 3. Solicitar acción al jugador
        entrada = vista.pedir_jugada()

        # 4. Manejar solicitud de pausa
        if entrada == "P" or entrada == "PAUSA":
            debe_salir = manejar_pausa(partida)
            if debe_salir:
                break
            continue

        # 5. Validar formato de entrada
        if len(entrada) != 1 or not entrada.isalpha():
            vista.mostrar_mensaje("\n[!] Ingresa una sola letra válida (A-Z).")
            vista.pausar()
            continue

        # 6. Procesar el intento en el modelo
        resultado = partida.intentar_letra(entrada)
        if resultado == "repetida":
            vista.mostrar_mensaje(f"\n[!] Ya habías probado la letra '{entrada}'.")
            vista.pausar()

def manejar_menu():
    """Bucle principal de la aplicación."""
    while True:
        opcion = vista.ver_menu()

        if opcion == "1":
            # Iniciar nuevo juego con una de las 5 palabras aleatorias
            partida = modelo.crear_nueva_partida()
            jugar(partida)

        elif opcion == "2":
            # Cargar juego previo
            partida = modelo.cargar_partida()
            vista.limpiar_pantalla()
            if partida:
                vista.mostrar_mensaje("[✓] ¡Partida cargada exitosamente!")
                vista.pausar()
                jugar(partida)
            else:
                vista.mostrar_mensaje("[!] No se encontró ninguna partida guardada.")
                vista.pausar()

        elif opcion == "3":
            # Mostrar instrucciones
            vista.mostrar_instrucciones()

        elif opcion == "4":
            # Salir
            vista.limpiar_pantalla()
            vista.mostrar_mensaje("¡Gracias por jugar con el Zorrito! Hasta pronto.\n")
            sys.exit()

        else:
            vista.mostrar_mensaje("\n[!] Opción no válida.")
            vista.pausar()
