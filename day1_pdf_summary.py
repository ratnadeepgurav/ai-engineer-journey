from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing. Add it to your .env file.")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

text = "".join(p.extract_text() for p in PdfReader("Ratnadeep_Gurav.pdf").pages)
print("Characters:", len(text))

r = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "Summarize in 5 bullet points. Only use the given text."},
        {"role": "user", "content": text[:12000]},
    ],
)
print(r.choices[0].message.content)