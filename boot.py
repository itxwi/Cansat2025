import time,os,subprocess
#import screen

# configs
COORDINATOR = "cansat2025"
WAIT = 0

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COORDINATOR_PATH = os.path.join(BASE_DIR,"coordinators",f"{COORDINATOR}.py")


home = os.path.expanduser("~")
with open(os.path.join(home,"boot.log"), "a") as f:
    f.write(f"boot.py started! @{time.time()}\n")

# Program

if os.path.isfile(COORDINATOR_PATH):
    subprocess.run(['python3',COORDINATOR_PATH])

else:
    print(f"Error: Coordinator file {COORDINATOR_PATH} doesn't exist")