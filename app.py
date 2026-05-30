import streamlit as st
import random
import time
import urllib.parse

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="نظام التحليل الذكي", layout="centered")

# --- 2. التصميم (CSS) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Tajawal', sans-serif; direction: rtl; text-align: right; }
    .stButton>button {
        width: 100%; border-radius: 15px; font-weight: bold;
        background: linear-gradient(90deg, #4CAF50, #2196F3);
        color: white; border: none; padding: 12px; font-size: 18px;
    }
    .result-box { padding: 25px; border-radius: 15px; margin-top: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); color: white; text-align: center; }
</style>
""", unsafe_allow_html=True)

# --- 3. محرك التحليل (الاسم متغير تماماً) ---
def analyze_mood(text, person_name):
    text = text.lower()
    
    # مجموعات الكلمات العامية
    neg_keys = ["زعلان", "ضايق", "طفشان", "زهقان", "تعبان", "مالي خلق", "منغث"]
    pos_keys = ["مبسوط", "مستانس", "فرحان", "مروق", "وناسة", "الحمدلله"]
    neu_keys = ["عادي", "تمام", "طيب", "ماشي"]

    # الردود تعتمد كلياً على متغير person_name
    if any(word in text for word in neg_keys):
        replies = [f"أفا يا {person_name}! الضيقة ما تدوم وبكرا أجمل.", f"لا يضيق صدرك يا {person_name}، كل عسر وبعده يسر."]
        color, m_type = "#F44336", "سلبي"
    elif any(word in text for word in pos_keys):
        replies = [f"يا سلام على الروقان يا {person_name}! دوم هالضحكة.", f"كفو يا {person_name}! طاقة إيجابية تشرح الصدر."]
        color, m_type = "#4CAF50", "إيجابي"
    elif any(word in text for word in neu_keys):
        replies = [f"يوم هادي ومستقر يا {person_name}، الاستقرار نعمة.", f"ماشي الحال، أهم شي إنك مرتاح يا {person_name}."]
        color, m_type = "#607D8B", "محايد"
    else:
        replies = [f"كلامك جميل يا {person_name}، خلك دايم بخير."]
        color, m_type = "#2196F3", "غير محدد"
    
    return m_type, color, random.choice(replies)

# --- 4. الواجهة ---
st.title("🤖 نظام التحليل الذكي")
st.write("وش يدور في خاطرك: فضفض وسوف يتم تحليلك!")

col1, col2 = st.columns(2)
with col1:
    current_user = st.text_input("سجل اسمك:", placeholder="اكتب أي اسم هنا للاختبار")
with col2:
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

u_input = st.text_area("اكتب شعورك هنا:")

if st.button("بدء التحليل 🚀"):
    if not current_user.strip() or not u_input.strip():
        st.warning("سجل بياناتك كاملة!")
    else:
        with st.spinner("جاري التحليل..."):
            time.sleep(1)
        
        # هنا يتم تمرير الاسم المدخل فعلياً للدالة
        m_type, color, final_reply = analyze_mood(u_input, current_user)
        prefix = "الأستاذ" if gender == "ذكر" else "الأستاذة"
        
        st.markdown(f"""
        <div class="result-box" style="background:{color};">
            <h2 style="color:white; margin:0;">النتيجة يا {prefix} {current_user}</h2>
            <hr style="border:0.5px solid rgba(255,255,255,0.2); margin: 15px 0;">
            <p style="font-size: 22px; font-weight: bold; margin:0;">{final_reply}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.caption(f"صنع بـ ❤️ بواسطة {current_user if current_user else 'المطور'} | 2026")
