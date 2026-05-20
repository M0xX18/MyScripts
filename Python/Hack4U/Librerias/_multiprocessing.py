#!/usr/bin/env python3

import multiprocessing
import time

def waiting(seconds):

    time.sleep(seconds)

    text = f"1 segundo" if seconds == 1 else f"{seconds} segundos"
    
    print(f"Esperamos {text} satisfactoriamente")

first_process = multiprocessing.Process(target=waiting, args=(2,))
second_process = multiprocessing.Process(target=waiting, args=(3,))

first_process.start()
second_process.start()

first_process.join()
second_process.join()
