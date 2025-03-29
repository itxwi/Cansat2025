# coordinator requisit
print("launched")
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import camera
print("camera libarieid")

myCamera = camera.rpiCam()
print("camera made, takin picture")
myCamera.picture('nice')
print("picture taken")