import streamlit as st
import json
from pathlib import Path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# -----------------------------
# CONFIG
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "results" / "segments_final.json"

PAGE_SIZE = 50

st.set_page_config(
    page_title="Podcast Transcript Navigation System",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------

if not DATA_FILE.exists():
    st.error("❌ segments_final.json not found in results/")
    st.stop()

with open(DATA_FILE, "r", encoding="utf-8") as f:
    segments = json.load(f)

TOTAL = len(segments)

# -----------------------------
# SESSION STATE INIT
# -----------------------------

if "selected_segment" not in st.session_state:
    st.session_state.selected_segment = segments[0]["id"]

if "timeline_page" not in st.session_state:
    st.session_state.timeline_page = 0

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("🎯 Choose a Topic Segment")

labels = []
id_lookup = []

for seg in segments:
    title = seg.get("title", "")
    short = title[:35] + "..." if len(title) > 35 else title
    labels.append(f"Segment {seg['id']} – {short}")
    id_lookup.append(seg["id"])

default_index = id_lookup.index(st.session_state.selected_segment)

selected_label = st.sidebar.selectbox(
    "Segments",
    labels,
    index=default_index
)

new_selected_id = selected_label.split()[1]

# -----------------------------
# AUTO-SYNC PAGE AFTER SELECTION
# -----------------------------

selected_index = next(
    i for i, s in enumerate(segments)
    if s["id"] == new_selected_id
)

new_page = selected_index // PAGE_SIZE

if new_page != st.session_state.timeline_page:
    st.session_state.timeline_page = new_page
    st.session_state.selected_segment = new_selected_id
    st.rerun()

st.session_state.selected_segment = new_selected_id

segment = next(s for s in segments if s["id"] == new_selected_id)

# -----------------------------
# MAIN HEADER
# -----------------------------

st.title("🎧 Podcast Transcript Navigation System")
st.caption("Week-5 – Visualization & Detail Enhancements")

# -----------------------------
# TIMELINE
# -----------------------------

st.subheader("🎯 Podcast Timeline")

start = st.session_state.timeline_page * PAGE_SIZE
end = min(start + PAGE_SIZE, TOTAL)

st.caption(f"Showing segments {start+1}–{end} of {TOTAL}")

nav1, nav2, nav3 = st.columns([1, 6, 1])

with nav1:
    if st.button("⬅ Prev") and st.session_state.timeline_page > 0:
        st.session_state.timeline_page -= 1
        st.rerun()

with nav3:
    if st.button("Next ➡") and end < TOTAL:
        st.session_state.timeline_page += 1
        st.rerun()

cols = st.columns(10)

for idx, seg in enumerate(segments[start:end]):
    col = cols[idx % 10]

    sentiment = seg.get("sentiment", "Neutral")

    icon = (
        "🟢" if sentiment == "Positive"
        else "🔴" if sentiment == "Negative"
        else "🔵"
    )

    label = f"{icon} {seg['id']}"

    with col:
        if st.button(label, key=f"seg_{seg['id']}"):
            st.session_state.selected_segment = seg["id"]
            st.rerun()

st.divider()

# -----------------------------
# SEGMENT TITLE
# -----------------------------

st.subheader("📌 Segment")
st.write(segment.get("title", ""))

# -----------------------------
# SUMMARY
# -----------------------------

st.subheader("📝 Summary")

summary = segment.get("summary", "")
if summary:
    st.success(summary)
else:
    st.warning("Summary not available.")

# -----------------------------
# KEYWORDS
# -----------------------------

st.subheader("🔑 Keywords")

keywords = segment.get("keywords", "")
if keywords:
    st.write(keywords)
else:
    st.warning("Keywords not available.")

# -----------------------------
# WORD CLOUD
# -----------------------------

st.subheader("☁ Keyword Cloud")

if keywords:
    wc = WordCloud(
        width=900,
        height=400,
        background_color="black",
        colormap="viridis"
    ).generate(keywords)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

else:
    st.info("No keywords available for cloud.")

# -----------------------------
# SENTIMENT
# -----------------------------

st.subheader("😊 Sentiment")

sent = segment.get("sentiment", "Unknown")
score = segment.get("sentiment_score", 0)

if sent.lower() == "positive":
    st.success(f"{sent} ({score:.2f})")
elif sent.lower() == "negative":
    st.error(f"{sent} ({score:.2f})")
else:
    st.info(f"{sent} ({score:.2f})")

# -----------------------------
# TRANSCRIPT
# -----------------------------

st.subheader("📜 Transcript")
st.write(segment.get("text", ""))
