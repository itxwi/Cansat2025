from picamzero import Camera


class rpiCam:
    def __init__(self, resolution, brightness = 0, contrast = 1, greyscale = False, white_balance = 'auto', gain = None, flips = (True,False)):
        self.brightness = brightness            # -1 ~ 1
        self.contrast = contrast                # 0 ~ 32
        self.greyscale = greyscale              # Bool
        self.white_balance = white_balance      # 'auto', 'tungsten', 'fluorescent', 'indoor' , 'daylight', 'cloudy'
        self.gain = gain                        # Int
        self.flips = flips                      # Vertical flip, Horizontal flip

        self.resolution = resolution
        self.current_camera = Camera(self.resolution,self.brightness,self.contrast,self.greyscale,self.white_balance,self.gain)

        self.current_camera.flip_camera(flips[0],flips[1])

    def get_camera(self):
        """
        when making any adjustments to the cameras resolution during program runtime, you will need to create a new instance of the camera
        """
        del self.current_camera
        self.current_camera = Camera(self.resolution,self.brightness,self.contrast,self.greyscale,self.white_balance,self.gain)
        self.current_camera.flip_camera(self.flips[0],self.flips[1])
        return self.current_camera
