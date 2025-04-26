import cv2 as cv
import numpy as np
import math
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

# measurements of video to make it square


# start = offset
# stop = higher - offset
desired = int(min(width,height) * math.sqrt(2)/2) # desired size of the square video, accounting for rotations
y_offset =(height -  desired )//2
x_offset = (width -  desired )//2



# rotation tracking of the video

orb = cv.ORB_create(nfeatures=1000) # the guy that finds features for me

ret,previous = cap.read()

# stabilized video

output = cv.VideoWriter(path+"output.mp4",fourcc,fps,(desired,desired))


prev_gray = cv.cvtColor(previous, cv.COLOR_BGR2GRAY)
prev_keyp,prev_descr = orb.detectAndCompute(prev_gray, None) # finding features in first frame


total_rotation = 0 # rotation in case 

reference = prev_descr #reference in case no more features r found
while True:
    ret,cur =  cap.read()
    if not ret or cur is None:
        break



    cur_gray = cv.cvtColor(cur, cv.COLOR_BGR2GRAY)
    cur_keyp,cur_descr = orb.detectAndCompute(cur_gray, None) # finding features in current frame
    if cur_descr is None:
        print("failed")
        continue




    matcher = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True) # the guy that matches the features, using brute force stuffs

    matches = matcher.match(prev_descr,cur_descr) # matching!

    matches = sorted(matches,key=lambda x:x.distance) # sorting the matches by distance
    if len(matches) < 15: #if there are enough matches to work with, otherwise do nothing
        matches = matches[0:15]
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
            rotation_mtrx = cv.getRotationMatrix2D(center, -angle, 1.0) # getting the rotation matrix for total rotation
            stabilized = cv.warpAffine(cur, rotation_mtrx, (w, h)) # rotating the frame using the rotation matrix
        else:
            stabilized = cur # if there is no rotation, just use the current frame
                
    else:
        stabilized = cur # if there are not enough matches, just use the current frame
        print("Not enough matches")
    stabilized = stabilized[y_offset:y_offset+desired,x_offset:x_offset+desired] # cropping the frame to the desired size
    output.write(stabilized) # write the stabilized frame to the output video
cap.release()
output.release() # finished!

print("finished stabilizing!")





