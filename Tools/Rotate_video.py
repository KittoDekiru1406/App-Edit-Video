import cv2

def rotate_video(Video, angle):
    ret, frame = Video.read()
    frame_width = int(Video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(Video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter("new_video.mp4", cv2.VideoWriter_fourcc(*"mp4v"), Video.get(cv2.CAP_PROP_FPS), (frame_width, frame_height))

    while True:
        success, frame1 = Video.read()
        center = (frame_width // 2, frame_height // 2)

        if not success:
            break
        M = cv2.getRotationMatrix2D(center, angle, 1)
        warped_frame = cv2.warpAffine(frame1, M, (frame_width, frame_height))
        out.write(warped_frame)

    out.release()
    return out