#!/usr/bin/env python
# 
import in_place
import sys 

with in_place.InPlace(sys.argv[1]) as gcode: 
    for line in gcode:
        if line.startswith("M104"):
            gcode.write("")
        elif line.startswith("M109"):
            gcode.write("")
        else:
            gcode.write(line)