import streamlit as st
from moviepy.editor import ImageClip, AudioFileClip

st.title("Ghép Ảnh + Audio thành Video 🎬")

# Upload file
image_file = st.file_uploader("Chọn ảnh (JPG/PNG)", type=["jpg", "jpeg", "png"])
audio_file = st.file_uploader("Chọn audio (MP3/WAV)", type=["mp3", "wav"])

if image_file and audio_file:
    if st.button("Tạo video"):
        # Lưu file tạm
        with open("temp_audio.mp3", "wb") as f:
            f.write(audio_file.read())
        with open("temp_image.png", "wb") as f:
            f.write(image_file.read())

        # Load audio & ảnh
        audio = AudioFileClip("temp_audio.mp3")
        duration = audio.duration
        clip = ImageClip("temp_image.png").set_duration(duration)

        # Gắn audio
        final = clip.set_audio(audio)

        # Xuất video
        output_file = "output.mp4"
        final.write_videofile(output_file, fps=24)

        # Cho tải video
        with open(output_file, "rb") as f:
            st.download_button("📥 Tải video", f, file_name="output.mp4")
