import streamlit as st
import time
import random
import urllib.parse

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="نظام حمد الذكي", layout="centered", initial_sidebar_state="collapsed")

# --- 2. CSS حق التصميم (تعديلات حمد الفخمة) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="st-"] {
        font-family: 'Tajawal', sans-serif;
        direction: rtl;
        text-align: right;
    }
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        font-weight: bold;
        background: linear-gradient(90deg, #4CAF50, #2196F3);
        color: white;
        border: none;
        padding: 12px;
        font-size: 18px;
    }
    .result-box {
        background: #1e1e1e;
        padding: 20px;
        border-radius: 15px;
        border-right: 5px solid #4CAF50;
        margin-top: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        color: white;
    }
    .whatsapp-btn {
        display: block;
        width: 100%;
        background-color: #25D366;
        color: white !important;
        padding: 12px;
        border-radius: 15px;
        text-align: center;
        text-decoration: none;
        margin-top: 15px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. الواجهة (رجعت الاسم وكل شي حذفته) ---
st.title("🤖 نظام حمد الذكي")
st.write("وش يدور في خاطرك: فضفض وسوف يتم تحليلك!")

# خانة الاسم والجنس (الأشياء اللي رجعت)
col1, col2 = st.columns(2)
with col1:
    user_name = st.text_input("سجل اسمك:", placeholder="مثلاً: حمد")
with col2:
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

user_input = st.text_area("اكتب شعورك هنا:", height=100, placeholder="مثال: طفشان، تعبان، مبسوط...")

# دالة التحليل
def analyze_feeling(text):
    if any(word in text for word in ["طفشان", "زهقان", "ملل"]): return "طفشان", "😴"
    if any(word in text for word in ["تعبان", "مرهق", "نوم"]): return "تعبان", "🥱"
    if any(word in text for word in ["مبسوط", "فرحان", "تمام"]): return "مبسوط", "😄"
    if any(word in text for word in ["زعلان", "حزين", "ضايق"]): return "زعلان", "😢"
    return "عادي", "😐"

# --- 4. بدء التحليل ---
if st.button("بدء التحليل وإطلاق القوة 🚀"):
    if not user_name.strip() or not user_input.strip():
        st.warning("يا بطل سجل اسمك واكتب شعورك أول!")
    else:
        with st.spinner("جاري تحليل قوتك النفسية..."):
            time.sleep(1.5)
        
        feeling, emoji = analyze_feeling(user_input)
        
        # اللقب بناءً على الاختيار
        prefix = "الأستاذ" if gender == "ذكر" else "الأستاذة"
        name_display = user_name.strip()
        
        # الرد المخصص
        if feeling == "تعبان":
            final_msg = f"{emoji} شكل السهر مأثر عليك يا {prefix} {name_display}.. روح ارتاح، النوم سلطان."
        elif feeling == "مبسوط":
            final_msg = f"{emoji} يا سلام على الروقان يا {prefix} {name_display}! دوم هالضحكة."
        elif feeling == "طفشان":
            final_msg = f"{emoji} الطفش مجرد لحظة يا {name_display}، فكها وبتزين."
        else:
            final_msg = f"{emoji} أهلاً بك يا {prefix} {name_display}، وضعك مستقر وجميل."

        # عرض النتيجة
        st.markdown(f'<div class="result-box"><h3>{final_msg}</h3></div>', unsafe_allow_html=True)
        st.balloons()
        
        # مشاركة الواتساب
        share_msg = urllib.parse.quote(final_msg + " \nجرب نظام حمد: https://fljg.streamlit.app")
        st.markdown(f'<a href="https://wa.me/?text={share_msg}" target="_blank" class="whatsapp-btn">📤 شارك النتيجة على واتساب</a>', unsafe_allow_html=True)

st.markdown("---")
st.caption("صنع بـ ❤️ بواسطة حمد | 2026")
        
