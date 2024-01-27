from Tools import *

st.title("Video Edit App")
video_file = st.file_uploader("Choose video file", type=["mp4", "avi", "mkv"], accept_multiple_files=False)
if video_file is not None:
    Video = load_video(video_file)
    st.video(video_file)
    st.header("Video Speed")
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    def change_video_speed(speed):
        change_speed(Video, speed)
        st.success("Video speed has been changed successfully!")
    
    button_speed_025 = col1.button("0.25x", on_click=lambda: change_video_speed(0.25))
    button_speed_05 = col2.button("0.5x", on_click=lambda: change_video_speed(0.5))
    button_speed_075 = col3.button("0.75x", on_click=lambda: change_video_speed(0.75))
    button_speed_125 = col4.button("1.25x", on_click=lambda: change_video_speed(1.25))
    button_speed_15 = col5.button("1.5x", on_click=lambda: change_video_speed(1.5))
    button_speed_175 = col6.button("1.75x", on_click=lambda: change_video_speed(1.75))
    button_speed_20 = col7.button("2.0x", on_click=lambda: change_video_speed(2.0))

    st.header("Video Rotate")
    rotate1, rotate2, rotate3, rotate4, rotate5, rotate6 = st.columns(6)
    def Rotate_video(angle):
        rotate_video(Video, angle)
        st.success("Video rotation has been successfully!")
    
    button_rotate_45 = rotate1.button("45°", on_click=lambda: Rotate_video(45))
    button_rotate_90 = rotate2.button("90°", on_click=lambda: Rotate_video(90))
    button_rotate_135 = rotate3.button("135°", on_click=lambda: Rotate_video(135))
    button_rotate_180 = rotate4.button("180°", on_click=lambda: Rotate_video(180))
    button_rotate_225 = rotate5.button("225°", on_click=lambda: Rotate_video(225))
    button_rotate_270 = rotate6.button("270°", on_click=lambda: Rotate_video(270))

    st.header("Video Cut")
    fps, frame_count, duration = get_info_video(Video)
    range_values = st.slider("Drag time to cut(second)", 0, duration, (0, duration), 5)
    def func_cut():
        start_time, end_time = range_values[0], range_values[1]
        cut_video(Video, start_time, end_time)
        st.success("Video cut success")
    button_cut = st.button("Cut", on_click=func_cut)

    st.header("Video Merge")
    st.markdown("Upload video of you wanna merge with above video")
    video_merge = st.file_uploader("Choose file video", type=["mp4", "avi", "mkv"], accept_multiple_files=False)
    if video_merge is not None:
        video_new_merge = load_video(video_merge)
        st.video(video_merge)


    st.header("Undo Edit")

    st.header("Export")
    def final_func():
        pass
    final_button = st.button("Download", on_click=final_func)


