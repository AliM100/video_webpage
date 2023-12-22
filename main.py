import flask
from flask import Flask, render_template
from flask_ngrok import run_with_ngrok
import os

app = Flask(__name__,static_folder='static')
run_with_ngrok(app)

video_index = 0
video_folder = 'static/'
# Specify the video file path
video_files = [file for file in os.listdir(video_folder) if file.endswith(('.mp4', '.webm', '.ogg'))]

@app.route('/')
def index():
    return render_template('index.html', video_files=video_files, video_index=video_index)

@app.route('/next_video', methods=['POST'])
def next_video():
    global video_index
    video_index = (video_index + 1) % len(video_files)
    return render_template('index.html', video_files=video_files, video_index=video_index)

if __name__ == '__main__':
   # app.run(host='0.0.0.0', port=5000, debug=True)
    app.run()
