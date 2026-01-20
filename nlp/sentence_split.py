import nltk
import os

nltk.download('punkt')

INPUT_FILE = "data/final_transcript.txt"
OUTPUT_FILE = "data/sentences.txt"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# Split into sentences
sentences = nltk.sent_tokenize(text)

# Clean empty sentences
sentences = [s.strip() for s in sentences if s.strip()]

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for s in sentences:
        f.write(s + "\n")

print("Total sentences:", len(sentences))
print("Sentence file created at:", OUTPUT_FILE)
