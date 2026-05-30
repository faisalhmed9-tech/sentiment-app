import streamlit as st
import random
import time
import urllib.parse

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="نظام حمد الذكي", layout="centered", initial_sidebar_state="collapsed")

# --- 2. CSS حق التصميم ---
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

# --- 3. بوت الردود ---
class HamadBot:
    def __init__(self):
        # الردود هنا نظيفة تماماً من أي رموز
        self.replies = {
            "طفشان": ["طفشان؟ قم ارقص 10 ثواني قدام المراية وارجع لي 😂", "الحل: افتح نوت واكتب اسوأ فكرة تجي ببالك"],
            "تعبان": ["تعبان؟ طيب استلقي وتخيل انك سحابة كسلانة 😴", "الحل السحري: اغسل وجهك بموية باردة"],
            "جوعان": ["جوعان؟ افتح الثلاجة طالع 5 ثواني وسكرها 😂", "تخيل اكلت اندومي الحين. وصلتك السعرات افتراضي"],
            "قوي": ["ايه والله قوي! ارفع الجوال بيد وحدة 3 ثواني 💪", "قوي؟ تحمل نكتة بايخة مني بدون ما تضحك"],
            "مبسوط": ["يا سلام على الروقان! دوم هالضحكة 🔥", "مبسوط؟ وقت القرارات الغبية. وش ناوي تسوي؟"]
        }
        self.colors = {"طفشان": "#FF9800", "تعبان": "#2196F3", "جوعان": "#4CAF50", "قوي": "#F44336", "مبسوط": "#FFC107"}

    def get_reply(self, mood):
        mood = mood.lower()
        for key in self.replies.keys():
            if key in mood:
                return random.choice(self.replies[key]), self.colors.get(key, "#333")
        return "ما شاء الله عليك، واصل في يومك الجميل يا بطل 😎", "#607D8B"

bot = HamadBot()

# --- 4. واجهة التطبيق ---
st.title("🤖 نظام حمد الذكي")
st.write("فضفض وسوف يتم تحليلك فوراً!")

col1, col2 = st.columns(2)
with col1:
    user_name = st.text_input("سجل اسمك:", placeholder="حمد")
with col2:
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

user_input = st.text_area("اكتب شعورك هنا:")

if st.button("بدء التحليل 🚀"):
    if not user_name.strip() or not user_input.strip():
        st.warning("سجل بياناتك كاملة يا بطل!")
    else:
        with st.spinner("جاري التحليل..."):
            time.sleep(1)
        
        reply, color = bot.get_reply(user_input)
        prefix = "الأستاذ" if gender == "ذكر" else "الأستاذة"
        
        # هنا كان مصدر المشكلة وشلت النجوم نهائياً
        st.markdown(f"""
        <div class="result-box" style="background:{color};">
            <h2 style="color:white; margin:0;">النتيجة يا {prefix} {user_name}</h2>
            <hr style="border:0.5px solid rgba(255,255,255,0.2); margin: 15px 0;">
            <p style="font-size: 22px; font-weight: bold; margin:0;">{reply}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # زر الواتساب
        share_msg = urllib.parse.quote(f"تحليل مزاجي من نظام حمد: {reply}")
        st.markdown(f'<a href="https://wa.me/?text={share_msg}" target="_blank" class="whatsapp-btn">📤 مشاركة النتيجة</a>', unsafe_allow_html=True)

st.markdown("---")
st.caption("صنع بـ ❤️ بواسطة حمد | 2026")
