#!/usr/bin/env python3
"""Coping files on the local system"""
import shutil

def main():
    shutil.copyfile('/home/student/pyna/pyfy/ciscoex.json', '/home/student/pyna/pyfy/ciscoex.json.bkup')
    # that was easy!

main()
