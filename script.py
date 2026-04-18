import feedparser
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

KEYWORDS = [
    "underwater acoustics",
    "sonar signal processing",
    "underwater drone",
    "naval defense"
]

def is_relevant(text):
    return any(k.lower() in text.lower() for k in KEYWORDS)

def summarize(text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Expert en acoustique sous-marine et défense."},
            {"role": "user", "content": f"Résume en 5 lignes et explique l'intérêt:\n{text}"}
        ]
    )
    return response.choices[0].message.content

feed = feedparser.parse("https://export.arxiv.org/rss/eess.SP")

results = []

for entry in feed.entries[:5]:
    if is_relevant(entry.title + entry.summary):
        summary = summarize(entry.summary)
        results.append(f"## {entry.title}\n{summary}\n{entry.link}\n")

output = "\n\n".join(results)

with open("report.txt", "w") as f:
    f.write(output)
