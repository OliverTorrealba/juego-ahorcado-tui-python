======= Juego del Ahorcado (Edición Zorrito) - TUI en Python

Un clásico juego del ahorcado para terminal (**TUI - Text User Interface**) desarrollado en **Python**, implementando una arquitectura de software limpia basada en el patrón de diseño **MVC (Modelo - Vista - Controlador)**.

A diferencia del ahorcado tradicional, en esta versión el dibujo en arte ASCII corresponde a un **zorrito** que se va completando pieza por pieza con cada intento fallido hasta llegar a las 6 vidas máximas.

---

======= Características

- **Arquitectura MVC**: Separación estricta entre la lógica del juego (`modelo.py`), la interfaz de usuario (`vista.py`) y el orquestador (`controlador.py`).
- **Arte ASCII Progresivo**: 7 etapas visuales del zorrito (desde el terreno despejado, orejas, rostro, cuerpo, patitas, hasta la cola esponjosa y expresión de derrota).
- **Sistema de Pausa y Persistencia (Guardar / Cargar)**:
  - Posibilidad de pausar la partida en cualquier turno escribiendo `P`.
  - Guardado del estado completo en formato **JSON** (`partida_guardada.json`).
  - Carga automática de partidas incompletas desde el menú principal.
- **Banco de Palabras**: Selección aleatoria integrada (`zorro`, `python`, `fennec`, `arduino`, `milo`).
- **Sin Dependencias Externas**: Desarrollado 100% con la biblioteca estándar de Python.

---

======= Estructura del Proyecto

```text
Juego_ahorcado_py/
│
├── main.py          # Punto de entrada de la aplicación
├── modelo.py        # Modelo: Lógica de la partida, palabras y guardado JSON
├── vista.py         # Vista: Dibujos ASCII, menús interactivos y pantallas
├── controlador.py   # Controlador: Manejo de flujo, pausas y validaciones
├── .gitignore       # Archivos ignorados por Git
└── README.md        # Documentación del proyecto
```

---

======= Cómo Ejecutar el Juego

### Requisitos
- Python 3.8 o superior instalado en el sistema.

### Ejecución
Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
python main.py
```

---

======= Controles en el Juego

- **`1 - 4`**: Navegación por los menús principales.
- **`A - Z`**: Ingreso de letras para adivinar la palabra secreta.
- **`P` o `PAUSA`**: Abrir el menú de pausa durante una partida activa para guardar o salir.

---

======= Tecnologías Utilizadas

- **Lenguaje**: Python 3
- **Patrón de Arquitectura**: MVC (Model-View-Controller)
- **Persistencia**: JSON (`json`, `os`)
- **Interfaz**: Terminal User Interface (TUI) con códigos ANSI y compatibilidad multiplataforma.
