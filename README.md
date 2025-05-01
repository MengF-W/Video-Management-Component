# Overall Idea
![image](https://github.com/user-attachments/assets/363bb3ca-b81e-41bb-9014-2d25273e7090)


The idea is to flow a process for the video management. 


# Video_Management_Component
The video management component act as a hub of video processing. It captures video sources (for example camera streaming,video files),manipulates video sources and produces the manipulation output. It can be interacted through communication interfaces. At the moment, the MotionJPEG(MJPEG) video playing and recording is available. The output of playing and recoding is exposed and returned to user interfaces through REST webservice   

# Libraries used
* OpenCV Python
* Flask

# How to Run
- `pip install --no-cache-dir --no-input -r requirements.txt` Install dependencies under the root directory:  
- `python app.py` Run the application under src directory
