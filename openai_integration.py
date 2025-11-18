import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt="Once upon a time",
  max_tokens=50
)

print(response.choices[0].text.strip())