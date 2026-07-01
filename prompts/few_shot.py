from openai import OpenAI

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

print("FEW-SHOT PROMPT DEMO: SENTIMENT CLASSIFICATION")
print()

# Few-shot prompt: provide examples before asking for actual classification
few_shot_prompt = """Classify the sentiment of these product reviews as POSITIVE, NEGATIVE, or NEUTRAL.

Example 1:
Review: "This product is amazing! Works perfectly and arrived quickly."
Sentiment: POSITIVE

Example 2:
Review: "Terrible quality. Broke after one day."
Sentiment: NEGATIVE

Example 3:
Review: "It's an okay product. Nothing special but does the job."
Sentiment: NEUTRAL

Now classify this review:
Review: "Love it! Best purchase I've made this year. Highly recommend to everyone!"
Sentiment:"""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": few_shot_prompt}],
    temperature=0
)

sentiment = response.choices[0].message.content.strip()
print(f"Classification: {sentiment}")
print()

# Another few-shot example with different task
print("FEW-SHOT PROMPT DEMO: EXTRACT ENTITIES")
print()

entity_prompt = """Extract the person's name and age from these sentences.

Example 1:
Text: "Sarah is 28 years old and works as a software engineer."
Name: Sarah
Age: 28

Example 2:
Text: "My friend Michael, who is 35, just started a new business."
Name: Michael
Age: 35

Now extract from this:
Text: "John is 42 and has been in the industry for over 15 years."
Name:
Age:"""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": entity_prompt}],
    temperature=0
)

entities = response.choices[0].message.content.strip()
print(entities)
print()

# Few-shot with format specification
print("FEW-SHOT PROMPT DEMO: JSON RESPONSE FORMAT")
print()

json_prompt = """Convert customer feedback into structured JSON.

Example 1:
Feedback: "The app is slow and crashes frequently"
Output: {"issue": "performance", "severity": "high", "description": "slow and crashes"}

Example 2:
Feedback: "Great UI design, very intuitive"
Output: {"issue": "design", "severity": "low", "description": "great UI and intuitive"}

Convert this feedback:
Feedback: "Customer support was unhelpful and rude"
Output:"""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": json_prompt}],
    temperature=0
)

json_output = response.choices[0].message.content.strip()
print(json_output)
