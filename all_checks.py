#!/usr/bin/env python3

import os
import sys
import shutil

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



def main():
    if reboot_exit():
        print("reboot is pending?")
        sys.exit(1)
    if check_disk_full(disk="/", min_gb=2, min_percant=10):
        print("disk full for your infomration")
        sys.exit(1)
    print("Everything] OK!")
    sys.exit(0)


main()
