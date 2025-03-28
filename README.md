# Atlas Cansat 2025 - Mechatronics club of Fraser Heights Secondary School

# Main mission
Transmit barometric, temperature, and altitude data during descent <br />

# Secondary mission
Geographical imagery <br />

# For tinkers

## boot.py
File ran upon booting, configures which coordinator to run <br />

## screen.py
Manages screen module <br />

# Coordinators
All coordinators should have this at the beginning of the file,
```
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
```

## five_pebbles.py
Early development testing coordinator, used to test OLED screen responsiveness and update speed. <br />
