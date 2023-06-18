import os
import openai
from pydub import AudioSegment
from moviepy.editor import VideoFileClip, AudioFileClip
import speech_recognition as sr
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_file():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return jsonify(error='No file part in the request'), 400

    file = request.files['file']

    # If the user does not select a file, the browser might
    # submit an empty file part without a filename, so check for this case
    if file.filename == '':
        return jsonify(error='No selected file'), 400

    # Save the file to a temporary location
    temp_file_path = os.path.join('/tmp', file.filename)
    file.save(temp_file_path)

    # Convert the file to text
    text = convert_to_text(temp_file_path)

    # Convert the text to notes
    notes = convert_to_notes(text)

    # Clean up the temporary file
    os.remove(temp_file_path)

    # Return the notes as a JSON response
    return jsonify(notes=notes)

    # Connect to the database (this will create it if it doesn't exist)
    conn = sqlite3.connect('my_database.db')

    # Create a cursor object
    c = conn.cursor()

    # Create a table (this only needs to be done once)
    c.execute('''
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY,
            response TEXT
        )
    ''')

    # Insert the chatGPT_response into the table
    c.execute('INSERT INTO responses (response) VALUES (?)', (chatGPT_response,))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def convert_to_text(file_path):
    if file_path.lower().endswith('.mp3'):
        save_audio(file_path)
        return transcribe_audio(file_path)
    elif file_path.lower().endswith('.mp4'):
        save_video(file_path)
        mp3_file_path = file_path.rsplit('.', 1)[0] + '.mp3'
        convert_mp4_to_mp3(file_path, mp3_file_path)
        return transcribe_audio(mp3_file_path)
    elif file_path.lower().endswith('.txt'):
        with open(file_path, 'r') as file:
            return file.read()
    else:
        return None

def convert_to_notes(text):
    response = send_to_chatGPT(text)
    return get_chat_response(response)

if __name__ == '__main__':
    app.run(port=5000)

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

def send_to_chatGPT(user_input):
    messages = [
        {'role': 'system', 'content': 'You are a tutor. Your job is to create notes based on the text I give you.'},
        {'role': 'user', 'content': user_input}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4.0",
        messages=messages
    )
    return response

def get_chat_response(response):
    chatGPT_response = response.choices[0].message.content
    return chatGPT_response