import cv2

def change_speed(video, speed):
    original_fps = video.get(cv2.CAP_PROP_FPS)
    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    video_write = cv2.VideoWriter("new_video.mp4", cv2.VideoWriter_fourcc(*"mp4v"), original_fps * speed, (frame_width, frame_height))

    while True:
        success, frame = video.read()
        if not success:
            break
        video_write.write(frame)

    video.release()
    video_write.release()
    return video_write
