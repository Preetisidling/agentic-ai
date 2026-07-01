from openai import OpenAI

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

print("CHAIN OF THOUGHT DEMO: MATH PROBLEM")
print()

# Chain of thought: ask model to show step-by-step reasoning
math_prompt = """Solve this step by step:

If a store sells 3 apples for $5, and you buy 12 apples, how much will you spend?

Think through this step by step:
Step 1: Figure out how many groups of 3 are in 12
Step 2: Calculate the total cost
Final Answer:"""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": math_prompt}],
    temperature=0
)

answer = response.choices[0].message.content.strip()
print("Math Problem Solution:")
print(answer)
print()

# Chain of thought for logic puzzle
print("CHAIN OF THOUGHT DEMO: LOGIC PUZZLE")
print()

logic_prompt = """Solve this logic puzzle step by step:

Alice, Bob, and Charlie have different colored cars: red, blue, and green.
- Alice's car is not blue
- Bob's car is not green
- Charlie's car is red

Who has which color car?

Think step by step:
Step 1: What do we know for certain?
Step 2: What can we deduce next?
Step 3: Final deduction
Answer:"""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": logic_prompt}],
    temperature=0
)

logic_answer = response.choices[0].message.content.strip()
print("Logic Puzzle Solution:")
print(logic_answer)
print()

# Chain of thought for decision making
print("CHAIN OF THOUGHT DEMO: DECISION MAKING")
print()

decision_prompt = """Help me decide whether to buy a laptop.

Consider these factors:
- Price: $1200
- My budget: $1500
- I need it for work
- Current laptop works but is 5 years old
- This model has great reviews

Should I buy it? Think through the pros and cons:
Step 1: List the pros
Step 2: List the cons
Step 3: Weigh the decision
Final Recommendation:"""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": decision_prompt}],
    temperature=0
)

decision = response.choices[0].message.content.strip()
print("Decision Analysis:")
print(decision)
print()

# Chain of thought for code debugging
print("CHAIN OF THOUGHT DEMO: CODE DEBUG")
print()

code_prompt = """Debug this Python code:

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total = total + num
    average = total / len(numbers)
    return average

result = calculate_average([10, 20, 30])
print(result)  # Expected output: 20, but getting 0

What's wrong? Think step by step:
Step 1: Trace through the code
Step 2: Identify the issue
Step 3: Explain the fix
Solution:"""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": code_prompt}],
    temperature=0
)

debug = response.choices[0].message.content.strip()
print("Code Debug Analysis:")
print(debug)
print()

# Chain of thought for content analysis
print("CHAIN OF THOUGHT DEMO: TEXT ANALYSIS")
print()

analysis_prompt = """Analyze the sentiment and tone of this customer review:

"The product arrived damaged. Packaging was terrible. Tried to contact support but no response for 2 weeks.
When they finally replied, they were dismissive of my concerns."

Analyze step by step:
Step 1: Identify emotional indicators
Step 2: Assess overall sentiment
Step 3: Determine the tone and urgency
Step 4: Recommend action
Analysis:"""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": analysis_prompt}],
    temperature=0
)

analysis = response.choices[0].message.content.strip()
print("Text Analysis:")
print(analysis)
