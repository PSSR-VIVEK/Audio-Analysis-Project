# Podcast AI Project

An automated pipeline for analyzing podcast audio using AI. This project processes raw audio, transcribes it using OpenAI's Whisper model, and aims to perform NLP analysis (keywords, summarization) in future updates.

## 🚀 Features

- **Audio Preprocessing Pipeline**:
  - Auto-conversion of MP3/WAV to compatible formats.
  - Resampling to 16kHz.
  - Noise reduction and audio normalization.
  - Smart chunking (30s) for efficient processing.
- **ASR (Automatic Speech Recognition)**:
  - Transcribes audio chunks using OpenAI's Whisper model (`base` model).
  - Outputs transcriptions in JSON format.

## 📂 Project Structure

```
├── app/                  # Web application (Upcoming)
├── asr/                  # Automatic Speech Recognition modules
│   └── transcribe.py     # Whisper transcription script
├── data/                 # Data storage
│   ├── raw_audio/        # Input directory for MP3/WAV files
│   ├── processed_audio/  # Cleaned 16kHz chunked audio
│   └── transcripts/      # Output JSON transcripts
├── nlp/                  # NLP Analysis (Upcoming: Summarization, Topic Segmentation)
├── preprocessing/        # Audio processing scripts
│   └── pipeline.py       # Main preprocessing pipeline
└── requirements.txt      # Python dependencies
```

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/PSSR-VIVEK/Audio-Analysis-Project.git
   cd Audio-Analysis-Project
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: You may need to install [FFmpeg](https://ffmpeg.org/download.html) separately if you encounter audio loading issues, though `soundfile` handles most formats natively.*

## 🏃 Usage

### 1. Preprocessing
Place your raw podcast files (`.mp3` or `.wav`) in `data/wav_clean` (or configure `RAW` path in `preprocessing/pipeline.py`).

Run the pipeline to clean and chunk the audio:
```bash
python preprocessing/pipeline.py
```
Output chunks will be saved to `data/processed_audio`.

### 2. Transcription
Transcribe the processed audio chunks:
```bash
python asr/transcribe.py
```
JSON transcripts will be saved to `data/transcripts`.

## 🔮 Roadmap

- [ ] Implement NLP Summarization & Keyword Extraction.
- [ ] Build interactive Web App (Streamlit/Flask).
- [ ] Add Topic Segmentation.
