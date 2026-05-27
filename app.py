import streamlit as st
import pandas as pd
from textblob import TextBlob
from gtts import gTTS
import base64
import random

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="محلل المشاعر الذكي", page_icon="🤖")

# --- 2. دالة الصوت ---
def speak(text):
    try:
        tts = gTTS(text=text, lang='ar')
        tts.save("speech.mp3")
        with open("speech.mp3", "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f'<audio controls autoplay><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
        st.markdown(md, unsafe_allow_html=True)
    except:
        pass

# --- 3. واجهة المستخدم ---
st.title("🤖 محلل المشاعر الذكي - نسخة المشاهير")
st.markdown("---")

visitor_name = st.text_input("يا هلا بك! وش اسمك الكريم؟")

# اختيار الجنس لتحديد الألوان واللقب
gender = st.radio("كيف تحب أن أخاطبك؟", ["ذكر", "أنثى"], horizontal=True)

# تحديد الألوان واللقب بناءً على الاختيار
if gender == "ذكر":
    main_color = "#1e90ff"  # أزرق
    bg_color = "rgba(30, 144, 255, 0.1)"
    title_prefix = "الشهير"
    welcome = f"مرحباً بك يا {title_prefix} **{visitor_name}** ⚡"
    ask_feel = "وش تحس فيه الحين؟"
else:
    main_color = "#ff69b4"  # وردي
    bg_color = "rgba(255, 105, 180, 0.1)"
    title_prefix = "الشهيرة"
    welcome = f"مرحباً بك يا {title_prefix} **{visitor_name}** ✨"
    ask_feel = "وش تحسين فيه الحين؟"

# تطبيق الثيم الملون
st.markdown(f"""
    <style>
    .result-box {{
        padding: 20px; border-radius: 15px; border: 2px solid {main_color};
        background-color: {bg_color}; color: white;
        text-align: center; box-shadow: 0 0 15px {main_color}; margin: 10px 0;
    }}
    h1, h2, h3 {{ color: {main_color} !important; }}
    </style>
    """, unsafe_allow_html=True)

if visitor_name:
    st.write(welcome)
    user_input = st.text_input(ask_feel)

    if st.button("تحليل المشاعر"):
        if user_input:
            blob = TextBlob(user_input)
            score = blob.sentiment.polarity
            
            # قوائم الكلمات العربية للفهم الدقيق
            pos_words = ['سعيد', 'مبسوط', 'كفو', 'جميل', 'حلو', 'بطل', 'فخم', 'ممتاز', 'شكرا', 'وناسة', 'راضي', 'مبدع']
            neg_words = ['سيء', 'خايس', 'تعبان', 'متضايق', 'زعلان', 'حزين', 'ضيق', 'فاشل', 'غبي', 'قهر']

            found_pos = any(word in user_input for word in pos_words)
            found_neg = any(word in user_input for word in neg_words)

            if found_pos or score > 0.1:
                advice = random.choice(["يومك سعيد يا بطل! 🚀", "طاقة إيجابية فخمة 🔥", "دووم هالانبساط يا رب! ✨"])
                st.markdown(f'<div class="result-box"><h3>النتيجة: إيجابي 😍 ✨</h3><p>{advice}</p></div>', unsafe_allow_html=True)
                st.balloons()
                msg = f"ما شاء الله، كلامك كله إيجابية يا {title_prefix} {visitor_name}. {advice}"
            
            elif found_neg or score < -0.1:
                advice = random.choice(["استغفر الله، وريح بالك.. 🤲", "قم اشرب قهوة وروّق ☕", "تذكر: إن مع العسر يسراً ✨"])
                st.markdown(f'<div class="result-box"><h3>النتيجة: سلبي 😔 💔</h3><p>{advice}</p></div>', unsafe_allow_html=True)
                msg = f"النتيجة سلبية يا {title_prefix} {visitor_name}. نصيحتي لك: {advice}"
            
            else:
                advice = "كلامك موزون وهادي.. 🤔"
                st.markdown(f'<div class="result-box"><h3>النتيجة: محايد 😐</h3><p>{advice}</p></div>', unsafe_allow_html=True)
                msg = f"هذه جملة محايدة يا {title_prefix} {visitor_name}. {advice}"

            st.write(f"### 🔊 اسمع النتيجة بصوت {title_prefix}:")
            speak(msg)
            
            st.write("---")
            st.table(pd.DataFrame({
                "الاسم": [visitor_name], 
                "اللقب": [title_prefix],
                "الجنس": [gender], 
                "النص": [user_input],
                "التصنيف": [msg]
            }))
        else:
            st.warning("اكتب شيئاً أولاً!")
else:
    st.info("سجل اسمك لبدء التجربة")
    



                



        


      
