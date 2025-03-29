# coordinator requisit
print("launched")
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import camera
print("library called, takes time")

myCamera = camera.rpiCam()
print("camera made")
print("taking picture")
myCamera.picture('nice')
print("picture taken")
print("taking video")
myCamera.video('fun',duration=1000)
print("video taken")
