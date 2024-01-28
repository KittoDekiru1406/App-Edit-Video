# import cv2
from moviepy.editor import VideoFileClip

def change_speed(video, speed):
    '''
        The function changes the speed of the video. Return about new video with speed changed
    '''
    # original_fps = video.get(cv2.CAP_PROP_FPS)
    # frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    # frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # video_write = cv2.VideoWriter("new_video.mp4", cv2.VideoWriter_fourcc(*"mp4v"), original_fps * speed, (frame_width, frame_height))

    # while True:
    #     success, frame = video.read()
    #     if not success:
    #         break
    #     video_write.write(frame)

    # video.release()
    # video_write.release()
    # return video_write

    new_video = video.speedx(factor = speed)    
    # new_video.write_videofile("new_video.mp4", codec = 'libx264', audio_codec = 'aac')
    return new_video