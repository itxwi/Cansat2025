# Atlas Cansat 2025 - Mechatronics club of Fraser Heights Secondary School

# Main mission
Transmit barometric, temperture, and altitude data during descend

# Secondary mission
Geographical imagery and depth

# For tinkers

## Camera.py
Manages camera module
Contains text class for text on images
createText function creates text with default settings
createImage takes picture from camera

## Gyro.py
Manages gyroscope module
calibrateAccel function calibrates accelerometer
calibrateGyro function calibrates gyroscope
It is reccommened to keep the module still during calibration
Default rounds to nearest tenth, +- .1 error
Not reccomended to use temperture data

## Radio.py
Manages radio module
Contained in class

## Screen.py
Manages screen module
Contained in class

## Sensor.py
Manages sensor module
Temp, altitude, pressure

# Helper.py
Contains helper functions
Mostly involving data management

# Data organization
state.json - config files as to which coordinator program to run, will contain orientation and velocity in future
log.json - dictionary, UTC time stamp followed by gyro data and sensor data