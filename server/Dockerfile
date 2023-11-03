# Start by pulling the python image
FROM python:3.10

#copy requirements file
COPY . /app/ 

#change current working directory
WORKDIR /app

#update pip.
RUN pip install --upgrade pip

#pip install requirements file
RUN pip install -r ./requirements.txt

#Update Ubuntu application package manager
RUN apt-get update

#Install requirements for PyAudio
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y
RUN apt-get install -y pulseaudio

#Install PyAudio
RUN pip install pyaudio

CMD [ "python", "main.py" ]
