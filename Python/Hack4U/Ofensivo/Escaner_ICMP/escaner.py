#!/usr/bin/env python3

import argparse
import re
import subprocess
import signal
import sys
from concurrent.futures import ThreadPoolExecutor
from termcolor import colored


def def_handler(sig, frame):
    print(colored(f"\nSaliendo del programa...", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def get_arguments():
    parser = argparse.ArgumentParser(description="Esta utilidad permite escanear dispositivos activos en una red usando ICMP.")
    parser.add_argument("-t", "--target", required=True, dest="target_str", help="Host o rango de red a escanear")

    args = parser.parse_args()

    return args.target_str

def parse_targets(target_str):
    target_splitted = target_str.split(".")
    target_first_part = ".".join(target_splitted[:3])
    targets = target_splitted[-1]
    
    if len(target_splitted) == 4:
        if "-" in targets:
            target_range = targets.split("-")
            start, end = target_range
            return [f"{target_first_part}.{i}" for i in range(int(start), int(end)+1)]

        else:
            return [target_str]
    
    else:
        print(colored(f"El formato o rango de la IP no es correcto", "red"))

def host_discover(target):
    try:
        ping = subprocess.run(["ping", "-c", "1", target], timeout=1, stdout=subprocess.DEVNULL)
        if ping.returncode == 0:
            print(colored(f"La IP -> {target} esta activa!", "green"))
    
    except subprocess.TimeoutExpired:
        pass

def main():
    target_str = get_arguments()
    targets = parse_targets(target_str)

    max_threads = 100

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(host_discover, targets)

if __name__ == "__main__":
    main()
