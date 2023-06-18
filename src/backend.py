import openai
openai.api_key = "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"

audio_file= open("/path/to/file/german.mp3", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)
