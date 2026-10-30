import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing. Add it to your .env file.")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

r = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[{"role": "user", "content": "You are a strict teacher"}],
    temperature=1,
)
print(r.choices[0].message.content)
print("Tokens used:", r.usage)