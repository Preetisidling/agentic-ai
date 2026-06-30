from openai import OpenAI
client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {
            "role": "system",
            "content": "You are expert for maths, You should on ans for math related queries, for any other say, Sorry I can only answer math related queries"
        },
        {
            "role": "user",
            "content": "Hey where is Taj mahal located"
        }
    ]
)

print(response.choices[0].message.content)