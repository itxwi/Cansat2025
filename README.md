# Atlas Cansat 2025  
**Mechatronics Club of Fraser Heights Secondary School**

## Main Mission
Transmit barometric, temperature, and altitude data during descent.

## Secondary Mission
Capture geographical imagery.

---

## For Tinkerers

### `boot.py`
This file is executed automatically when the system boots. It is responsible for selecting and running the appropriate coordinator script.  
- **Configuration**:  
  - The `COORDINATOR` variable specifies which coordinator script to execute.  
  - The `WAIT` variable introduces a delay (in seconds) before the coordinator script is executed. This can be useful for ensuring that all hardware components are properly initialized before running the script.  
- **Error Handling**: If the specified coordinator file does not exist, an error message is displayed.  
- **Usage**: Modify the `COORDINATOR` variable to point to the desired coordinator script.

### `screen.py`
This module manages the OLED screen using the Adafruit SSD1306 library.  
- **Features**:  
  - **`__init__`**: Initializes the OLED screen with a specified font size and prepares the in-memory image for drawing.  
  - **`clear_image`**: Clears both the physical screen and the in-memory image, resetting the drawing context.  
  - **`display`**: Displays the current in-memory image on the physical OLED screen.  
  - **`draw_point`**: Draws a single point on the in-memory image at a specified position.  
  - **`draw_font`**: Draws text on the in-memory image at a specified position using the initialized font.  
- **Usage**: Import the `OLED` class and use its methods to interact with the screen for graphical or textual output.

---

## Coordinators
All coordinators should include the following snippet at the beginning of the file to ensure proper module imports:
```python
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
```

### `five_pebbles.py`
An early development testing coordinator used to test OLED screen responsiveness and update speed.
