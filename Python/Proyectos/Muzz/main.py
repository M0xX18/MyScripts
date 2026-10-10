import requests
import string
import signal
import sys
import threading
import time
from pwn import log
from termcolor import colored
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED

detener = threading.Event()

def def_handler(sig, frame):
    time.sleep(2)
    print(colored(f"\nSaliendo del programa...", "red"))
    detener.set()

signal.signal(signal.SIGINT, def_handler)

caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits

status_lock = threading.Lock()

estado = log.waitfor("Iniciando...")

def limpiar_status():
    sys.stdout.write("\r\033[K")
    sys.stdout.flush()

def actualizar_status(mensaje):
    with status_lock:
        sys.stdout.write(f"\r\033[K[TRY] {mensaje}")
        sys.stdout.flush()

def siguiente(nombre):
    indices = [caracteres.index(c) for c in nombre]
    i = len(indices) - 1

    while i >= 0:
        if indices[i] + 1 < len(caracteres):
            indices[i] += 1
            break
        indices[i] = 0
        i -= 1
    if i < 0:
        return None
    return ''.join(caracteres[n] for n in indices)

def probar(nombre):
    url = f"https://pastebin.com/{nombre}"

    try:
        with requests.get(url, timeout=3, stream=True) as r:
            if 200 <= r.status_code < 300:
                with status_lock:
                    sys.stdout.write("\r\033[K")
                    sys.stdout.flush()
                    log.success(f"HTTP {r.status_code}: {url}")
            else:
                actualizar_status(
                    f"Probando {nombre} | HTTP {r.status_code}"
                )

    except requests.RequestException:
        actualizar_status(f"Probando {nombre} | Fallido")

def generar_elementos(inicio):
    elemento = inicio

    while elemento is not None and not detener.is_set():
        yield elemento
        elemento = siguiente(elemento)

def main():
    max_threads = 10
    tareas_pendientes = set()
    executor = ThreadPoolExecutor(max_workers=max_threads)
    elementos = generar_elementos("QQ5ynU3A")

    try:
        while not detener.is_set():
            
            while (len(tareas_pendientes) < max_threads and not detener.is_set()):
                try:
                    elemento = next(elementos)
                except StopIteration:
                    break

                tareas_pendientes.add(executor.submit(probar, elemento))

            if tareas_pendientes:
                completadas, tareas_pendientes = wait(tareas_pendientes, timeout=0.2, return_when=FIRST_COMPLETED)

    finally:
        detener.set()
        for tarea in tareas_pendientes:
            tarea.cancel()

        executor.shutdown(wait=False, cancel_futures=True)
        print("Programa detenido.")

if __name__ == "__main__":
    main()
