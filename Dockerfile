FROM python:3.8

COPY . /src/app

WORKDIR /src/app

ENV PYTHONPATH "${PYTHONPATH}:/src/app"

RUN apt-get update

RUN apt-get -y install build-essential nghttp2 libnghttp2-dev

RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN apt-get install tesseract-ocr -y

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install -r requirements.txt

CMD ["python", "app.py"]
