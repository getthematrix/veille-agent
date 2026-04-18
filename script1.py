import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": "Dis bonjour en une phrase."}
        ]
)

result = response.choices[0].message.content

with open("report.txt", "w") as f:
    f.write(result)
