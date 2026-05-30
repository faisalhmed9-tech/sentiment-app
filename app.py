import streamlit as st
import random
import time
import urllib.parse

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="نظام حمد الذكي", layout="centered")

# --- 2. التصميم (نفس اللي بالصور) ---
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

# --- 3. محرك التحليل (الكلمات الشاطحة + الردود المتغيرة) ---
def analyze_mood(text, name):
    text = text.lower()
    
    # الكلمات العامية الشاطحة
    neg_keys = ["زعلان", "ضايق", "طفشان", "زهقان", "تعبان", "مالي خلق", "منغث", "مغلق", "نفسية"]
    pos_keys = ["مبسوط", "مستانس", "فرحان", "مروق", "وناسة", "كفو", "منتعش", "طاير"]
    neu_keys = ["عادي", "تمام", "طيب", "ماشي", "نص نص"]

    # منطق الردود باستخدام الاسم المدخل {name}
    if any(word in text for word in neg_keys):
        replies = [f"أفا يا {name}! الضيقة ما تدوم وبكرا أجمل.", f"لا يضيق صدرك يا {name}، فضفض وطلع اللي بقلبك."]
        return "سلبي", "#F44336", random.choice(replies)
    
    elif any(word in text for word in pos_keys):
        replies = [f"يا سلام على الروقان يا {name}! عسى هالوناسة دوم.", f"كفو يا {name}! طاقة إيجابية تشرح الصدر."]
        return "إيجابي", "#4CAF50", random.choice(replies)
    
    elif any(word in text for word in neu_keys):
        replies = [f"يوم هادي ومستقر يا {name}، الاستقرار نعمة.", f"ماشي الحال يا {name}، أهم شي راحتك."]
        return "محايد", "#607D8B", random.choice(replies)
    
    else:
        return "غير محدد", "#2196F3", f"كلامك كبير يا {name}، الأهم إنك تكون بخير دائماً."

# --- 4. واجهة التطبيق ---
st.title("🤖 نظام حمد الذكي")
st.write("وش يدور في خاطرك: فضفض وسوف يتم تحليلك!")

col1, col2 = st.columns(2)
with col1:
    test_name = st.text_input("سجل اسمك:", placeholder="اكتب اسمك هنا")
with col2:
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

u_input = st.text_area("اكتب شعورك هنا (بالعامية):")

if st.button("بدء التحليل وإطلاق القوة 🚀"):
    if not test_name.strip() or not u_input.strip():
        st.warning("سجل بياناتك كاملة يا بطل!")
    else:
        with st.spinner("جاري التحليل..."):
            time.sleep(1)
        
        m_type, color, reply = analyze_mood(u_input, test_name)
        prefix = "الأستاذ" if gender == "ذكر" else "الأستاذة"
        
        # عرض النتيجة
        st.markdown(f"""
        <div class="result-box" style="background:{color};">
            <h2 style="color:white; margin:0;">النتيجة يا {prefix} {test_name}</h2>
            <hr style="border:0.5px solid rgba(255,255,255,0.2); margin: 15px 0;">
            <p style="font-size: 22px; font-weight: bold; margin:0;">{reply}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # زر الواتساب المضمون (بدون أخطاء f-string)
        msg = urllib.parse.quote(f"تحليل مزاجي من نظام حمد الذكي: {reply}")
        whatsapp_url = f"https://wa.me/?text={msg}"
        st.markdown(f'<a href="{whatsapp_url}" target="_blank" style="text-decoration:none;"><button style="margin-top:15px; width:100%; background:#25D366; color:white; border-radius:15px; padding:12px; border:none; font-weight:bold; cursor:pointer;">📤 شارك النتيجة على واتساب</button></a>', unsafe_allow_html=True)

st.markdown("---")
st.caption(f"صنع بـ ❤️ بواسطة حمد | 2026")
