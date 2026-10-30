import numpy as np
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing. Add it to your .env file.")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


sentences = [
    "How many leaves do employees get per year?",
    "What is the annual vacation policy?",
    "The cat sat on the mat.",
]
res = client.embeddings.create(model="gemini-embedding-001", input=sentences)
v = [np.array(d.embedding) for d in res.data]

def cos(a, b): return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))
print("leaves vs vacation:", cos(v[0], v[1]))   # high
print("leaves vs cat:", cos(v[0], v[2]))        # low