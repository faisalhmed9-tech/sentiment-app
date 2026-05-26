import streamlit as st
import pandas as pd
from textblob import TextBlob
from gtts import gTTS
import base64

# إعدادات الواجهة
st.set_page_config(page_title="محلل حمد الأسطوري", page_icon="👑")

st.title("👑 تطبيق حمد الذكي (الإصدار الأسطوري)")
st.markdown("---")

# مكان كتابة النص
user_input = st.text_input("وش في خاطرك اليوم؟ (اكتب جملة أو إيموجي):")

# دالة لتحويل النص إلى صوت
def speak(text):
    tts = gTTS(text=text, lang='ar')
    tts.save("speech.mp3")
    with open("speech.mp3", "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    md = f'<audio controls autoplay><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
    st.markdown(md, unsafe_allow_html=True)

if st.button("تحليل ومحاكاة"):
    if user_input:
        # تحليل المشاعر والإيموجي
        blob = TextBlob(user_input)
        score = blob.sentiment.polarity
        
        pos_words = ['حلو', 'جميل', 'رائع', 'كفو', 'سعيد', 'بطل', 'رهيب', 'فنان', '🔥', '😍', '✅']
        neg_words = ['سيء', 'خايس', 'تعبان', 'زفت', 'حزين', '💔', '❌', '👎']

        if score > 0 or any(word in user_input for word in pos_words):
            status = "إيجابي 😍"
            msg = f"يا حمد، جملتك إيجابية ورهيبة مثلك!"
            st.success(f"النتيجة: {status}")
            st.balloons()
        elif score < 0 or any(word in user_input for word in neg_words):
            status = "سلبي 😞"
            msg = "يا حمد، النتيجة سلبية، تفاءل بالخير!"
            st.error(f"النتيجة: {status}")
        else:
            status = "محايد 😐"
            msg = "جملة عادية يا حمد."
            st.info(f"النتيجة: {status}")

        # 1. عداد المشاعر (Slider)
        st.write("### 📊 مقياس الشعور:")
        val = "إيجابي" if "إيجابي" in status else ("سلبي" if "سلبي" in status else "محايد")
        st.select_slider("القوة:", options=["سيء جداً", "سلبي", "محايد", "إيجابي", "ممتاز!"], value=val)

        # 2. تحويل النص إلى صوت
        st.write("### 🔊 اسمع النتيجة:")
        speak(msg)

        # الجدول
        df = pd.DataFrame({"النص": [user_input], "التصنيف": [status]})
        st.table(df)
        
        # ميزة التحميل
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 تحميل سجل التحليل", data=csv, file_name='faisal_analysis.csv', mime='text/csv')
    else:
        st.warning("يا حمد، الخانة فاضية!")


      
