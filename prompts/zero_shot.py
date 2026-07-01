from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

print("ZERO-SHOT PROMT DEMO: SUMMARIZE TEXT")
print("=" * 70)

long_text = """
Python is a high-level programming language known for its simplicity and readability.
It was created in 1989 by Guido van Rossum. Python supports multiple programming paradigms
including procedural, object-oriented, and functional programming. It is widely used in
web development, data science, artificial intelligence, and automation. Python has a large
community and extensive libraries that make it popular among developers and scientists.
"""

# Zero-shot prompt: just ask for summary, no examples
summarize_prompt = f"""Summarize the following text in 2 sentences:

{long_text}

Summary:"""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": summarize_prompt}],
    temperature=0
)

summary = response.choices[0].message.content
print(f"Original text length: {len(long_text)} characters")
print(f"\nSummary: {summary}")