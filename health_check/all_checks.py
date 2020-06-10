#!/usr/bin/env python3

import os
import sys
import shutil
import socket
import psutil

def reboot_exit():
    """Returns True if reboot file exit- reset"""
    return os.path.exists("/run/reboot-required/")

def check_disk_full(disk, min_gb, min_percant):
    """Check if the disk is full or not"""
    du = shutil.disk_usage(disk)
    # calculate the percantage of free
    percent_free = 100 * du.free / du.total
    # calculate how many giga bytes are free
    gigabytes_free = du.free / 2 ** 30

    if percent_free < min_percant  or gigabytes_free < min_gb:
        return True
    return False

def check_root_full():
    """Returns True if roo partition is full, False otherwise"""
    return check_disk_full(disk="/", min_gb=2, min_percant=10)

def check_network():
    """Retruns True if the network is available"""
    try:
        socket.gethostname("www.google.com")
        return True
    except:
        return False

def check_cpu_constrain():
    return psutil.cpu_percent(1) > 75
def main():
    checks = [
        (reboot_exit, "disk is full"),
        (check_root_full, "root partition full"),
        (check_network, "there is no network"),
        (check_cpu_constrain, "cpu is so huge"),
    ]
    everything_OK = True
    for check, msg in checks:
        if check():
            print(msg)
            everything_OK = False

        if not everything_OK:
            sys.exit(1)
    print("Everything OK!")
    sys.exit(0)


main()
