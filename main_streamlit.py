import streamlit as st
import os

def main():
    st.title("Video Player with Streamlit")

    # Specify the folder path where video files are stored
    video_folder = 'static/'

    # Get a list of all video files in the folder
    video_files = [file for file in os.listdir(video_folder) if file.endswith(('.mp4', '.webm', '.ogg'))]

    # Display the video player
    video_index = st.button('Next Video')
    
    if video_index and video_index < len(video_files) - 1:
        video_index += 1

 
    video_path = os.path.join(video_folder, video_files[video_index])
    
    st.video(video_path)

if __name__ == '__main__':
    main()
