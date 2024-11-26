from asgiref.sync import async_to_sync
# Create your views here.
from django import forms
import json, os, uuid
from channels.generic.websocket import WebsocketConsumer
from pydub import AudioSegment
import speech_recognition as sr
import subprocess
import time,sys




class CustomWebsocketConsumer(WebsocketConsumer):
    def loading_animation(self, duration=15):
        animation = ['|', '/', '--', '\\']
        end_time = time.time() + duration
        idx = 0

        while time.time() < end_time:
            # Print the current frame of the animation and flush it immediately
            sys.stdout.write(f"\rLoading {animation[idx % len(animation)]}")
            sys.stdout.flush()

            # Pause for a short time to simulate animation speed
            time.sleep(0.1)

            # Move to the next frame
            idx += 1

        # Print a final message after the loading animation ends
        sys.stdout.write("\rLoading complete!\n")
    def connect(self):
        self.room_name = "test"
        self.room_group_name = "test_group"
        async_to_sync(self.channel_layer.group_add)(self.room_name, self.room_group_name)
        self.accept()
        self.send(text_data="Websocket connected")
        # return super().connect()

    def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            try:
                with open('received_audio.webm', 'ab') as f:
                    f.write(bytes_data)
                print("Raw audio data saved as 'received_audio.webm'.")
                self.send("Data stored successfully")
            except Exception as e:
                self.send(text_data=json.dumps({
                    'error': f"Error: {str(e)}"
                }))

    def close(self, code=None, reason=None):
        self.send(text_data="Connection is closede")
    
    def disconnect(self, code):
        print("code:::::::::::::", code)
        # try:
        #     uuid4 = uuid.uuid4()
        #     audio_file_path = f'test.wav'
        #     command = [
        #         'ffmpeg', 
        #         '-i', "received_audio.webm",  # Input file (webm)
        #         '-vn',  # Skip video
        #         '-acodec', 'pcm_s16le',  # Audio codec (use wav format)
        #         '-ar', '44100',  # Audio sampling rate (44.1kHz)
        #         '-ac', '2', '-y', # Number of audio channels (stereo)
        #         audio_file_path  # Output audio file
        #     ]
        #     subprocess.run(command, check=True)
        #     os.remove("received_audio.webm")
        # except Exception as e:
        #     print(e)
        # print("Generating transcription.........................")
        # self.loading_animation()
        # recognizer = sr.Recognizer()
        
        # with sr.AudioFile("test.wav") as source:
        #     audio_data = recognizer.record(source)  # Read the entire audio file

        #     try:
        #         # Recognize and transcribe the audio using Google's Speech Recognition API
        #         text = recognizer.recognize_google(audio_data)
        #         print("Transcription: " + text)
        #     except sr.UnknownValueError:
        #         print("Google Speech Recognition could not understand the audio")
        #     except sr.RequestError as e:
        #         print(f"Could not request results from Google Speech Recognition service; {e}")
        return super().disconnect(code)