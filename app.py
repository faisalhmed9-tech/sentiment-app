import streamlit as st
import urllib.parse
import random
import time
from datetime import datetime

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="نظام حمد العالمي 2026", page_icon="🛡️", layout="wide")

# اختيار الوضع (إبداع حمد 😎)
mode = st.sidebar.toggle("🌙 الوضع الليلي", value=False)

if mode:
    bg = "linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%)"
    text_color = "white"
    card_bg = "rgba(255,255,255,0.1)"
else:
    bg = "linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)"
    text_color = "black"
    card_bg = "white"

st.markdown(f"""
    <style>
    .main {{ background: {bg}; color: {text_color}; }}
    .stButton>button {{
        background: linear-gradient(to right, #1E3A8A, #3B82F6);
        color: white; border-radius: 25px; border: none;
        padding: 15px 30px; font-size: 20px; transition: 0.5s;
    }}
    .suggestion-box {{
        background-color: {card_bg}; padding: 20px; border-radius: 15px;
        border-left: 5px solid #E1306C; box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 2. عداد الزيارات ---
if 'visits' not in st.session_state:
    st.session_state.visits = random.randint(15400, 16000)
else:
    st.session_state.visits += 1

# --- 3. الواجهة ---
st.title("🛡️ نظام حمد العالمي للتحليل الذكي")
st.write(f"👥 عدد المستفيدين: **{st.session_state.visits:,}**")
st.markdown("---")

c1, c2 = st.columns(2)
with c1:
    name = st.text_input("سجل اسمك الكريم:", placeholder="مثلاً: حمد")
with c2:
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

display_name = name.strip() if name.strip() else "يا بطل"
prefix = "الأستاذ" if gender == "ذكر" else "الأستاذة"

user_text = st.text_area(f"يا {prefix} {display_name}، وش شعورك اليوم؟")

# --- 4. التحليل ---
if st.button("بدء التحليل الذكي 🚀"):
    if name and user_text:
        with st.spinner('⏳ جاري استشارة خوارزميات حمد العالمية...'):
            time.sleep(2)
        
        t = user_text.lower()
        pos_keywords = ["سعيد", "مستانس", "رايق", "كفو", "بطل", "رهيب", "حلو", "ممتاز"]
        neg_keywords = ["متضايق", "طفشان", "حزين", "زعلان", "تعبان", "قهر", "ضيق"]

        if any(w in t for w in pos_keywords):
            st.balloons()
            st.success(f"النتيجة إيجابية! كفو يا {prefix} {display_name} ✨")
        elif any(w in t for w in neg_keywords):
            st.warning("النتيجة سلبية.. غير جوك يا وحش.")
            st.video("https://www.youtube.com/watch?v=2p8nreL_lTo")
        else:
            st.info("حالة اتزان ⚖️")
            st.video("https://www.youtube.com/watch?v=68pY7z-S2_Q")
    else:
        st.error("سجل بياناتك أولاً!")

# --- 5. التواصل ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f'''
    <div class="suggestion-box">
        <h4>💡 عندك فكرة لتطوير النظام؟</h4>
        <a href="https://www.instagram.com/hamd_9367_?igsh=MTV6eHF5ZXdndGZ1dw==" target="_blank" style="text-decoration: none;">
            <button style="background: linear-gradient(45deg, #f09433, #bc1888); color: white; border: none; padding: 10px 20px; border-radius: 10px; cursor: pointer;">
                📸 أرسل اقتراحك للمطور حمد
            </button>
        </a>
    </div>
''', unsafe_allow_html=True)

st.markdown(f"<br><center>برمجة <b>حمد</b> © 2026</center>", unsafe_allow_html=True)
