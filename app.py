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
        background: linear-gradient(90deg, #FF4B2B, #FF416C);
        color: white; border: none; padding: 15px; font-size: 18px;
    }
    .result-box { padding: 30px; border-radius: 20px; margin-top: 25px; color: white; text-align: center; font-size: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.2); }
</style>
""", unsafe_allow_html=True)

# --- 2. محرك التحليل الشاطح (حب، جوع، تعب، قوة) ---
def analyze_mood_shateh(text, name):
    text = text.lower()
    
    # 1. قسم الحب ️❤️
    love_keys = ["أحبك", "يا بعدي", "حب", "أعشقك", "غالي", "يا روحي"]
    love_replies = [f"يا بعد قلبي يا {name}، المحبة متبادلة والله!", f"يا {name} جعل ما يحب غيرك إلا السعادة والهنا.", f"قلبك أبيض يا {name}، وتستاهل كل الحب!"]

    # 2. قسم الجوع 🍔
    hunger_keys = ["جوعان", "أبي أكل", "جعت", "ميت جوع", "وش العشا"]
    hunger_replies = [f"يا {name} الجوع كافر، قم اضرب بالخمس وخل عنك التحليل!", f"عوافي مقدماً يا {name}، لا تنسى تعزمنا على هالوجبة.", f"يا {name} من جاع هان، قم دور لك أقرب مطعم وضبط وضعك."]

    # 3. قسم التعب 😫
    tired_keys = ["تعبان", "مرهق", "مهلوك", "أبي أنام", "دايخ"]
    tired_replies = [f"سلامة قلبك يا {name}، ريح جسمك النوم سلطان.", f"يا {name} لا تضغط على نفسك، خذ لك بريك وشاهي وبتزين.", f"الراحة مطلوبة يا {name}، تعبك هذا دليل إنك بذلت جهد بطل."]

    # 4. قسم القوة 🔥
    power_keys = ["قوي", "وحش", "كفو", "أقدر", "عزيمة", "إصرار"]
    power_replies = [f"كفو يا {name}! إنت قدها وقدود، وحش والله.", f"هذي العزيمة اللي نعرفها فيك يا {name}، استمر يا بطل!", f"يا {name} قوتك هذي تلهم اللي حولك، لا تتراجع."]

    # 5. الحالات العادية
    pos_keys = ["مستانس", "مروق", "وناسة"]
    neg_keys = ["ضايق", "طفشان", "منغث"]

    # منطق الفحص والاختيار
    if any(word in text for word in love_keys):
        return "#FF4B2B", random.choice(love_replies)
    elif any(word in text for word in hunger_keys):
        return "#FFA500", random.choice(hunger_replies)
    elif any(word in text for word in tired_keys):
        return "#607D8B", random.choice(tired_replies)
    elif any(word in text for word in power_keys):
        return "#4CAF50", random.choice(power_replies)
    elif any(word in text for word in pos_keys):
        return "#FFD700", f"دوم هالوناسة يا {name}!"
    elif any(word in text for word in neg_keys):
        return "#000000", f"أفا يا {name}، فضفض لي أنا أسمعك."
    else:
        return "#2196F3", f"منور يا {name}، كلامك له هيبة مثلك."

# --- 3. الواجهة ---
st.title("🛡️ نظام حمد الذكي (النسخة الشاطحة)")
st.write("اختبرني في الحب، الجوع، التعب، أو القوة.. وشوف الردود!")

input_name = st.text_input("سجل اسمك للاختبار:", placeholder="مثلاً: حمد")
user_input = st.text_area("وش بخاطرك الحين؟ (شطّح بالكلام عادي):")

if st.button("إطلاق التحليل الذكي 🚀"):
    if not input_name.strip() or not user_input.strip():
        st.warning("يا بطل سجل اسمك وكلامك أول!")
    else:
        with st.spinner("جاري فك الشفرة الشاطحة..."):
            time.sleep(1)
        
        color, reply = analyze_mood_shateh(user_input, input_name)
        
        st.markdown(f"""
        <div class="result-box" style="background:{color};">
            <p style="font-weight: bold; margin:0;">{reply}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.caption(f"صنع بـ ❤️ بواسطة حمد | 2026")
