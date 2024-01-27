import cv2

def cut_video(video, start_time, end_time):
    fps = video.get(cv2.CAP_PROP_FPS)
    start_frame = int(start_time * fps)
    end_frame = int(end_time * fps)
    # Đặt con trỏ đọc video về khung hình bắt đầu
    video.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out = cv2.VideoWriter("new_video.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (frame_width, frame_height))

    for FrameNum in range(start_frame, end_frame + 1):
        success, frame = video.read()
        if not success: 
            break
        out.write(frame)

    video.release()
    out.release()
    return out
        