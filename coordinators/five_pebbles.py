# coordinator requisit
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import screen

OLED = screen.OLED()
OLED.drawFont("hello world", (15,15))