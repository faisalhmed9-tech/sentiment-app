import streamlit as st
import random
import time
import urllib.parse

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="نظام حمد الذكي", layout="centered")

# --- 2. التصميم الفخم ---
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

# --- 3. محرك التحليل الذكي ---
def analyze_mood(text):
    text = text.lower()
    
    # الكلمات العامية (إيجابي، سلبي، محايد)
    neg_keys = ["زعلان", "ضايق", "طفشان", "زهقان", "تعبان", "مالي خلق", "منغث", "حزين"]
    pos_keys = ["مبسوط", "مستانس", "فرحان", "مروق", "وناسة", "الحمدلله", "كفو", "راضي"]
    neu_keys = ["عادي", "تمام", "طيب", "ماشي", "نص نص", "بخير"]

    # ردود متنوعة عشان ما تتكرر
    if any(word in text for word in neg_keys):
        replies = ["أفا يا حمد! الضيقة ما تدوم، وبكرا أجمل بإذن الله.", "فضفض يا بطل، اليوم السيء يجي بعده يوم يشرح الصدر.", "لا يضيق صدرك، خذ نفس عميق وكل شي بيزين."]
        return "سلبي", "#F44336", random.choice(replies)
    
    elif any(word in text for word in pos_keys):
        replies = ["يا سلام على الروقان! عسى هالضحكة دوم يا حمد.", "كفو! طاقة إيجابية رهيبة، استمر يا بطل.", "دوم مستانس يارب، الروح الحلوة هذي هي اللي تفتح الأبواب."]
        return "إيجابي", "#4CAF50", random.choice(replies)
    
    elif any(word in text for word in neu_keys):
        replies = ["يوم هادي ومستقر، الاستقرار نعمة يا حمد.", "ماشي الحال، أهم شي إنك بخير ومرتاح البال.", "جميل إن الواحد يكون متزن، يومك موفق."]
        return "محايد", "#607D8B", random.choice(replies)
    
    else:
        return "غير محدد", "#2196F3", "كلامك جميل يا حمد، الأهم إنك تكون بخير ومرتاح البال."

# --- 4. الواجهة ---
st.title("🤖 نظام حمد الذكي")
st.write("وش يدور في خاطرك: فضفض وسوف يتم تحليلك!")

col1, col2 = st.columns(2)
with col1:
    u_name = st.text_input("سجل اسمك:", placeholder="حمد")
with col2:
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

u_input = st.text_area("اكتب شعورك هنا:")

if st.button("بدء التحليل وإطلاق القوة 🚀"):
    if not u_name.strip() or not u_input.strip():
        st.warning("سجل بياناتك أول يا بطل!")
    else:
        with st.spinner("جاري التحليل..."):
            time.sleep(1)
        
        m_type, color, reply = analyze_mood(u_input)
        prefix = "الأستاذ" if gender == "ذكر" else "الأستاذة"
        
        st.markdown(f"""
        <div class="result-box" style="background:{color};">
            <h2 style="color:white; margin:0;">النتيجة يا {prefix} {u_name}</h2>
            <hr style="border:0.5px solid rgba(255,255,255,0.2); margin: 15px 0;">
            <p style="font-size: 22px; font-weight: bold; margin:0;">{reply}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # زر الواتساب (تم تصحيحه)
        msg = urllib.parse.quote(f"نتيجتي من نظام حمد الذكي: {reply}")
        st.markdown(f'<a href="https://wa.me/?text={msg}" target="_blank" style="text-decoration:none;"><button style="margin-top:15px; width:100%; background:#25D366; color:white; border-radius:15px; padding:12px; border:none; font-weight:bold; cursor:pointer;">📤 شارك النتيجة على واتساب</button></a>', unsafe_allow_html=True)

st.markdown("---")
st.caption("صنع بـ ❤️ بواسطة حمد | 2026")
