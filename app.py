import json
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Những mảnh suy nghĩ",
    page_icon="✦",
    layout="centered",
    initial_sidebar_state="collapsed",
)

DATA_FILE = Path(__file__).parent / "timeline_data.json"

def load_data():
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)

data = load_data()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Playfair+Display:wght@500;600&display=swap');
:root {
    --ink: #292a35;
    --muted: #777789;
    --paper: #f1eff4;
    --accent: #82738f;
    --line: rgba(67, 62, 81, .15);
}
.stApp {
    background:
        radial-gradient(ellipse at 12% 4%, rgba(202, 190, 214, .40), transparent 38%),
        radial-gradient(ellipse at 92% 30%, rgba(218, 207, 217, .36), transparent 34%),
        linear-gradient(160deg, #f4f1f6 0%, #eeedf3 48%, #f5f0ed 100%);
    color: var(--ink);
}
.block-container { max-width: 760px; padding-top: 3rem; padding-bottom: 4rem; }
h1, h2, h3, .serif { font-family: 'Playfair Display', Georgia, serif !important; color: #30303d; }
.eyebrow { text-transform: uppercase; letter-spacing: .22em; font-size: .72rem; color: var(--muted); }
.intro { font-size: 1.05rem; line-height: 1.9; color: #626271; max-width: 590px; }
.chapter-kicker { color: var(--accent); text-transform: uppercase; letter-spacing: .16em; font-size: .72rem; }
.fragment {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: clamp(1.35rem, 4vw, 2rem);
    line-height: 1.7;
    color: #30303d;
    padding: 1.15rem 1.25rem;
    margin: .8rem 0;
    background: rgba(255, 255, 255, .54);
    border: 1px solid rgba(255, 255, 255, .78);
    border-left: 3px solid #a99bb6;
    border-radius: 5px 14px 14px 5px;
    box-shadow: 0 8px 24px rgba(62, 54, 77, .045);
    animation: appear .45s ease-out;
}
@keyframes appear { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
.small-note { font-size: .82rem; color: var(--muted); line-height: 1.7; }
div[data-testid="stSelectbox"] label { color: #5f5d6e; }
div[data-testid="stSelectbox"] > div > div { background: rgba(255,255,255,.7); border-color: #d8d2df; border-radius: 12px; }
div.stButton > button {
    border-radius: 999px; border: 1px solid #82738f; background: #82738f;
    color: white; padding: .6rem 1.3rem; min-height: 2.8rem;
    transition: all .2s ease;
}
div.stButton > button:hover { background: #6e607c; border-color: #6e607c; color: white; transform: translateY(-1px); }
div.stButton > button:disabled { background: #d7d1dd; color: #777182; border-color: #d7d1dd; }
hr { border-color: var(--line); }
[data-testid="stProgressBar"] > div { background: rgba(130, 115, 143, .17); border-radius: 999px; }
[data-testid="stProgressBar"] > div > div { background: linear-gradient(90deg, #9b8aa8, #82738f); border-radius: 999px; }
[data-testid="stCaptionContainer"] { color: #777789; }
footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

if "chapter_idx" not in st.session_state:
    st.session_state.chapter_idx = 0
if "revealed" not in st.session_state:
    st.session_state.revealed = 0

chapters = data["chapters"]
chapter_idx = min(st.session_state.chapter_idx, len(chapters) - 1)
chapter = chapters[chapter_idx]
fragments = chapter["fragments"]
revealed = min(st.session_state.revealed, len(fragments))

st.markdown(f"<div class='eyebrow'>{data.get('eyebrow', 'Một câu chuyện — từ góc nhìn của tôi')}</div>", unsafe_allow_html=True)
st.markdown(f"<h1 style='font-size:clamp(2.3rem,7vw,4rem); line-height:1.13; margin:1rem 0 .8rem'>{data.get('title', 'Những mảnh suy nghĩ')}</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='intro'>{data.get('subtitle', '')}</p>", unsafe_allow_html=True)
st.write("")

# Chapter navigation
options = [f"{i+1:02d} · {c['title']}" for i, c in enumerate(chapters)]
selected = st.selectbox(
    "Chọn một khoảng thời gian",
    options=range(len(chapters)),
    format_func=lambda i: options[i],
    index=chapter_idx,
    label_visibility="collapsed",
)
if selected != chapter_idx:
    st.session_state.chapter_idx = selected
    st.session_state.revealed = 0
    st.rerun()

st.markdown(f"<div class='chapter-kicker'>CHƯƠNG {chapter_idx + 1:02d} / {len(chapters):02d}</div>", unsafe_allow_html=True)
st.markdown(f"<h2 style='font-size:2rem; margin:.35rem 0 .25rem'>{chapter['title']}</h2>", unsafe_allow_html=True)
if chapter.get("period"):
    st.markdown(f"<p class='small-note'>{chapter['period']}</p>", unsafe_allow_html=True)
if chapter.get("opening"):
    st.markdown(f"<p style='color:#666158; line-height:1.7'>{chapter['opening']}</p>", unsafe_allow_html=True)

st.progress(revealed / max(len(fragments), 1))
st.caption(f"{revealed} / {len(fragments)} mảnh suy nghĩ đã mở")

for line in fragments[:revealed]:
    st.markdown(f"<div class='fragment'>{line}</div>", unsafe_allow_html=True)

st.write("")
left, right = st.columns([1, 1])
with left:
    if revealed < len(fragments):
        if st.button("Mở mảnh tiếp theo  →", use_container_width=True):
            st.session_state.revealed += 1
            st.rerun()
    else:
        st.button("Đã đọc hết chương này", disabled=True, use_container_width=True)
with right:
    if st.button("Bắt đầu lại chương", use_container_width=True):
        st.session_state.revealed = 0
        st.rerun()

st.write("")
if revealed == len(fragments):
    if chapter_idx < len(chapters) - 1:
        if st.button("Sang khoảng thời gian tiếp theo  ↗", use_container_width=True):
            st.session_state.chapter_idx += 1
            st.session_state.revealed = 0
            st.rerun()
    else:
        st.markdown("---")
        st.markdown("<p class='small-note'>Câu chuyện dừng lại ở hiện tại. Phần tiếp theo vẫn chưa được viết.</p>", unsafe_allow_html=True)

st.markdown("---")
st.markdown(
    "<p class='small-note'>Đây là những suy nghĩ từ một góc nhìn. Người đọc có thể cảm nhận theo cách riêng; không có câu trả lời nào được yêu cầu.</p>",
    unsafe_allow_html=True,
)
