#!/usr/bin/env python 
"""
Search algorithms for active alignment; searches for the laser beam's global maxima for optimal coupling.  

Gayatri 10/2026
"""

class AlignmentSearch:
    def __init__(self, power_meter, stage_handle):
        self.pm = power_meter
        self.stage = stage_handle

    def hill_climbing(self, grid):
        print(grid)



