#!/usr/bin/env python
"""
Hardware control using PyVISA.
"""

import pyvisa

rm = pyvisa.ResourceManager("@sim")

print(rm.list_resources())


rm.close()