from dotenv import load_dotenv
import openai
import os
import json

load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Transcribe the audio file
# Need to LINK the file directory
audio_file= open("/Users/adrianlam/Downloads/noc.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

transcription = transcript

# Generate notes using OpenAI's API
prompt = "Create a bullet point note sheet of" + str(transcription)
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
notes = response.choices[0].text.strip()

with open('notes.txt', 'w') as f:
    f.write(str(notes)) #returns a .txt file 

