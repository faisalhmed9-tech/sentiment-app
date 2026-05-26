import streamlit as st
import pandas as pd
from textblob import TextBlob
from gtts import gTTS
import base64

# إعدادات الصفحة
st.set_page_config(page_title="تطبيق حمد لتحليل المشاعر", page_icon="🤖")

# اسم التطبيق ثابت باسم حمد
st.title("🤖 تطبيق حمد لتحليل المشاعر")
st.markdown("---")

# سؤال المستخدم عن اسمه
visitor_name = st.text_input("مرحباً بك في تطبيقي! وش اسمك الكريم؟")

if visitor_name:
    st.write(f"أهلاً بك يا **{visitor_name}** في عالمي الذكي! 🚀")
    
    # مكان كتابة النص للتحليل
    user_input = st.text_input(f"اكتب جملتك هنا يا {visitor_name}:")

    # دالة الصوت
    def speak(text):
        tts = gTTS(text=text, lang='ar')
        tts.save("speech.mp3")
        with open("speech.mp3", "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f'<audio controls autoplay><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
        st.markdown(md, unsafe_allow_html=True)

    if st.button("بدء التحليل"):
        if user_input:
            blob = TextBlob(user_input)
            score = blob.sentiment.polarity
            
            pos_words = ['حلو', 'جميل', 'رائع', 'كفو', 'سعيد', 'بطل', 'رهيب', 'فنان', 'متحمس', 'مبسوط', 'ممتاز']
            neg_words = ['سيء', 'خايس', 'تعبان', 'زفت', 'حزين', 'ضايق', 'فاشل']

            is_positive = score > 0 or any(word in user_input for word in pos_words)
            is_negative = score < 0 or any(word in user_input for word in neg_words)

            if is_positive:
                status = "إيجابي 😍"
                msg = f"يا {visitor_name}، جملتك إيجابية ورهيبة!"
                st.success(status)
                st.balloons()
            elif is_negative:
                status = "سلبي 😞"
                msg = f"يا {visitor_name}، النتيجة سلبية، تفاءل بالخير!"
                st.error(status)
            else:
                status = "محايد 😐"
                msg = f"هذه جملة عادية يا {visitor_name}."
                st.info(status)

            # العداد والصوت
            st.write("### 🔊 اسمع النتيجة:")
            speak(msg)

            # الجدول
            df = pd.DataFrame({"اسم الزائر": [visitor_name], "النص": [user_input], "التصنيف": [status]})
            st.table(df)
        else:
            st.warning(f"يا {visitor_name}، اكتب شيئاً لأحلله!")
else:
    st.info("من فضلك سجل اسمك أولاً عشان أقدر أرحب بك في تطبيقي!")



        


      
