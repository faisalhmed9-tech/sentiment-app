import streamlit as st
import random
import time
import urllib.parse

# --- 1. إعدادات الصفحة والتصميم ---
st.set_page_config(page_title="نظام حمد الذكي - النسخة الشاطحة", layout="centered")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="st-"] {font-family: 'Tajawal', sans-serif; direction: rtl; text-align: right;}
    .stButton>button {
        width: 100%; border-radius: 15px; font-weight: bold;
        background: linear-gradient(90deg, #FF4B2B, #FF416C); /* لون شاطح جديد */
        color: white; border: none; padding: 12px; font-size: 18px;
    }
    .result-box {
        padding: 20px; border-radius: 15px; margin-top: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3); color: white;
        animation: fadeIn 0.8s ease-in;
    }
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }
</style>
""", unsafe_allow_html=True)

# --- 2. بوت الردود الشاطحة (كود حمد بعد الدمج) ---
class Shat7aBot:
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
            "وانا قوي": "#F44336", "الحب": "#E91E63", "زعلان": "#9C27B0", "مبسوط": "#FFEB3B"
        }

    def get_reply(self, mood):
        for key in self.replies.keys():
            if key in mood:
                return random.choice(self.replies[key]), self.colors.get(key, "#333")
        return "وش فيك ساكت؟ تكلم خل نجلد سوالف 😎", "#607D8B"

# تشغيل البوت
bot = Shat7aBot()

# --- 3. واجهة المستخدم ---
st.title("🛡️ نظام حمد الشاطح الذكي")
st.write("أهلاً بك في عالم الشطحات.. سجل بياناتك وخلنا نحللك!")

col1, col2 = st.columns(2)
with col1:
    user_name = st.text_input("سجل اسمك يا بطل:", placeholder="حمد")
with col2:
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

user_input = st.text_area("وش جوك الحين؟ (اكتب: طفشان، جوعان، قوي...)", placeholder="فضفض هنا...")

if st.button("بدء التحليل الشاطح 🚀"):
    if not user_name.strip() or not user_input.strip():
        st.warning("لازم تكتب اسمك ومزاجك أول!")
    else:
        with st.spinner("جاري استدعاء الردود الشاطحة..."):
            time.sleep(1)
        
        reply, color = bot.get_reply(user_input)
        prefix = "الأستاذ" if gender == "ذكر" else "الأستاذة"
        
        # عرض النتيجة
        st.markdown(f"""
        <div class="result-box" style="background:{color}; color: {'black' if color=='#FFEB3B' else 'white'}">
            <h3>النتيجة يا {prefix} {user_name}:</h3>
            <p style="font-size: 20px; font-weight: bold;">{reply}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # زر مشاركة واتساب
        share_msg = urllib.parse.quote(f"حللت مزاجي عند حمد الشاطح وطلعت النتيجة: {reply}")
        st.markdown(f'<a href="https://wa.me/?text={share_msg}" target="_blank" style="text-decoration:none;"><button style="margin-top:10px; background:#25D366; color:white; width:100%; border-radius:15px; padding:10px; border:none; font-weight:bold;">📤 شارك الشطحة على واتساب</button></a>', unsafe_allow_html=True)

st.markdown("---")
st.caption("برمجة وتطوير حمد الشاطح © 2026")
