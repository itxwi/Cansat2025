import cv2 as cv
import numpy as np
import sys
import os


path = os.path.dirname(os.path.abspath(__file__)) + "\\"
print(path, "is th path") 



#debug point comment
cap = cv.VideoCapture(path+"rotated.mp4")

if not cap.isOpened():
    print("Error when opening sdfasdf")
    sys.exit(1)
else:
    print("Video opened successfully")

# Get FPS
fps = cap.get(cv.CAP_PROP_FPS)

# init fourcc

fourcc = cv.VideoWriter_fourcc(*'mp4v')

# Get dimensions of video
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# Cropping video to make it square

if width > height:
    offset = (width - height) // 2 # offset to crop the video
    lower = height # lower bound of the crop
    higher = width # higher bound of the crop
else:
    offset = (height - width) // 2
    higher = height
    lower = width # higher bound of the crop

start = offset
stop = higher - offset

square_video = cv.VideoWriter(path+"original_square.mp4",fourcc,fps,(lower,lower)) #square frame of video
while True:
    ret,frame = cap.read()

    
    if not ret:
        print("End of video")
        break
    if higher==width: # if the video is wider than it is tall
        cropped = frame[0:lower, offset:higher-offset]
    else:
        cropped = frame[offset:higher-offset, 0:lower] #cropping each frame
    cv.waitKey(1)

    square_video.write(cropped) #append cropped frame to video



cap.release() # dont need it anymore
square_video.release() # finished cropping the video
square_video = cv.VideoCapture(path+"original_square.mp4")
print("finished cropping")

# rotation tracking of the video

orb = cv.ORB_create(nfeatures=1000) # the guy that finds features for me

ret,previous = square_video.read()

# stabilized video

output = cv.VideoWriter(path+"output.mp4",fourcc,fps,(min(width,height),min(width,height)))


prev_gray = cv.cvtColor(previous, cv.COLOR_BGR2GRAY)
prev_keyp,prev_descr = orb.detectAndCompute(prev_gray, None) # finding features in first frame

total_rotation = 0 # rotation as the video progresses


while True:
    ret,cur = square_video.read()
    if not ret:
        break


    cur_gray = cv.cvtColor(cur, cv.COLOR_BGR2GRAY)
    cur_keyp,cur_descr = orb.detectAndCompute(cur_gray, None) # finding features in current frame

    matcher = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True) # the guy that matches the features, using brute force stuffs
    matches = matcher.match(prev_descr,cur_descr) # matching!
    matches = sorted(matches,key=lambda x:x.distance) # sorting the matches by distance
    if len(matches) > 10: #if there are enough matches to work with, otherwise do nothing
        previous_points = np.float32([prev_keyp[m.queryIdx].pt for m in matches]) # getting the points from the previous frame
        current_points = np.float32([cur_keyp[m.trainIdx].pt for m in matches]) # getting the points from the current frame
        
        #reshaping the points so they are a 2D array of points

        previous_points = previous_points.reshape(-1,1,2)
        current_points = current_points.reshape(-1,1,2)
        
        # finding rotation
        mtrx, mask = cv.estimateAffinePartial2D(previous_points, current_points) # finding the transformation matrix (some linear algebra stuff)
        if mtrx is not None: # if there is a rotation
            angle = np.arctan2(mtrx[1,0],mtrx[0,0]) * (180/np.pi) # finding the angle of rotation in degrees
            total_rotation += angle # adding the angle to the total rotation

            # rotating the frame
            h, w = cur.shape[:2]
            center = (w//2, h//2)
            rotation_mtrx = cv.getRotationMatrix2D(center, angle, 1.0) # getting the rotation matrix for total rotation
            stabilized = cv.warpAffine(cur, rotation_mtrx, (w, h)) # rotating the frame using the rotation matrix
        else:
            stabilized = cur # if there is no rotation, just use the current frame
                
    else:
        stabilized = cur # if there are not enough matches, just use the current frame
    output.write(stabilized) # write the stabilized frame to the output video
output.release() # finished!

print("finished stabilizing!")





