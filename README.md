# 🎙️ Automated Podcast Transcription & Analysis Project

An end-to-end AI-powered pipeline for podcast audio analysis. This project processes raw audio, transcribes it using OpenAI's Whisper model, performs topic segmentation, generates summaries, extracts keywords, analyzes sentiment, and presents everything through an interactive web dashboard.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Table of Contents
- [Features](#-features)
- [Project Timeline](#-project-timeline)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Technologies Used](#-technologies-used)
- [Results](#-results)

---

## ✨ Features

### 🎵 Audio Processing (Week 1-2)
- **Audio Preprocessing Pipeline**:
  - Auto-conversion of MP3/WAV to compatible formats
  - Resampling to 16kHz for optimal ASR performance
  - Noise reduction and audio normalization
  - Smart chunking (30s segments) for efficient processing

### 🗣️ Speech Recognition (Week 1-2)
- **ASR (Automatic Speech Recognition)**:
  - Transcribes audio using OpenAI's Whisper model (`base` model)
  - Processes 30-second chunks for memory efficiency
  - Outputs transcriptions in JSON format
  - Handles 2,847+ audio segments

### 📊 NLP Analysis (Week 3-4)
- **Topic Segmentation**:
  - Baseline segmentation using sentence boundaries
  - Advanced embedding-based segmentation
  - Identifies distinct discussion topics within podcasts
  
- **Text Summarization**:
  - Generates concise 2-3 sentence summaries per segment
  - Uses BART-large-CNN transformer model
  - Resumable processing for large datasets
  
- **Keyword Extraction**:
  - TF-IDF based keyword extraction
  - Top 5 keywords per segment
  - CSV output for easy analysis

### 🎨 Visualization Dashboard (Week 5)
- **Interactive Web Application**:
  - Built with Streamlit framework
  - Interactive timeline with color-coded sentiment
  - Clickable segment navigation with pagination
  - Real-time keyword cloud generation
  - Comprehensive segment detail view

- **Sentiment Analysis**:
  - TextBlob-based sentiment scoring
  - Positive/Negative/Neutral classification
  - Visual color coding (🟢 Positive, 🔴 Negative, 🔵 Neutral)
  - Sentiment scores from -1.0 to +1.0

### 🧪 System Testing & Upload Feature (Week 6)
- **Upload & Analyze Tab**:
  - Upload any audio file (WAV, MP3, M4A)
  - Full NLP pipeline runs in real-time
  - Whisper transcription → Sentence splitting → Topic segmentation → Summarization → Keywords → Sentiment
  - Progress bar with stage-by-stage feedback
  - Interactive results with segment timeline, word clouds, and sentiment pie chart

- **Multi-Genre Support**:
  - Genre 1: Education (2,847 segments from English learning podcasts)
  - Genre 2: News (40 segments from current affairs podcasts)
  - Genre filter in sidebar for easy switching

- **System Testing**:
  - Comprehensive testing across 7 areas
  - 8 issues documented with severity levels
  - User feedback collected from 3 testers
  - Bug fixes for segment selection and navigation

---

## 📅 Project Timeline

### Week 1-2: Audio Processing & Transcription
**Objective**: Build foundation for audio-to-text conversion

**Completed**:
- ✅ Audio preprocessing pipeline (resampling, noise reduction, chunking)
- ✅ Whisper ASR integration
- ✅ Batch processing for large audio files
- ✅ JSON transcript generation

**Output**: 2,847 transcribed audio segments

---

### Week 3: Topic Segmentation & Summarization
**Objective**: Organize transcripts into meaningful segments

**Completed**:
- ✅ Baseline topic segmentation (sentence-based)
- ✅ Embedding-based segmentation (semantic similarity)
- ✅ BART-large-CNN summarization
- ✅ Resumable summarization pipeline

**Output**: 
- Segmented transcripts (`segmented_baseline.txt`, `segmented_embedding.txt`)
- Segment summaries (`segment_summaries.txt`)

---

### Week 4: Keyword Extraction
**Objective**: Extract important terms from each segment

**Completed**:
- ✅ TF-IDF vectorization implementation
- ✅ Top-5 keyword extraction per segment
- ✅ CSV export for analysis

**Output**: `segment_keywords.csv` with 14,235 keywords

---

### Week 5: Visualization & Detail Enhancements
**Objective**: Create interactive dashboard for data exploration

**Completed**:
- ✅ Interactive timeline with sentiment color-coding
- ✅ TextBlob sentiment analysis (2,847 segments)
- ✅ Keyword cloud visualization
- ✅ Data integration into master JSON file
- ✅ Streamlit web application with pagination
- ✅ Professional UI with clear formatting

**Output**: 
- Interactive dashboard (`app/app.py`)
- Master data file (`segments_final.json` - 2.7 MB)
- Live web application

---

### Week 6: System Testing, Upload Feature & Feedback
**Objective**: Add real-time audio analysis, test the system, and collect user feedback

**Completed**:
- ✅ "Upload & Analyze" tab with full NLP pipeline
- ✅ Reusable pipeline module (`app/upload_analyzer.py`)
- ✅ Multi-genre support (education + news)
- ✅ News sentiment re-analysis (fixed 100% neutral issue)
- ✅ News keywords regenerated with KeyBERT
- ✅ System testing across 7 areas (`testing_log.md`)
- ✅ User feedback collection — 3 respondents (`feedback_responses.md`)
- ✅ Bug fixes: segment selection, timeline navigation, Prev/Next buttons

**Output**:
- Upload & Analyze feature (`app/upload_analyzer.py`)
- Testing log (`testing_log.md`)
- Feedback form & responses (`feedback_form.md`, `feedback_responses.md`)
- Fixed UI bugs in `app/app.py`

## 📁 Project Structure

```
Podcast_AI_Project/
├── app/                          # Web application
│   ├── app.py                    # Main Streamlit dashboard (Genre Browser + Upload)
│   ├── upload_analyzer.py        # Real-time audio analysis pipeline
│   └── utils.py                  # Helper functions
│
├── asr/                          # Automatic Speech Recognition
│   ├── transcribe.py             # Whisper transcription script
│   ├── merge_transcripts.py      # Combine JSON transcripts
│   └── whisper_batch.py          # Batch processing
│
├── data/                         # Data storage
│   ├── raw_audio/                # Input MP3/WAV files
│   ├── processed_audio/          # Cleaned 16kHz chunks
│   ├── transcripts/              # JSON transcripts
│   └── wav_clean/                # Cleaned audio files
│
├── nlp/                          # NLP Analysis modules
│   ├── build_segment_index.py    # Data integration & sentiment
│   ├── keyword_extraction.py     # TF-IDF keyword extraction
│   ├── segment_baseline.py       # Baseline segmentation
│   ├── segment_embedding.py      # Embedding-based segmentation
│   ├── summarizer.py             # BART summarization
│   └── topic_segmentation.py     # Topic modeling
│
├── preprocessing/                # Audio preprocessing
│   ├── pipeline.py               # Main preprocessing pipeline
│   ├── audio_cleaner.py          # Noise reduction
│   ├── chunker.py                # Audio chunking
│   └── resampler.py              # Resampling to 16kHz
│
├── results/                      # Analysis outputs
│   ├── segments_final.json       # Master data file (2.7 MB)
│   ├── segment_keywords.csv      # Extracted keywords
│   ├── segment_summaries.txt     # Generated summaries
│   ├── segmented_baseline.txt    # Baseline segments
│   └── segmented_embedding.txt   # Embedding segments
│
├── testing_log.md                # Week 6 system testing results
├── feedback_form.md              # User feedback template
├── feedback_responses.md         # Collected feedback (3 testers)
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- FFmpeg (for audio processing)
- 4GB+ RAM recommended

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/PSSR-VIVEK/Audio-Analysis-Project.git
   cd Audio-Analysis-Project
   ```

2. **Create virtual environment** (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install FFmpeg** (if not already installed):
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html)
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt-get install ffmpeg`

---

## 💻 Usage

### 1. Audio Preprocessing
Place your podcast files (`.mp3` or `.wav`) in `data/wav_clean/`:

```bash
python preprocessing/pipeline.py
```

**Output**: Cleaned, chunked audio in `data/processed_audio/`

---

### 2. Transcription
Transcribe the processed audio chunks:

```bash
python asr/transcribe.py
```

**Output**: JSON transcripts in `data/transcripts/`

---

### 3. Topic Segmentation
Segment transcripts into topic-based sections:

```bash
# Baseline segmentation
python nlp/segment_baseline.py

# Embedding-based segmentation (recommended)
python nlp/segment_embedding.py
```

**Output**: `results/segmented_embedding.txt`

---

### 4. Summarization
Generate summaries for each segment:

```bash
python nlp/summarizer.py
```

**Output**: `results/segment_summaries.txt`

---

### 5. Keyword Extraction
Extract keywords from segments:

```bash
python nlp/keyword_extraction.py
```

**Output**: `results/segment_keywords.csv`

---

### 6. Data Integration & Sentiment Analysis
Combine all data and analyze sentiment:

```bash
python nlp/build_segment_index.py
```

**Output**: `results/segments_final.json`

---

### 7. Launch Interactive Dashboard
Start the web application:

```bash
streamlit run app/app.py
```

**Access**: Open browser to `http://localhost:8501`

---

## 🛠️ Technologies Used

### Audio Processing
- **librosa** - Audio analysis and feature extraction
- **soundfile** - Audio file I/O
- **pydub** - Audio manipulation
- **noisereduce** - Noise reduction

### Speech Recognition
- **OpenAI Whisper** - State-of-the-art ASR model
- **torch** - PyTorch for model inference

### NLP & Analysis
- **transformers** (Hugging Face) - BART summarization
- **sentence-transformers** - Semantic embeddings
- **scikit-learn** - TF-IDF vectorization
- **TextBlob** - Sentiment analysis
- **spaCy** - Text processing

### Visualization
- **Streamlit** - Interactive web dashboard
- **WordCloud** - Keyword cloud generation
- **matplotlib** - Plotting and visualization

### Data Processing
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **json** - Data serialization

---

## 📊 Results

### Dataset Statistics
- **Total Audio Segments**: 2,887 (2,847 education + 40 news)
- **Genres**: 2 (Education, News)
- **Total Transcripts**: 2,887 JSON files
- **Topic Segments**: 2,887 distinct segments
- **Summaries Generated**: 2,887 (2-3 sentences each)
- **Keywords Extracted**: 14,435+ (5 per segment)
- **Sentiment Scores**: 2,887 (all segments analyzed)

### Output Files
- **Master Data File**: `segments_final.json` (2.7 MB)
- **Keywords CSV**: `segment_keywords.csv` (116 KB)
- **Summaries**: `segment_summaries.txt` (650 KB)
- **Segmented Transcripts**: `segmented_embedding.txt` (1.4 MB)

### Dashboard Features
- ✅ Interactive timeline with 2,887 segments
- ✅ Color-coded sentiment visualization
- ✅ Pagination (50 segments per page)
- ✅ Real-time keyword cloud generation
- ✅ Comprehensive segment details
- ✅ Upload & Analyze for custom audio files
- ✅ Multi-genre filtering
- ✅ Sentiment pie chart for uploaded audio
- ✅ Responsive design

---

## 🎯 Key Features Demonstrated

### Week 1-2: Foundation
- Audio preprocessing pipeline
- Whisper ASR integration
- Batch processing capabilities

### Week 3: NLP Basics
- Topic segmentation algorithms
- Transformer-based summarization
- Text processing pipelines

### Week 4: Information Extraction
- TF-IDF keyword extraction
- Statistical text analysis
- Data export and formatting

### Week 5: Visualization & Integration
- Sentiment analysis implementation
- Interactive web dashboard
- Data integration and presentation
- User experience design

### Week 6: Testing, Upload & Feedback
- Upload & Analyze with full NLP pipeline
- Multi-genre support (education + news)
- System testing (7 areas, 8 issues documented)
- User feedback collection (3 respondents)
- Bug fixes and UI improvements
- News sentiment re-analysis

---

## 👨‍💻 Author

**PSSR Vivek**
- GitHub: [@PSSR-VIVEK](https://github.com/PSSR-VIVEK)
- Project: [Audio-Analysis-Project](https://github.com/PSSR-VIVEK/Audio-Analysis-Project)

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- OpenAI Whisper for ASR capabilities
- Hugging Face for transformer models
- Streamlit for the amazing web framework
- The open-source community for excellent libraries

---

## 📞 Contact

For questions or feedback, please open an issue on GitHub or contact via the repository.

---

**Last Updated**: February 12, 2026  
**Project Status**: Week 6 Complete ✅
