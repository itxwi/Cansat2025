# Run this program upon booting
import Helper
import subprocess

coordinator_path = Helper.getState()['coordinator']
subprocess.run(['python3', coordinator_path])