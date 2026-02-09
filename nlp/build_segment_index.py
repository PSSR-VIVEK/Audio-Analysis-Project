import json
import csv
from pathlib import Path
from textblob import TextBlob

EMBEDDING_FILE = "results/segmented_embedding.txt"
SUMMARY_FILE = "results/segment_summaries.txt"
KEYWORD_FILE = "results/segment_keywords.csv"
OUTPUT_FILE = "results/segments_final.json"

# ------------------------
# Load embedding segments
# ------------------------

print("📥 Loading embedding segments...")

segments = []
current_id = None
current_text = []

with open(EMBEDDING_FILE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        # Match: --- SEGMENT 12 ---
        if line.startswith("--- SEGMENT"):
            if current_id is not None:
                segments.append({
                    "id": str(current_id),
                    "text": " ".join(current_text).strip()
                })

            current_id = (
                line.replace("---", "")
                .replace("SEGMENT", "")
                .replace("-", "")
                .strip()
            )

            current_text = []

        elif line:
            current_text.append(line)

    # last segment
    if current_id is not None:
        segments.append({
            "id": str(current_id),
            "text": " ".join(current_text).strip()
        })

print(f"📊 Total embedding segments: {len(segments)}")

if len(segments) == 0:
    print("❌ ZERO segments parsed — stopping.")
    exit()

# ------------------------
# Load summaries
# ------------------------

summaries = {}

if Path(SUMMARY_FILE).exists():
    print("📄 Loading summaries...")

    with open(SUMMARY_FILE, "r", encoding="utf-8") as f:
        current = None
        buffer = []

        for line in f:
            line = line.strip()

            if line.startswith("SEGMENT"):
                if current:
                    summaries[current] = " ".join(buffer)

                current = (
                    line.replace("SEGMENT", "")
                    .replace(":", "")
                    .strip()
                )

                buffer = []

            else:
                buffer.append(line)

        if current:
            summaries[current] = " ".join(buffer)

else:
    print("⚠ No summary file found.")

# ------------------------
# Load keywords CSV
# ------------------------

keywords = {}

if Path(KEYWORD_FILE).exists():
    print("🔑 Loading keywords...")

    with open(KEYWORD_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            seg_id = row["Segment"].strip()
            kw = row["Keywords"].strip()
            keywords[seg_id] = kw

else:
    print("⚠ No keyword CSV found.")

# ------------------------
# Merge everything + sentiment
# ------------------------

final_segments = []

print("🧠 Running sentiment analysis...")

for seg in segments:
    sid = seg["id"]
    text = seg["text"]

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    label = (
        "Positive" if polarity > 0.1 else
        "Negative" if polarity < -0.1 else
        "Neutral"
    )

    final_segments.append({
        "id": sid,
        "title": text[:80] + "...",
        "text": text,
        "summary": summaries.get(sid, ""),
        "keywords": keywords.get(sid, ""),
        "sentiment": label,
        "sentiment_score": round(polarity, 3)
    })

# ------------------------
# Save JSON
# ------------------------

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(final_segments, f, indent=2)

print(f"✅ Final segment index saved to: {OUTPUT_FILE}")
print(f"📊 Total segments indexed: {len(final_segments)}")
