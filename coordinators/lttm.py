# coordinator requisit
import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import camera

myCamera = camera.rpiCam((1000,1000))

myCamera.picture()
