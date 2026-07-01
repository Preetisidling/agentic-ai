from openai import OpenAI

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

print("PERSONA-BASED PROMPT DEMO: TEACHER vs STUDENT")
print()

# Same question, but as a teacher
teacher_prompt = """You are an experienced high school teacher with 15 years of experience.
A student asks you: "Why is Python useful for beginners?"

Respond as a teacher would to a student."""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": teacher_prompt}],
    temperature=0.7
)

teacher_response = response.choices[0].message.content.strip()
print("Teacher's Answer:")
print(teacher_response)
print()

# Same question, but as a student
student_prompt = """You are a curious high school student learning programming for the first time.
Ask someone experienced: "Why is Python useful for beginners?"

Ask as a student would."""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": student_prompt}],
    temperature=0.7
)

student_response = response.choices[0].message.content.strip()
print("Student's Perspective:")
print(student_response)
print()

print("PERSONA-BASED PROMPT DEMO: TECHNICAL EXPERT vs CASUAL FRIEND")
print()

# As a technical expert
expert_prompt = """You are a senior software architect with 20+ years of experience.
Someone asks: "How should I structure my web application?"

Answer as a technical expert would."""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": expert_prompt}],
    temperature=0.7
)

expert_response = response.choices[0].message.content.strip()
print("Technical Expert's Answer:")
print(expert_response)
print()

# As a casual friend
friend_prompt = """You are a friendly developer chatting with a friend over coffee.
Your friend asks: "How should I structure my web application?"

Answer casually, like friends do."""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": friend_prompt}],
    temperature=0.7
)

friend_response = response.choices[0].message.content.strip()
print("Casual Friend's Answer:")
print(friend_response)
print()

print("PERSONA-BASED PROMPT DEMO: BUSINESS CONSULTANT vs CREATIVE WRITER")
print()

# As a business consultant
consultant_prompt = """You are a business strategy consultant.
A startup founder asks: "How do I grow my SaaS product?"

Answer as a business consultant would, focusing on strategy and metrics."""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": consultant_prompt}],
    temperature=0.7
)

consultant_response = response.choices[0].message.content.strip()
print("Business Consultant's Answer:")
print(consultant_response)
print()

# As a creative writer
writer_prompt = """You are a creative storyteller and novelist.
Someone asks: "How do I grow my SaaS product?"

Answer creatively, using vivid metaphors and narrative techniques."""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": writer_prompt}],
    temperature=0.7
)

writer_response = response.choices[0].message.content.strip()
print("Creative Writer's Answer:")
print(writer_response)
print()

print("PERSONA-BASED PROMPT DEMO: SCIENTIST vs ARTIST")
print()

# As a scientist
scientist_prompt = """You are a research scientist with a PhD in computer science.
Question: "What is artificial intelligence?"

Explain it scientifically with precision and technical accuracy."""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": scientist_prompt}],
    temperature=0.7
)

scientist_response = response.choices[0].message.content.strip()
print("Scientist's Explanation:")
print(scientist_response)
print()

# As an artist
artist_prompt = """You are a creative digital artist and visual thinker.
Question: "What is artificial intelligence?"

Explain it using visual metaphors and artistic concepts."""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": artist_prompt}],
    temperature=0.7
)

artist_response = response.choices[0].message.content.strip()
print("Artist's Perspective:")
print(artist_response)
print()

print("PERSONA-BASED PROMPT DEMO: MENTOR vs COMPETITOR")
print()

# As a mentor
mentor_prompt = """You are a senior mentor who genuinely wants to help junior developers succeed.
A junior developer asks: "What skills should I focus on?"

Answer as a supportive mentor would."""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": mentor_prompt}],
    temperature=0.7
)

mentor_response = response.choices[0].message.content.strip()
print("Mentor's Advice:")
print(mentor_response)
print()

# As a competitor
competitor_prompt = """You are someone competing in the same field as another developer.
They ask: "What skills should I focus on?"

Answer based on your competitive perspective."""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[{"role": "user", "content": competitor_prompt}],
    temperature=0.7
)

competitor_response = response.choices[0].message.content.strip()
print("Competitor's Perspective:")
print(competitor_response)
