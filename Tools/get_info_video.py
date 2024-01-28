# import cv2
from moviepy.editor import VideoFileClip

def get_info_video(video):
    '''
        The function returns duration of video
    '''
    # fps = int(video.get(cv2.CAP_PROP_FPS))
    # frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    # duration = round(frame_count / fps)
    # return fps, frame_count, duration
    return round(video.duration)