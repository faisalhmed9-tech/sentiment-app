import streamlit as st
import pandas as pd
from textblob import TextBlob
from gtts import gTTS
import base64
import random

# --- 1. إعدادات الصفحة والديكور (CSS) ---
st.set_page_config(page_title="محلل المشاعر الذكي", page_icon="🤖")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .positive-glow {
        padding: 20px; border-radius: 15px; border: 2px solid #22c55e;
        background-color: rgba(34, 197, 94, 0.1); color: #4ade80;
        text-align: center; box-shadow: 0 0 15px #22c55e; margin: 10px 0;
    }
    .negative-glow {
        padding: 20px; border-radius: 15px; border: 2px solid #ef4444;
        background-color: rgba(239, 68, 68, 0.1); color: #f87171;
        text-align: center; box-shadow: 0 0 15px #ef4444; margin: 10px 0;
    }
    .neutral-glow {
        padding: 20px; border-radius: 15px; border: 2px solid #eab308;
        background-color: rgba(234, 179, 8, 0.1); color: #fde047;
        text-align: center; box-shadow: 0 0 15px #eab308; margin: 10px 0;
    }
    h1, h2, h3 { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)

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
st.title("🤖 محلل المشاعر الذكي - النسخة الذهبية")
st.markdown("---")

visitor_name = st.text_input("يا هلا بك! وش اسمك الكريم؟")

if visitor_name:
    st.write(f"مرحباً بك يا **{visitor_name}**")
    user_input = st.text_input(f"اكتب وش تحس فيه الحين:")

    if st.button("تحليل المشاعر"):
        if user_input:
            blob = TextBlob(user_input)
            score = blob.sentiment.polarity
            
            # --- قاموس الفزعة العربية (تمت إضافة سعيد ومبسوط) ---
            pos_words = ['سعيد', 'مبسوط', 'كفو', 'جميل', 'حلو', 'بطل', 'فخم', 'ممتاز', 'شكرا', 'وناسة', 'راضي', 'مبدع', 'رائع', 'حب', 'قلب']
            neg_words = ['سيء', 'خايس', 'تعبان', 'متضايق', 'زعلان', 'حزين', 'ضيق', 'فاشل', 'غبي', 'قهر', 'كرهت', 'زفت', 'هم']

            found_pos = any(word in user_input for word in pos_words)
            found_neg = any(word in user_input for word in neg_words)

            if found_pos or score > 0.1:
                advice = random.choice(["يومك سعيد ومليء بالإنجازات! 🚀", "طاقة إيجابية فخمة، استمر 🔥", "دووم هالانبساط يا رب! ✨"])
                st.markdown(f'<div class="positive-glow"><h3>النتيجة: إيجابي 😍 ✨</h3><p>{advice}</p></div>', unsafe_allow_html=True)
                st.balloons()
                msg = f"ما شاء الله، كلامك كله إيجابية يا {visitor_name}. {advice}"
            
            elif found_neg or score < -0.1:
                advice = random.choice(["استغفر الله، وريح بالك.. الدنيا ما تسوى 🤲", "قم اشرب قهوة وروّق المنال ☕", "تذكر: (إن مع العسر يسراً) ✨"])
                st.markdown(f'<div class="negative-glow"><h3>النتيجة: سلبي 😔 💔</h3><p><b>نصيحة:</b> {advice}</p></div>', unsafe_allow_html=True)
                msg = f"النتيجة سلبية يا {visitor_name}. نصيحتي لك: {advice}"
            
            else:
                advice = random.choice(["كلامك موزون وهادي.. جرب تعبر أكثر 😉", "شكلك اليوم رايق وماسك العصا من النص ⚖️", "جملة دبلوماسية بامتياز! 🤔"])
                st.markdown(f'<div class="neutral-glow"><h3>النتيجة: محايد 😐</h3><p>{advice}</p></div>', unsafe_allow_html=True)
                msg = f"هذه جملة محايدة يا {visitor_name}. {advice}"

            st.write("### 🔊 اسمع النتيجة:")
            speak(msg)
            
            st.write("---")
            st.table(pd.DataFrame({"الاسم": [visitor_name], "النص": [user_input], "التصنيف": [msg]}))
        else:
            st.warning("اكتب شيئاً أولاً!")
else:
    st.info("سجل اسمك لبدء التجربة")



                



        


      
