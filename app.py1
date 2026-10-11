import streamlit as st

# Configure page layout and aesthetics
st.set_page_config(
    page_title="Hành Trình Thanh Xuân - Interactive Presentation",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    /* Global Styling - Bright Youthful Pastel & Clean White Palette */
    .stApp {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
        color: #2d3748;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Hide standard Streamlit header and footer for a clean presentation feel */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Presentation Card Container */
    .presentation-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.8);
        border-radius: 24px;
        padding: 45px 50px;
        box-shadow: 0 20px 40px rgba(100, 116, 139, 0.08), 0 1px 3px rgba(0, 0, 0, 0.05);
        margin-top: 30px;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    /* Typography & Headings */
    .slide-tag {
        display: inline-block;
        font-size: 0.85rem;
        font-weight: 600;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #818cf8;
        background: rgba(129, 140, 248, 0.1);
        padding: 6px 14px;
        border-radius: 30px;
        margin-bottom: 20px;
    }
    
    .slide-title {
        font-size: 2.4rem;
        font-weight: 800;
        color: #1e293b;
        margin-bottom: 20px;
        line-height: 1.3;
        background: linear-gradient(120deg, #3b82f6, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Bullet points / sequential reveal items */
    .reveal-item {
        font-size: 1.15rem;
        color: #475569;
        background: rgba(248, 250, 252, 0.7);
        border-left: 4px solid #f472b6;
        padding: 16px 20px;
        border-radius: 0 12px 12px 0;
        margin-bottom: 14px;
        animation: fadeIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(15px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Progress and Navigation Indicators */
    .progress-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid rgba(226, 232, 240, 0.8);
    }
    
    .progress-text {
        font-size: 0.95rem;
        font-weight: 600;
        color: #64748b;
    }
    
    /* Customize Streamlit Buttons to fit the pastel theme */
    .stButton button {
        border-radius: 14px !important;
        font-weight: 600 !important;
        padding: 0.6rem 1.4rem !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.15) !important;
    }
</style>
""", unsafe_allow_html=True)

slides_data = [
    {
        "tag": "Chương I • Khởi Đầu",
        "title": "🌸 Hơi Thở Mùa Hè & Những Ước Mơ Đầu Tiên",
        "content": [
            "Chào mừng bạn đến với không gian thuyết trình số mang phong cách thanh xuân tươi sáng.",
            "Nơi mỗi cú click chuột sẽ mở ra một chương mới trong câu chuyện của chúng ta.",
            "Hãy cùng nhìn lại những khoảnh khắc rực rỡ nhất của tuổi trẻ đầy nhiệt huyết."
        ]
    },
    {
        "tag": "Chương II • Hành Trình",
        "title": "✨ Khám Phá Bản Thân & Vượt Qua Giới Hạn",
        "content": [
            "Tuổi trẻ không phải là thời kỳ của cuộc sống, mà là trạng thái của tâm hồn.",
            "Dám nghĩ, dám làm, dám đương đầu với mọi thử thách và bão giông.",
            "Mỗi thất bại đều là một bài học quý giá nuôi dưỡng sự trưởng thành.",
            "Tỏa sáng rực rỡ theo cách riêng biệt mà không cần phải lặp lại bất kỳ ai."
        ]
    },
    {
        "tag": "Chương III • Kỷ Niệm",
        "title": "🌿 Những Người Bạn Đồng Hành Dưới Ánh Nắng",
        "content": [
            "Cùng nhau đi qua những con đường ngập tràn hoa phượng đỏ và tiếng ve kêu.",
            "Những buổi chuyện trò thâu đêm suốt sáng về tương lai và hoài bão.",
            "Tình bạn chân thành chính là hành trang vững chãi nhất trên mọi chặng đường."
        ]
    },
    {
        "tag": "Chương IV • Tương Lai",
        "title": "🕊️ Chắp Cánh Bay Cao Tới Những Chân Trời Mới",
        "content": [
            "Thanh xuân tuy ngắn ngủi nhưng dư âm và giá trị của nó là vĩnh cửu.",
            "Hãy giữ mãi ngọn lửa đam mê trong trái tim dù sau này có đi đến đâu.",
            "Cảm ơn bạn đã đồng hành trong bài thuyết trình này. Chúc bạn một đời bình an và rực rỡ!"
        ]
    }
]

if "slide_idx" not in st.session_state:
    st.session_state.slide_idx = 0

if "step_idx" not in st.session_state:
    st.session_state.step_idx = 0

# Helper functions for navigation logic
def advance_presentation():
    current_slide = slides_data[st.session_state.slide_idx]
    if st.session_state.step_idx < len(current_slide["content"]) - 1:
        st.session_state.step_idx += 1
    else:
        if st.session_state.slide_idx < len(slides_data) - 1:
            st.session_state.slide_idx += 1
            st.session_state.step_idx = 0

def previous_presentation():
    if st.session_state.step_idx > 0:
        st.session_state.step_idx -= 1
    else:
        if st.session_state.slide_idx > 0:
            st.session_state.slide_idx -= 1
            st.session_state.step_idx = len(slides_data[st.session_state.slide_idx]["content"]) - 1

def reset_presentation():
    st.session_state.slide_idx = 0
    st.session_state.step_idx = 0

current_slide = slides_data[st.session_state.slide_idx]

st.markdown('<div class="presentation-card">', unsafe_allow_html=True)

# Slide Tag & Title
st.markdown(f'<div class="slide-tag">{current_slide["tag"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="slide-title">{current_slide["title"]}</div>', unsafe_allow_html=True)

# Render revealed bullet points up to current step_idx
for i in range(st.session_state.step_idx + 1):
    st.markdown(f'<div class="reveal-item">💡 {current_slide["content"][i]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])

with col1:
    if st.button("⏮️ Đầu", use_container_width=True, help="Quay về slide đầu tiên"):
        reset_presentation()
        st.rerun()

with col2:
    if st.button("⬅️ Trước", use_container_width=True, help="Quay lại ý trước hoặc slide trước"):
        previous_presentation()
        st.rerun()

with col3:
    # Progress indicator text
    total_slides = len(slides_data)
    current_step_num = st.session_state.step_idx + 1
    total_steps_in_slide = len(current_slide["content"])
    st.markdown(
        f"<div style='text-align: center; font-weight: 600; color: #64748b; padding-top: 8px;'>"
        f"Slide {st.session_state.slide_idx + 1} / {total_slides} &nbsp;|&nbsp; Ý {current_step_num}/{total_steps_in_slide}"
        f"</div>",
        unsafe_allow_html=True
    )

with col4:
    if st.button("Tiếp ➡️", use_container_width=True, type="primary", help="Hiện ý tiếp theo hoặc chuyển slide mới"):
        advance_presentation()
        st.rerun()

with col5:
    if st.button("🔄 Làm lại", use_container_width=True, help="Chạy lại từ đầu"):
        reset_presentation()
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)
click_col1, click_col2, click_col3 = st.columns([1, 2, 1])
with click_col2:
    if st.button("✨ Click vào đây để xem tiếp nội dung ✨", use_container_width=True, type="secondary"):
        advance_presentation()
        st.rerun()