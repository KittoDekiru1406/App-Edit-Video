import cv2

def get_info_video(video):
    fps = int(video.get(cv2.CAP_PROP_FPS))
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = round(frame_count / fps)
    return fps, frame_count, duration