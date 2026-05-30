import streamlit as st
import random
import time
import urllib.parse

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="نظام حمد الذكي", layout="centered", initial_sidebar_state="collapsed")

# --- 2. التصميم (CSS) ---
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

# --- 3. محرك التحليل الذكي (عامي + ردود متنوعة) ---
def analyze_mood(text):
    text = text.lower()
    
    # 🔴 كلمات سلبية عامية (زهقان، منغث، مالي خلق...)
    negative_keys = ["زعلان", "ضايق", "طفشان", "زهقان", "تعبان", "مالي خلق", "منغث", "مغبون", "حزين", "متنكد"]
    # 🟢 كلمات إيجابية عامية (مروق، مستانس، وناسة...)
    positive_keys = ["مبسوط", "مستانس", "فرحان", "مروق", "وناسة", "الحمدلله", "كفو", "راضي", "منتعش"]
    # 🟡 كلمات محايدة عامية (عادي، ماشي الحال، نص نص...)
    neutral_keys = ["عادي", "تمام", "طيب", "ماشي", "نص نص", "ماشي الحال"]

    # ردود سلبية متنوعة
    neg_replies = [
        "أفا يا حمد! فضفض وطلع اللي بقلبك، الضيقة ما تدوم وبكرا أجمل بإذن الله.",
        "لا يضيق صدرك يا بطل، حنا معك واليوم السيء يجي بعده يوم يشرح الصدر.",
        "الخاطر يضيق ويرجع يزين، تفاءل وخذ لك بريك وبتعدي السحابة."
    ]
    
    # ردود إيجابية متنوعة
    pos_replies = [
        "يا سلام على الروقان! عسى هالضحكة والوناسة مرافقة لخطواتك دوم يا حمد.",
        "كفو! طاقة إيجابية رهيبة، استمر في يومك الجميل يا بطل.",
        "ما شاء الله! الروح الحلوة هذي هي اللي تفتح الأبواب، دوم مستانس يارب."
    ]
    
    # ردود محايدة متنوعة
    neu_replies = [
        "يوم هادي ومستقر، الاستقرار أحياناً يكون أجمل شي. خلك رايق.",
        "ماشي الحال، أهم شي إنك بخير ومرتاح البال يا حمد.",
        "الاستقرار النفسي نعمة، يومك موفق وسعيد بإذن الله."
    ]

    # منطق الفحص
    if any(word in text for word in negative_keys):
        return "سلبي", "#F44336", random.choice(neg_replies)
    elif any(word in text for word in positive_keys):
        return "إيجابي", "#4CAF50", random.choice(pos_replies)
    elif any(word in text for word in neutral_keys):
        return "محايد", "#607D8B", random.choice(neu_replies)
    else:
        return "غير محدد", "#2196F3", "كلامك جميل يا حمد، الأهم إنك تكون بخير ومرتاح البال دائماً."

# --- 4. واجهة التطبيق ---
st.title("🤖 نظام حمد الذكي")
st.write("وش يدور في خاطرك: فضفض وسوف يتم تحليلك!")

col1, col2 = st.columns(2)
with col1:
    user_name = st.text_input("سجل اسمك:", placeholder="مثلاً: حمد")
with col2:
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

user_input = st.text_area("اكتب شعورك هنا بالعامية عادي:")

if st.button("بدء التحليل وإطلاق القوة 🚀"):
    if not user_name.strip() or not user_input.strip():
        st.warning("يا بطل سجل بياناتك أول!")
    else:
        with st.spinner("جاري التحليل الفوري..."):
            time.sleep(1)
        
        mood_type, color, reply = analyze_mood(user_input)
        prefix = "الأستاذ" if gender == "ذكر" else "الأستاذة"
        
        st.markdown(f"""
        <div class="result-box" style="background:{color};">
            <h2 style="color:white; margin:0;">النتيجة يا {prefix} {user_name}</h2>
            <hr style="border:0.5px solid rgba(255,255,255,0.2); margin: 15px 0;">
            <p style="font-size: 22px; font-weight: bold; margin:0;">{reply}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # زر الواتساب
        share_msg = urllib.parse.quote(f"تحليل مزاجي من نظام حمد الذكي: {reply}")
        st.markdown(f'<a href="https://wa.me/?text={share_msg}" target="_blank" class="whatsapp-btn">📤 شارك الن
