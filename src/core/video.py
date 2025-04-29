import os
import time
from collections import deque
from datetime import datetime
import cv2
from io import BytesIO

_frame_per_second_dict = {}
_recording_duration_in_seconds = 20
_video_files_folder = os.path.join(os.path.normpath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), os.path.normpath("resources"), os.path.normpath("recorded_video_files_storage"))

def play(url: str) -> bool:

    print("verifying if the video url is playable")
    if _frame_per_second_dict.get(url) is None:
        check_url_player = cv2.VideoCapture(url)
        playable_url = None

        success, frame = check_url_player.read()

        if success:
            print("The video url is playable")
            playable_url = True
            check_frame_per_second(url, check_url_player)
        else:
            print("The video url is not playable")
            playable_url = False

        check_url_player.release()

        return playable_url
    else:
        print("The video url is playable")
        playable_url = True
        return playable_url

def check_frame_per_second(url: str,check_url_player: cv2.VideoCapture) -> bool:

    print("checking the video's frames per second")

    global _frame_per_second_dict

    frames_number = 30

    start = time.time()

    for i in range(0, frames_number):
        check_url_player.read()

    end = time.time()

    seconds = end - start

    result = frames_number / seconds

    print("The video is about " + str(round(result)) + " frame per second")

    _frame_per_second_dict.update({url:round(result)})

def process_video_recording(url: str)-> [bytes,str]:

    frames_deque = deque()

    collect_video_frame_player = cv2.VideoCapture(url)

    number_recording_frames = _recording_duration_in_seconds * _frame_per_second_dict.get(url)

    for count in range(0, number_recording_frames):
        success_status, frame = collect_video_frame_player.read()

        if success_status:
            frames_deque.append(frame)
        else:
            break

    return record_video(url, collect_video_frame_player, frames_deque)

def record_video(url : str, collect_video_frame_player : cv2.VideoCapture,frames_deque : deque) -> [bytes,str]:

    video_file_name = 'video_recorded_at_' + str(datetime.now().strftime("%Y.%m.%d_%H%M%S")) + ".mp4"
    video_writer = cv2.VideoWriter(os.path.join(_video_files_folder, video_file_name), cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), _frame_per_second_dict.get(url),
                                   (int(collect_video_frame_player.get(cv2.CAP_PROP_FRAME_WIDTH)), int(collect_video_frame_player.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    for frame in frames_deque:
        video_writer.write(frame)
    video_writer.release()
    frames_deque.clear()

    video_file_bytes = BytesIO()
    with open(os.path.join(_video_files_folder, video_file_name), "rb") as file:
        video_file_bytes.write(file.read())
    video_file_bytes.seek(0)

    print("the video recording is done. returning back the video file")
    return video_file_bytes,video_file_name

