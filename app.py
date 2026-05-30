import streamlit as st
import random
import time

# --- 1. إعدادات وتصميم الصفحة ---
st.set_page_config(page_title="نظام حمد الذكي", layout="centered")

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

# --- 2. محرك التحليل بالعامية (تطوير حمد) ---
def analyze_mood_pro(text):
    text = text.lower()
    
    # 🔴 كلمات سلبية عامية (حق الزعل والطفش)
    negative = ["زعلان", "ضايق", "طفشان", "زهقان", "مهموم", "تعبان", "مالي خلق", "متنكد", "منغث", "مغبون", "حزين"]
    
    # 🟢 كلمات إيجابية عامية (حق الوناسة والروقان)
    positive = ["مبسوط", "مستانس", "فرحان", "مروق", "كفو", "منتعش", "طاير من الفرح", "وناسة", "الحمدلله", "راضي"]
    
    # 🟡 كلمات محايدة عامية (حق اللي نص نص)
    neutral = ["عادي", "ماشي الحال", "تمام", "طيب", "نص نص", "الحمدلله على كل حال", "ماشي"]

    # فحص الكلمات
    if any(word in text for word in negative):
        return "سلبي", "#F44336", "أفا يا حمد! فضفض وطلع اللي بقلبك، والله ما يذوق الضيق من كان متوكل على الله."
    
    elif any(word in text for word in positive):
        return "إيجابي", "#4CAF50", "يا بعدي يا حمد! عسى هالوناسة والروقان دوم، كذا نبغاك دايم!"
    
    elif any(word in text for word in neutral):
        return "محايد", "#607D8B", "يوم هادي وجميل، الاستقرار نعمة يا حمد. خلك على وضعك الرايق."
    
    else:
        return "غير محدد", "#2196F3", f"سمعنا صوتك يا {user_name}، كلامك يحتاج تفكير.. بس الأكيد إننا معك!"

# --- 3. الواجهة ---
st.title("🤖 نظام حمد الذكي (نسخة العامية)")
st.write("اكتب بأي لهجة وبأي طريقة.. أنا أفهمك!")

user_name = st.text_input("سجل اسمك:", placeholder="حمد")
user_input = st.text_area("وش جوك اليوم؟ (اكتب بالعامية عادي)", placeholder="مثال: والله اليوم مروق عالاخر...")

if st.button("تحليل المزاج 🚀"):
    if not user_name.strip() or not user_input.strip():
        st.warning("عطنا اسمك وكلامك يا بطل!")
    else:
        with st.spinner("جاري فك الشفرة العامية..."):
            time.sleep(1)
        
        mood_type, color, reply = analyze_mood_pro(user_input)
        
        st.markdown(f"""
        <div class="result-box" style="background:{color};">
            <h2 style="color:white; margin:0;">تحليل المشاعر لـ {user_name}</h2>
            <hr style="border:0.5px solid rgba(255,255,255,0.2); margin: 15px 0;">
            <p style="font-size: 22px; font-weight: bold; margin:0;">{reply}</p>
            <p style="font-size: 14px; margin-top: 10px; opacity: 0.8;">الحالة المكتشفة: {mood_type}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.caption("صنع بـ ❤️ بواسطة حمد | 2026")
