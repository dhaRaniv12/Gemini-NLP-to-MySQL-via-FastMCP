import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
apy = os.getenv('API_KEY')

client = genai.Client(api_key=apy)

while True:
    prompt = input("Ask a prompt? (Y to exit.) ")
    if prompt.strip() == 'Y' or prompt.strip() == 'y':
        break
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,)
    print(response.text)



