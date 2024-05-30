#!/usr/bin/env python3
# Author ID: 160637229

import subprocess

def free_space():
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, shell=True)
    output = p.communicate()[0]
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
