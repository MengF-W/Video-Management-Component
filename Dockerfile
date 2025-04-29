FROM python:3.9-slim
RUN apt update && apt install -y build-essential wget libgl1 libglib2.0-0 libsm6 libxrender1 libxext6 && apt autoremove && apt clean
WORKDIR /video_management_component/src
COPY src/ /video_management_component/src/
COPY ./requirements.txt /video_management_component/requirements.txt

RUN pip install --no-cache-dir --no-input -r /video_management_component/requirements.txt

ENV PYTHONPATH /video_management_component
RUN echo "Make sure opencv is installed:"
RUN python -c "import cv2"
RUN echo "Make sure flask is installed:"
RUN python -c "import flask"

CMD ["python","/video_management_component/src/main.py"]