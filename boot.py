import time,os,subprocess

# configs
COORDINATOR = "five_pebbles"
WAIT = 5

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COORDINATOR_PATH = os.path.join(BASE_DIR,"coordinators",f"{COORDINATOR}.py")

time.sleep(WAIT)

if os.path.isfile(COORDINATOR_PATH):
    subprocess.run(['python3',COORDINATOR_PATH])
else:
    print(f"Error: Coordinator file {COORDINATOR_PATH} doesn't exist")