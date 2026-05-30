import streamlit as st
import random
import time
import urllib.parse

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="نظام حمد الذكي", layout="centered", initial_sidebar_state="collapsed")

# --- 2. CSS الأصلي (نفس اللي بالصورة) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="st-"] {
        font-family: 'Tajawal', sans-serif; 
        direction: rtl; 
        text-align: right;
    }
    .stButton>button {
        width: 100%; border-radius: 15px; font-weight: bold;
        background: linear-gradient(90deg, #4CAF50, #2196F3);
        color: white; border: none; padding: 12px; font-size: 18px;
    }
    .result-box {
        padding: 25px; border-radius: 15px; margin-top: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3); color: white;
        text-align: center;
    }
    .whatsapp-btn {
        display: block; width: 100%; background-color: #25D366;
        color: white !important; padding: 12px; border-radius: 15px;
        text-align: center; text-decoration: none; margin-top: 15px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. محرك التحليل (الكلمات العامية اللي طلبتها) ---
def analyze_mood(text):
    text = text.lower()
    
    # تصنيف الكلمات (عامي وفصحى)
    negative = ["زعلان", "ضايق", "طفشان", "زهقان", "مهموم", "تعبان", "مالي خلق", "منغث", "حزين"]
    positive = ["مبسوط", "مستانس", "فرحان", "مروق", "وناسة", "الحمدلله", "راضي"]
    neutral = ["عادي", "تمام", "طيب", "ماشي"]

    if any(word in text for word in negative):
        return "سلبي", "#F44336", "أفا يا حمد! فضفض وطلع اللي بقلبك، الضيقة ما تدوم وبكرا أجمل بإذن الله."
    
    elif any(word in text for word in positive):
        return "إيجابي", "#4CAF50", "يا سلام على الروقان! عسى هالضحكة والوناسة دوم يا بطل."
    
    elif any(word in text for word in neutral):
        return "محايد", "#607D8B", "يوم هادي ومستقر، الاستقرار نعمة يا حمد."
    
    else:
        return "غير محدد", "#2196F3", "كلامك جميل يا حمد، الأهم إنك تكون بخير ومرتاح البال."

# --- 4. الواجهة (نفس الصورة تماماً) ---
st.title("🤖 نظام حمد الذكي")
st.write("وش يدور في خاطرك: فضفض وسوف يتم تحليلك!")

col1, col2 = st.columns(2)
with col1:
    user_name = st.text_input("سجل اسمك:", placeholder="مثلاً: حمد")
with col2:
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

user_input = st.text_area("اكتب شعورك هنا:")

if st.button("بدء التحليل وإطلاق القوة 🚀"):
    if not user_name.strip() or not user_input.strip():
        st.warning("يا بطل سجل بياناتك أول!")
    else:
        with st.spinner("جاري التحليل..."):
            time.sleep(1)
        
        mood_type, color, reply = analyze_mood(user_input)
        prefix = "الأستاذ" if gender == "ذكر" else "الأستاذة"
        
        # عرض النتيجة بدون النجوم ✨ اللي ضايقتك
        st.markdown(f"""
        <div class="result-box" style="background:{color};">
            <h2 style="color:white; margin:0;">النتيجة يا {prefix} {user_name}</h2>
            <hr style="border:0.5px solid rgba(255,255,255,0.2); margin: 15px 0;">
            <p style="font-size: 22px; font-weight: bold; margin:0;">{reply}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # زر الواتساب
        share_msg = urllib.parse.quote(f"تحليل مزاجي من نظام حمد الذكي: {reply}")
        st.markdown(f'<a href="https://wa.me/?text={share_msg}" target="_blank" class="whatsapp-btn">📤 شارك النتيجة على واتساب</a>', unsafe_allow_html=True)

st.markdown("---")
st.caption("صنع بـ ❤️ بواسطة حمد | 2026")
