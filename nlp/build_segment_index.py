import json
import os
import re

SEGMENTS_FILE = "results/segmented_embedding.txt"
KEYWORDS_FILE = "results/keywords.txt"
OUTPUT_FILE = "results/segments_final.json"

segments = []
current_segment = None

# ---------- Load keywords ----------
keywords_map = {}
if os.path.exists(KEYWORDS_FILE):
    with open(KEYWORDS_FILE, "r", encoding="utf-8") as f:
        for block in f.read().split("\n\n"):
            if "SEGMENT" in block:
                lines = block.strip().split("\n")
                seg_id = re.findall(r"\d+", lines[0])
                if seg_id:
                    keywords_map[seg_id[0]] = lines[-1].replace("Keywords:", "").strip()

# ---------- Parse segments ----------
with open(SEGMENTS_FILE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        # Detect any segment header format
        if re.search(r"SEGMENT\s*\d+", line):
            if current_segment:
                segments.append(current_segment)

            seg_id = re.findall(r"\d+", line)[0]
            current_segment = {
                "id": seg_id,
                "text": "",
                "keywords": keywords_map.get(seg_id, "N/A"),
            }

        else:
            if current_segment and line:
                current_segment["text"] += line + " "

# Add last segment
if current_segment:
    segments.append(current_segment)

# ---------- Generate titles ----------
for seg in segments:
    first_sentence = seg["text"].split(".")[0][:80]
    kw = seg["keywords"].split(",")[:2]
    kw_text = ", ".join(kw)

    seg["title"] = f"{first_sentence} ({kw_text})".strip()

# ---------- Save ----------
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(segments, f, indent=2)

print(f"✅ Final segment index saved to: {OUTPUT_FILE}")
print(f"📊 Total segments indexed: {len(segments)}")
