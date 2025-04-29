from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from src.core import video

_app = Flask(__name__)
CORS(_app, expose_headers=["Content-Disposition"])


@_app.route('/play', methods=['POST'])
def play():
    print("playing video url")

    verified_playable_url = video.play(request.get_json()['video_url'])

    response = jsonify({"playable_url": verified_playable_url})

    return response

@_app.route('/record', methods=['POST'])
def record():
    print("processing video recording")

    video_file,video_file_name = video.process_video_recording(request.get_json()['video_url'])

    return send_file(video_file, mimetype='video/mp4', as_attachment=True,
                     download_name=video_file_name)

def start():
    _app.run(port=5000, debug=True, threaded=True)