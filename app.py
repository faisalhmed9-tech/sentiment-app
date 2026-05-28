import streamlit as st
import time
import random
import urllib.parse

st.set_page_config(page_title="نظام حمد الذكي", layout="centered", initial_sidebar_state="collapsed")

# --- CSS حق التصميم ---
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
        font-size: 16px;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        transition: 0.2s;
    }
    .result-box {
        background: #1e1e1e;
        padding: 20px;
        border-radius: 15px;
        border-right: 5px solid #4CAF50;
        margin-top: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
</style>
""", unsafe_allow_html=True)

st.title("🤖 نظام حمد الذكي")
st.write("وس يبدور حي معكرد: حمستس رسدم حمد يسستب!")

user_input = st.text_area("اكتب شعورك هنا:", height=100, placeholder="مثال: طفشان، تعبان، مبسوط...")

def analyze_feeling(text):
    text = text.lower()
    if any(word in text for word in ["طفشان", "زهقان", "ملل", "طفش"]):
        return "طفشان", "😴"
    elif any(word in text for word in ["تعبان", "مرهق", "سهر", "تعب", "ارهاق"]):
        return "تعبان", "🥱"
    elif any(word in text for word in ["مبسوط", "فرحان", "تمام", "مبسوطه", "فرحانه"]):
        return "مبسوط", "😄"
    elif any(word in text for word in ["زعلان", "حزين", "ضايق"]):
        return "زعلان", "😢"
    else:
        return "عادي", "😐"

if st.button("بدء التحليل وإطلاق القوة 🚀"):
    if not user_input.strip():
        st.warning("اكتب شي اول يا بطل!")
    else:
        with st.spinner("جالس احلل قوتك النفسية..."):
            time.sleep(2)
        
        feeling, emoji = analyze_feeling(user_input)
        
        # --- الفرق بين الذكر والانثى ---
        if "الأستاذة" in user_input or "استاذة" in user_input or "معلمة" in user_input or "دكتورة" in user_input:
            address = "يا الأستاذة"
            advice = "روحي ارتاحي، النوم سلطان."
        else:
            address = "يا الأستاذ"
            advice = "روح ارتاح، النوم سلطان."
        
        final_result = f"{emoji} شكل السهر مأثر عليك {address}.. {advice}"
        
        # عرض النتيجة
        st.markdown(f'<div class="result-box"><h3>{final_result}</h3></div>', unsafe_allow_html=True)
        
        # بالونات للاحتفال
        st.balloons()
        
        # زر مشاركة واتساب
        share_msg = urllib.parse.quote(final_result + " \nجرب نظام حمد الذكي: https://fljg.streamlit.app")
        whatsapp_url = f"https://wa.me/?text={share_msg}"
        st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="margin-top:10px;">📤 شارك النتيجة على واتساب</button></a>', unsafe_allow_html=True)

st.markdown("---")
st.caption("صنع بـ ❤️ بواسطة حمد | 2026")
