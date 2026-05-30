import streamlit as st
import random
import time
import urllib.parse

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="نظام حمد الذكي", layout="centered", initial_sidebar_state="collapsed")

# --- 2. CSS حق التصميم (لمسة حمد الفخمة) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="st-"] {
        font-family: 'Tajawal', sans-serif; 
        direction: rtl; 
        text-align: right;
    }
    /* تنسيق زر التحليل بتدرج الألوان حقك */
    .stButton>button {
        width: 100%; border-radius: 15px; font-weight: bold;
        background: linear-gradient(90deg, #4CAF50, #2196F3);
        color: white; border: none; padding: 12px; font-size: 18px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    /* صندوق النتيجة */
    .result-box {
        padding: 25px; border-radius: 15px; margin-top: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3); color: white;
        animation: fadeIn 0.8s ease-in;
    }
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    /* زر الواتساب */
    .whatsapp-btn {
        display: block; width: 100%; background-color: #25D366;
        color: white !important; padding: 12px; border-radius: 15px;
        text-align: center; text-decoration: none; margin-top: 15px;
        font-weight: bold; font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. كود بوت الردود (كود حمد المرتب) ---
class HamadBot:
    def __init__(self):
        self.replies = {
            "طفشان": ["طفشان؟ قم ارقص 10 ثواني قدام المراية وارجع لي 😂", "الحل: افتح نوت واكتب اسوأ فكرة تجي ببالك", "ارسل ايموجي عشوائي وانا بألف لك قصة عليه الحين"],
            "تعبان": ["تعبان؟ طيب استلقي وتخيل انك سحابة... سحابة كسلانة بس 😴", "الحل السحري: اغسل وجهك بموية باردة وانت تقول 'انا سوبرمان'", "تحدي 30 ثانية: غمض عينك وتخيل سريرك يناديك"],
            "جوعان": ["جوعان؟ افتح الثلاجة طالع 5 ثواني وسكرها. شبعت؟ 😂", "تخيل اكلت اندومي الحين. وصلتك السعرات افتراضي", "قوم جيب لك شي، بس وانت رايح غني 'انا جوعان جوعان'"],
            "وانا قوي": ["ايه والله قوي! ارفع الجوال بيد وحدة 3 ثواني 💪😂", "قوي؟ تحمل نكتة بايخة مني بدون ما تضحك. يلا تحدى", "ماشاء الله. طيب شيل همي معك شوي بما انك قوي؟"],
            "الحب": ["الحب؟ ياحليلك انت 😂 تحب مين؟ اعترف ولا بفضحك", "قلبك دق؟ هذا مو حب هذا اكلت شي حار وارتفع الضغط", "الحب حلو... بس اشرب موية بين كل رسالة والتانية"],
            "زعلان": ["الزعل مو لايق عليك. نكتة بايخة ولا حضن افتراضي؟", "اكتب اسم اللي معصبك بحروف مقلوبة عشان نقهره 😈", "تخيل الزعل كيس زبالة وارميه من الشباك"],
            "مبسوط": ["المبسوط معدي! انقل لي العدوى بستكر 🔥", "وقف ضحك. قولي وش اكثر شي يضحك عشان اسرقه", "مبسوط؟ وقت القرارات الغبية. وش ناوي تسوي؟"]
        }
        self.colors = {
            "طفشان": "#FF9800", "تعبان": "#2196F3", "جوعان": "#4CAF50",
            "وانا قوي": "#F44336", "الحب": "#E91E63", "زعلان": "#9C27B0", "مبسوط": "#FFC107"
        }

    def get_reply(self, mood):
        mood = mood.lower()
        for key in self.replies.keys():
            if key in mood:
                return random.choice(self.replies[key]), self.colors.get(key, "#333")
        return "وش يدور في خاطرك؟ فضفض وسوف يتم تحليلك 😎", "#607D8B"

# تشغيل البوت
bot = HamadBot()

# --- 4. واجهة التطبيق ---
st.title("🤖 نظام حمد الذكي")
st.write("وش يدور في خاطرك: فضفض وسوف يتم تحليلك!")

col1, col2 = st.columns(2)
with col1:
    user_name = st.text_input("سجل اسمك:", placeholder="مثلاً: حمد")
with col2:
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

user_input = st.text_area("اكتب شعورك هنا (مثلاً: طفشان، جوعان، قوي...):", height=100)

if st.button("بدء التحليل وإطلاق القوة 🚀"):
    if not user_name.strip() or not user_input.strip():
        st.warning("يا بطل سجل اسمك واكتب شعورك أول!")
    else:
        with st.spinner("جاري تحليل قوتك النفسية..."):
            time.sleep(1.2)
        
        reply, color = bot.get_reply(user_input)
        prefix = "الأستاذ" if gender == "ذكر" else "الأستاذة"
        name_display = f"{prefix} {user_name.strip()}"
        
        # عرض النتيجة بتصميم حمد
        st.markdown(f"""
        <div class="result-box" style="background:{color}; color: {'black' if color=='#FFC107' else 'white'}">
            <h3 style="margin-top:0;">النتيجة يا {name_display} ✨</h3>
            <p style="font-size: 20px; font-weight: bold;">{reply}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.balloons()
        
        # زر مشاركة واتساب
        share_msg = urllib.parse.quote(f"حللت مزاجي في نظام حمد الذكي وطلعت النتيجة: {reply}")
        st.markdown(f'<a href="https://wa.me/?text={share_msg}" target="_blank" class="whatsapp-btn">📤 شارك النتيجة على واتساب</a>', unsafe_allow_html=True)

st.markdown("---")
st.caption("صنع بـ ❤️ بواسطة حمد | 2026")
        
