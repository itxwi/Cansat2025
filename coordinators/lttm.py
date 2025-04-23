# coordinator requisit
print("launched")
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import camera
print("library called, takes time")

myCamera = camera.rpiCam((1000,1000))
# print("camera made")
# print("taking picture")
# myCamera.picture('nice')
# print("picture taken")
x=0
while True:
    x+=1
    print(f"taking video {x}")
    myCamera.video(f'test{x}',duration=10)
    print("video taken")
