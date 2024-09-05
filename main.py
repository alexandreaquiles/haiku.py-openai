from openai import OpenAI
import openai
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "Você é um poeta brasileiro com herança japonesa que escreve poemas no estilo haiku.\nVocê deve escrever apenas uma estrofe. Use muitos emojis."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Gere um poema sobre a fumaça no Brasil em 2024."
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=1800,
  response_format={
    "type": "text"
  }
)

haiku = response.choices[0].message.content
print(haiku)

speech_file_path = "haiku.mp3"
response = openai.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input=haiku
)
response.stream_to_file(speech_file_path)
