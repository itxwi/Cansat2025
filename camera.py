from picamzero import Camera
import os
import subprocess

class rpiCam:
    def __init__(self,resolution,brightness=0,contrast=1,greyscale=False,white_balance='auto',flips=(True, False)):
        self.brightness = brightness
        self.contrast = contrast
        self.greyscale = greyscale
        self.white_balance = white_balance
        self.flips = flips
        self.resolution = resolution

        self.current_camera = Camera()

        self.current_camera.video_size = resolution
        self.current_camera.still_size = resolution
        self.current_camera.brightness = self.brightness
        self.current_camera.contrast = self.contrast
        self.current_camera.greyscale = self.greyscale
        self.current_camera.white_balance = self.white_balance

        self.current_camera.flip_camera(flips[0], flips[1])

    def get_camera(self):
        self.current_camera.video_size = self.resolution
        self.current_camera.still_size = self.resolution
        self.current_camera.brightness = self.brightness
        self.current_camera.contrast = self.contrast
        self.current_camera.greyscale = self.greyscale
        self.current_camera.white_balance = self.white_balance

        self.current_camera.flip_camera(self.flips[0], self.flips[1])
        return self.current_camera

    def picture(self, name):
        directory = os.path.abspath(os.path.join(os.path.dirname(__file__), 'camera_data/photos'))
        if not os.path.exists(directory):
            os.makedirs(directory)

        path = os.path.join(directory, f'{name}.jpg')
        self.current_camera.take_photo(path)

    def video(self, name, duration=10):
        """
        Takes a video and saves it as H264.
        """

        # Define the directory for saving videos
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'camera_data/videos'))
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

        # Ensure that the file name is correctly formed with .h264 extension
        h264_path = os.path.join(base_dir, f'{name}.h264')

        # Capture the video in H264 format
        self.current_camera.take_video(h264_path, duration)