import streamlit as st
import time
import random
import urllib.parse

st.set_page_config(page_title="نظام حمد الذكي", layout="centered", initial_sidebar_state="collapsed")

# --- CSS مع الوان متغيرة ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    html, body, [class*="st-"] {font-family: 'Tajawal', sans-serif; direction: rtl; text-align: right;}
   .stButton>button {
        width: 100%; border-radius: 15px; font-weight: bold;
        background: linear-gradient(90deg, #4CAF50, #2196F3);
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
   .whatsapp-btn {
        display: block; width: 100%; background-color: #25D366;
        color: white!important; padding: 12px; border-radius: 15px;
        text-align: center; text-decoration: none; margin-top: 15px; font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.title("🤖 نظام حمد الذكي")
st.write("وش يدور في خاطرك: فضفض وسوف يتم تحليلك!")

col1, col2 = st.columns(2)
with col1:
    user_name = st.text_input("سجل اسمك:", placeholder="مثلاً: حمد")
with col2:
    gender = st.radio("الجنس:", ["ذكر", "أنثى"], horizontal=True)

user_input = st.text_area("اكتب شعورك هنا:", height=100, placeholder="مثال: طفشان، تعبان، مبسوط...")

# ردود عشوائية + الوان + اقتباسات
responses = {
    "طفشان": {
        "replies": ["الطفش مجرد لحظة يا {name}، قم سوي لك كوب شاي وبتزين",
                   "يا {name} الطفش يقتل الابداع، قم تحرك 5 دقايق بس",
                   "معقولة {name} طفشان؟ لا تقولها قدامي 😤"],
        "color": "#FF9800", "quote": "الملل بداية الابداع"
    },
    "تعبان": {
        "replies": ["شكل السهر مأثر عليك يا {name}.. روح ارتاح، النوم سلطان",
                   "جسمك يقولك كفاية يا {name}، اسمع له",
                   "حتى الابطال يحتاجون راحة يا {name}"],
        "color": "#2196F3", "quote": "الراحة جزء من الانجاز"
    },
    "مبسوط": {
        "replies": ["يا سلام على الروقان يا {name}! دوم هالضحكة",
                   "الفرحة تليق فيك يا {name} 🔥",
                   "الله يديم هالمزاج يا {name}!"],
        "color": "#4CAF50", "quote": "الابتسامة صدقة"
    },
    "زعلان": {
        "replies": ["كل شي يعدي يا {name}، شد حيلك",
                   "الضيقة ما تدوم يا {name}، بكرا احلى",
                   "انا معك يا {name}، تكلم وفض"],
        "color": "#9C27B0", "quote": "بعد العسر يسر"
    },
    "عادي": {
        "replies": ["تمام يا {name}، الاستقرار نعمة",
                   "يوم عادي = يوم ناجح يا {name}",
                   "الحمدلله على كل حال يا {name}"],
        "color": "#607D8B", "quote": "الحمدلله على كل شيء"
    }
}

def analyze_feeling(text):
    text = text.lower()
    if any(w in text for w in ["طفشان", "زهقان", "ملل"]): return "طفشان"
    if any(w in text for w in ["تعبان", "مرهق", "نوم"]): return "تعبان"
    if any(w in text for w in ["مبسوط", "فرحان", "تمام"]): return "مبسوط"
    if any(w in text for w in ["زعلان", "حزين", "ضايق"]): return "زعلان"
    return "عادي"

if st.button("بدء التحليل وإطلاق القوة 🚀"):
    if not user_name.strip() or not user_input.strip():
        st.warning("يا بطل سجل اسمك واكتب شعورك أول!")
    else:
        with st.spinner("جاري تحليل قوتك النفسية..."):
            time.sleep(1.2)

        feeling = analyze_feeling(user_input)
        prefix = "الأستاذ" if gender == "ذكر" else "الأستاذة"
        name_display = user_name.strip()

        data = responses[feeling]
        reply = random.choice(data["replies"]).format(name=name_display)
        final_msg = f"{reply}\n\n💡 *{data['quote']}*"

        # عرض النتيجة بتأثير كتابة
        st.markdown(f'<div class="result-box" style="background:{data["color"]}; border-right: 5px solid white;">', unsafe_allow_html=True)
        placeholder = st.empty()
        for i in range(len(final_msg)):
            placeholder.markdown(f"<h3>{final_msg[:i+1]}</h3></div>", unsafe_allow_html=True)
            time.sleep(0.02)

        st.balloons()

        share_msg = urllib.parse.quote(reply + " \nجرب نظام حمد: https://fljg.streamlit.app")
        st.markdown(f'<a href="https://wa.me/?text={share_msg}" target="_blank" class="whatsapp-btn">📤 شارك النتيجة على واتساب</a>', unsafe_allow_html=True)

st.markdown("---")
st.caption("صنع بـ ❤️ بواسطة حمد | 2026")
