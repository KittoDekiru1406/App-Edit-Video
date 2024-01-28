# import cv2
from moviepy.editor import VideoFileClip, concatenate_videoclips

def merge_video(video_merge_1, video_merge_2):
    '''
        The function is used to merge two video files. Return about video files merged
    '''
    # fps = video_merge_1.get(cv2.CAP_PROP_FPS)
    # frame_width = int(video_merge_1.get(cv2.CAP_PROP_FRAME_WIDTH))
    # frame_height = int(video_merge_1.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # output = cv2.VideoWriter("new_video.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (frame_width, frame_height))

    # while True:
    #     success, frame = video_merge_1.read()
    #     if not success:
    #         break
    #     output.write(frame)
    # while True:
    #     success1, frame1 = video_merge_2.read()
    #     if not success1:
    #         break
    #     output.write(frame1)
        
    # video_merge_1.release()
    # video_merge_2.release()
    # output.release()
    # return output
    final_clip = concatenate_videoclips([video_merge_1, video_merge_2], method = "compose")

    # final_clip.write_videofile("new_video.mp4", codec='libx264', audio_codec='aac')
    return final_clip