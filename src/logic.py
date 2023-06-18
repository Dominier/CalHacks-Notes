import os
import openai
from pydub import AudioSegment
from moviepy.editor import VideoFileClip, AudioFileClip
import speech_recognition as sr

def save_audio(audio_file_path):
    audio = AudioSegment.from_mp3(audio_file_path)
    print(f"Loaded audio file of duration {len(audio)} ms")

def save_video(video_file_path):
    video = VideoFileClip(video_file_path)
    print(f"Loaded video file of duration {video.duration} s")

def convert_mp4_to_mp3(mp4_file_path, mp3_file_path):
    audio = AudioFileClip(mp4_file_path)
    audio.write_audiofile(mp3_file_path)

def transcribe_audio(audio_file_path):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text

def gen_notes(user_input):
    messages = [
        {'role': 'system', 'content': 'You are a tutor. Your job is to create notes based on the text I give you.'},
        {'role': 'user', 'content': 'Take notes based on the text given.' + user_input}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4.0",
        messages=messages
    )
    return response

def gen_test(user_input):
    messages = [
        {'role': 'system', 'content': 'You are a teacher. Your job is to create tests based on the text I give you.'},
        {'role': 'user', 'content': 'Make a multiple choice question test based on this information:' + user_input}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4.0",
        messages=messages
    )
    return response

def get_chat_response(user_input):
    response = gen_notes(user_input)
    chatGPT_response = response.choices[0].message.content
    return chatGPT_response

# Usage
save_audio('input.mp3')
save_video('input.mp4')
convert_mp4_to_mp3('input.mp4', 'output.mp3')
transcribed_text = transcribe_audio('output.mp3')
chat_response = gen_notes(transcribed_text)
print(chat_response)
chat_response = gen_test(transcribed_text)
print(chat_response)