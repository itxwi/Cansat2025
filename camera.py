from picamzero import Camera
import os


class rpiCam:
    def __init__(self, resolution, brightness = 0, contrast = 1, greyscale = False, white_balance = 'auto', flips = (True,False)):
        self.brightness = brightness            # -1 ~ 1
        self.contrast = contrast                # 0 ~ 32
        self.greyscale = greyscale              # Bool
        self.white_balance = white_balance      # 'auto', 'tungsten', 'fluorescent', 'indoor' , 'daylight', 'cloudy'
        self.flips = flips                      # Vertical flip, Horizontal flip
        self.resolution = resolution

        self.current_camera = Camera()

        self.current_camera.video_size = resolution
        self.current_camera.still_size = resolution
        self.current_camera.brightness = self.brightness
        self.current_camera.contrast = self.contrast
        self.current_camera.greyscale = self.greyscale
        self.current_camera.white_balance = self.white_balance

        self.current_camera.flip_camera(flips[0],flips[1])

    def get_camera(self):
        """
        when making any adjustments to the cameras resolution during program runtime run this function
        """

        self.current_camera.video_size = self.resolution
        self.current_camera.still_size = self.resolution
        self.current_camera.brightness = self.brightness
        self.current_camera.contrast = self.contrast
        self.current_camera.greyscale = self.greyscale
        self.current_camera.white_balance = self.white_balance

        self.current_camera.flip_camera(self.flips[0],self.flips[1])
        return self.current_camera


    def picture(self, name):
        """
        Take a photo. Ensures the directory exists before saving.
        """
        directory = os.path.abspath(os.path.join(os.path.dirname(__file__), 'camera_data/photos'))
        if not os.path.exists(directory):
            os.makedirs(directory) 

        path = os.path.join(directory, f'{name}.jpg')
        self.current_camera.take_photo(path)

    def video(self, name, duration=180000):
        """
        Take a video. Ensures the directory exists before saving. Duration is in ms.
        """
        directory = os.path.abspath(os.path.join(os.path.dirname(__file__), 'camera_data/videos'))
        if not os.path.exists(directory):
            os.makedirs(directory)  

        path = os.path.join(directory, f'{name}.mp4')
        self.current_camera.take_video(path, duration)