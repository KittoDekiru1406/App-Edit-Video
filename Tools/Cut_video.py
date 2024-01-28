# import cv2
from moviepy.editor import VideoFileClip

def cut_video(video, start_time, end_time):
    '''
        The function is used to cut a video. Returns about a new video cut
    '''
    # fps = video.get(cv2.CAP_PROP_FPS)
    # start_frame = int(start_time * fps)
    # end_frame = int(end_time * fps)
    # # Đặt con trỏ đọc video về khung hình bắt đầu
    # video.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    # frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    # frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # out = cv2.VideoWriter("new_video.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (frame_width, frame_height))

    # for FrameNum in range(start_frame, end_frame + 1):
    #     success, frame = video.read()
    #     if not success: 
    #         break
    #     out.write(frame)

    # video.release()
    # out.release()
    # return out

    cut_clip = video.subclip(start_time, end_time)
    # cut_clip.write_videofile("new_video.mp4", codec = 'libx264', audio_codec = 'aac')
    return cut_clip
