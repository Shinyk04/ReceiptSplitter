from openai import OpenAI
import os
import base64
from dotenv import load_dotenv

load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")
apiKey = os.getenv("OPENAI_SECRET")
org = os.getenv("ORGANIZATION_KEY")

client = OpenAI(api_key=apiKey)
image_path = "Receipts/rec_1.jpg"

with open(image_path, "rb") as img_file:
    image_bytes = img_file.read()
    b64_image = base64.b64encode(image_bytes).decode("utf-8")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Extract all text from this image. Return only the transcription formatted to match the layout."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{b64_image}"
                    }
                }
            ]
        }
    ]
)


#client = OpenAI(api_key=apiKey, organization=org)
# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages = [
#         {"role": "system", "content": "You are a poetic assistant skilled in explaining complex programming concepts with creative flair."},
#         {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#     ]
# )


# response = openai.Completion.create(
#   engine="text-davinci-003",
#   prompt="Once upon a time",
#   max_tokens=50
# )
print("\n--- TRANSCRIPTION ---\n")
print(response.choices[0].message.content)