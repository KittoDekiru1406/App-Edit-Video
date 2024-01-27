import tempfile
import cv2

def load_video(file_content):
    # Lưu nội dung vào một file tạm thời
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_file.write(file_content.read())
    temp_file.close()

     # Mở video từ file tạm thời
    video = cv2.VideoCapture(temp_file.name)
    if not video.isOpened():
        raise FileNotFoundError
    
    return video