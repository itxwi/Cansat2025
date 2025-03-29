import time,os,subprocess
import screen

# configs
COORDINATOR = "lttm"
WAIT = 1

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COORDINATOR_PATH = os.path.join(BASE_DIR,"coordinators",f"{COORDINATOR}.py")

# Program
screen_on = False
try:
    OLED = screen.OLED()
    screen_on = True
except:
    pass
if screen_on:
    OLED.clear_image()
    OLED.draw_font(f"Atlas {COORDINATOR}", (0,32))
    OLED.display()
time.sleep(WAIT)
if screen_on:
    OLED.clear_image()
    OLED.display()

if os.path.isfile(COORDINATOR_PATH):
    subprocess.run(['python3',COORDINATOR_PATH])

else:
    print(f"Error: Coordinator file {COORDINATOR_PATH} doesn't exist")
    if screen_on:
        OLED.draw_font("Coordinator Path Error", (0,32))
        OLED.display()