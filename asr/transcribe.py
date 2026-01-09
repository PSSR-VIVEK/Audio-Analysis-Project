import whisper
import os
import json

AUDIO_DIR = "data/processed_audio"
OUT_DIR = "data/transcripts"
os.makedirs(OUT_DIR, exist_ok=True)

print("Loading Whisper model...")
model = whisper.load_model("base")

for file in os.listdir(AUDIO_DIR):
    if not file.endswith(".wav"):
        continue

    out_file = file.replace(".wav", ".json")
    out_path = os.path.join(OUT_DIR, out_file)

    # Skip if already transcribed
    if os.path.exists(out_path):
        continue

    print("Transcribing:", file)

    audio_path = os.path.join(AUDIO_DIR, file)
    result = model.transcribe(audio_path)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

print("All remaining transcriptions completed.")
