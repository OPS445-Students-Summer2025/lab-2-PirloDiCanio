#!/usr/bin/env python3
# Author: Festus Othuke Uwhumiakpo
# Author ID: fouwhumiakpo@myseneca.ca
# Date Created: 2025/05/23

import sys

timer = int(sys.argv[1])  # Get the first argument and turn it into a number

while timer != 0:
    print(timer)
    timer -= 1  # Reduce timer by 1

print("blast off!")
