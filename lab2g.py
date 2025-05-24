#!/usr/bin/env python3
# Author: Festus Othuke Uwhumiakpo
# Author ID: fouwhumiakpo@myseneca.ca
# Date Created: 2025/05/23

import sys

# Check if an argument is given
if len(sys.argv) == 2:
    timer = int(sys.argv[1])  # use the number provided
else:
    timer = 3  # default value

while timer != 0:
    print(timer)
    timer -= 1

print("blast off!")
