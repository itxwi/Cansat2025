# Atlas Cansat 2025 - Mechatronics club of Fraser Heights Secondary School

# Main mission
Transmit barometric, temperture, and altitude data during descend

# Secondary mission
Geographical imagery and depth

# For tinkers

## Camera.py
Manages camera module <br />
Contains text class for text on images <br />
createText function creates text with default settings <br />
createImage takes picture from camera

## Gyro.py
Manages gyroscope module <br />
calibrateAccel function calibrates accelerometer <br />
calibrateGyro function calibrates gyroscope <br />
It is reccommened to keep the module still during calibration <br />
Default rounds to nearest tenth, +- .1 error <br />
Not reccomended to use temperture data 

## Radio.py
Manages radio module <br />
Contained in class

## Screen.py
Manages screen module <br />
Contained in class

## Sensor.py
Manages sensor module <br />
Temp, altitude, pressure

# Helper.py
Contains helper functions <br />
Mostly involving data management

# Data organization
state.json - config files as to which coordinator program to run, will contain orientation and velocity in future <br />
log.json - dictionary, UTC time stamp followed by gyro data and sensor data