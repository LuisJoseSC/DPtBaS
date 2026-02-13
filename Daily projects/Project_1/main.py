import time
import sys
import threading
#Funciones encargadas de la animacion y el cursor.
def typewriter(text, delay = 0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    

def cursor_blink(stop_event: threading.Event, interval: float = 0.25, symbol: str = "▋"):
    visible = False
    while not stop_event.is_set():
        if visible:
            sys.stdout.write("\b \b")
        else:
            sys.stdout.write(symbol)
        sys.stdout.flush()
        visible = not visible
        time.sleep(interval)

    if visible:
        sys.stdout.write("\b \b")
        sys.stdout.flush()
    

#Texto.
texto = """
Bienvenido al proyecto 1:
Autor: Luis José Sánchez Carreño
Motivo: Diversión.
Descripción: Este proyecto fue construido con el mero interés de
aprender y explorar los límites del aprendizaje autónomo.

Opciones:
"""

#Controlador
stop_event = threading.Event()
cursor_thread = threading.Thread(target=cursor_blink, args= (stop_event,))

cursor_thread.start()
time.sleep(2)
stop_event.set()
cursor_thread.join()

typewriter(texto)

