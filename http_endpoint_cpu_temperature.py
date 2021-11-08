#! /usr/bin/python3

import json
from gpiozero import CPUTemperature

print('Content-Type: text/plain')
print('')

cpu = CPUTemperature()

print(cpu.temperature)