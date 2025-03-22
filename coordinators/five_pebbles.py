# coordinator requisit
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# dependencies
import time
import screen

OLED = screen.OLED()

OLED.clear_image()

def type_write(word,delay=.02):
    cur_word = ''
    for letter in word:
        time.sleep(delay)
        cur_word+=letter
        OLED.draw_font(cur_word,(0,32))
        OLED.display()

while True:
    OLED.clear_image()
    type_write("whats up, world!")
    OLED.clear_image()
    OLED.draw_font("what what what what", (0,32))
    OLED.display()
    time.sleep(.02)
    OLED.clear_image()
    OLED.draw_font("atlas mechatronics team", (0,32))
    OLED.display()
    time.sleep(.02)
    OLED.clear_image()
    OLED.draw_font("westgate technology", (0,32))
    OLED.display()
    time.sleep(.02)
    OLED.clear_image()
    OLED.draw_font("3.14159", (0,32))
    OLED.display()
    time.sleep(.02)