from io import BytesIO
from moviepy.editor import VideoFileClip

def download_video(video):
    '''
    The function is used to 
    '''
    temp_file = "temp_video.mp4"
    video.write_videofile(temp_file, codec='libx264', audio_codec='aac')
    
    # Đọc nội dung của tệp tạm thời
    with open(temp_file, "rb") as f:
        video_buffer = BytesIO(f.read())

    return video_buffer