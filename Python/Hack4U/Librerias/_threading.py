#!/usr/bin/env python3

import threading
import time

def waiting(seconds):

    time.sleep(seconds)
    
    text = f"1 segundo" if seconds == 1 else f"{seconds} segundos"
    
    print(f"Esperamos {text} satisfactoriamente")

initial_thread = threading.Thread(target=waiting, args=(1,))
first_thread = threading.Thread(target=waiting, args=(2,))
second_thread = threading.Thread(target=waiting, args=(3,))
third_thread = threading.Thread(target=waiting, args=(4,))

initial_thread.start()
first_thread.start()
second_thread.start()
third_thread.start()

initial_thread.join()
first_thread.join()
second_thread.join()
third_thread.join()

print(f"Tiempos de espera completados!")
