import flask
from flask import Flask, render_template

app = Flask(__name__,static_folder='static')

@app.route('/')
def index():
    # Specify the video file path
    video_path = '/static/khanyounes.mp4'
    
    # Render the HTML template with the video path
    return render_template('index.html', video_path=video_path)

if __name__ == '__main__':
    #To make it accessible from other machines on the network, you need 
    #to change the host binding to 0.0.0.0 when running your Flask app.
    app.run(host='0.0.0.0', port=5000, debug=True)

