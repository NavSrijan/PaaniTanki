import pyvirtualcam
from pyvirtualcam import PixelFormat
import cv2
import numpy as np

def showVideo(Path):
    video = cv2.VideoCapture(Path)
    #if not video.isOpened():
    #    raise ValueError("error opening video")

    length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)

    with pyvirtualcam.Camera(width, height, fps, fmt=PixelFormat.BGR) as cam:
        count = 0
        while True:
            # Restart video on last frame.
            if count == length:
                count = 0
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            # Read video frame.
            ret, frame = video.read()
            if not ret:
                raise RuntimeError('Error fetching frame')
            # Send to virtual cam.
            cam.send(frame)
            # Wait until it's time for the next frame
            cam.sleep_until_next_frame()
            count += 1

showVideo("trial.mp4")