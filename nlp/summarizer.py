import re
from sklearn.feature_extraction.text import TfidfVectorizer

INPUT = "results/segmented_embedding.txt"
OUTPUT = "results/segment_summaries.txt"

with open(INPUT, "r", encoding="utf-8") as f:
    content = f.read()

segments = re.split(r"--- SEGMENT \d+ ---", content)
segments = [s.strip() for s in segments if s.strip()]

summaries = []

print("Generating summaries for", len(segments), "segments...")

for idx, segment in enumerate(segments):
    sentences = segment.split(". ")
    
    if len(sentences) <= 2:
        summary = segment
    else:
        vectorizer = TfidfVectorizer(stop_words="english")
        X = vectorizer.fit_transform(sentences)
        scores = X.sum(axis=1).A1

        top_sent = sentences[scores.argmax()]
        summary = top_sent.strip()

    summaries.append(f"SEGMENT {idx+1}:\nSummary: {summary}\n")

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write("\n".join(summaries))

print("Summarization completed.")
print("Saved at:", OUTPUT)
