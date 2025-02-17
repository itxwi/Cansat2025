from picamzero import Camera
import cv2
import numpy as np
import json
import os

class Text:
    def __init__(self,text,font,color ,scale,thick,pos,bgcolor):
        self.text = text
        self.font = font
        self.color = color #RGBA
        self.scale = scale
        self.thick=thick
        self.pos=pos
        self.bgcolor = bgcolor

def createText(text,font='plain1',color=(255,255,255,255) ,scale=3,thick=3,pos=(0,0),bgcolor=None):
    return Text(text=text,font=font,color=color,scale=scale,thick=thick,pos=pos,bgcolor=bgcolor)

def createImage(brightness=0, contrast = 1, greyscale = False, resolution = (128,128), name = 'image.jpg', txt = None, array = False):
    myCam = Camera()
    myCam.brightness = brightness # -1 ~ 1
    myCam.contrast = contrast # 0 ~ 32
    myCam.greyscale = greyscale # Bool
    myCam.still_size = resolution # Tuple

    myCam.flip_camera(vflip=True)
    if txt:
        myCam.annotate(text=txt.text,font=txt.font,color=txt.color,scale=txt.scale,thickness=txt.thick,position=txt.pos,bgcolor=txt.bgcolor)

    myCam.take_photo(f'{os.getcwd()}/images/{name}')

    if array:
        image_array = myCam.capture_array()
        with open(f'{os.getcwd()}/images/array.json', 'w') as json_file:
            json.dump(image_array.tolist(), json_file)

#createImage(array=True,resolution=(25,25),greyscale=True)