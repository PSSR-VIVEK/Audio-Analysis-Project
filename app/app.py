import streamlit as st
import json
import os

# ---------- Page Configuration ----------
st.set_page_config(
    page_title="Podcast Transcript Navigation",
    layout="wide"
)

# ---------- Load Segments ----------
@st.cache_data
def load_segments():
    path = "results/segments_final.json"
    if not os.path.exists(path):
        st.error("segments_final.json not found. Please run build_segment_index.py")
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

segments = load_segments()

# ---------- UI Header ----------
st.title("🎧 Podcast Transcript Navigation System")
st.caption("Week 4 – Topic-wise Segment Jumping Interface")

if not segments:
    st.warning("No segments available.")
    st.stop()

# ---------- Sidebar ----------
st.sidebar.header("Choose a Topic Segment")

labels = [
    f"Segment {seg['id']} – {seg.get('title', 'Untitled')}"
    for seg in segments
]

selected_label = st.sidebar.selectbox(
    "Segments",
    labels
)

selected_index = labels.index(selected_label)
seg = segments[selected_index]

# ---------- Main Content ----------
st.subheader("📌 Segment")
st.write(f"Segment {seg['id']}")

st.subheader("📝 Summary")
st.write(seg.get("summary", "Summary not available."))

st.subheader("🔑 Keywords")
keywords = seg.get("keywords", "")
st.write(keywords if keywords else "Keywords not available.")

st.subheader("📄 Transcript")
st.write(seg.get("text", ""))
