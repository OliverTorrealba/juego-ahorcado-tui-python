import json
import os
import random

# Banco de 5 palabras del juego
PALABRAS = ["zorro", "python", "fennec", "arduino", "Milo"]

ARCHIVO_GUARDADO = "partida_guardada.json"

class Partida:
    """Modela el estado y la lógica de una partida del juego."""
    def __init__(self, palabra_secreta, palabra_oculta=None, intentos_restantes=6, fallos=0, letras_usadas=None):
        self.palabra_secreta = palabra_secreta.upper()
        self.palabra_oculta = palabra_oculta if palabra_oculta is not None else ["_"] * len(self.palabra_secreta)
        self.intentos_restantes = intentos_restantes
        self.fallos = fallos
        self.letras_usadas = letras_usadas if letras_usadas is not None else []

    def intentar_letra(self, letra):
        """
        Procesa el intento de una letra.
        Retorna: 'repetida', 'acierto' o 'fallo'.
        """
        letra = letra.upper()
        if letra in self.letras_usadas:
            return "repetida"

        self.letras_usadas.append(letra)

        if letra in self.palabra_secreta:
            for idx, char in enumerate(self.palabra_secreta):
                if char == letra:
                    self.palabra_oculta[idx] = letra
            return "acierto"
        else:
            self.intentos_restantes -= 1
            self.fallos += 1
            return "fallo"

    def ha_ganado(self):
        return "_" not in self.palabra_oculta

    def ha_perdido(self):
        return self.intentos_restantes <= 0

    def a_diccionario(self):
        """Convierte los datos de la partida a un diccionario para serializar en JSON."""
        return {
            "palabra_secreta": self.palabra_secreta,
            "palabra_oculta": self.palabra_oculta,
            "intentos_restantes": self.intentos_restantes,
            "fallos": self.fallos,
            "letras_usadas": self.letras_usadas
        }

    @classmethod
    def desde_diccionario(cls, datos):
        """Reconstruye una partida a partir de un diccionario."""
        return cls(
            palabra_secreta=datos["palabra_secreta"],
            palabra_oculta=datos["palabra_oculta"],
            intentos_restantes=datos["intentos_restantes"],
            fallos=datos["fallos"],
            letras_usadas=datos["letras_usadas"]
        )


def crear_nueva_partida():
    """Selecciona aleatoriamente una de las 5 palabras e inicia la partida."""
    palabra = random.choice(PALABRAS)
    return Partida(palabra)


def guardar_partida(partida):
    """Guarda el estado actual de la partida en un archivo JSON."""
    try:
        with open(ARCHIVO_GUARDADO, "w", encoding="utf-8") as f:
            json.dump(partida.a_diccionario(), f, indent=4, ensure_ascii=False)
        return True
    except IOError:
        return False


def cargar_partida():
    """
    Carga la partida guardada si existe.
    Retorna la instancia de Partida o None si no hay archivo.
    """
    if not os.path.exists(ARCHIVO_GUARDADO):
        return None
    try:
        with open(ARCHIVO_GUARDADO, "r", encoding="utf-8") as f:
            datos = json.load(f)
        return Partida.desde_diccionario(datos)
    except (IOError, json.JSONDecodeError, KeyError):
        return None


def eliminar_partida_guardada():
    """Elimina el archivo guardado cuando la partida concluye (victoria o derrota)."""
    if os.path.exists(ARCHIVO_GUARDADO):
        try:
            os.remove(ARCHIVO_GUARDADO)
        except OSError:
            pass
