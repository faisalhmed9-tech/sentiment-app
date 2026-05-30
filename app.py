import streamlit as st
import random
import time

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

# --- 3. محرك التحليل الشامل (المود + الشطحات) ---
def analyze_mood(text, name):
    text = text.lower()
    
    # [1] قسم الحب
    if any(word in text for word in ["أحبك", "حب", "يا بعدي", "عشق"]):
        replies = [f"يا بعد روحي يا {name}!", f"المحبة متبادلة يا {name}.", f"تستاهل كل الحب يا {name}."]
        return "#FF4B2B", random.choice(replies)

    # [2] قسم الجوع
    elif any(word in text for word in ["جوعان", "أكل", "جعت", "ميت جوع"]):
        replies = [f"يا {name} قم اضرب بالخمس!", f"عوافي مقدماً يا {name}.", f"الجوع شين يا {name}، رح تعش."]
        return "#FFA500", random.choice(replies)

    # [3] قسم التعب
    elif any(word in text for word in ["تعبان", "مرهق", "أبي أنام", "دايخ"]):
        replies = [f"سلامتك من التعب يا {name}.", f"ارتاح يا {name} الجسم له حق.", f"نوم العوافي يا {name}."]
        return "#607D8B", random.choice(replies)

    # [4] قسم القوة
    elif any(word in text for word in ["قوي", "وحش", "كفو", "أقدر"]):
        replies = [f"كفو يا وحش يا {name}!", f"إنت قدها يا {name}.", f"عزيمة حديد يا {name}!"]
        return "#4CAF50", random.choice(replies)

    # [5] قسم المود (إيجابي، سلبي، محايد)
    elif any(word in text for word in ["مستانس", "مروق", "وناسة", "فرحان", "مبسوط"]):
        replies = [f"دوم هالضحكة والروقان يا {name}!", f"يا عيني على الوناسة يا {name}.", f"كفو! خلك دايم مروق يا {name}."]
        return "#4CAF50", random.choice(replies)
    
    elif any(word in text for word in ["ضايق", "منغث", "طفشان", "زهقان", "زعلان"]):
        replies = [f"أفا يا {name}، الضيقة ما تدوم وبكرا أجمل.", f"فضفض يا {name}، كلنا نمر بأيام كذا وتعدي.", f"لا يضيق صدرك يا {name}، اضحك للدنيا."]
        return "#F44336", random.choice(replies)
    
    elif any(word in text for word in ["عادي", "تمام", "طيب", "ماشي"]):
        replies = [f"يوم هادي ومستقر يا {name}، نعمة.", f"أهم شي إنك بخير يا {name}.", f"ماشي الحال، الله يكتب لك الخير يا {name}."]
        return "#808080", random.choice(replies)

    # الرد التلقائي
    else:
        return "#2196F3", f"منور يا {name}، نورت البرنامج بكلامك."

# --- 4. الواجهة ---
st.title("🤖 نظام حمد الذكي")
st.write("حلل مزاجك أو شطحاتك (حب، جوع، تعب، قوة)!")

input_name = st.text_input("سجل اسمك للاختبار:", placeholder="مثلاً: فهد")
user_input = st.text_area("وش بخاطرك الحين؟")

if st.button("بدء التحليل 🚀"):
    if not input_name.strip() or not user_input.strip():
        st.warning("سجل بياناتك كاملة!")
    else:
        with st.spinner("جاري التحليل..."):
            time.sleep(1)
        
        color, reply = analyze_mood(user_input, input_name)
        
        st.markdown(f"""
        <div class="result-box" style="background:{color};">
            <p style="font-size: 22px; font-weight: bold; margin:0;">{reply}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.caption("صنع بـ ❤️ بواسطة حمد | 2026")
