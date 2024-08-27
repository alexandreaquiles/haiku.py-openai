from openai import OpenAI
from dotenv import load_dotenv
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
  temperature=0,
  max_tokens=1800,
  response_format={
    "type": "text"
  }
)

print(response.choices[0].message.content)